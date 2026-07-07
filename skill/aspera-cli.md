---
name: aspera-cli
category: utility
description: Aspera CLI - Command Line Interface for IBM Aspera high-speed file transfer
tags: [aspera-cli, utility, file-transfer, high-speed, ibm, bioinformatics]
author: oxo-call-community
source_url: "https://www.rubydoc.info/gems/aspera-cli"
---

## Concepts

- **Tool Overview**: Aspera CLI is the command-line interface for IBM Aspera products, enabling high-speed file transfers over standard networks. Version 4.20.0.
- **Core Function**: Provides fast, secure file transfer capabilities using Aspera's FASP protocol for efficient data movement.
- **FASP Protocol**: Uses Aspera's Fast, Adaptive, Secure Protocol for high-speed transfers regardless of network conditions.
- **High Performance**: Transfers data at line speed with minimal latency, ideal for large bioinformatics datasets.
- **Secure Transfer**: Supports encryption and authentication for secure data transmission.
- **Cloud Integration**: Works with cloud storage providers and Aspera on Cloud for seamless data movement.
- **Input/Output**: Transfers files and directories between local and remote systems.
- **Installation**: `conda install -c bioconda aspera-cli` or install from IBM.

## Pitfalls

- **License Required**: Requires valid Aspera license for commercial use. Evaluation licenses available.
- **Network Configuration**: May require firewall configuration for FASP protocol (UDP ports).
- **Authentication**: Requires proper credentials (password, API key, or SSH key).
- **Transfer Limits**: Some Aspera deployments have transfer size or speed limits.
- **Dependency**: Requires Aspera Connect client for some operations.
- **Version Compatibility**: CLI version must match Aspera server version.

## Examples

### Display help
**Args:** `aspera-cli --help`
**Explanation:** Shows all available command-line options and subcommands.

### Basic file transfer
**Args:** `aspera-cli transfer --source /local/path --destination user@server:/remote/path`
**Explanation:** Transfers local files to remote server using Aspera FASP protocol.

### Download from server
**Args:** `aspera-cli transfer --source user@server:/remote/path --destination /local/path`
**Explanation:** Downloads files from remote server to local system.

### Set transfer speed
**Args:** `aspera-cli transfer --source /local/path --destination user@server:/remote/path --speed 1000m`
**Explanation:** Limits transfer speed to 1000 Mbps. Prevents network saturation.

### Use SSH key authentication
**Args:** `aspera-cli transfer --source /local/path --destination user@server:/remote/path --ssh-key ~/.ssh/id_rsa`
**Explanation:** Uses SSH key for authentication instead of password.

### Transfer directory recursively
**Args:** `aspera-cli transfer --source /local/dir --destination user@server:/remote/dir --recursive`
**Explanation:** Transfers entire directory tree including all subdirectories.

### Check transfer status
**Args:** `aspera-cli transfer --status transfer_id`
**Explanation:** Checks status of ongoing or completed transfer.

### Transfer to Aspera on Cloud
**Args:** `aspera-cli transfer --source /local/path --destination aspera://cloud.example.com/workspace`
**Explanation:** Transfers files to Aspera on Cloud workspace.

### Resume interrupted transfer
**Args:** `aspera-cli transfer --source /local/path --destination user@server:/remote/path --resume`
**Explanation:** Resumes previously interrupted transfer from last checkpoint.