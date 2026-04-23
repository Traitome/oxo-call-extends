---
name: augustus
category: annotation
description: AUGUSTUS - Ab initio gene prediction program for eukaryotes with extrinsic evidence integration
tags: [gene-prediction, eukaryotes, annotation, ab-initio, rna-seq-integration]
author: oxo-call-community
source_url: "https://github.com/Gaius-Augustus/Augustus"
---

## Concepts

- **Tool Overview**: AUGUSTUS is a gene prediction program for eukaryotes that can operate as an ab initio predictor (using only sequence information) or incorporate extrinsic evidence from EST, protein alignments, RNA-Seq, and other sources.

- **Species Models**: Comes with pre-trained parameter sets for many species including human, mouse, zebrafish, Drosophila, C. elegans, Arabidopsis, rice, maize, yeast, and many others. Use --species to specify the appropriate model.

- **Extrinsic Evidence Integration**: Can incorporate hints from various sources: EST alignments, protein alignments, RNA-Seq alignments, and syntenic genomic alignments to improve prediction accuracy.

- **Alternative Splicing**: Capable of predicting alternative splicing and alternative transcripts. Can report multiple alternative gene structures with probabilities for transcripts, exons, and introns.

- **UTR Prediction**: Supports prediction of 5' and 3' UTRs, including introns within UTRs, when appropriate parameters are set.

- **Training Capability**: Includes training programs to estimate species-specific parameters from a set of known genes, allowing optimization for new organisms.

- **Output Formats**: Supports multiple output formats including GFF, GTF, GBrowse-compatible formats, and can generate SVG visualizations.

## Pitfalls

- **Species Model Selection**: Using an inappropriate species model significantly reduces prediction accuracy. If no close model exists, train a new model using known gene annotations.

- **Hint File Format**: Extrinsic hints must be in correct GFF format with proper feature types and sources. Malformatted hints can cause crashes or incorrect predictions.

- **Memory Requirements**: Large genomes require substantial memory. For mammalian genomes, ensure sufficient RAM (often >16GB) is available.

- **Strand Specificity**: By default, predicts genes on both strands. Use appropriate options to restrict predictions if needed.

- **Overprediction Risk**: Ab initio predictions without extrinsic evidence may have high false positive rates. Always validate predictions with experimental data when possible.

- **Training Data Quality**: Training new models requires high-quality, representative gene sets. Poor training data leads to poor predictions.

- **Genome Masking**: Repeats should be soft-masked (lowercase) rather than hard-masked (N's) for better prediction accuracy.

## Examples

### Basic gene prediction with species model
**Args:** `augustus --species=human genome.fasta > genes.gff`
**Explanation:** Performs ab initio gene prediction on a human genome using the pre-trained human model. Output in GFF format.

### Prediction with RNA-Seq hints
**Args:** `augustus --species=mouse --hintsfile=rna_seq_hints.gff genome.fasta > genes.gff`
**Explanation:** Incorporates RNA-Seq alignment hints to improve gene structure prediction. Hints file contains intron and exon evidence.

### Using protein alignment hints
**Args:** `augustus --species=zebrafish --hintsfile=protein_hints.gff --extrinsicCfgFile=extrinsic.cfg genome.fasta > genes.gff`
**Explanation:** Uses protein alignment evidence with custom extrinsic configuration file to guide gene prediction.

### Output in GTF format
**Args:** `augustus --species=human --gff=off --outfile=genes.gtf genome.fasta`
**Explanation:** Generates output in GTF format instead of default GFF, more compatible with some downstream tools.

### Predicting alternative transcripts
**Args:** `augustus --species=human --alternatives-from-sampling=true --minexonintronprob=0.2 --minmeanexonintronprob=0.5 genome.fasta > genes.gff`
**Explanation:** Enables prediction of alternative transcripts with probability thresholds for exon/intron inclusion.

### UTR prediction
**Args:** `augustus --species=mouse --UTR=on --hintsfile=rna_seq_hints.gff genome.fasta > genes.gff`
**Explanation:** Enables prediction of 5' and 3' UTRs, requires RNA-Seq evidence for accurate UTR boundaries.

### Single-strand prediction
**Args:** `augustus --species=human --strand=forward genome.fasta > genes.gff`
**Explanation:** Restricts gene prediction to the forward strand only, useful for certain applications.

### Using soft-masked genome
**Args:** `augustus --species=human --softmasking=1 genome.fasta > genes.gff`
**Explanation:** Processes soft-masked genome (repeats in lowercase) appropriately for better prediction accuracy.

### Training new species model
**Args:** `etraining --species=new_organism training_genes.gb`
**Explanation:** Trains a new AUGUSTUS model using GenBank format training gene sequences. Creates species-specific parameters.

### Prediction with multiple hint sources
**Args:** `augustus --species=human --hintsfile=combined_hints.gff --extrinsicCfgFile=extrinsic.cfg genome.fasta > genes.gff`
**Explanation:** Uses combined hints from multiple sources (RNA-Seq, proteins, ESTs) with weighted extrinsic configuration.
