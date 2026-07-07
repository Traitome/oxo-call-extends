---
name: lusstr
category: annotation
description: Tool for converting NGS sequence data of forensic STR loci to various annotation styles
tags: [lusstr, annotation, forensic, STR]
author: oxo-call-community
source_url: "https://www.github.com/bioforensics/lusSTR"
---

## Concepts

- **Tool Overview**: lusstr v0.11 is a tool for converting NGS sequence data of forensic STR (Short Tandem Repeat) loci to various annotation styles.
- **Core Function**: Converts raw STR sequence data to standardized forensic annotation formats.
- **STR Loci**: Supports various forensic STR loci including CODIS markers.
- **Input/Output**: Input: FASTA/FASTQ sequences or aligned BAM files; Output: Annotated STR alleles in various formats.
- **Installation**: `conda install -c bioconda lusstr`
- **Key Features**: Supports multiple annotation styles, handles mixed STR types, forensic-grade accuracy.

## Pitfalls

- **Sequence Quality**: Requires high-quality sequence data for accurate STR calling.
- **Locus Coverage**: May fail if STR loci are not adequately covered.
- **Repeat Complexity**: Complex repeat structures may affect calling accuracy.
- **Allele Ladder**: Requires reference allele ladder for proper sizing.
- **Software Updates**: Forensic standards may change requiring tool updates.
- **Validation**: Results should be validated against known reference samples.

## Examples

### Convert STR sequences
**Args:** `lusstr -i str_sequences.fasta -o annotations.txt`
**Explanation:** Converts STR sequences to annotated format.

### Specific loci
**Args:** `lusstr -i str_sequences.fasta -l CODIS -o annotations.txt`
**Explanation:** Processes only CODIS loci.

### Output format
**Args:** `lusstr -i str_sequences.fasta -f csv -o annotations.csv`
**Explanation:** Outputs results in CSV format.

### Minimum quality
**Args:** `lusstr -i str_sequences.fasta -q 30 -o annotations.txt`
**Explanation:** Filters reads with quality < 30.

### Verbose mode
**Args:** `lusstr -i str_sequences.fasta -v -o annotations.txt`
**Explanation:** Outputs detailed processing information.

### Help documentation
**Args:** `lusstr --help`
**Explanation:** Displays all available options and parameters.