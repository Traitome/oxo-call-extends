---
name: liftoff
category: annotation
description: An accurate GFF3/GTF lift over pipeline
tags: [liftoff, annotation]
author: oxo-call-community
source_url: "https://github.com/agshumate/Liftoff"
---

## Concepts

- **Tool Overview**: liftoff v1.6.3 - An accurate GFF3/GTF lift over pipeline.
- **Core Function**: An accurate GFF3/GTF lift over pipeline
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda liftoff`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Lift annotations
**Args:** `liftoff -g annotation.gff -o lifted.gff -r target.fa reference.fa`
**Explanation:** Lifts over GFF annotations from reference to target genome.

