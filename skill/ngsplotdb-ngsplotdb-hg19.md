---
name: ngsplotdb-ngsplotdb-hg19
category: utility
description: HG19 genome database for NGSplot visualization tool.
tags: [ngsplotdb-ngsplotdb-hg19, utility, hg19, ngsplot]
author: oxo-call-community
source_url: "https://github.com/shenlab-sinai/ngsplot"
---

## Concepts

- **Tool Overview**: HG19 database provides genome annotations for NGSplot visualization.
- **Core Function**: Provides reference data for NGSplot to generate genomic plots.
- **Algorithm**: Organizes genome annotations for efficient access.
- **Input Format**: Used by NGSplot for plotting genomic data.
- **Output**: Enables NGSplot to generate publication-quality figures.
- **Use Case**: ChIP-seq visualization, gene expression analysis, and genomic feature plotting.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Genome Version**: Specific to hg19 (GRCh37) reference assembly.
- **Storage Requirements**: Database files require storage space.
- **Dependency**: Requires NGSplot installation.
- **Annotation Updates**: Annotations may be outdated.
- **Compatibility**: Only works with hg19-aligned data.

## Examples

### Install database
**Args:** `conda install -c bioconda ngsplotdb-ngsplotdb-hg19`
**Explanation:** Installs HG19 database for NGSplot.

### List available databases
**Args:** `ngsplotdb.py -l`
**Explanation:** Lists available genome databases.

### Download database
**Args:** `ngsplotdb.py -d hg19`
**Explanation:** Downloads HG19 database (if not installed via conda).

### Plot ChIP-seq profile
**Args:** `ngsplot -G hg19 -R genebody -C chip.bam -O chip_profile`
**Explanation:** Generates genebody profile plot using HG19 database.

### Plot heatmap
**Args:** `ngsplot -G hg19 -R promoter -C chip.bam -O chip_heatmap -H`
**Explanation:** Generates promoter heatmap using HG19 database.

### Custom region plot
**Args:** `ngsplot -G hg19 -R bed -B regions.bed -C chip.bam -O custom_plot`
**Explanation:** Plots custom regions using HG19 database.