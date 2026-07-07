---
name: jbrowse
category: utility
description: JBrowse - A fast, embeddable genome browser built with JavaScript and HTML5.
tags: [jbrowse, utility, genome-browser, visualization, javascript]
author: oxo-call-community
source_url: "https://jbrowse.org/"
---

## Concepts

- **Tool Overview**: jbrowse (v1.16.11) - A lightweight, embeddable genome browser for visualizing genomic data.
- **Standalone Browser**: Self-contained genome browser with no server dependencies.
- **JavaScript-based**: Runs entirely in the browser using HTML5 technologies.
- **Multiple Formats**: Supports FASTA, BAM, VCF, BED, GFF, and WIG formats.
- **Embeddable**: Can be embedded in websites and applications.
- **Customizable**: Supports custom track types and plugins.

## Pitfalls

- **Browser Performance**: Older browsers may have performance issues.
- **Data File Size**: Large files require preprocessing for optimal performance.
- **Offline Usage**: Requires internet connection for initial load.
- **Memory Limitations**: Browser memory limits may affect large genome viewing.
- **Mobile Support**: Limited mobile browser support.
- **Legacy Version**: Version 1.x is legacy; consider upgrading to JBrowse 2.

## Examples

### Quick start with sample data
**Args:** `jbrowse setup --sample data`
**Explanation:** Sets up JBrowse with sample data for demonstration.

### Add reference sequence
**Args:** `prepare-refseqs.pl --fasta ref.fasta --out data/`
**Explanation:** Prepares reference sequence for JBrowse.

### Add alignment track
**Args:** `bam-to-json.pl --bam alignments.bam --out data/`
**Explanation:** Converts BAM file to JBrowse-compatible JSON format.

### Add feature track
**Args:** `flatfile-to-json.pl --gff features.gff --out data/`
**Explanation:** Converts GFF file to JBrowse-compatible JSON.

### Start web server
**Args:** `perl -MHTTP::Server::Simple::CGI -e 'my $s = HTTP::Server::Simple::CGI->new(8080); $s->run();'`
**Explanation:** Starts simple web server for JBrowse.

### Configure track display
**Args:** Edit trackList.json to customize track appearance
**Explanation:** Manually configures track display options.