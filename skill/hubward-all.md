---
name: hubward-all
category: alignment
description: hubward-all is a meta-package that bundles hubward along with bedtools and UCSC genome browser tools for genomic data processing and visualization.
tags: [hubward-all, alignment, BED, UCSC, bedtools]
author: oxo-call-community
source_url: "https://bioconda.github.io/recipes/hubward-all/"
---

## Concepts

- **Meta-package Overview**: hubward-all is a conda meta-package that installs hubward and its dependencies including bedtools and UCSC tools.
- **bedtools Integration**: Comprehensive suite for genomic interval operations (intersect, merge, subtract, coverage).
- **UCSC Tools**: Includes utilities like liftOver, bedGraphToBigWig, bedToBigBed for genome browser data preparation.
- **CrossMap**: Tool for liftover between genome assemblies.
- **Hubward**: Tool for creating UCSC Genome Browser hubs.
- **Installation**: `conda install -c bioconda hubward-all`

## Pitfalls

- **Meta-package**: Individual tool versions may vary; check dependencies for specific versions.
- **Coordinate Systems**: UCSC tools use 0-based coordinates for BED format.
- **Genome Assemblies**: liftOver requires appropriate chain files for target assembly.
- **BigWig/BigBed**: Index files required for efficient access.
- **Memory Requirements**: Some operations on large files may require significant memory.
- **Tool Specificity**: Different tools have different input requirements and formats.

## Examples

### Intersect BED files
**Args:** `bedtools intersect -a peaks.bed -b genes.bed -o result.bed`
**Explanation:** Finds overlapping regions between peaks and genes BED files.

### Convert BED to BigBed
**Args:** `bedToBigBed genes.bed chrom.sizes genes.bb`
**Explanation:** Converts a BED file to BigBed format for UCSC Genome Browser visualization.

### Liftover coordinates
**Args:** `liftOver input.bed hg19ToHg38.over.chain output.bed unMapped.bed`
**Explanation:** Converts coordinates from hg19 to hg38 assembly.

### Convert bedGraph to BigWig
**Args:** `bedGraphToBigWig coverage.bg chrom.sizes coverage.bw`
**Explanation:** Converts a bedGraph file to BigWig format for track visualization.

### Merge overlapping intervals
**Args:** `bedtools merge -i peaks.bed -o merged_peaks.bed`
**Explanation:** Merges overlapping or adjacent intervals in a BED file.