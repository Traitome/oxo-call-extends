---
name: schema-salad
category: annotation
description: Schema Annotations for Linked Avro Data (SALAD)
tags: ["schema-salad", "annotation"]
author: oxo-call-community
source_url: "https://github.com/common-workflow-language/schema_salad"
---

## Concepts

- **Tool Overview**: Schema Annotations for Linked Avro Data (SALAD) (version 2.7.20180809223002)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda schema-salad`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Annotate features
**Args:** `-i genome.fasta -o annotation.gff`
**Explanation:** Predicts and annotates genomic features.

