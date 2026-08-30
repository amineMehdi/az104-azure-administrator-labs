@minLength(3)
param suffix string
@description('Globally unique Storage account name')
param storageName string

var tags = { purpose: 'az104-lab', labId: '26', workload: 'capstone' }

resource vnet 'Microsoft.Network/virtualNetworks@2024-05-01' = {
  name: 'vnet-${suffix}'
  location: resourceGroup().location
  tags: tags
  properties: {
    addressSpace: { addressPrefixes: [ '10.26.0.0/16' ] }
    subnets: [
      { name: 'web', properties: { addressPrefix: '10.26.1.0/24' } }
      { name: 'private-endpoints', properties: { addressPrefix: '10.26.2.0/24', privateEndpointNetworkPolicies: 'Disabled' } }
    ]
  }
}

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageName
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
  tags: tags
  properties: { supportsHttpsTrafficOnly: true, minimumTlsVersion: 'TLS1_2', allowBlobPublicAccess: false, publicNetworkAccess: 'Disabled' }
}

resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: 'law-${suffix}'
  location: resourceGroup().location
  tags: tags
  properties: { retentionInDays: 30, sku: { name: 'PerGB2018' } }
}

resource publicIp 'Microsoft.Network/publicIPAddresses@2024-05-01' = {
  name: 'pip-${suffix}'
  location: resourceGroup().location
  tags: tags
  sku: { name: 'Standard' }
  properties: { publicIPAllocationMethod: 'Static' }
}

resource loadBalancer 'Microsoft.Network/loadBalancers@2024-05-01' = {
  name: 'lb-${suffix}'
  location: resourceGroup().location
  tags: tags
  sku: { name: 'Standard' }
  properties: { frontendIPConfigurations: [ { name: 'frontend', properties: { publicIPAddress: { id: publicIp.id } } } ] }
}

output virtualNetworkId string = vnet.id
output storageId string = storage.id
output workspaceId string = workspace.id
output loadBalancerId string = loadBalancer.id
