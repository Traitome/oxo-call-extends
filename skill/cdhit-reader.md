---
name: cdhit-reader
category: sequence-analysis
description: Parse CD-HIT cluster files
tags: [cdhit-reader, cd-hit, cluster-analysis, parsing]
author: oxo-call-community
source_url: "https://github.com/telatin/cdhit-parser"
---

## Concepts

- **Tool Overview**: cdhit-reader parses CD-HIT cluster (.clstr) files for analysis.
- **Core Function**: Reads and analyzes CD-HIT clustering results.
- **Input**: CD-HIT cluster file (.clstr) and optionally the original FASTA file.
- **Output**: Parsed cluster information in various formats.
- **Application**: Analyzing sequence clustering results and extracting cluster statistics.
- **Installation**: Install via bioconda: `conda install -c bioconda cdhit-reader`

## Pitfalls

- **Cluster File Format**: Requires properly formatted CD-HIT .clstr files.
- **FASTA Matching**: When extracting sequences, FASTA file must match original clustering input.
- **Large Files**: May require memory for very large cluster files.
- **Version Compatibility**: Works with standard CD-HIT output format.

## Examples

### Parse cluster file
**Args:** `cdhit-reader clusters.clstr`
**Explanation:** Parses CD-HIT cluster file and outputs summary.

### Extract representative sequences
**Args:** `cdhit-reader -i clusters.clstr -f sequences.fa -o representatives.fa`
**Explanation:** Extracts representative sequences from clusters.

### Output CSV format
**Args:** `cdhit-reader -i clusters.clstr --csv -o clusters.csv`
**Explanation:** Outputs cluster information in CSV format.

### Display help
**Args:** `cdhit-reader --help`
**Explanation:** Shows all available options and usage information.