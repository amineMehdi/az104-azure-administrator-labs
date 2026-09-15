# Azure DNS: AZ-104 Study Note

This note covers the DNS knowledge most relevant to the current AZ-104 objectives:

- configuring Azure DNS;
- mapping a custom DNS name to an App Service web app;
- public and private DNS resolution;
- common DNS record types;
- private DNS zones and virtual network links;
- the relationship between DNS, private endpoints, and load balancing.

The main exam objective is `NW-DNSLB-01: Configure Azure DNS`. Custom App Service domain mapping also appears under `CP-APP-05`.

## 1. The problem DNS solves

People use names such as:

```text
www.contoso.com
```

Computers need an address such as an IPv4 or IPv6 address. **DNS (Domain Name System)** translates a name into an address or another DNS name.

```text
www.contoso.com  ──DNS lookup──>  address or target name  ──connection──> service
```

DNS answers **where should the client try to connect?** It does not itself:

- prove that you own a domain;
- authorize a user;
- encrypt HTTPS traffic;
- route HTTP requests between application servers;
- replace a firewall or NSG.

This distinction is central to the App Service question: one DNS record verifies ownership, while another record directs client traffic.

## 2. Public DNS and Azure DNS

**Azure Public DNS** is a DNS hosting service. It stores public DNS zones and records using Azure tools, permissions, APIs, and billing.

A **DNS zone** is the administrative container for a domain, such as:

```text
contoso.com
```

A **record** inside the zone provides an answer for a name, such as:

```text
www.contoso.com
```

Azure DNS does not automatically become authoritative for a domain merely because you created a zone. At the domain registrar, you delegate the domain to the Azure DNS name servers shown for the zone.

The public resolution path is:

```text
Browser
  -> recursive DNS resolver
  -> authoritative name servers for contoso.com
  -> record in the Azure DNS public zone
  -> returned address or target
  -> browser connects to the service
```

If delegation is missing or incorrect, records in the Azure zone may be correct but public clients will not use them.

## 3. Important DNS record types

| Record | Purpose | Example |
|---|---|---|
| `A` | Maps a name to an IPv4 address | `contoso.com -> 203.0.113.10` |
| `AAAA` | Maps a name to an IPv6 address | `contoso.com -> 2001:db8::10` |
| `CNAME` | Makes one name an alias of another name | `www.contoso.com -> contoso.azurewebsites.net` |
| `TXT` | Stores text used for verification, policy, or other metadata | `asuid.www -> verification-token` |
| `MX` | Identifies mail servers for a domain | `contoso.com -> mail.contoso.com` |
| `NS` | Identifies authoritative name servers | `contoso.com -> Azure DNS name servers` |
| `SOA` | Stores authority and zone metadata | zone serial and timing values |
| `PTR` | Reverse lookup from address to name | address -> `vm01.contoso.com` |
| `SRV` | Identifies a service, port, and target | service discovery |

For AZ-104, do not memorize record types as an isolated list. Ask what the client needs:

- an IPv4 address: `A`;
- an IPv6 address: `AAAA`;
- an alias to another hostname: `CNAME`;
- proof or metadata: `TXT`;
- email routing: `MX`.

## 4. The App Service custom-domain question

Question:

> You need to configure an Azure web app named `contoso.azurewebsites.net` to host `www.contoso.com`. What should you do first?

The important words are:

- existing App Service hostname: `contoso.azurewebsites.net`;
- desired custom hostname: `www.contoso.com`;
- custom-domain ownership must be verified before the mapping is completed.

There are two separate DNS jobs:

```text
1. Prove ownership of the custom domain
2. Direct client traffic to the App Service
```

### Domain verification record

App Service provides a **domain verification ID**. You publish it as a TXT record so App Service can check that you control the DNS zone.

For a subdomain such as `www.contoso.com`, current Microsoft documentation shows the verification record as:

```text
Type:  TXT
Host:  asuid.www
Value: <domain verification ID shown by App Service>
```

Some exam questions or DNS-provider interfaces simplify the host label to `asuid`, especially when discussing a root-domain scenario. Follow the exact host label shown by the App Service custom-domain dialog. The important concept is:

```text
TXT + asuid host + App Service verification ID
```

`asuid` is not the application name and not an IP address. It is the conventional App Service verification label used with the verification token.

### Traffic mapping record

