---
name: igv
category: annotation
description: Integrative Genomics Viewer. Fast, efficient, scalable visualization tool for genomics data and annotations.
tags: [igv, genome visualization, NGS, BAM, VCF]
author: oxo-call-community
source_url: "https://igv.org"
---

## Concepts

- **Tool Overview**: IGV (Integrative Genomics Viewer) is a powerful, interactive visualization tool for exploring and analyzing genomic data
- **Core Function**: Enables visual exploration of aligned reads, variants, gene annotations, and other genomic data types
- **Input/Output**: Supports BAM, VCF, BED, bigWig, GFF/GTF, and many other standard bioinformatics formats
- **Installation**: `conda install -c bioconda igv`
- **Key Features**: Supports whole-genome, chromosome, and base-pair level views; multiple tracks; session saving; image export

## Pitfalls

- **Memory Requirements**: Loading large BAM files can require significant memory
- **Index Files**: BAM and VCF files must be indexed (.bai, .tbi) for efficient access
- **Genome Versions**: Ensure reference genome matches the data being visualized
- **Network Dependencies**: Loading remote files requires stable network connection
- **Java Version**: Requires Java 11+ for desktop version

## Examples

### Launch IGV with a specific genome
**Args:** `igv.sh -g hg38`
**Explanation:** Starts IGV with the human hg38 reference genome loaded.

### Load data files on startup
**Args:** `igv.sh -g hg38 sample.bam sample.vcf.gz`
**Explanation:** Launches IGV with specified data files pre-loaded.

### Load from URL
**Args:** `igv.sh https://example.com/data/sample.bam`
**Explanation:** Loads a remote BAM file directly into IGV.

### Start in batch mode
**Args:** `igv.sh -b commands.txt`
**Explanation:** Executes a batch script of commands for automated analysis.

### Set initial locus
**Args:** `igv.sh -g hg38 -l chr1:1000000-1001000`
**Explanation:** Starts IGV with a specific genomic region displayed.
