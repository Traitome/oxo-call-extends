---
name: percolator
category: expression
description: Percolator identifies peptides from shotgun proteomics data.
tags: [percolator, expression, proteomics, peptide-identification]
author: oxo-call-community
source_url: "https://github.com/percolator/percolator"
---

## Concepts

- **Tool Overview**: Percolator validates peptide identifications.
- **Core Function**: Uses semi-supervised learning for validation.
- **Algorithm**: Uses machine learning scoring.
- **Input Format**: Accepts search engine results.
- **Output**: Produces validated peptide identifications.
- **Use Case**: Proteomics, peptide validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Search Quality**: Results depend on search quality.
- **Training Data**: Requires proper training data.
- **Runtime**: Validation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `percolator --help`
**Explanation:** Shows available options and usage instructions.

### Validate peptides
**Args:** `percolator -i search_results.pin -o validated.txt`
**Explanation:** Validates peptide identifications.

### With decoys
**Args:** `percolator -i search_results.pin -d decoys.pin -o validated.txt`
**Explanation:** Uses decoys for validation.

### Verbose mode
**Args:** `percolator -v -i search_results.pin -o validated.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `percolator -t 4 -i search_results.pin -o validated.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `percolator -i search_results.pin -o validated.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `percolator -i search_results.pin -o validated.txt --report report.html`
**Explanation:** Generates HTML report.