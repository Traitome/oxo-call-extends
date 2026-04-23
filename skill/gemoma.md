---
name: gemoma
category: alignment
description: Gene Model Mapper (GeMoMa) is a homology-based gene prediction program. GeMoMa uses the annotation of protein-coding genes in a reference genome to infer the annotation of protein-coding genes in a target genome. Thereby, GeMoMa utilizes amino acid sequence and intron position conservation. In addition, GeMoMa allows to incorporate RNA-seq evidence for splice site prediction.
tags: [gemoma, alignment]
author: oxo-call-community
source_url: "http://www.jstacs.de/index.php/GeMoMa"
---

## Concepts

- **Tool Overview**: gemoma (v1.9) - Gene Model Mapper (GeMoMa) is a homology-based gene prediction program. GeMoMa uses the annotation of protein-coding genes in a reference genome to infer the annotation of protein-coding genes in a target genome. Thereby, GeMoMa utilizes amino acid sequence and intron position conservation. In addition, GeMoMa allows to incorporate RNA-seq evidence for splice site prediction.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda gemoma`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
