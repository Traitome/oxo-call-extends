---
name: transgenescan
category: annotation
description: TransGeneScan - Tool for gene prediction in transcript sequences.
tags: [transgenescan, gene-prediction, transcriptome, annotation, orf]
author: oxo-call-community
source_url: "https://github.com/compbio/transgenescan"
---

## Concepts

- **Tool Overview**: TransGeneScan - A tool for predicting gene structures from transcript sequences.
- **Core Function**: Identifies gene structures, exons, and splice sites from RNA-seq data.
- **Input**: Transcript sequences (FASTA), genome sequence (optional).
- **Output**: Gene predictions (GTF), exon annotations, coding regions.
- **Installation**: `pip install transgenescan` or `conda install -c bioconda transgenescan`
- **Use Case**: Gene prediction, transcriptome annotation, genome analysis.

## Pitfalls

- **Complex Genes**: May have difficulty with complex gene structures.
- **Evidence Integration**: May benefit from additional evidence sources.

## Examples

### Predict genes
**Args:** `transgenescan -i transcripts.fasta -o gene_predictions.gtf`
**Explanation:** Predict gene structures from transcript sequences.

### With genome
**Args:** `transgenescan -i transcripts.fasta -g genome.fasta -o predictions/`
**Explanation:** Integrate genome sequence for improved predictions.
