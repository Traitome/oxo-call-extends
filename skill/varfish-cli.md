---
name: varfish-cli
category: bioinformatics
description: VarFish CLI - Command line interface for VarFish.
tags: [varfish-cli, variant-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/varfish-org/varfish-cli"
---

## Concepts

- **Tool Overview**: VarFish CLI - Command line interface for VarFish variant analysis.
- **Core Function**: Provides various utilities for variant analysis.
- **Input**: Variant files.
- **Output**: Analysis results.
- **Installation**: Install via pip
- **Use Case**: Variant analysis, clinical genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Network**: May require network for database access.

## Examples

### Upload variants
**Args:** `varfish-cli upload --input variants.vcf --server https://varfish.example.com`
**Explanation:** Upload variants to VarFish server.

### Query variants
**Args:** `varfish-cli query --server https://varfish.example.com --gene BRCA1`
**Explanation:** Query variants by gene.
