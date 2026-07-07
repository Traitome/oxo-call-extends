---
name: marvd2
category: metagenomics
description: Metagenomic Archaeal Virus Detector 2
tags: [marvd2, metagenomics, virus-detection]
author: oxo-call-community
source_url: "https://bitbucket.org/MAVERICLab/marvd2"
---

## Concepts

- **Tool Overview**: marvd2 v0.11.9 - MARVD2 (Metagenomic Archaeal Virus Detector 2) identifies archaeal viruses from metagenomic data.
- **Core Function**: Detects and identifies archaeal viruses from metagenomic sequencing data.
- **Input/Output**: Input: Metagenomic reads/contigs (FASTA/FASTQ); Output: Viral sequences, taxonomy assignments.
- **Installation**: `conda install -c bioconda marvd2`
- **Archaeal Viruses**: Specifically designed for detecting archaeal viruses.
- **Metagenomic Analysis**: Analyzes complex metagenomic datasets.

## Pitfalls

- **Sequence Quality**: Poor quality sequences affect detection.
- **Database Completeness**: Incomplete databases miss novel viruses.
- **Memory Usage**: Large datasets require significant memory.
- **False Positives**: May identify non-viral sequences as viral.
- **Computational Time**: Complex analyses may take time.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.

## Examples

### Detect archaeal viruses
**Args:** `marvd2 -i contigs.fasta -o viruses.fasta`
**Explanation:** Identifies archaeal viruses from contigs.

### With taxonomy
**Args:** `marvd2 -i contigs.fasta -o viruses.fasta --taxonomy`
**Explanation:** Includes taxonomy assignments.

### Multiple files
**Args:** `marvd2 -i fasta/ -o viruses.fasta`
**Explanation:** Processes multiple FASTA files.

### Verbose mode
**Args:** `marvd2 -i contigs.fasta -o viruses.fasta -v`
**Explanation:** Provides detailed logging during analysis.

### Generate report
**Args:** `marvd2 -i contigs.fasta -o viruses.fasta --report`
**Explanation:** Generates detection report.

### Custom threshold
**Args:** `marvd2 -i contigs.fasta -o viruses.fasta -t 0.8`
**Explanation:** Sets detection threshold to 0.8.