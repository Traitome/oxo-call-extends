---
name: ncbi-fcs-gx
category: alignment
description: NCBI Foreign Contamination Screen (FCS-GX) is a genomic cross-species aligner for contamination detection.
tags: [ncbi-fcs-gx, alignment, contamination, screening, ncbi]
author: oxo-call-community
source_url: "https://github.com/ncbi/fcs"
---

## Concepts

- **Tool Overview**: NCBI FCS-GX is a tool for detecting foreign DNA contamination in genomic sequences.
- **Core Function**: Identifies contaminating sequences from other species using cross-species alignment.
- **Algorithm**: Uses sequence alignment against a comprehensive database of known organisms.
- **Input Format**: Accepts FASTA files containing assembled genomic sequences.
- **Output**: Produces reports identifying potential contaminants and their likely sources.
- **Use Case**: Quality control for genome assemblies, detecting cross-contamination in sequencing projects.

## Pitfalls

- **Database Dependencies**: Requires up-to-date reference database for accurate results.
- **False Positives**: May report false positives for highly conserved sequences.
- **Computational Cost**: Can be computationally intensive for large sequences.
- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Processing large genomes requires significant memory.
- **Reference Bias**: May miss contaminants from unrepresented species.

## Examples

### Display help
**Args:** `fcs-gx --help`
**Explanation:** Shows available options and usage instructions.

### Basic contamination screening
**Args:** `fcs-gx -i input.fasta -o contamination_report.tsv`
**Explanation:** Detects foreign contamination in input sequence.

### Custom database
**Args:** `fcs-gx -i input.fasta -d custom_db/ -o report.tsv`
**Explanation:** Uses custom reference database for screening.

### Fast mode
**Args:** `fcs-gx -i input.fasta --fast -o report.tsv`
**Explanation:** Runs screening in fast mode with reduced sensitivity.

### Output HTML report
**Args:** `fcs-gx -i input.fasta --html -o report.html`
**Explanation:** Generates HTML report with visualizations.

### Threads
**Args:** `fcs-gx -i input.fasta -t 8 -o report.tsv`
**Explanation:** Uses 8 threads for parallel processing.