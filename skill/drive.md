---
name: drive
category: utility
description: "Google Drive client for the commandline"
tags: [drive, utility, google-drive, cloud-storage]
author: oxo-call-community
source_url: "https://github.com/odeke-em/drive"
---

## Concepts

- **Tool Overview**: drive is a command-line client for Google Drive, enabling file uploads, downloads, and management.
- **Core Function**: Provides command-line interface for interacting with Google Drive storage.
- **Input/Output**: Input: Local files/directories. Output: Remote files on Google Drive.
- **Algorithm**: Uses Google Drive API for authentication and file operations.
- **Key Features**: File syncing, folder management, sharing, version history, batch operations.
- **Installation**: `conda install -c bioconda drive`

## Pitfalls

- **Authentication**: Requires Google account authentication and API credentials.
- **Rate Limits**: Google Drive API has rate limits that can affect large operations.
- **File Size**: Maximum file size limits apply for uploads.
- **Permissions**: Ensure proper permissions for shared drives and folders.
- **Network Issues**: Requires stable internet connection for operations.

## Examples

### Upload file
**Args:** `upload --file local_file.txt --folder remote_folder/`
**Explanation:** Uploads a local file to Google Drive folder.

### Download file
**Args:** `download --file remote_file.txt --output local_file.txt`
**Explanation:** Downloads a file from Google Drive to local system.

### Sync directory
**Args:** `sync --source local_dir/ --destination remote_dir/`
**Explanation:** Synchronizes local directory with Google Drive directory.

### List files
**Args:** `list --folder remote_folder/`
**Explanation:** Lists files in a Google Drive folder.

### Share file
**Args:** `share --file file.txt --email user@example.com --permission read`
**Explanation:** Shares a file with specified user with read permissions.