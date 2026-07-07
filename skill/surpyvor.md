---
name: surpyvor
category: variant-calling
description: Evaluating, merging and plotting SV VCF files for structural variant analysis.
tags: [surpyvor, structural-variants, vcf, visualization]
author: oxo-call-community
source_url: "https://github.com/wdecoster/surpyvor"
---

## Concepts

- **Tool Overview**: surpyvor (v0.15.0) is a tool for evaluating, merging and plotting SV VCF files.
- **Core Function**: Analyzes and visualizes structural variant calls from VCF files.
- **Algorithm**: Uses various methods for SV comparison, merging and visualization.
- **Input/Output**: Input: SV VCF files; Output: Merged VCF, plots, statistics.
- **Applications**: Structural variant analysis, SV calling validation, visualization.
- **Installation**: `conda install -c bioconda surpyvor` or download from GitHub.

## Pitfalls

- **Input Format**: Requires properly formatted SV VCF files.
- **Memory Requirements**: Large VCF files require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect merging results.
- **Visualization Complexity**: May be hard to interpret complex SV plots.
- **Version Compatibility**: May not support all VCF versions.

## Examples

### Display help
**Args:** `surpyvor --help`
**Explanation:** Shows available options and usage information.

### Basic SV merging
**Args:** `surpyvor merge -i sv1.vcf sv2.vcf -o merged.vcf`
**Explanation:** Merge multiple SV VCF files.

### Plot SV distribution
**Args:** `surpyvor plot -i sv.vcf -o sv_plot.png`
**Explanation:** Generate visualization of SV distribution.

### Verbose mode
**Args:** `surpyvor merge -i sv1.vcf sv2.vcf -o merged.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `surpyvor stats -i sv.vcf -o stats.txt`
**Explanation:** Generate statistics about SV calls.

### Batch processing
**Args:** `surpyvor merge -i vcfs/ -o merged.vcf`
**Explanation:** Merge multiple VCF files from directory.

### Filter by size
**Args:** `surpyvor filter -i sv.vcf -o filtered.vcf -m 100`
**Explanation:** Filter SVs by minimum size of 100bp.

### Include annotations
**Args:** `surpyvor annotate -i sv.vcf -a annotations.gtf -o annotated.vcf`
**Explanation:** Annotate SVs with gene information.

### Generate report
**Args:** `surpyvor report -i sv.vcf -o report.html`
**Explanation:** Generate comprehensive HTML report.
