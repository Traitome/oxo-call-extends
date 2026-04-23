---
name: braker
category: annotation
description: Automated prediction of protein coding gene structures with GeneMark and AUGUSTUS
tags: [braker, gene-prediction, annotation, augustus, genemark]
author: oxo-call-community
source_url: "https://github.com/Gaius-Augustus/BRAKER"
---

## Concepts

- **Tool Overview**: BRAKER is a pipeline for fully automated gene prediction using GeneMark-ET/EP/ETP and AUGUSTUS.
- **Core Function**: Predicts protein-coding genes in eukaryotic genomes using RNA-Seq and/or protein homology evidence.
- **Evidence Types**: Supports RNA-Seq (BAM files), protein sequences, or combined RNA-Seq + protein evidence.
- **Output Formats**: GTF, GFF3, CDS FASTA, and protein FASTA files.
- **Training**: Automatically trains GeneMark and AUGUSTUS on the target genome.
- **Installation**: Install via bioconda: `conda install -c bioconda braker`

## Pitfalls

- **Genome Masking**: Genome should be soft-masked (lowercase repeats) for best results.
- **BAM Requirements**: BAM files must contain XS tags for strand information (use HISAT2 --dta or STAR --outSAMstrandField intronMotif).
- **Protein Database**: Use diverse protein database (e.g., OrthoDB) not single-species proteins.
- **Memory Usage**: Training steps require significant memory for large genomes.
- **Thread Limit**: More than 8 threads provides minimal benefit for some steps.

## Examples

### Basic RNA-Seq based prediction
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --threads=8`
**Explanation:** Runs BRAKER with RNA-Seq BAM file for gene prediction with 8 threads.

### Combined RNA-Seq and protein evidence
**Args:** `braker.pl --genome=genome.fa --bam=rna.bam --prot_seq=proteins.fa --species=mySpecies`
**Explanation:** Uses both RNA-Seq and protein homology for improved gene prediction.

### Using SRA data directly
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --rnaseq_sets_ids=SRR123456`
**Explanation:** Downloads RNA-Seq data from SRA and uses protein database for prediction.

### With UTR prediction
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --UTR=on`
**Explanation:** Enables experimental UTR prediction from RNA-Seq coverage information.

### Fungal genome prediction
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --fungus`
**Explanation:** Uses fungal-specific branch point model for improved intron prediction.

### Skip training (use existing parameters)
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --useexisting`
**Explanation:** Uses existing species parameters without retraining AUGUSTUS.

### Ab initio mode (no evidence)
**Args:** `braker.pl --genome=genome.fa --esmode`
**Explanation:** Runs GeneMark-ES self-training without external evidence.

### Output GFF3 format
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --gff3`
**Explanation:** Generates additional GFF3 format output alongside default GTF.

### Specify minimum contig length
**Args:** `braker.pl --genome=genome.fa --bam=aligned.bam --min_contig=10000`
**Explanation:** Overrides minimum contig length threshold for GeneMark training.
