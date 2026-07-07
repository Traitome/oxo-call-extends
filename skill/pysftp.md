---
name: pysftp
category: utility
description: PySFTP is a friendly Python interface for SFTP file transfer operations.
tags: [pysftp, utility, sftp, file-transfer]
author: oxo-call-community
source_url: "https://bitbucket.org/dundeemt/pysftp"
---

## Concepts

- **Tool Overview**: pysftp transfers files via SFTP.
- **Core Function**: Secure file transfer.
- **Algorithm**: Uses SSH protocol.
- **Input Format**: Accepts file paths.
- **Output**: Produces transferred files.
- **Use Case**: File transfer.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Connection**: Must be stable.
- **Authentication**: Must be correct.
- **Permissions**: Must be set properly.
- **File Size**: Large files may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pysftp --help`
**Explanation:** Shows available options and usage instructions.

### Upload file
**Args:** `pysftp upload -l local.txt -r remote.txt -s server`
**Explanation:** Uploads file to server.

### With parameters
**Args:** `pysftp upload -l local.txt -p params.yaml -s server`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pysftp -v upload -l local.txt -s server`
**Explanation:** Runs with verbose output.

### Download file
**Args:** `pysftp download -r remote.txt -l local.txt -s server`
**Explanation:** Downloads file from server.

### List files
**Args:** `pysftp list -s server -d /path`
**Explanation:** Lists remote directory.

### Generate report
**Args:** `pysftp upload -l local.txt -s server --report report.html`
**Explanation:** Generates HTML report.