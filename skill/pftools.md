---
name: pftools
category: utility
description: pftools analyzes biomolecular sequence motifs.
tags: [pftools, utility, motif, profile]
author: oxo-call-community
source_url: "https://github.com/sib-swiss/pftools3"
---

## Concepts

- **Tool Overview**: pftools analyzes sequence motifs.
- **Core Function**: Uses generalized profile syntax.
- **Algorithm**: Uses profile-based motif detection.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces motif annotations.
- **Use Case**: Motif analysis, sequence interpretation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequence sets require memory.
- **Profile Quality**: Results depend on profile quality.
- **Motif Detection**: May miss distant motifs.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pftools --help`
**Explanation:** Shows available options and usage instructions.

### Search motifs
**Args:** `pftools -i sequences.fasta -p profiles.txt -o motifs.txt`
**Explanation:** Searches for sequence motifs.

### With profile
**Args:** `pftools -i sequences.fasta -p profile.prf -o motifs.txt`
**Explanation:** Uses specific profile for search.

### Verbose mode
**Args:** `pftools -v -i sequences.fasta -p profiles.txt -o motifs.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pftools -t 4 -i sequences.fasta -p profiles.txt -o motifs.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pftools -i sequences.fasta -p profiles.txt -o motifs.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pftools -i sequences.fasta -p profiles.txt -o motifs.txt --report report.html`
**Explanation:** Generates HTML report.