---
name: csi-ssu
category: expression
description: CSI SSU screening tool for genomic and transcriptomic data
tags: [csi-ssu, expression, rRNA, SSU, screening, classification]
author: oxo-call-community
source_url: "https://github.com/AlexTiceLab/CSI-SSU/blob/main/README.md"
---

## Concepts

- **Tool Overview**: csi-ssu (v1.0.3+) is a command-line tool for screening and classifying Small Subunit (SSU) ribosomal RNA sequences from genomic and transcriptomic data.
- **Core Function**: Identifies SSU sequences using phylogenetic placement and provides taxonomic classification based on reference databases.
- **Input/Output**: Input: FASTA or FASTQ sequence files. Output: Classified sequences, taxonomic reports, and screening statistics.
- **Database**: Uses SILVA rRNA database for reference alignments and taxonomic classification.
- **Key Features**: Supports both short-read and long-read sequencing data, provides confidence scores for classifications, and generates visual summaries.
- **Installation**: `conda install -c bioconda csi-ssu`

## Pitfalls

- **Database Download**: First run requires database download; use `csi-ssu download` to initialize.
- **Sequence Quality**: Low-quality sequences may produce unreliable classifications; pre-filter with quality trimming.
- **Memory Requirements**: Large input files may require significant memory; consider splitting large datasets.
- **Taxonomic Resolution**: Classification accuracy depends on reference database completeness for specific taxa.
- **Output Formats**: Multiple output files are generated; ensure output directory exists before running.

## Examples

### Download reference database
**Args:** `csi-ssu download`
**Explanation:** Download and initialize the SILVA reference database for SSU classification.

### Screen FASTQ reads for SSU sequences
**Args:** `csi-ssu screen -i reads.fastq -o results/ --threads 8`
**Explanation:** Screen raw sequencing reads to identify and classify SSU rRNA sequences using 8 threads.

### Classify FASTA sequences
**Args:** `csi-ssu classify -i sequences.fasta -o classifications.tsv --confidence 0.9`
**Explanation:** Classify sequences with a minimum confidence threshold of 0.9 and output results to TSV file.
