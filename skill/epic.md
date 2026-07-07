---
name: epic
category: epigenomics
description: "Chip-Seq broad peak/domain finder."
tags: [epic, epigenomics, ChIP-seq, peak-calling, broad-peaks]
author: oxo-call-community
source_url: "http://github.com/endrebak/epic"
---

## Concepts

- **Tool Overview**: EPIC (Extreme Parameter IC) is a ChIP-seq peak caller specifically designed for identifying broad peaks and domains, such as those associated with histone modifications.
- **Core Function**: Detects broad genomic regions with significant ChIP-seq signal enrichment compared to control samples.
- **Input/Output**: Input: ChIP-seq BAM files (treatment and control), genome size file. Output: Peak calls (BED format), enrichment statistics, visualization tracks.
- **Algorithm**: Uses a Hidden Markov Model (HMM) to identify enriched regions, accounting for spatial correlation and background noise.
- **Key Features**: Broad peak detection, HMM-based calling, background normalization, reproducibility analysis, visualization support.
- **Installation**: `conda install -c bioconda epic`

## Pitfalls

- **Control Sample**: Requires matched control sample for accurate peak calling.
- **Sequencing Depth**: Low coverage may miss weak peaks.
- **Parameter Tuning**: Default parameters may need adjustment for specific datasets.
- **Memory Usage**: Large genomes require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic peak calling
**Args:** `epic --treatment chip.bam --control control.bam --genome hg38 --out peaks.bed`
**Explanation:** Calls broad peaks from ChIP-seq data.

### With custom parameters
**Args:** `epic --treatment chip.bam --control control.bam --genome hg38 --out peaks.bed --threshold 0.01`
**Explanation:** Sets significance threshold to 0.01.

### Output bigWig track
**Args:** `epic --treatment chip.bam --control control.bam --genome hg38 --out peaks.bed --bigwig signal.bw`
**Explanation:** Generates bigWig track for visualization.

### Reproducibility analysis
**Args:** `epic --treatment rep1.bam rep2.bam --control control.bam --genome hg38 --out peaks.bed --reproducibility`
**Explanation:** Analyzes reproducibility across replicates.

### Batch processing
**Args:** `epic --treatment samples/ --control controls/ --genome hg38 --out results/`
**Explanation:** Processes multiple samples in batch mode.