---
name: biopet-validateannotation
category: assembly
description: ValidateAnnotationvalidates whether an annotation file is correct.
tags: [biopet-validateannotation, assembly, GTF]
author: oxo-call-community
source_url: "https://github.com/biopet/validateannotation"
---

## Concepts

- **Tool Overview**: biopet-validateannotation (v0.1) - ValidateAnnotationvalidates whether an annotation file is correct.
- **Core Function**: ValidateAnnotationvalidates whether an annotation file is correct. It checks whether all the annotated contigs are present on the reference. It can check gtf or refflat files. It can also check both, ...
- **Input/Output**: GFF/GTF annotation input/output
- **Installation**: `conda install -c bioconda biopet-validateannotation`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
