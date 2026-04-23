---
name: braker2
category: annotation
description: BRAKER2 extends BRAKER1 for gene prediction with RNA-Seq and protein homology evidence
tags: [braker2, gene-prediction, annotation, augustus, genemark]
author: oxo-call-community
source_url: "https://github.com/Gaius-Augustus/BRAKER"
---

## Concepts

- **Tool Overview**: BRAKER2 is an automated gene prediction pipeline using GeneMark-EX and AUGUSTUS with RNA-Seq and/or protein evidence.
- **Core Function**: Trains and predicts genes using extrinsic evidence from RNA-Seq and protein homology.
- **Evidence Types**: Supports RNA-Seq BAM files, protein sequences, or combined evidence.
- **Improvements over BRAKER1**: Better handling of protein homology evidence via GeneMark-EP.
- **Output**: GTF gene models, CDS and protein FASTA files.
- **Installation**: Install via bioconda: `conda install -c bioconda braker2`

## Pitfalls

- **Genome Masking**: Soft-masked genomes (lowercase repeats) produce best results.
- **BAM Requirements**: BAM files need XS tags for strand information.
- **Protein Database**: Use diverse protein set (e.g., OrthoDB) for better training.
- **Memory**: Training steps require significant memory for large genomes.
- **Dependencies**: Requires GeneMark-EX, AUGUSTUS, and BAMtools in PATH.

## Examples

### Run with RNA-Seq evidence
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --species=mySpecies --threads=8`
**Explanation:** Predicts genes using RNA-Seq evidence with 8 threads.

### Run with protein evidence
**Args:** `braker.pl --genome=genome.fa --prot_seq=proteins.fa --species=mySpecies`
**Explanation:** Predicts genes using protein homology evidence only.

### Combined RNA-Seq and protein evidence
**Args:** `braker.pl --genome=genome.fa --bam=rna.bam --prot_seq=proteins.fa --species=mySpecies`
**Explanation:** Uses both RNA-Seq and protein evidence for improved prediction.

### Skip training with existing parameters
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --useexisting`
**Explanation:** Uses existing AUGUSTUS parameters without retraining.

### Output GFF3 format
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --gff3`
**Explanation:** Outputs additional GFF3 format alongside default GTF.
