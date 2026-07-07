---
name: scsplit
category: single-cell
description: scSplit - Genotype-free demultiplexing of pooled single-cell RNA-Seq
tags: ["scsplit", "single-cell", "demultiplexing", "RNA-seq"]
author: oxo-call-community
source_url: "https://github.com/jon-xu/scSplit"
---

## Concepts

- **Tool Overview**: scSplit (v1.0.8.2) performs genotype-free demultiplexing of pooled single-cell RNA-Seq data.
- **Core Function**: Demultiplexes pooled single-cell RNA-seq data without requiring genotype information.
- **Algorithm**: Uses k-mer-based approach for sample identification.
- **Input/Output**: Accepts BAM files and produces demultiplexed FASTQ files.
- **Genotype-Free**: Does not require prior genotype information for demultiplexing.
- **Applications**: Single-cell RNA-seq demultiplexing, pooled sequencing analysis.

## Pitfalls

- **Data Quality**: Results depend on sequencing depth and quality.
- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May incorrectly assign reads to samples.
- **Sample Overlap**: May struggle with highly similar samples.

## Examples

### Basic demultiplexing
**Args:** `scsplit demultiplex -i aligned.bam -o demultiplexed/`
**Explanation:** `-i` input BAM; `-o` output directory.

### With reference
**Args:** `scsplit demultiplex -i aligned.bam -r reference.fasta -o demultiplexed/`
**Explanation:** `-r` specifies reference genome.

### Quality filtering
**Args:** `scsplit demultiplex -i aligned.bam -q 20 -o demultiplexed/`
**Explanation:** `-q 20` filters reads with quality below 20.

### Verbose logging
**Args:** `scsplit demultiplex -i aligned.bam -v -o demultiplexed/`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `scsplit demultiplex -i aligned.bam -t 8 -o demultiplexed/`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Output FASTQ
**Args:** `scsplit demultiplex -i aligned.bam --fastq -o demultiplexed/`
**Explanation:** Outputs FASTQ files instead of BAM.

### Sample sheet
**Args:** `scsplit demultiplex -i aligned.bam -s samples.csv -o demultiplexed/`
**Explanation:** `-s` specifies sample sheet for known barcodes.