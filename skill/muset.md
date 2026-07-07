---
name: muset
category: alignment
description: A pipeline for building an abundance unitig matrix from FASTA/FASTQ files
tags: [muset, metagenomics, unitig, abundance-matrix, k-mer, reads]
author: oxo-call-community
source_url: "https://github.com/CamilaDuitama/muset"
---

## Concepts

- **Tool Overview**: MUSET v0.5.1 is a pipeline for constructing abundance unitig matrices from metagenomic sequencing data. It builds unitigs (unique k-mer stretches) and quantifies their abundance across multiple samples.
- **Core Function**: Combines k-mer counting, unitig graph construction, and abundance estimation to produce a sample-by-unitig abundance matrix. Useful for metagenomic profiling and comparative analysis.
- **Algorithm**: Uses de Bruijn graph approaches to construct unitigs from input reads. Each unitig represents a maximal unique k-mer sequence. Abundance is estimated by mapping reads back to unitigs.
- **Input Format**: Accepts FASTA/FASTQ files from multiple samples. Files can be gzipped. Each sample should be provided as separate input file.
- **Output**: Produces a tab-delimited abundance matrix with samples as columns and unitigs as rows. Also outputs unitig sequences in FASTA format.
- **Installation**: Available via Bioconda (`conda install -c bioconda muset`). Requires Python and k-mer counting dependencies.

## Pitfalls

- **K-mer Size Selection**: Default k-mer size may not be optimal for all datasets. Longer k-mers increase uniqueness but reduce sensitivity. Consider dataset characteristics when choosing.
- **Memory Requirements**: K-mer counting and graph construction can be memory-intensive for large datasets. Ensure sufficient RAM for your dataset size.
- **Sample Naming**: Output matrix uses input file names as sample identifiers. Use consistent and informative file naming before running.
- **Paired-end Reads**: MUSET may handle paired-end data in specific ways. Check documentation for proper input format for paired files.
- **Empty Unitigs**: Some unitigs may have zero abundance in certain samples. These can be filtered based on minimum abundance thresholds.
- **Version Availability**: MUSET is relatively specialized. Check Bioconda for current version availability and potential dependency issues.

## Examples

### Basic usage with single sample
**Args:** `muset -i sample1.fastq -o output/`
**Explanation:** Processes a single sample FASTQ file and outputs abundance matrix. Output directory will contain matrix and unitig sequence files.

### Multiple sample input
**Args:** `muset -i sample1.fastq sample2.fastq sample3.fastq -o output/`
**Explanation:** Processes multiple samples together, constructing a combined unitig set and individual abundance profiles for each sample.

### Specify k-mer size
**Args:** `muset -i input.fq -k 31 -o output/`
**Explanation:** Uses k-mer size of 31 (default may differ). Longer k-mers produce more unique unitigs but require more memory.

### Gzipped input files
**Args:** `muset -i sample1.fastq.gz sample2.fastq.gz -o output/`
**Explanation:** MUSET can directly process gzipped FASTQ files without decompression. Saves disk space and preprocessing time.

### Set minimum abundance threshold
**Args:** `muset -i input.fq -m 5 -o output/`
**Explanation:** Filters out unitigs with abundance less than 5 across all samples. Reduces matrix size and removes rare k-mers that may be sequencing errors.
