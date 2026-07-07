---
name: hubward
category: visualization
description: Tool for creating UCSC Genome Browser hubs
tags: [hubward, UCSC, genome browser, track hub]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent"
---

## Concepts

- **Tool Overview**: hubward is a tool for creating and managing UCSC Genome Browser track hubs, enabling researchers to share and visualize genomic data through the UCSC Genome Browser interface.
- **Track Hub Structure**: Creates hub.txt, genomes.txt, and trackDb.txt configuration files that define metadata, supported genome assemblies, and individual track properties.
- **Big Data Formats**: Supports BigWig, BigBed, BAM, VCF, and other indexed formats for efficient data access and visualization.
- **Remote Hosting**: Enables hosting data on web servers, cloud storage (AWS S3, Google Cloud), or FTP services for global access.
- **Metadata Management**: Organizes track metadata including labels, colors, visibility settings, and subgroup definitions.
- **Installation**: `conda install -c bioconda hubward`

## Pitfalls

- **URL Accessibility**: All data files must be publicly accessible via HTTP(S) or FTP; UCSC browser cannot access local files.
- **CORS Configuration**: Servers hosting data must have proper CORS headers configured for cross-origin resource sharing.
- **Genome Assembly Matching**: Ensure track data matches the specified genome assembly (e.g., hg38 vs hg19).
- **Index Requirements**: BAM files need BAI indices, VCF files need TABIX indices, BigWig/BigBed files need built-in indices.
- **File Size Limits**: Large track files may cause browser performance issues; consider data aggregation or summarization.
- **hubCheck Validation**: Always validate hubs using UCSC's hubCheck tool before public release.

## Examples

### Create a basic track hub
**Args:** `hubward init --hub-name my_project --genome hg38 --output hub/`
**Explanation:** Initializes a new track hub directory structure with hub.txt and genomes.txt files for the hg38 assembly.

### Add a BigWig track
**Args:** `hubward add-track --hub hub/ --name signal_track --type bigWig --bigDataUrl https://example.com/data/signal.bw`
**Explanation:** Adds a BigWig track to the hub configuration with a remote data URL.

### Add a BAM track with visibility settings
**Args:** `hubward add-track --hub hub/ --name alignments --type bam --bigDataUrl https://example.com/data/alignments.bam --visibility dense --color 0,0,255`
**Explanation:** Adds a BAM track with dense visibility mode and blue color scheme.

### Validate hub configuration
**Args:** `hubward validate hub/`
**Explanation:** Runs validation checks on the hub configuration to ensure compliance with UCSC standards.

### Deploy hub to web server
**Args:** `hubward deploy --hub hub/ --server myserver.example.com --path /var/www/hubs/`
**Explanation:** Deploys the hub configuration and data files to a web server for public access.