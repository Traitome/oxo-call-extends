---
name: pridepy
category: programming
description: pridepy is a Python client library for the PRIDE Rest API.
tags: [pridepy, programming, api, proteomics]
author: oxo-call-community
source_url: "https://github.com/PRIDE-Archive/pridepy"
---

## Concepts

- **Tool Overview**: pridepy interacts with PRIDE database.
- **Core Function**: API client for proteomics data.
- **Algorithm**: Uses REST API methods.
- **Input Format**: Accepts API queries.
- **Output**: Produces proteomics data.
- **Use Case**: Proteomics data retrieval.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **API Rate Limits**: May have access restrictions.
- **Network Issues**: Requires internet connection.
- **Data Availability**: Depends on PRIDE database.
- **Authentication**: May require credentials.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import pridepy; help(pridepy)"`
**Explanation:** Shows available options and usage instructions.

### Search PRIDE
**Args:** `python -c "from pridepy import PrideClient; client = PrideClient(); results = client.search_projects('cancer')"`
**Explanation:** Searches PRIDE database for projects.

### Get project details
**Args:** `python -c "from pridepy import PrideClient; client = PrideClient(); project = client.get_project('PXD000001')"`
**Explanation:** Retrieves project details.

### List files
**Args:** `python -c "from pridepy import PrideClient; client = PrideClient(); files = client.get_project_files('PXD000001')"`
**Explanation:** Lists project files.

### Download file
**Args:** `python -c "from pridepy import PrideClient; client = PrideClient(); client.download_file('PXD000001', 'file.mzML')"`
**Explanation:** Downloads file from PRIDE.

### Verbose mode
**Args:** `python -c "from pridepy import PrideClient; client = PrideClient(verbose=True)"`
**Explanation:** Runs with verbose output.

### Generate report
**Args:** `python script.py --report report.html`
**Explanation:** Generates HTML report.