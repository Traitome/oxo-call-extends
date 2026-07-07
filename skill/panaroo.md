---
name: panaroo
category: utility
description: Panaroo is a pipeline for pangenome investigation and analysis.
tags: [panaroo, utility, pangenome, comparative-genomics]
author: oxo-call-community
source_url: "https://gtonkinhill.github.io/panaroo"
---

## Concepts

- **Tool Overview**: Panaroo analyzes bacterial pangenomes from annotated assemblies.
- **Core Function**: Identifies gene families and pangenome structure.
- **Algorithm**: Uses graph-based pangenome construction.
- **Input Format**: Accepts annotated genomes in GFF/GBK format.
- **Output**: Produces pangenome graphs and statistics.
- **Use Case**: Bacterial genomics, pangenome analysis, and population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Annotation Quality**: Results depend on input annotation quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `panaroo --help`
**Explanation:** Shows available options and usage instructions.

### Run pangenome analysis
**Args:** `panaroo -i gffs/*.gff -o results/`
**Explanation:** Performs pangenome analysis on GFF files.

### With reference
**Args:** `panaroo -i gffs/*.gff -r reference.gff -o results/`
**Explanation:** Uses reference genome for analysis.

### Verbose mode
**Args:** `panaroo -v -i gffs/*.gff -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `panaroo -t 8 -i gffs/*.gff -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `panaroo -i gffs/*.gff -o results/ --output-gene-families`
**Explanation:** Outputs gene families.

### Plot results
**Args:** `panaroo plot -i results/ -o plots/`
**Explanation:** Generates pangenome plots.