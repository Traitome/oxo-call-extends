---
name: braker3
category: annotation
description: BRAKER3 pipeline for gene prediction with combined RNA-Seq and protein data using GeneMark-ETP and AUGUSTUS
tags: [braker3, gene-prediction, annotation, augustus, genemark-etp]
author: oxo-call-community
source_url: "https://github.com/Gaius-Augustus/BRAKER"
---

## Concepts

- **Tool Overview**: BRAKER3 is the latest pipeline combining RNA-Seq and protein data for gene prediction with GeneMark-ETP and AUGUSTUS.
- **Core Function**: Predicts highly reliable genes using combined extrinsic evidence, merging GeneMark-ETP and AUGUSTUS results via TSEBRA.
- **Evidence Types**: Requires both RNA-Seq and protein data for optimal performance.
- **Output**: Combined gene set with high support from extrinsic evidence.
- **Improvements**: More accurate than BRAKER2 for genomes with both RNA-Seq and protein evidence.
- **Installation**: Install via bioconda: `conda install -c bioconda braker3`

## Pitfalls

- **Both Evidence Required**: Best results require both RNA-Seq and protein data.
- **Genome Masking**: Soft-masked genomes produce best results.
- **BAM XS Tags**: RNA-Seq BAMs must contain XS strand tags.
- **Protein Database**: Use diverse database like OrthoDB, not single-species proteins.
- **Memory**: Large genomes require significant memory during training.
- **Docker/Java**: Container versions may lack Java for GUSHR/UTR features.

## Examples

### Run with RNA-Seq and protein evidence
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --bam=aligned.bam --species=mySpecies`
**Explanation:** Full BRAKER3 pipeline with combined RNA-Seq and protein evidence.

### Using SRA data directly
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --rnaseq_sets_ids=SRR123456 --species=mySpecies`
**Explanation:** Downloads RNA-Seq from SRA and combines with protein evidence.

### With UTR prediction
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --bam=aligned.bam --UTR=on`
**Explanation:** Enables experimental UTR prediction from RNA-Seq coverage.

### Fungal genome mode
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --bam=aligned.bam --fungus`
**Explanation:** Uses fungal-specific branch point model for intron prediction.

### Specify strandedness
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --bam=aligned.bam --stranded=+,.,-`
**Explanation:** Specifies strand specificity for each input BAM file.

### Output GFF3 format
**Args:** `braker.pl --genome=genome.fa --prot_seq=orthodb.fa --bam=aligned.bam --gff3`
**Explanation:** Outputs additional GFF3 format alongside default GTF.
