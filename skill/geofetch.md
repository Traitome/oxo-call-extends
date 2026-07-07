---
name: geofetch
category: data-download
description: geofetch - Downloads data and metadata from GEO and SRA and creates standard PEPs.
tags: [geofetch, data-download, GEO, SRA, PEPs]
author: oxo-call-community
source_url: "http://geofetch.databio.org"
---

## Concepts
- **Data Retrieval**: Retrieves data from GEO and SRA.
- **Metadata Management**: Manages experiment metadata.
- **PEP Creation**: Creates Project Execution Plans (PEPs).
- **Data Organization**: Organizes downloaded data.
- **Batch Processing**: Processes multiple experiments.

## Pitfalls
- **Network Dependency**: Requires network connectivity.
- **Data Volume**: Large datasets require storage.
- **Rate Limits**: May hit NCBI rate limits.
- **Authentication**: Requires SRA authentication.
- **Metadata Completeness**: Requires complete metadata.

## Examples
### Download GEO data
**Args:** `geofetch -i GSE12345 -o ./project/`
**Explanation:** Downloads GEO data and creates PEP.

### Download SRA data
**Args:** `geofetch -i SRP12345 -o ./project/`
**Explanation:** Downloads SRA data and creates PEP.

### Batch processing
**Args:** `geofetch -l accessions.txt -o ./projects/`
**Explanation:** Processes multiple accessions.

### Update existing PEP
**Args:** `geofetch -i GSE12345 -u -o ./project/`
**Explanation:** Updates existing PEP with new data.

### Generate report
**Args:** `geofetch -i GSE12345 -r -o report.html`
**Explanation:** Generates download report.