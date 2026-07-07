---
name: tirank
category: analysis
description: TiRank - RNA-seq differential expression analysis tool with ranking.
tags: [tirank, differential-expression, rna-seq, ranking, gene-expression]
author: oxo-call-community
source_url: "https://github.com/compbio/tirank"
---

## Concepts

- **Tool Overview**: TiRank - A tool for differential expression analysis with gene ranking based on multiple statistical metrics.
- **Core Function**: Identifies differentially expressed genes and ranks them based on fold change, statistical significance, and other metrics.
- **Input**: Gene expression matrices, sample metadata, contrast definitions.
- **Output**: Ranked list of differentially expressed genes, visualization plots.
- **Installation**: `pip install tirank` or `conda install -c bioconda tirank`
- **Use Case**: Gene expression analysis, biomarker discovery, pathway analysis.

## Pitfalls

- **Normalization**: Requires proper normalization of expression data.
- **Multiple Testing**: Correct for multiple testing when interpreting results.

## Examples

### Differential expression analysis
**Args:** `tirank -i expression_matrix.tsv -m metadata.tsv -c condition -o de_results/`
**Explanation:** Perform differential expression analysis between conditions.

### Rank genes
**Args:** `tirank rank -i de_genes.tsv -m combined -o ranked_genes.tsv`
**Explanation:** Rank differentially expressed genes by combined metrics.
