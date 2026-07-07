---
name: clippy
category: utility
description: Intuitive and interactive peak caller for CLIP data
tags: [clippy, clip-seq, peak-calling, rna-binding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ulelab/clippy"
---

## Concepts

- **Tool Overview**: Clippy is an intuitive and interactive peak caller specifically designed for CLIP (Cross-Linking and ImmunoPrecipitation) sequencing data analysis.
- **Core Function**: Identifies and annotates binding sites (peaks) from CLIP-seq experiments with interactive visualization capabilities.
- **Algorithm**: Uses statistical methods to detect significant peaks from CLIP-seq data with user-friendly interactive interface.
- **Input**: Aligned CLIP-seq reads (BAM/SAM) and optional control data.
- **Output**: Peak calls in BED format with confidence scores and visualization.
- **Application**: RNA-binding protein analysis, post-transcriptional regulation studies.
- **Installation**: Install via bioconda: `conda install -c bioconda clippy`

## Pitfalls

- **Data Quality**: Requires high-quality CLIP-seq data for accurate peak calling.
- **Control Data**: Control experiments recommended for background subtraction.
- **Parameter Tuning**: May require adjustment of peak calling parameters.
- **Computational Resources**: May require significant resources for large datasets.
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Call peaks from CLIP data
**Args:** `clippy -i clip_alignments.bam -o peaks.bed`
**Explanation:** Identifies binding peaks from CLIP-seq aligned reads.

### With control data
**Args:** `clippy -i clip.bam -c control.bam -o peaks.bed`
**Explanation:** Uses control data for background subtraction.

### Interactive mode
**Args:** `clippy -i clip.bam --interactive`
**Explanation:** Opens interactive visualization and peak selection interface.

### Display help
**Args:** `clippy --help`
**Explanation:** Shows all available options and usage information.