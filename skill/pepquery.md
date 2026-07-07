---
name: pepquery
category: expression
description: PepQuery identifies and validates novel peptides.
tags: [pepquery, expression, peptide, validation]
author: oxo-call-community
source_url: "https://github.com/bzhanglab/PepQuery"
---

## Concepts

- **Tool Overview**: PepQuery searches novel peptides.
- **Core Function**: Identifies and validates peptide sequences.
- **Algorithm**: Uses peptide-centric search engine.
- **Input Format**: Accepts peptide and MS data files.
- **Output**: Produces peptide identifications.
- **Use Case**: Proteomics, novel peptide discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Peptide Quality**: Results depend on peptide quality.
- **MS Data**: Requires proper MS data format.
- **Runtime**: Search may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pepquery --help`
**Explanation:** Shows available options and usage instructions.

### Search peptides
**Args:** `pepquery -i peptides.txt -m ms_data.mgf -o results.txt`
**Explanation:** Searches for novel peptides.

### With database
**Args:** `pepquery -i peptides.txt -m ms_data.mgf -d protein.fasta -o results.txt`
**Explanation:** Uses protein database for search.

### Verbose mode
**Args:** `pepquery -v -i peptides.txt -m ms_data.mgf -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pepquery -t 4 -i peptides.txt -m ms_data.mgf -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pepquery -i peptides.txt -m ms_data.mgf -o results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pepquery -i peptides.txt -m ms_data.mgf -o results.txt --report report.html`
**Explanation:** Generates HTML report.