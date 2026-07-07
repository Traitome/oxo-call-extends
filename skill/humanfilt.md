---
name: humanfilt
category: qc
description: WGS human-read filtering with auto-downloaded human references
tags: [humanfilt, host removal, contamination, WGS]
author: oxo-call-community
source_url: "https://github.com/jprehn-lab/humanfilt"
---

## Concepts

- **Tool Overview**: humanfilt is a pipeline for removing human reads from whole-genome sequencing data using multiple aligners and auto-downloaded human reference sequences.
- **Multi-aligner Approach**: Combines multiple alignment tools (Bowtie2, BWA, Minimap2) for comprehensive host read detection.
- **Auto-reference Download**: Automatically downloads and builds human reference databases including GRCh38 and alternative references.
- **Quality Control Integration**: Includes trimming (Trim Galore!) and deduplication (fastuniq) steps as part of the filtering pipeline.
- **Taxonomic Filtering**: Integrates Kraken2 for additional taxonomic classification and filtering.
- **Installation**: `conda install -c bioconda humanfilt`

## Pitfalls

- **Reference Download Time**: Initial reference download can be time-consuming due to large genome files; consider pre-downloading.
- **Memory Requirements**: Aligners like BWA and Bowtie2 require significant memory for large reference indexes; allocate sufficient resources.
- **Paired-end Handling**: Ensure proper handling of paired-end reads; mispaired reads can cause unexpected filtering behavior.
- **Adapter Contamination**: Trim adapters before human filtering to avoid spurious alignments.
- **Sensitivity vs Specificity**: Adjust alignment parameters based on desired sensitivity; stricter filters may remove true microbial reads.
- **Output File Management**: Filtering generates multiple intermediate files; ensure adequate disk space.

## Examples

### Basic human read filtering
**Args:** `humanfilt -i input_R1.fastq.gz -i2 input_R2.fastq.gz -o filtered/`
**Explanation:** Filters human reads from paired-end FASTQ files and outputs non-human reads to the specified directory.

### With custom reference genome
**Args:** `humanfilt -i input.fastq.gz -r /path/to/human_reference.fasta -o filtered/`
**Explanation:** Uses a custom human reference genome instead of auto-downloading.

### Include Kraken2 filtering
**Args:** `humanfilt -i input.fastq.gz -k -o filtered/`
**Explanation:** Enables Kraken2-based taxonomic filtering in addition to alignment-based filtering.

### Single-end read processing
**Args:** `humanfilt -i single_end.fastq.gz --single-end -o filtered/`
**Explanation:** Processes single-end sequencing data instead of paired-end.

### Specify aligners to use
**Args:** `humanfilt -i input_R1.fastq.gz -i2 input_R2.fastq.gz -a bowtie2 -a bwa -o filtered/`
**Explanation:** Uses only Bowtie2 and BWA aligners for host read detection.