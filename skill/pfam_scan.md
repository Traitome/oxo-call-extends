---
name: pfam_scan
category: variant-calling
description: pfam_scan searches sequences against Pfam HMM library.
tags: [pfam_scan, variant-calling, pfam, domain]
author: oxo-call-community
source_url: "http://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/"
---

## Concepts

- **Tool Overview**: pfam_scan annotates protein domains.
- **Core Function**: Searches sequences against Pfam HMMs.
- **Algorithm**: Uses HMMER v3 for domain search.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces domain annotations.
- **Use Case**: Protein annotation, domain analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequence sets require memory.
- **HMM Library**: Requires proper Pfam HMM library.
- **Domain Detection**: May miss distant domains.
- **Runtime**: Search may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pfam_scan.pl --help`
**Explanation:** Shows available options and usage instructions.

### Scan sequences
**Args:** `pfam_scan.pl -i proteins.fasta -o domains.txt`
**Explanation:** Scans sequences for Pfam domains.

### With HMM library
**Args:** `pfam_scan.pl -i proteins.fasta -d Pfam-A.hmm -o domains.txt`
**Explanation:** Uses specific HMM library.

### Verbose mode
**Args:** `pfam_scan.pl -v -i proteins.fasta -o domains.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pfam_scan.pl -t 4 -i proteins.fasta -o domains.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pfam_scan.pl -i proteins.fasta -o domains.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pfam_scan.pl -i proteins.fasta -o domains.txt --report report.html`
**Explanation:** Generates HTML report.