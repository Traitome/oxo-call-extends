---
name: export2graphlan
category: formatting
description: Conversion software tool for annotating tree with GraPhlAn
tags: [export2graphlan, formatting]
author: oxo-call-community
source_url: "https://github.com/segatalab/export2graphlan"
---

## Concepts
- **Tool Overview**: export2graphlan is a conversion software tool for producing both annotation and tree file for GraPhlAn. It automatically generate the input tree and the annotation file for GraPhlAn, starting from the input/output of MetaPhlAn, LEfSe, and HUMAnN. It supports also the biom file format. The annotation file will highlight specific sub-trees/clades automatically inferred from input file(s) provided. The two output file of export2graphlan should then be used with GraPhlAn.
- **Core Function**: Conversion software tool for annotating tree with GraPhlAn
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda export2graphlan`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
