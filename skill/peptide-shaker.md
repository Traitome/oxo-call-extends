---
name: peptide-shaker
category: expression
description: PeptideShaker interprets proteomics identification results.
tags: [peptide-shaker, expression, proteomics, identification]
author: oxo-call-community
source_url: "https://compomics.github.io/projects/peptide-shaker.html"
---

## Concepts

- **Tool Overview**: PeptideShaker interprets proteomics results.
- **Core Function**: Combines multiple search engine results.
- **Algorithm**: Uses multi-engine integration approach.
- **Input Format**: Accepts search engine output files.
- **Output**: Produces protein identifications.
- **Use Case**: Proteomics, protein identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Search Engine**: Requires proper search engine results.
- **PTM Localization**: May have localization errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peptide-shaker --help`
**Explanation:** Shows available options and usage instructions.

### Analyze results
**Args:** `peptide-shaker -i search_results.mzid -o peptide_report.txt`
**Explanation:** Interprets proteomics identification results.

### With database
**Args:** `peptide-shaker -i search_results.mzid -d protein.fasta -o peptide_report.txt`
**Explanation:** Uses protein database for interpretation.

### Verbose mode
**Args:** `peptide-shaker -v -i search_results.mzid -o peptide_report.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peptide-shaker -t 4 -i search_results.mzid -o peptide_report.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peptide-shaker -i search_results.mzid -o peptide_report.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peptide-shaker -i search_results.mzid -o peptide_report.txt --report report.html`
**Explanation:** Generates HTML report.