---
name: pmidcite
category: utility
description: pmidcite downloads citation data from PubMed.
tags: [pmidcite, utility, pubmed, citation]
author: oxo-call-community
source_url: "http://github.com/dvklopfenstein/pmidcite"
---

## Concepts

- **Tool Overview**: pmidcite retrieves citation information.
- **Core Function**: PubMed citation data download.
- **Algorithm**: Uses API query methods.
- **Input Format**: Accepts PubMed IDs.
- **Output**: Produces citation results.
- **Use Case**: Literature analysis, bibliometrics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **API Rate Limits**: May hit NCBI rate limits.
- **Network Issues**: Requires internet connection.
- **Data Availability**: Not all papers have citation data.
- **Runtime**: Query may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pmidcite --help`
**Explanation:** Shows available options and usage instructions.

### Download citations
**Args:** `pmidcite -i pmids.txt -o citations.txt`
**Explanation:** Downloads "Cited by" data from PubMed.

### With parameters
**Args:** `pmidcite -i pmids.txt -p params.yaml -o citations.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pmidcite -v -i pmids.txt -o citations.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pmidcite -t 4 -i pmids.txt -o citations.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pmidcite -i pmids.txt -o citations.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pmidcite -i pmids.txt -o citations.txt --report report.html`
**Explanation:** Generates HTML report.