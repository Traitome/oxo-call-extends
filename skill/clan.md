---
name: clan
category: utility
description: CrossLinked reads ANalysis tool for analyzing cross-linked sequencing data
tags: [clan, crosslink, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/clan-mapping/"
---

## Concepts

- **Tool Overview**: CLAN (CrossLinked reads ANalysis) is a tool for analyzing cross-linked sequencing data, used to study protein-DNA interactions and chromatin structure.
- **Core Function**: Processes and analyzes cross-linked sequencing reads to identify protein-binding sites and chromatin interactions.
- **Algorithm**: Identifies cross-linked read pairs and maps them to reference genome to detect interaction sites.
- **Input**: Cross-linked sequencing reads (FASTQ) and reference genome.
- **Output**: Interaction sites and binding profiles.
- **Application**: Chromatin interaction analysis, protein-DNA binding studies, and 3D genome architecture research.
- **Installation**: Install via bioconda: `conda install -c bioconda clan`

## Pitfalls

- **Data Type**: Designed specifically for cross-linked sequencing data.
- **Reference Genome**: Must match the reference used for alignment.
- **Data Quality**: Requires high-quality cross-linked data.
- **Complexity**: May require computational resources for large datasets.
- **Parameter Tuning**: May require adjustment of analysis parameters.

## Examples

### Analyze cross-linked reads
**Args:** `clan -i reads.fastq -g genome.fasta -o interactions.txt`
**Explanation:** Analyzes cross-linked sequencing reads to identify interaction sites.

### With paired-end data
**Args:** `clan -1 read1.fastq -2 read2.fastq -g genome.fasta -o interactions.txt`
**Explanation:** Processes paired-end cross-linked sequencing data.

### Specify fragment size
**Args:** `clan -i reads.fastq -g genome.fasta -f 500 -o interactions.txt`
**Explanation:** Uses specific fragment size for analysis.

### Display help
**Args:** `clan --help`
**Explanation:** Shows all available options and usage information.