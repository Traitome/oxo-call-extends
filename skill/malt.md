---
name: malt
category: alignment
description: A tool for mapping metagenomic data
tags: [malt, alignment, metagenomics, mapping]
author: oxo-call-community
source_url: "http://ab.inf.uni-tuebingen.de/software/malt/"
---

## Concepts

- **Tool Overview**: malt v0.62 - MALT (MEGAN Alignment Tool) is a high-performance aligner specifically designed for metagenomic sequence data.
- **Core Function**: Maps metagenomic reads to reference databases for taxonomic and functional analysis.
- **Input/Output**: Input: FASTQ reads, reference database; Output: SAM/BAM alignments, taxonomic assignments.
- **Installation**: `conda install -c bioconda malt`
- **Metagenomics Optimization**: Optimized for the unique challenges of metagenomic data analysis.
- **MEGAN Integration**: Designed to work seamlessly with MEGAN for downstream analysis.

## Pitfalls

- **Database Size**: Large reference databases require significant storage.
- **Memory Usage**: Mapping requires substantial RAM for database loading.
- **Taxonomic Bias**: Reference database composition affects classification.
- **Read Length**: Short reads may map to multiple taxa ambiguously.
- **Sensitivity/Speed**: Trade-off between mapping sensitivity and speed.
- **Output Size**: Large output files require efficient storage.

## Examples

### Map reads to reference
**Args:** `malt-run -i reads.fastq -d reference_db -o mappings.sam`
**Explanation:** Maps metagenomic reads to reference database.

### Paired-end mapping
**Args:** `malt-run -i read1.fastq -j read2.fastq -d reference_db -o mappings.sam`
**Explanation:** Maps paired-end reads to reference.

### BAM output
**Args:** `malt-run -i reads.fastq -d reference_db -o mappings.bam -b`
**Explanation:** Outputs alignments in BAM format.

### Build database
**Args:** `malt-build -i reference.fasta -o reference_db`
**Explanation:** Creates MALT index from reference sequences.

### Sensitive mode
**Args:** `malt-run -i reads.fastq -d reference_db -o mappings.sam --sensitive`
**Explanation:** Runs in sensitive mode for better mapping.

### Quick mode
**Args:** `malt-run -i reads.fastq -d reference_db -o mappings.sam --quick`
**Explanation:** Runs in quick mode for faster mapping.