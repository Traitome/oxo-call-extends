---
name: nanocompore
category: epigenomics
description: Nanocompore - Detect RNA modifications from Nanopore direct RNA sequencing
tags: [nanocompore, epigenomics, nanopore, rna-modification, signal, drna-seq]
author: oxo-call-community
source_url: "https://github.com/tleonardi/nanocompore"
---

## Concepts

- **Tool Overview**: Nanocompore v1.0.4 identifies RNA modifications by comparing raw signal changes between two conditions in direct RNA sequencing (dRNA-Seq) data from Oxford Nanopore.
- **Core Function**: Detects RNA modifications by analyzing differences in raw signal characteristics between treated and control samples. RNA modifications affect current levels during sequencing.
- **Algorithm**: Compares event-level signal data from Nanopolish eventalign output between two conditions. Uses statistical tests to identify positions with significant signal differences.
- **Input Format**: Requires eventalign TSV files from Nanopolish for both sample and control conditions. Can also use raw signal data directly from FAST5 files.
- **Output**: Produces tabular results with modification site coordinates, statistical significance values, and effect sizes. Includes visualization tools for exploring results.
- **Use Case**: Epigenomics research, detecting RNA modifications in different biological conditions, studying epitranscriptomics, and identifying modified sites in RNA-seq data.

## Pitfalls

- **Nanopolish Dependency**: Requires preprocessing with Nanopolish eventalign. Proper alignment is critical for accurate results.
- **Replicate Design**: Best results require biological replicates. Single comparisons may produce false positives.
- **Signal Normalization**: Differences in library preparation or sequencing conditions can confound results. Normalize carefully.
- **Modification Types**: Primarily detects modifications that affect current levels (m6A, m5C, etc.). Other modifications may not be detected.
- **False Discovery Rate**: Multiple testing correction is essential. Always apply FDR correction for genome-wide analyses.
- **Read Depth**: Requires sufficient coverage at potential modification sites. Low coverage reduces detection power.

## Examples

### Basic modification detection
**Args:** `-i sample_eventalign.tsv -c control_eventalign.tsv -o output_dir`
**Explanation:** Standard Nanocompore workflow. Compares signal between sample and control.

### Use raw signal files
**Args:** `-f sample_fast5_dir -F control_fast5_dir -o results/`
**Explanation:** Uses raw FAST5 files directly instead of precomputed eventalign data.

### Set significance threshold
**Args:** `-i sample.tsv -c control.tsv -o output/ -p 0.01`
**Explanation:** Uses stricter p-value threshold of 0.01 instead of default.

### Include visualization
**Args:** `-i sample.tsv -c control.tsv -o output/ --plot`
**Explanation:** Generates visualizations of signal differences at modification sites.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.
