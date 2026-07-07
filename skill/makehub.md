---
name: makehub
category: utility
description: MakeHub is a command line tool for the fully automatic generation of track data hubs for visualizing genomes with the UCSC genome browser.
tags: [makehub, utility, UCSC, genome-browser]
author: oxo-call-community
source_url: "https://github.com/Gaius-Augustus/MakeHub"
---

## Concepts

- **Tool Overview**: makehub v1.0.8 - A command line tool for automatically generating track data hubs for the UCSC Genome Browser.
- **Core Function**: Creates comprehensive track hubs with minimal configuration for visualizing genomic data.
- **Input/Output**: Input: Genomic data files (BED, BigWig, BAM, VCF); Output: Track hub directory structure and configuration files.
- **Installation**: `conda install -c bioconda makehub`
- **UCSC Integration**: Generates hubs compatible with UCSC Genome Browser track hub format.
- **Automatic Indexing**: Automatically creates required index files for supported formats.

## Pitfalls

- **File Formats**: Only supports specific file formats (BED, BigWig, BAM, VCF).
- **Genome Assembly**: Requires correct genome assembly specification.
- **File Sizes**: Large files may require significant storage and bandwidth.
- **URL Configuration**: Incorrect URL paths prevent hub access.
- **Track Naming**: Duplicate track names cause conflicts.
- **Memory Usage**: Processing many tracks may require significant memory.

## Examples

### Create basic hub
**Args:** `makehub -i data/ -o hub/ -g hg38 -n MyHub`
**Explanation:** Creates track hub from data directory for hg38 assembly.

### With custom description
**Args:** `makehub -i data/ -o hub/ -g hg38 -n MyHub -d "My custom hub"`
**Explanation:** Adds custom description to the hub.

### Include specific file types
**Args:** `makehub -i data/ -o hub/ -g hg38 -t bed,bigwig`
**Explanation:** Only includes BED and BigWig files.

### Set public URL
**Args:** `makehub -i data/ -o hub/ -g hg38 -u https://example.com/hub/`
**Explanation:** Sets public URL for hub access.

### Verbose mode
**Args:** `makehub -i data/ -o hub/ -g hg38 -v`
**Explanation:** Provides detailed logging during hub creation.

### Update existing hub
**Args:** `makehub -i new_data/ -o existing_hub/ -g hg38 -u`
**Explanation:** Updates existing hub with new data.