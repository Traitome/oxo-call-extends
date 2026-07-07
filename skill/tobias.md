---
name: tobias
category: analysis
description: TOBIAS - Transcription factor Occupancy prediction By Investigation of ATAC-seq Signal.
tags: [tobias, atac-seq, transcription-factor, footprinting, chromatin-accessibility]
author: oxo-call-community
source_url: "https://github.com/loosolab/TOBIAS"
---

## Concepts

- **Tool Overview**: TOBIAS - A tool for transcription factor binding site prediction from ATAC-seq data.
- **Core Function**: Identifies transcription factor footprints and predicts binding sites from chromatin accessibility data.
- **Input**: ATAC-seq BAM files, genome FASTA, motif databases.
- **Output**: Footprint locations, binding site predictions, TF occupancy scores.
- **Installation**: `pip install pytobias` or `conda install -c bioconda tobias`
- **Use Case**: Transcription factor analysis, regulatory genomics, gene expression regulation.

## Pitfalls

- **Data Quality**: Requires high-quality ATAC-seq data with good signal-to-noise ratio.
- **Motif Database**: Prediction depends on motif database completeness.

## Examples

### Predict TF binding
**Args:** `TOBIAS ATACorrect --bam sample.bam --genome genome.fasta --outdir corrected/`
**Explanation:** Correct ATAC-seq signal and prepare for footprinting.

### Footprinting
**Args:** `TOBIAS FootprintScores --signal corrected.bw --regions peaks.bed --output footprints.bw`
**Explanation:** Calculate footprint scores from ATAC-seq data.
