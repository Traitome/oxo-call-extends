---
name: ggcaller
category: gene-prediction
description: ggcaller - De Bruijn graph-based gene caller and pangenome analysis tool.
tags: [ggcaller, gene-prediction, pangenome, de-bruijn-graph]
author: oxo-call-community
source_url: "https://github.com/bacpop/ggCaller"
---

## Concepts
- **Gene Calling**: Identifies genes from sequences.
- **De Bruijn Graphs**: Uses de Bruijn graph approach.
- **Pangenome Analysis**: Analyzes pangenome content.
- **Sequence Analysis**: Analyzes genomic sequences.
- **Gene Family Analysis**: Identifies gene families.

## Pitfalls
- **Graph Complexity**: Complex graphs may affect performance.
- **Sequence Quality**: Requires high-quality sequences.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Memory Usage**: Large datasets require memory.
- **Result Validation**: Results should be validated.

## Examples
### Call genes
**Args:** `ggcaller -i genome.fasta -o genes.gff3`
**Explanation:** Calls genes from genome.

### With pangenome
**Args:** `ggcaller -i genomes.fasta -p -o pangenome.gff3`
**Explanation:** Performs pangenome analysis.

### Specify k-mer size
**Args:** `ggcaller -i genome.fasta -k 31 -o genes.gff3`
**Explanation:** Uses specified k-mer size.

### Batch processing
**Args:** `ggcaller -l genomes.txt -o ./results/`
**Explanation:** Processes multiple genomes.

### Generate report
**Args:** `ggcaller -i genome.fasta -r -o report.html`
**Explanation:** Generates gene calling report.