---
name: genblastg
category: annotation
description: GenBlastG - Gene prediction program that uses BLAST alignments and genomic sequences to predict gene structures.
tags: [genblastg, gene-prediction, blast, genome-annotation]
author: oxo-call-community
source_url: "http://genome.sfu.ca/genblast/download.html"
---

## Concepts
- **Gene Prediction**: Predicts gene structures from genomic sequences.
- **BLAST Integration**: Uses BLAST alignments for homology-based prediction.
- **Intron Prediction**: Predicts intron-exon boundaries.
- **Splice Site Prediction**: Identifies splice donor and acceptor sites.
- **ORF Prediction**: Predicts open reading frames.

## Pitfalls
- **Alignment Quality**: Requires high-quality BLAST alignments.
- **Computational Time**: May be slow for large genomes.
- **False Positives**: May predict non-functional ORFs.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Validation**: Predicted genes require experimental validation.

## Examples
### Predict genes
**Args:** `genblastg -g genome.fasta -b blast_output.txt -o gene_predictions.gff`
**Explanation:** Predicts gene structures from genome and BLAST alignments.

### With reference proteins
**Args:** `genblastg -g genome.fasta -p proteins.fasta -o gene_predictions.gff`
**Explanation:** Uses protein sequences to guide gene prediction.

### Predict splice sites
**Args:** `genblastg -g genome.fasta -b blast_output.txt -o gene_predictions.gff -s`
**Explanation:** Enables splice site prediction.

### Output FASTA sequences
**Args:** `genblastg -g genome.fasta -b blast_output.txt -o gene_predictions.gff -f predicted_proteins.fasta`
**Explanation:** Outputs predicted protein sequences.

### Batch prediction
**Args:** `genblastg -g genome.fasta -b ./blast_results/ -o ./predictions/`
**Explanation:** Processes multiple BLAST files for batch prediction.