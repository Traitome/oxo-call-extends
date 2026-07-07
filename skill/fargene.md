---
name: fargene
category: metagenomics
description: "Fragmented Antibiotic Resistance Gene iENntifiEr takes either fragmented metagenomic data or longer sequences as input and predicts and delivers full-length antiobiotic resistance genes as output"
tags: [fargene, metagenomics, antibiotic-resistance, gene-prediction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fannyhb/fargene"
---

## Concepts

- **Tool Overview**: FARGene is a tool for identifying and reconstructing full-length antibiotic resistance genes from fragmented metagenomic data.
- **Core Function**: Takes fragmented reads or longer sequences and predicts complete antibiotic resistance genes.
- **Input/Output**: Input: Metagenomic reads (FASTQ), contigs (FASTA). Output: Predicted antibiotic resistance genes (FASTA), annotation report.
- **Algorithm**: Uses hidden Markov models (HMMs) and machine learning to identify resistance gene fragments and assemble full-length genes.
- **Key Features**: Fragmented read support, full-length gene reconstruction, antibiotic resistance prediction, HMM-based classification, batch processing.
- **Installation**: `conda install -c bioconda fargene`

## Pitfalls

- **Data Quality**: Requires high-quality sequencing data.
- **Fragment Length**: Short fragments may affect gene reconstruction.
- **Database Completeness**: Depends on resistance gene database.
- **False Positives**: May produce false positive predictions.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic resistance gene prediction
**Args:** `fargene -i reads.fastq -o resistance_genes.fasta`
**Explanation:** Predicts antibiotic resistance genes from metagenomic reads.

### From contigs
**Args:** `fargene -i contigs.fasta -o resistance_genes.fasta`
**Explanation:** Identifies resistance genes from assembled contigs.

### Generate report
**Args:** `fargene -i reads.fastq -o resistance_genes.fasta -r report.txt`
**Explanation:** Generates detailed annotation report.

### Custom database
**Args:** `fargene -i reads.fastq -o resistance_genes.fasta -d custom_db.hmm`
**Explanation:** Uses custom HMM database for prediction.

### Batch processing
**Args:** `fargene -i samples/ -o results/ --batch`
**Explanation:** Processes multiple samples in batch mode.