For the `www` subdomain, the recommended mapping is normally:

```text
Type:  CNAME
Host:  www
Value: contoso.azurewebsites.net
```

This means:

```text
www.contoso.com -> contoso.azurewebsites.net
```

A CNAME is preferred for a subdomain because the App Service IP address can change. The alias remains pointed at the stable App Service hostname.

For a root domain such as `contoso.com`, a CNAME generally cannot be used in the ordinary DNS model. App Service uses an `A` record to the app IP, plus the TXT verification record.

### Why the TXT record comes first

The question asks what to do **first**. Before App Service accepts the custom-domain binding, it needs evidence that you control the domain. Therefore:

```text
First: publish the TXT verification record
Then: publish the CNAME mapping for www
Then: validate and add the custom domain in App Service
```

The answer you chose was wrong in two ways:

```text
TXT www.contoso.com = contoso.azurewebsites.net
```

1. `TXT` is not the normal record for directing web traffic.
2. `contoso.azurewebsites.net` is the CNAME target, not the TXT verification value.

The verification TXT value must be the token generated by App Service.

## 5. How to reason about custom-domain questions

Use this sequence:

1. Is the desired name a root domain or a subdomain?
2. Is the question asking for ownership verification or traffic mapping?
3. Which record type performs that job?
4. Is the value an App Service token, an IP address, or a hostname?
5. Does the DNS provider's host field include the zone name automatically?

For this question:

```text
Desired name: www.contoso.com
First operation: prove ownership
Record: TXT
Host: asuid.www (or the exact label shown by App Service)
Value: App Service domain verification ID
```

Then the traffic record is:

```text
CNAME www -> contoso.azurewebsites.net
```

The general rule is:

```text
TXT = verification/metadata
CNAME = hostname alias
A = IPv4 address
```

## 6. Azure Private DNS

**Azure Private DNS** resolves names inside linked virtual networks. It is not the same thing as Azure Public DNS.

A private DNS zone might be:

```text
internal.contoso.com
```

A VM could resolve:

```text
db.internal.contoso.com -> 10.20.2.4
```

The record is private and is not intended to be returned to arbitrary internet clients.

A private DNS zone must be linked to a virtual network before resources in that VNet can use it for resolution:

```text
Private DNS zone
        │ virtual network link
        ▼
VNet -> VM DNS query -> private record -> private IP
```

The link is the glue. Creating the zone alone does not make every VNet resolve it.

### Autoregistration

A virtual network link can enable VM autoregistration. Azure then creates and maintains VM hostname records in the private zone as VMs are created, change IP addresses, or are deleted.

### Multiple VNets

A private zone can be linked to multiple VNets. This supports name resolution across environments or regions. DNS resolution and network connectivity are separate concerns:

```text
Private DNS can resolve the name
but the VNets still need a valid network path to exchange traffic.
```

Peering, VPN, or ExpressRoute may be needed for the actual packet path.

### Split-horizon DNS

A public and private zone can use the same domain name but return different answers depending on where the query originates:

```text
Internet client: www.contoso.com -> public address
Internal client: www.contoso.com -> private address
```

This is called split-horizon DNS.

## 7. Private endpoints and DNS

A private endpoint gives a PaaS resource a private IP address in a VNet. DNS must direct the service hostname to that private IP for clients to use the private path.

Typical flow:

```text
Client in VNet
  -> resolves service name
  -> private DNS record returns private endpoint IP
  -> route reaches private endpoint
  -> private endpoint connects to the PaaS resource
```

A private endpoint without the correct DNS resolution path is a common failure:

```text
Name resolves to public IP -> client uses public path
```

The private endpoint may exist and the NSG may be correct, but the client still does not use it because DNS returned the wrong address.

Azure Private DNS zones are commonly used with Private Link. The exact zone depends on the Azure service, so in practice use the service's Private Endpoint DNS configuration guidance rather than guessing the zone name.

## 8. Azure-provided DNS, custom DNS, and Private Resolver

Azure VNets provide Azure DNS by default for basic name resolution. A VNet can also be configured to use custom DNS servers, such as:

- an on-premises DNS server reachable through VPN or ExpressRoute;
- a DNS server running on an Azure VM;
- Azure DNS Private Resolver.

Changing the VNet DNS setting changes which resolver clients use. It does not automatically create records or guarantee connectivity to the chosen DNS server.

