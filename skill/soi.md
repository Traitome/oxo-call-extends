---
name: soi
category: comparative-genomics
description: SOI - Orthology Index for determining orthology of syntenic blocks
tags: [soi, comparative-genomics, orthology, synteny, evolution]
author: oxo-call-community
source_url: "https://github.com/zhangrengang/SOI/"
---

## Concepts

- **Tool Overview**: soi (v1.3.0) - An orthology index calculation tool
- **Core Function**: Determines orthology of syntenic blocks between genomes
- **Input/Output**: Accepts syntenic blocks; outputs orthology index scores
- **Algorithm**: Calculates OrthoIndex (OI) for syntenic block evaluation
- **Installation**: `conda install -c bioconda soi`
- **Key Features**: Orthology determination, synteny analysis, index calculation

## Pitfalls

- **Input Requirements**: Requires properly formatted syntenic block data
- **Reference Genomes**: Requires reference genomes for comparison
- **Block Quality**: Quality of syntenic blocks affects index calculation
- **Interpretation**: Results require biological interpretation
- **Memory Usage**: Large genomes require significant memory
- **Threshold Setting**: Requires proper threshold for orthology

## Examples

### Display help
**Args:** `soi --help`
**Explanation:** Shows available options and usage information.

### Basic orthology index
**Args:** `soi -i synteny_blocks.txt -o orthology_index.txt`
**Explanation:** Calculate orthology index for blocks.

### With reference genomes
**Args:** `soi -i synteny_blocks.txt -r genome1.fasta genome2.fasta -o orthology_index.txt`
**Explanation:** Use reference genomes for calculation.

### With threshold
**Args:** `soi -i synteny_blocks.txt -o orthology_index.txt --threshold 0.8`
**Explanation:** Set orthology threshold.

### Output detailed report
**Args:** `soi -i synteny_blocks.txt -o orthology_index.txt --detailed`
**Explanation:** Output detailed orthology report.

### Filter by score
**Args:** `soi -i synteny_blocks.txt -o orthology_index.txt --min-score 0.5`
**Explanation:** Filter blocks by minimum score.

### With threads
**Args:** `soi -i synteny_blocks.txt -o orthology_index.txt -p 8`
**Explanation:** Use multiple threads for calculation.

### Generate statistics
**Args:** `soi -i synteny_blocks.txt -o orthology_index.txt --stats`
**Explanation:** Output orthology statistics.