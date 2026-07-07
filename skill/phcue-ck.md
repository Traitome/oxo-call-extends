---
name: phcue-ck
category: formatting
description: phcue-ck retrieves FTP URLs for FASTQ files from ENA.
tags: [phcue-ck, formatting, ftp, ena]
author: oxo-call-community
source_url: "https://lgi-onehealth.github.io/phcue-ck"
---

## Concepts

- **Tool Overview**: phcue-ck retrieves ENA URLs.
- **Core Function**: Gets FTP URLs for FASTQ files.
- **Algorithm**: Uses ENA API access.
- **Input Format**: Accepts ENA accession numbers.
- **Output**: Produces FTP URL lists.
- **Use Case**: Data retrieval, ENA access.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large queries require memory.
- **Network Access**: Requires internet connection.
- **ENA Access**: Requires proper ENA access.
- **Runtime**: Retrieval may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phcue-ck --help`
**Explanation:** Shows available options and usage instructions.

### Retrieve URLs
**Args:** `phcue-ck -i accession.txt -o urls.txt`
**Explanation:** Retrieves FTP URLs from ENA.

### With parameters
**Args:** `phcue-ck -i accession.txt -p params.yaml -o urls.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phcue-ck -v -i accession.txt -o urls.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phcue-ck -t 4 -i accession.txt -o urls.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phcue-ck -i accession.txt -o urls.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phcue-ck -i accession.txt -o urls.txt --report report.html`
**Explanation:** Generates HTML report.