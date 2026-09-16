# Azure Private Link and Private Endpoints: AZ-104 Study Note

This note explains **why** Private Link and private endpoints exist, when to use them, and how they fit with DNS, routing, network security, and authorization.

The goal is not to memorize portal screens. The goal is to recognize the operational problem and choose the smallest Azure design that solves it.

## 1. The problem: PaaS is easy to use, but the network path is hidden

An application can use Azure Storage with a normal hostname:

```text
storageaccount.blob.core.windows.net
```

At the application level, this is simple:

```text
Application -> Storage SDK -> storageaccount.blob.core.windows.net
```

Normally, that hostname resolves to a public service endpoint. The application may still be strongly authenticated, but the network destination is public.

That becomes a problem when an organization requires:

- no public network access to the PaaS resource;
- traffic to remain on private Azure networking;
- access from a VNet, on-premises network, or another connected private network;
- private IP-based network controls;
- a private path for services such as Storage, SQL Database, Key Vault, or App Service.

The application code may be fine. The requirement is about **how the application reaches the service**.

## 2. The mental model

Think of a PaaS service as a building with two possible entrances:

```text
Public endpoint  = public entrance
Private endpoint = private entrance inside your VNet
```

**Azure Private Link** is the Azure technology that provides private connectivity to supported services.

A **private endpoint** is the resource you create in your VNet to consume that private connectivity.

```text
Private Link      = the underlying Azure connectivity technology
Private endpoint  = your private access point into a supported service
```

The private endpoint is not a second Storage account or a VM running Storage. It is a private network interface in your VNet that connects to a specific PaaS resource.

## 3. What a private endpoint creates

Suppose the VNet is:

```text
VNet: 10.20.0.0/16
```

You choose a subnet for private endpoints:

```text
Private endpoint subnet: 10.20.2.0/24
```

When you create a private endpoint for a Blob service, Azure creates a network interface with a private IP:

```text
Private endpoint IP: 10.20.2.7
```

Conceptually:

```text
VNet
  └── subnet 10.20.2.0/24
        └── private endpoint NIC: 10.20.2.7
              └── Private Link connection
                    └── storageaccount / Blob
```

The private endpoint is associated with a particular resource and commonly a particular subresource:

```text
Private endpoint
  -> Storage account: storageaccount
  -> Subresource: Blob
  -> Private IP: 10.20.2.7
```

It is not a generic private gateway to every Azure service.

## 4. Why use one? A concrete scenario

Imagine a web application running in an Azure VM or App Service. It stores customer documents in Azure Blob Storage.

### Without a private endpoint

```text
Application
   -> storageaccount.blob.core.windows.net
   -> public Storage endpoint
   -> Storage account
```

The Storage firewall and identity permissions may still protect the account, but the network path uses the public endpoint.

### With a private endpoint

```text
Application in VNet
   -> storageaccount.blob.core.windows.net
   -> private IP 10.20.2.7
   -> private endpoint
   -> Storage account
```

Now the application reaches Storage through a private IP in the VNet. You can commonly disable public network access to the Storage account after the private path is working.

The use case is not “make Storage more private” in the abstract. It is:

> Give this application a private network path to a Microsoft-managed PaaS service without making the application manage a new server or change its normal service hostname.

## 5. Private Link versus private endpoint

These terms describe different levels of the design:

| Term | Role |
|---|---|
| Private Link | Azure's private connectivity technology for supported services |
| Private endpoint | The consumer-side Azure resource placed in your VNet |
| PaaS resource | The service being reached, such as Storage or SQL |
| Private IP | The address clients in the VNet connect to |
| Private DNS zone | The name-resolution configuration that returns that private IP |

For Microsoft-managed services, Microsoft operates the service side. You create the private endpoint in your subscription and approve or establish the private-link connection as required.

## 6. Why DNS is required

The application normally uses the service's familiar hostname:

```text
storageaccount.blob.core.windows.net
```

Applications connect to IP addresses, not names. DNS translates the name into an IP address.

If DNS returns a public address:

```text
storageaccount.blob.core.windows.net
        -> public IP
```

the operating system creates traffic to that public destination. It does not inspect Azure resources and discover that a private endpoint also exists.

The private endpoint cannot automatically intercept traffic whose destination is a public IP.

For the private path, DNS must return the private endpoint IP:

```text
storageaccount.blob.core.windows.net
        -> 10.20.2.7
        -> private endpoint
        -> Storage
```

That is why Private Link designs commonly include a Private DNS zone.

## 7. What the `privatelink` DNS name means

Azure services have public hostnames. Private Link uses service-specific private-link namespaces, for example:

```text
Storage Blob:       privatelink.blob.core.windows.net
Azure SQL Database: privatelink.database.windows.net
Key Vault:          privatelink.vaultcore.azure.net
App Service:        privatelink.azurewebsites.net
```

For Storage, the private zone might contain:

```text
storageaccount.privatelink.blob.core.windows.net  A  10.20.2.7
```

Azure's DNS configuration makes the normal service hostname resolve through the private-link name or equivalent private-zone configuration.

The application continues using:

```text
storageaccount.blob.core.windows.net
```

It does not need to be rewritten to use a private hostname.

The exact zone is service-specific. Do not invent it from memory. Use the Azure service's Private Endpoint DNS guidance.

## 8. The complete request flow

Assume:

```text
Application VM:       10.20.1.4
Private endpoint:     10.20.2.7
Service hostname:     storageaccount.blob.core.windows.net
```

The request flows as follows:

