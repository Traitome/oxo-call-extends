---
name: ngseqbasic
category: alignment
description: NGseqBasic performs basic ChIP/DNaseI/ATAC analysis from FASTQ to track visualization.
tags: [ngseqbasic, alignment, chip-seq, atac-seq]
author: oxo-call-community
source_url: "http://userweb.molbiol.ox.ac.uk/public/telenius/NGseqBasicManual/external/instructionsBioconda.html"
---

## Concepts

- **Tool Overview**: NGseqBasic provides end-to-end analysis for ChIP-seq, DNase-seq, and ATAC-seq data.
- **Core Function**: Processes raw reads through alignment to visualization.
- **Algorithm**: Combines read mapping, peak calling, and track generation.
- **Input Format**: Accepts FASTQ files and reference genome.
- **Output**: Produces aligned BAM files, peaks, and visualization tracks.
- **Use Case**: Epigenomics analysis, chromatin accessibility studies, and transcription factor binding.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Genome**: Requires indexed reference genome.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Output Size**: Track files can be large.

## Examples

### Display help
**Args:** `ngseqbasic --help`
**Explanation:** Shows available options and usage instructions.

### Run ChIP-seq analysis
**Args:** `ngseqbasic -i reads.fastq -r reference.fasta -o output/ -t chip`
**Explanation:** Runs ChIP-seq analysis pipeline.

### ATAC-seq analysis
**Args:** `ngseqbasic -i reads.fastq -r reference.fasta -o output/ -t atac`
**Explanation:** Runs ATAC-seq analysis pipeline.

### DNase-seq analysis
**Args:** `ngseqbasic -i reads.fastq -r reference.fasta -o output/ -t dnase`
**Explanation:** Runs DNase-seq analysis pipeline.

### Paired-end reads
**Args:** `ngseqbasic -i reads_1.fastq -i2 reads_2.fastq -r reference.fasta -o output/`
**Explanation:** Processes paired-end sequencing data.

### Threads
**Args:** `ngseqbasic -i reads.fastq -r reference.fasta -o output/ -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `ngseqbasic -i reads.fastq -r reference.fasta -o output/ -q 20`
**Explanation:** Filters reads by quality score.