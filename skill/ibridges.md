---
name: ibridges
category: data-management
description: iBridges is a Python library for accessing data and metadata on iRODS servers.
tags: [ibridges, data-management, iRODS, Python, data-storage]
author: oxo-call-community
source_url: "https://ibridges.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: iBridges (v2.0.1) is a Python wrapper around python-irodsclient that simplifies interaction with iRODS data management servers.
- **iRODS Integration**: Enables seamless access to iRODS (Integrated Rule-Oriented Data System) for secure data storage and sharing.
- **Cross-Platform**: Works on Windows, Mac OS, and Linux with Python 3.8+.
- **Core Functionality**: Supports data upload/download, metadata management, synchronization, and ticket-based access control.
- **Interactive Authentication**: Provides interactive login for iRODS sessions.
- **Installation**: `pip install ibridges` or `conda install -c bioconda ibridges`

## Pitfalls

- **iRODS Configuration**: Requires properly configured `irods_environment.json` file for authentication.
- **Server Compatibility**: Requires iRODS server version 4.2.11+ or 4.3.0+.
- **Network Dependencies**: Performance depends on network connectivity to the iRODS server.
- **File Size Limits**: Very large file transfers may require special handling or chunking.
- **Metadata Complexity**: iRODS metadata operations have specific syntax requirements.
- **Session Management**: Proper session closing is essential to avoid connection leaks.

## Examples

### Basic file upload
**Args:** `ibridges upload /local/path/file.txt /irods/path/`
**Explanation:** Uploads a local file to the specified iRODS collection.

### Download data from iRODS
**Args:** `ibridges download /irods/path/file.txt /local/destination/`
**Explanation:** Downloads a file from iRODS to local filesystem.

### Search by metadata
**Args:** `ibridges search --metadata "project:myproject" /irods/collection/`
**Explanation:** Searches iRODS collection for files matching specified metadata criteria.

### Synchronize local and remote directories
**Args:** `ibridges sync /local/dir/ /irods/collection/ --direction both`
**Explanation:** Bidirectionally synchronizes files between local directory and iRODS collection.

### Create temporary access ticket
**Args:** `ibridges ticket create /irods/path/file.txt --expire 7d`
**Explanation:** Creates a 7-day temporary access ticket for sharing specific files.