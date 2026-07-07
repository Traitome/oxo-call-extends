---
name: scelestial
category: single-cell
description: Scelestial - Single Cell Lineage Tree Inference based on Steiner Tree Approximation
tags: ["scelestial", "single-cell", "lineage-tree", "evolution"]
author: oxo-call-community
source_url: "https://github.com/hzi-bifo/scelestial-paper-materials-devel"
---

## Concepts

- **Tool Overview**: Scelestial (v1.2) is a tool for Single Cell Lineage Tree Inference based on a Steiner Tree Approximation Algorithm.
- **Core Function**: Reconstructs cell lineage trees from single-cell sequencing data.
- **Algorithm**: Uses Steiner tree approximation to infer lineage relationships.
- **Input/Output**: Accepts variant data and produces lineage tree structures.
- **Lineage Inference**: Infers evolutionary relationships between cells.
- **Applications**: Cancer evolution, developmental biology, and cellular dynamics.

## Pitfalls

- **Variant Quality**: Results depend on input variant quality.
- **Tree Complexity**: May not handle very complex lineages well.
- **Computational Resources**: High memory and CPU requirements.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Missing Data**: Missing variants can affect tree topology.
- **Root Identification**: Requires accurate root identification.

## Examples

### Basic lineage inference
**Args:** `scelestial -i variants.vcf -o lineage.tree`
**Explanation:** `-i` input VCF with variants; `-o` output lineage tree.

### With reference
**Args:** `scelestial -i variants.vcf -r reference.fasta -o lineage.tree`
**Explanation:** `-r` reference genome for variant interpretation.

### Multiple samples
**Args:** `scelestial -i sample1.vcf sample2.vcf -o lineage.tree`
**Explanation:** Processes multiple samples simultaneously.

### Verbose logging
**Args:** `scelestial -i variants.vcf -v -o lineage.tree`
**Explanation:** `-v` enables verbose output for debugging.

### Output visualization
**Args:** `scelestial -i variants.vcf --plot -o tree.png`
**Explanation:** Generates visualization of lineage tree.

### Root specification
**Args:** `scelestial -i variants.vcf -root cell1 -o lineage.tree`
**Explanation:** `-root` specifies root cell for tree.

### Tree statistics
**Args:** `scelestial -i variants.vcf -s stats.txt -o lineage.tree`
**Explanation:** `-s` outputs tree statistics.