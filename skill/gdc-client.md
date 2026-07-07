---
name: gdc-client
category: data-transfer
description: GDC Data Transfer Tool for downloading and uploading data from the Genomic Data Commons.
tags: [gdc-client, gdc, data-transfer, cancer-genomics]
author: oxo-call-community
source_url: "https://docs.gdc.cancer.gov/Data_Transfer_Tool/Users_Guide/Getting_Started"
---

## Concepts
- **GDC Data Access**: Official tool for accessing data from NCI's Genomic Data Commons.
- **Secure Authentication**: Supports OAuth2 authentication for controlled access data.
- **Parallel Downloads**: Enables parallel downloading for faster data retrieval.
- **Resumable Transfers**: Supports resuming interrupted downloads.
- **Manifest Files**: Uses manifest files to specify datasets for download.

## Pitfalls
- **Authentication Required**: Controlled access data requires eRA Commons account.
- **Network Stability**: Large files require stable network connection.
- **Rate Limiting**: GDC imposes rate limits on API requests.
- **File Size**: Some genomic files can be extremely large (>100GB).
- **Data Integrity**: Always verify downloaded files using checksums.

## Examples
### Download data using manifest
**Args:** `gdc-client download -m manifest.txt -d ./downloads`
**Explanation:** Downloads all files listed in the manifest file to the specified directory.

### Upload data to GDC
**Args:** `gdc-client upload -m manifest.txt -d ./data_to_upload`
**Explanation:** Uploads data files to GDC using a manifest file.

### Download with multiple threads
**Args:** `gdc-client download -m manifest.txt -t 8 -d ./downloads`
**Explanation:** Downloads files using 8 parallel threads for faster transfer.

### Resume interrupted download
**Args:** `gdc-client download -m manifest.txt -d ./downloads --resume`
**Explanation:** Resumes a previously interrupted download session.

### Verify file integrity
**Args:** `gdc-client verify -m manifest.txt -d ./downloads`
**Explanation:** Verifies downloaded files against checksums in the manifest.