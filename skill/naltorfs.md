---
name: naltorfs
category: annotation
description: Nested Alternate Open Reading Frames (nAlt-ORFs)
tags: [naltorfs, annotation, orf, open-reading-frame, nested]
author: oxo-call-community
source_url: "https://github.com/BlankenbergLab/nAltORFs"
---

## Concepts

- **Tool Overview**: nAltORFs v0.1.2 - identifies nested alternate open reading frames.
- **Core Function**: Predicts and annotates nested alternate ORFs within known coding sequences.
- **Input/Output**: Takes gene annotation files; outputs predicted nested ORFs.
- **Installation**: `conda install -c bioconda naltorfs`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires GFF/GTF annotation files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i annotation.gff -o naltorfs.gff`
**Explanation:** Identifies nested alternate ORFs in annotation.
