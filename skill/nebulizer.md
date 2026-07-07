---
name: nebulizer
category: utility
description: Nebulizer provides command-line utilities to manage users, data libraries and tools in a Galaxy bioinformatics instance.
tags: [nebulizer, utility, galaxy, bioinformatics, workflow]
author: oxo-call-community
source_url: "https://github.com/pjbriggs/nebulizer"
---

## Concepts

- **Tool Overview**: Nebulizer is a command-line tool for managing Galaxy bioinformatics instances.
- **Core Function**: Enables programmatic management of Galaxy users, data libraries, tools, and workflows.
- **Algorithm**: Interfaces with Galaxy's REST API to perform administrative tasks.
- **Input Format**: Accepts command-line arguments and configuration files.
- **Output**: Produces status reports and performs administrative actions on Galaxy instances.
- **Use Case**: Automating Galaxy administration, managing multiple Galaxy instances, workflow deployment.

## Pitfalls

- **Galaxy Version**: Compatibility depends on Galaxy version and API availability.
- **Authentication**: Requires API key or credentials for Galaxy instance access.
- **Network Dependency**: Requires network access to Galaxy server.
- **Permissions**: Requires appropriate administrative privileges.
- **Rate Limiting**: Galaxy may enforce rate limits on API requests.
- **Version Differences**: Options may vary between versions.

## Examples

### Display help
**Args:** `nebulizer --help`
**Explanation:** Shows available options and usage instructions.

### List users
**Args:** `nebulizer list_users -g https://galaxy.example.com -k api_key`
**Explanation:** Lists all users on Galaxy instance.

### Create user
**Args:** `nebulizer create_user -g https://galaxy.example.com -k api_key -u newuser -e email@example.com`
**Explanation:** Creates new user account.

### List tools
**Args:** `nebulizer list_tools -g https://galaxy.example.com -k api_key`
**Explanation:** Lists all tools installed on Galaxy instance.

### Import workflow
**Args:** `nebulizer import_workflow -g https://galaxy.example.com -k api_key -w workflow.ga`
**Explanation:** Imports workflow into Galaxy instance.

### Export data library
**Args:** `nebulizer export_library -g https://galaxy.example.com -k api_key -l library_name -o output/`
**Explanation:** Exports data library from Galaxy instance.