**Azure DNS Private Resolver** provides managed inbound and outbound DNS forwarding for hybrid environments without requiring you to operate DNS server VMs.

For AZ-104, understand the choice conceptually:

| Requirement | Suitable concept |
|---|---|
| Host a public domain in Azure | Azure Public DNS zone |
| Resolve private names in VNets | Azure Private DNS zone + VNet link |
| Use an existing enterprise DNS system | Custom DNS or forwarding |
| Connect Azure and on-premises DNS without DNS VMs | Azure DNS Private Resolver |

## 9. DNS versus load balancing

DNS chooses or returns a destination name/address. A load balancer distributes packets or connections among backend instances.

```text
DNS:             Which frontend should the client use?
Load balancer:   Which healthy backend should receive this connection?
```

Azure Traffic Manager is a **DNS-based traffic load balancer**. It returns DNS answers according to a routing method and endpoint health. It does not sit in the packet path like an application gateway or load balancer.

For AZ-104, keep these separate:

- Azure DNS: host and resolve DNS records;
- Traffic Manager: DNS-based global endpoint selection;
- Load Balancer: Layer 4 traffic distribution;
- Application Gateway: Layer 7 HTTP(S) routing and features.

## 10. Troubleshooting DNS questions

When a client cannot reach a service by name, separate the failure stages:

```text
1. Does the name resolve?
2. Does it resolve to the intended IP or target?
3. Is there a route to that address?
4. Is traffic allowed by NSGs, firewalls, or the service?
5. Is the application listening and healthy?
```

Useful local commands include:

```bash
nslookup www.contoso.com
```

or:

```bash
dig www.contoso.com
```

These test name resolution only. Successful DNS resolution does not prove that TCP port 443 is reachable or that the web application is healthy.

For an App Service custom domain, check:

- the CNAME or A record;
- the TXT verification record and exact token;
- whether the domain is public rather than private;
- DNS propagation and caching;
- the custom hostname binding in App Service;
- the TLS certificate binding for HTTPS.

## AZ-104 decision checklist

When you see an Azure DNS question, ask:

1. Is this public or private name resolution?
2. Is Azure hosting the DNS zone, or is it merely using an external DNS provider?
3. Is the requirement ownership verification, name-to-name aliasing, or name-to-IP mapping?
4. Which record type fits: `TXT`, `CNAME`, `A`, or `AAAA`?
5. If private, is the DNS zone linked to the correct VNet?
6. If a private endpoint is involved, does DNS return the private endpoint IP?
7. Is the question actually about Traffic Manager or a load balancer rather than DNS hosting?

## What to prioritize for AZ-104

### High priority

- DNS translates names to addresses or target names.
- Azure Public DNS hosts public DNS zones.
- A zone must be delegated to authoritative name servers.
- `A`, `AAAA`, `CNAME`, and `TXT` record purposes.
- App Service custom-domain verification with `asuid` and a verification ID.
- CNAME mapping for an App Service subdomain.
- Azure Private DNS zones and VNet links.
- DNS resolution versus routing and authorization.
- Private endpoint DNS integration.
- The difference between Azure DNS, Traffic Manager, and a load balancer.

### Lower priority

- Memorizing every portal field.
- Detailed DNS resolver implementation internals.
- Rare record-type edge cases not present in the requirement.
- Operating your own DNS servers when Azure-managed DNS meets the requirement.

## Retrieval check

Explain this without looking at the note:

> A user wants `www.fabrikam.com` to reach an App Service whose default hostname is `fabrikam.azurewebsites.net`. App Service asks for a verification record before the custom domain can be added.

A complete answer should say:

1. Publish a TXT record containing the App Service domain verification ID, using the `asuid` label shown by App Service.
2. Publish a CNAME record for `www` pointing to `fabrikam.azurewebsites.net`.
3. Validate and add the custom hostname in App Service.
4. Configure TLS separately if HTTPS is required.

## Official references

- [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure DNS overview](https://learn.microsoft.com/en-us/azure/dns/dns-overview)
- [Host your domain in Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-delegate-domain-azure-dns)
- [Azure Private DNS overview](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview)
- [Set up an existing custom domain name for an App Service app](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)
- [Azure DNS Private Resolver overview](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview)
- [Azure Traffic Manager overview](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview)
