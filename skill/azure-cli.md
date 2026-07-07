---
name: azure-cli
category: utility
description: Microsoft Azure CLI - Command-line interface for managing Azure resources
tags: [azure-cli, cloud, azure, storage, azure-storage]
author: oxo-call-community
source_url: "https://github.com/azure/azure-cli"
---

## Concepts

- **Tool Overview**: Azure CLI is Microsoft's cross-platform command-line interface for managing Azure resources and services. Version 0.10.3.
- **Core Function**: Provides command-line access to Azure services including storage, compute, networking, and analytics.
- **Cross-Platform**: Works on Windows, macOS, and Linux operating systems.
- **Azure Resource Management**: Enables creation, management, and deletion of Azure resources.
- **Blob Storage**: Supports interaction with Azure Blob storage for data upload/download.
- **Virtual Machines**: Allows management of Azure virtual machines.
- **Azure Active Directory**: Integrates with Azure AD for authentication and access control.
- **Installation**: `conda install -c bioconda azure-cli` or download from Azure website.

## Pitfalls

- **Authentication**: Requires Azure account login. Use `az login` to authenticate.
- **Region Selection**: Must specify correct Azure region for resource deployment.
- **Subscription Management**: Multiple subscriptions require careful selection.
- **Rate Limiting**: Azure API calls have rate limits. Exceeding limits causes throttling.
- **Cost Management**: Azure services incur costs. Monitor usage to avoid unexpected charges.
- **Network Access**: Requires internet connection for Azure service access.

## Examples

### Login to Azure
**Args:** `az login`
**Explanation:** Authenticates with Azure using web browser or device code.

### List Azure subscriptions
**Args:** `az account list --output table`
**Explanation:** Displays all Azure subscriptions associated with the logged-in account.

### Set active subscription
**Args:** `az account set --subscription "My Subscription Name"`
**Explanation:** Sets the specified subscription as the active context for subsequent commands.

### Create resource group
**Args:** `az group create --name my-resource-group --location eastus`
**Explanation:** Creates a new resource group in the specified region.

### List blob containers
**Args:** `az storage container list --account-name mystorageaccount --output table`
**Explanation:** Lists all containers in the specified Azure storage account.

### Upload file to blob storage
**Args:** `az storage blob upload --account-name mystorageaccount --container-name mycontainer --name remotefile.txt --file localfile.txt`
**Explanation:** Uploads local file to Azure Blob storage container.

### Download file from blob storage
**Args:** `az storage blob download --account-name mystorageaccount --container-name mycontainer --name remotefile.txt --file localfile.txt`
**Explanation:** Downloads file from Azure Blob storage to local filesystem.

### Create virtual machine
**Args:** `az vm create --resource-group my-resource-group --name my-vm --image UbuntuLTS --admin-username azureuser --generate-ssh-keys`
**Explanation:** Creates a new Ubuntu VM with SSH key authentication.

### List virtual machines
**Args:** `az vm list --resource-group my-resource-group --output table`
**Explanation:** Lists all VMs in the specified resource group.

### Create storage account
**Args:** `az storage account create --name mystorageaccount --resource-group my-resource-group --location eastus --sku Standard_LRS`
**Explanation:** Creates new storage account with locally redundant storage.

### Delete resource group
**Args:** `az group delete --name my-resource-group --yes`
**Explanation:** Deletes resource group and all associated resources.

### Check Azure CLI version
**Args:** `az --version`
**Explanation:** Displays current Azure CLI version and component versions.