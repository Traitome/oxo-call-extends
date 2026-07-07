---
name: rdrpcatch
category: utility
description: RdRpCATCH is an RNA virus RdRp (RNA-dependent RNA polymerase) sequence scanner for virus detection.
tags: [rdrpcatch, utility, virus-detection, rna-virus]
author: oxo-call-community
source_url: "https://github.com/dimitris-karapliafis/RdRpCATCH"
---

## Concepts

- **Tool Overview**: rdrpcatch scans viruses.
- **Core Function**: RdRp detection.
- **Algorithm**: Uses scanning methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces virus matches.
- **Use Case**: Virus detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Scanning may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rdrpcatch --help`
**Explanation:** Shows available options and usage instructions.

### Scan for viruses
**Args:** `rdrpcatch scan -i sequences.fasta -o virus_matches.txt`
**Explanation:** Scans for RdRp sequences.

### With parameters
**Args:** `rdrpcatch scan -i sequences.fasta -p params.yaml -o virus_matches.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rdrpcatch -v scan -i sequences.fasta -o virus_matches.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rdrpcatch -t 4 scan -i sequences.fasta -o virus_matches.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `rdrpcatch scan -i sequences.fasta -d virus_db.fasta -o virus_matches.txt`
**Explanation:** Uses virus database.

### Generate report
**Args:** `rdrpcatch scan -i sequences.fasta -o virus_matches.txt --report report.html`
**Explanation:** Generates HTML report.