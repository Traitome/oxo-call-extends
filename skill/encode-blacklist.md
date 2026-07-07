---
name: encode-blacklist
category: utility
description: "The ENCODE Blacklist: Identification of Problematic Regions of the Genome"
tags: [encode-blacklist, utility, ENCODE, genome-analysis, quality-control]
author: oxo-call-community
source_url: "https://github.com/Boyle-Lab/Blacklist"
---

## Concepts

- **Tool Overview**: ENCODE Blacklist is a resource and tool for identifying problematic genomic regions that exhibit anomalous signal in sequencing experiments, particularly in ChIP-seq and ATAC-seq data.
- **Core Function**: Identifies and provides blacklisted genomic regions that should be excluded from analysis due to mapping artifacts or non-specific signal.
- **Input/Output**: Input: Genome assembly version, BED files. Output: Blacklisted regions (BED format), filtered data.
- **Algorithm**: Uses machine learning and statistical methods to detect regions with abnormal read mapping characteristics.
- **Key Features**: Pre-computed blacklists for major genomes, filtering tools, quality control, integration with analysis pipelines, regularly updated.
- **Installation**: `conda install -c bioconda encode-blacklist`

## Pitfalls

- **Genome Version**: Blacklist is genome-specific; use correct version for your data.
- **Data Type**: Blacklist optimized for specific assay types (ChIP-seq, ATAC-seq).
- **Threshold Selection**: Default thresholds may need adjustment for specific datasets.
- **False Positives**: Some legitimate regions may be incorrectly blacklisted.
- **Version Updates**: Regular updates may change blacklist composition.

## Examples

### Download blacklist
**Args:** `encode-blacklist download hg38 -o blacklist.bed`
**Explanation:** Downloads ENCODE blacklist for hg38 genome.

### Filter BAM file
**Args:** `encode-blacklist filter -b input.bam -bl blacklist.bed -o filtered.bam`
**Explanation:** Filters out reads mapping to blacklisted regions.

### Filter peaks
**Args:** `encode-blacklist filter -p peaks.bed -bl blacklist.bed -o filtered_peaks.bed`
**Explanation:** Removes peaks overlapping with blacklisted regions.

### Check region
**Args:** `encode-blacklist check -r chr1:1000-2000 -bl blacklist.bed`
**Explanation:** Checks if a specific region is in the blacklist.

### Update blacklist
**Args:** `encode-blacklist update hg38 -o updated_blacklist.bed`
**Explanation:** Updates blacklist to latest version.