```text
1. The application asks for storageaccount.blob.core.windows.net.
2. The VM asks its configured DNS resolver for an address.
3. Private DNS returns 10.20.2.7.
4. The operating system creates traffic to 10.20.2.7.
5. The VNet route determines how to reach the private endpoint.
6. NSGs and service network controls evaluate the network flow.
7. Private Link carries the connection to the Storage service.
8. Storage evaluates the caller's identity and data permissions.
9. Storage returns the response through the private path.
```

Each layer answers a different question:

```text
DNS:           Which IP represents the service name?
Routing:       Can the client reach that IP?
NSG/firewall:  Is this network flow allowed?
Authorization: May this identity use this Storage resource and data?
```

A private endpoint mainly changes the **network destination and path**. It does not replace authentication or authorization.

## 9. What goes wrong when DNS returns the public IP?

The private endpoint may exist correctly:

```text
Private endpoint = 10.20.2.7
```

But if DNS returns:

```text
storageaccount.blob.core.windows.net -> public IP
```

then the client sends traffic to the public IP.

The result is:

```text
Private endpoint exists
        +
DNS returns public address
        =
private endpoint is bypassed
```

Possible outcomes include:

- the connection is rejected because public network access is disabled;
- the connection is rejected by a public firewall rule;
- the connection succeeds, but violates the intended private-network design;
- the application reaches the wrong network path and troubleshooting becomes confusing.

This is why “the private endpoint exists” is not enough. The client must resolve the service hostname to the private endpoint address.

## 10. Private endpoint is not the same as private DNS

These are separate resources and responsibilities:

```text
Private endpoint
  = creates the private network interface and service connection

Private DNS zone
  = stores the private name-to-IP record

Virtual network link
  = makes that private zone available to a VNet
```

Creating the private endpoint does not mean every DNS client automatically uses it in every DNS architecture. The Azure portal may offer to create and link the recommended private DNS zone, but the underlying pieces remain distinct.

A private endpoint without the correct DNS path is like building a private doorway but leaving the application's address book pointing at the public entrance.

## 11. Private endpoint versus service endpoint

These are common alternatives in AZ-104 questions.

### Service endpoint

A service endpoint extends a VNet's identity and traffic path toward a supported Azure service. The service is generally still addressed using a Microsoft public IP.

```text
VM in VNet
   -> service public address
   -> Azure recognizes the VNet as an allowed source
```

Use this when subnet-based restriction is sufficient and a private IP is not required.

### Private endpoint

A private endpoint gives the service a private IP in your VNet.

```text
VM in VNet
   -> private IP in VNet
   -> private endpoint
   -> PaaS service
```

Use this when you need private addressing, private DNS, private connectivity from connected networks, or a design with public access disabled.

| Requirement | Service endpoint | Private endpoint |
|---|---:|---:|
| Private IP in your VNet | No | Yes |
| Private DNS usually involved | No | Yes |
| Service accessed through public address | Generally yes | No, for the private client path |
| Commonly used with public access disabled | Not inherently | Yes |
| Uses Private Link | No | Yes |

## 12. Private endpoint and public access

Creating a private endpoint does not necessarily disable the public endpoint. You can temporarily have both paths:

```text
Public clients -> public endpoint
VNet clients   -> private endpoint
```

This can be useful during migration or for mixed-access designs.

If the requirement is that the service must be private-only, you must also configure the PaaS resource's network settings to disable or restrict public access. Do this only after confirming that:

- private DNS resolves correctly;
- the client reaches the private IP;
- NSGs and routes allow the path;
- the service firewall permits the private endpoint;
- the application identity has the required permissions.

Otherwise, disabling public access can turn a working application into a connectivity outage.

## 13. Private endpoints and on-premises clients

Private endpoints are also useful for applications outside Azure.

Example:

```text
On-premises application
   -> VPN or ExpressRoute
   -> Azure VNet
   -> private endpoint
   -> Azure SQL or Storage
```

The network connection alone is not enough. On-premises DNS must also be able to resolve the service hostname to the private endpoint IP. This may require DNS forwarding, Azure DNS Private Resolver, or another enterprise DNS design.

The full requirement is:

```text
Private network path + correct DNS + network permission + data authorization
```

## 14. How to troubleshoot a private endpoint

Use this order:

1. **DNS:** Does the service hostname resolve?
2. **Destination:** Does it resolve to the expected private IP?
3. **Route:** Can the client reach that private IP?
4. **Network policy:** Do NSGs and service firewall settings allow the connection?
5. **Private-link state:** Is the private endpoint connection approved and healthy?
6. **Authorization:** Does the identity have permission to use the service?
7. **Application:** Is the connection string, TLS, or SDK configuration correct?

A basic DNS check from a client is:

```bash
nslookup storageaccount.blob.core.windows.net
```

or:

```bash
dig storageaccount.blob.core.windows.net
```

A private endpoint design is not proven merely because DNS returns an answer. You need the expected private answer and then a successful connection and authorization check.

## 15. What to remember for AZ-104

When a question mentions a PaaS service and private access, think:

```text
1. What service is being protected?
2. Where should the private endpoint NIC live?
3. Which private DNS zone matches the service?
4. Which VNet must be linked to that zone?
5. Does the client resolve the normal service hostname to the private IP?
6. Are routes, NSGs, service firewall settings, and identity permissions also correct?
```

The shortest useful summary is:

> **Private Link is the Azure technology. A private endpoint gives your VNet a private IP-based entrance to a supported PaaS service. Private DNS makes the normal service hostname resolve to that entrance.**

## Official references

- [Azure Private Link overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)
- [What is a private endpoint?](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
- [Azure Private Endpoint private DNS zone values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
- [Azure Private DNS overview](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview)
- [Compare private endpoints and service endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#private-endpoints)
