---
name: dxua
category: utility
description: "command-line tool for uploading files to the DNAnexus Platform"
tags: [dxua, utility, DNAnexus, upload, cloud-storage]
author: oxo-call-community
source_url: "https://documentation.dnanexus.com/user/objects/uploading-and-downloading-files/batch/upload-agent"
---

## Concepts

- **Tool Overview**: dxua (DNAnexus Upload Agent) is a command-line tool for efficient file uploads to the DNAnexus platform.
- **Core Function**: Provides fast, resumable file uploads with parallel transfer capabilities.
- **Input/Output**: Input: Local files to upload. Output: Uploaded files on DNAnexus platform.
- **Algorithm**: Uses parallel upload streams and checksum verification for reliable transfers.
- **Key Features**: Parallel uploads, resume capability, checksum verification, batch processing, progress reporting.
- **Installation**: `conda install -c bioconda dxua`

## Pitfalls

- **Authentication**: Requires valid DNAnexus credentials.
- **Network Stability**: Large uploads may fail on unstable connections.
- **Storage Costs**: Uploaded files consume DNAnexus storage quota.
- **File Size Limits**: Very large files may require special handling.
- **Concurrent Uploads**: Too many parallel uploads may overwhelm the connection.

## Examples

### Upload single file
**Args:** `dxua upload file.txt --project project-xxxx`
**Explanation:** Uploads a single file to DNAnexus project.

### Upload directory
**Args:** `dxua upload data/ --project project-xxxx --recursive`
**Explanation:** Recursively uploads entire directory.

### Resume upload
**Args:** `dxua upload large_file.bam --project project-xxxx --resume`
**Explanation:** Resumes interrupted upload of large file.

### Parallel upload
**Args:** `dxua upload files/ --project project-xxxx --threads 8`
**Explanation:** Uses 8 parallel threads for faster uploads.

### Upload with metadata
**Args:** `dxua upload file.txt --project project-xxxx --property key=value`
**Explanation:** Uploads file with custom metadata properties.