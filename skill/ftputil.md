---
name: ftputil
category: programming
description: High-level FTP client library (virtual file system and more).
tags: [ftputil, FTP, file transfer, Python]
author: oxo-call-community
source_url: "http://ftputil.sschwarzer.net/"
---

## Concepts
- **FTP Client Library**: High-level Python library for FTP operations.
- **Virtual File System**: Treats FTP servers as local file systems.
- **Recursive Operations**: Supports recursive file transfers.
- **Context Managers**: Supports Python context managers for resource handling.
- **Error Handling**: Comprehensive error handling for FTP operations.

## Pitfalls
- **Network Dependence**: Requires stable network connection.
- **Server Compatibility**: May have issues with non-standard FTP servers.
- **Security**: FTP is not secure; use FTPS or SFTP for sensitive data.
- **Passive Mode**: May require passive mode for firewalled connections.
- **Encoding Issues**: May have issues with non-ASCII file names.

## Examples
### Connect to FTP server
**Args:** `python -c "import ftputil; with ftputil.FTPHost('server', 'user', 'pass') as host: print(host.listdir('/'))"`
**Explanation:** Connects to FTP server and lists directory contents.

### Download file
**Args:** `python -c "import ftputil; ftputil.FTPHost('server', 'user', 'pass').download('remote.txt', 'local.txt')"`
**Explanation:** Downloads file from FTP server.

### Upload file
**Args:** `python -c "import ftputil; ftputil.FTPHost('server', 'user', 'pass').upload('local.txt', 'remote.txt')"`
**Explanation:** Uploads file to FTP server.

### Recursive directory download
**Args:** `python -c "import ftputil; ftputil.FTPHost('server', 'user', 'pass').download_dir('remote_dir', 'local_dir')"`
**Explanation:** Downloads entire directory recursively.

### List directory
**Args:** `python -c "import ftputil; print(ftputil.FTPHost('server', 'user', 'pass').listdir('/'))"`
**Explanation:** Lists files in remote directory.