---
name: jbrowse2
category: utility
description: JBrowse 2 - Next-generation genome browser for visualizing genomic data.
tags: [jbrowse2, utility, genome-browser, visualization, genomics]
author: oxo-call-community
source_url: "https://jbrowse.org/"
---

## Concepts

- **Tool Overview**: jbrowse2 (v4.1.3) - JBrowse 2 is a modern, extensible genome browser for visualizing genomic data.
- **Web-based Interface**: Provides interactive web-based genome visualization.
- **Multi-format Support**: Supports BAM, VCF, BED, GFF, and many other formats.
- **Plugin System**: Extensible through plugins for custom functionality.
- **Comparative Genomics**: Supports viewing multiple genomes simultaneously.
- **Track Customization**: Highly customizable track display and styling.

## Pitfalls

- **Large Data Files**: Very large files can impact performance.
- **Browser Compatibility**: Requires modern web browser with WebGL support.
- **Memory Usage**: Large genomes require significant browser memory.
- **Network Latency**: Remote data access can be slow.
- **Configuration Complexity**: Complex configurations require careful setup.
- **Track Rendering**: Too many tracks can slow down visualization.

## Examples

### Initialize JBrowse 2 instance
**Args:** `jbrowse create my_genome_browser`
**Explanation:** Creates a new JBrowse 2 instance in specified directory.

### Add genome assembly
**Args:** `jbrowse add-assembly ref.fasta --load copy`
**Explanation:** Adds a genome assembly to the browser.

### Add track from BAM file
**Args:** `jbrowse add-track alignments.bam --name "RNA-Seq Alignments"`
**Explanation:** Adds BAM alignment track to the browser.

### Add VCF track
**Args:** `jbrowse add-track variants.vcf --name "SNPs"`
**Explanation:** Adds VCF variant track to the browser.

### Start development server
**Args:** `jbrowse serve --port 8080`
**Explanation:** Starts development server on port 8080.

### Build production bundle
**Args:** `jbrowse build`
**Explanation:** Builds production-ready bundle for deployment.