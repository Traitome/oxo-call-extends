---
name: bamm
category: metagenomics
description: BamM - Metagenomics-focused BAM file manipulation tool
tags: [bamm, metagenomics, BAM, manipulation, coverage]
author: oxo-call-community
source_url: "https://ecogenomics.github.io/BamM"
---

## Concepts

- **Tool Overview**: BamM is a metagenomics-focused BAM file manipulation tool designed for processing and analyzing metagenomic alignment data. Version 1.7.3.
- **Core Function**: Provides specialized BAM operations for metagenomic data analysis and manipulation.
- **Metagenomics Focus**: Optimized for handling complex metagenomic datasets with multiple species.
- **Coverage Calculation**: Computes coverage metrics across metagenomic alignments.
- **BAM Processing**: Supports various BAM manipulation operations tailored for metagenomics.
- **Input/Output**: Accepts BAM alignment files, outputs processed BAM files or coverage statistics.
- **Installation**: `conda install -c bioconda bamm`.

## Pitfalls

- **Metagenomics Specific**: Designed for metagenomic data. May not be optimal for single-species analysis.
- **Complexity**: Metagenomic data complexity requires careful parameter tuning.
- **Memory Usage**: Large metagenomic BAM files may require significant memory.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Calculate coverage
**Args:** `bamm coverage -i alignments.bam -o coverage.txt`
**Explanation:** Computes coverage statistics from metagenomic BAM file.

### Filter by coverage
**Args:** `bamm filter -i alignments.bam -o filtered.bam --min-coverage 5`
**Explanation:** Filters reads based on coverage threshold.

### Merge BAM files
**Args:** `bamm merge -i sample1.bam sample2.bam -o merged.bam`
**Explanation:** Merges multiple metagenomic BAM files.

### Extract specific taxa
**Args:** `bamm extract -i alignments.bam -o species.bam --taxon "Escherichia coli"`
**Explanation:** Extracts reads aligning to specific taxon.

### Coverage histogram
**Args:** `bamm histogram -i alignments.bam -o coverage_hist.png`
**Explanation:** Generates coverage histogram visualization.

### Verbose mode
**Args:** `bamm coverage -i alignments.bam -o coverage.txt -v`
**Explanation:** Shows detailed processing information.

### Display help
**Args:** `bamm --help`
**Explanation:** Shows all available command-line options and usage information.