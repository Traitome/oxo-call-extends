---
name: pykofamsearch
category: utility
description: pykofamsearch performs KEGG Orthology (KO) annotation using HMM profiles.
tags: [pykofamsearch, utility, kegg, orthology]
author: oxo-call-community
source_url: "https://github.com/jolespin/pykofamsearch"
---

## Concepts

- **Tool Overview**: pykofamsearch annotates KEGG Orthology.
- **Core Function**: KO assignment via HMM.
- **Algorithm**: Uses HMMER algorithms.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces KO annotations.
- **Use Case**: Functional annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **HMM Database**: Requires KOfam database.
- **E-value Threshold**: Affects sensitivity.
- **Runtime**: Search may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pykofamsearch --help`
**Explanation:** Shows available options and usage instructions.

### Run KO search
**Args:** `pykofamsearch search -i proteins.fasta -d kofam_db/ -o annotations.txt`
**Explanation:** Annotates sequences with KEGG Orthology.

### With parameters
**Args:** `pykofamsearch search -i proteins.fasta -p params.yaml -o annotations.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pykofamsearch -v search -i proteins.fasta -o annotations.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pykofamsearch -t 4 search -i proteins.fasta -o annotations.txt`
**Explanation:** Uses 4 threads for parallel processing.

### E-value cutoff
**Args:** `pykofamsearch search -i proteins.fasta -e 0.001 -o annotations.txt`
**Explanation:** Sets E-value cutoff.

### Generate report
**Args:** `pykofamsearch search -i proteins.fasta -o annotations.txt --report report.html`
**Explanation:** Generates HTML report.