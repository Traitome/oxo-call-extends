---
name: krona
category: metagenomics
description: Krona Tools is a set of scripts to create Krona charts from several Bioinformatics tools as well as from text and XML files.
tags: [krona, metagenomics]
author: oxo-call-community
source_url: "https://github.com/marbl/Krona"
---

## Concepts

- **Tool Overview**: krona v2.8.1 - Krona Tools is a set of scripts to create Krona charts from several Bioinformatics tools as well as from text and XML files..
- **Core Function**: Krona Tools is a set of scripts to create Krona charts from several Bioinformatics tools as well as from text and XML files.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda krona`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Create chart
**Args:** `ktImportTaxonomy -o chart.html taxonomy.txt`
**Explanation:** Creates interactive Krona chart from taxonomy data.

