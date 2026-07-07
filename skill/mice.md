---
name: mice
category: utility
description: Markers Inferred by Compacting Elements (mice). Synteny blocks from pangenomes.
tags: [mice, utility, pangenomics]
author: oxo-call-community
source_url: "https://github.com/gi-bielefeld/mice"
---

## Concepts

- **Tool Overview**: MICE v0.1.2 identifies synteny blocks from pangenomes using compacted elements.
- **Core Function**: Identifies synteny blocks in pangenome sequences.
- **Synteny Analysis**: Detects conserved synteny blocks across genomes.
- **Pangenome Focus**: Optimized for pangenomic analysis.
- **Input/Output**: Accepts genome sequences; outputs synteny blocks.
- **Comparative Genomics**: Supports comparative genomic analysis.

## Pitfalls

- **Computational Resources**: Processing large pangenomes may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal synteny detection.
- **Data Quality**: Analysis accuracy depends on input sequence quality.
- **Runtime**: Analysis of large pangenomes can be time-consuming.
- **Genome Complexity**: May struggle with highly fragmented genomes.

## Examples

### Identify synteny blocks
**Args:** `mice -i genomes.fasta -o synteny.txt`
**Explanation:** Identifies synteny blocks from pangenome sequences.

### With custom parameters
**Args:** `mice -i genomes.fasta -o synteny.txt -k 21`
**Explanation:** Uses k-mer size of 21 for analysis.

### Batch processing
**Args:** `mice -i fasta/ -o synteny/`
**Explanation:** Processes multiple genome files in batch mode.

### Generate visualization
**Args:** `mice -i genomes.fasta -o synteny.txt -p plot.png`
**Explanation:** Generates synteny visualization.

### Detailed output
**Args:** `mice -i genomes.fasta -o synteny.txt -v`
**Explanation:** Generates detailed synteny report.