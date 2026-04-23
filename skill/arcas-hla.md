---
name: arcas-hla
category: annotation
description: arcasHLA - High-resolution HLA genotyping from RNA sequencing data for class I and class II genes
tags: [hla, genotyping, rna-seq, mhc, immunology, transplantation]
author: oxo-call-community
source_url: "https://github.com/RabadanLab/arcasHLA"
---

## Concepts

- **Tool Overview**: arcasHLA performs high-resolution genotyping for HLA (Human Leukocyte Antigen) class I (HLA-A, -B, -C) and class II genes from RNA sequencing data. Version 0.6.0.
- **Clinical Importance**: HLA typing is essential for transplantation compatibility, disease association studies, and immunotherapy development.
- **Resolution**: Provides high-resolution typing (4-digit or higher) distinguishing specific HLA alleles, not just broad antigen groups.
- **RNA-Seq Input**: Works directly from RNA-seq reads without requiring specialized HLA sequencing panels. Uses expression data naturally containing HLA transcripts.
- **Paired/Single-End**: Supports both paired-end and single-end RNA-seq samples. Paired-end recommended for better accuracy.
- **Database Integration**: Uses IMGT/HLA database for allele reference sequences. Regular database updates improve typing accuracy.
- **Workflow**: Extract HLA reads → Align to HLA reference → Quantify allele frequencies → Report genotype.

## Pitfalls

- **Expression Level**: Low HLA expression reduces typing accuracy. Ensure adequate RNA-seq depth (≥30M reads recommended).
- **Allele Similarity**: Highly similar HLA alleles may be difficult to distinguish. Some allele pairs have near-identical sequences.
- **Database Updates**: HLA database updates frequently. Use current database version for most accurate typing.
- **Sample Quality**: Degraded RNA or poor sequencing quality affects typing accuracy. QC RNA-seq data before typing.
- **Novel Alleles**: Novel or rare alleles not in database will be assigned to closest known allele. May not reflect true genotype.
- **Class II Challenges**: Class II genes (DRB1, DQB1, etc.) may have lower expression than Class I, requiring more reads for accurate typing.

## Examples

### Basic HLA typing from paired-end RNA-seq
**Args:** `arcasHLA extract --fastq sample_R1.fastq.gz sample_R2.fastq.gz --outdir extracted/; arcasHLA genotype --fastq extracted/sample.extracted.fastq.gz --outdir typing_results/`
**Explanation:** Two-step workflow: first extract HLA reads from RNA-seq, then genotype extracted reads. Outputs high-resolution HLA alleles for all class I and II genes.

### Single-end RNA-seq typing
**Args:** `arcasHLA extract --fastq sample.fastq.gz --outdir extracted/; arcasHLA genotype --fastq extracted/sample.extracted.fastq.gz --outdir typing_results/`
**Explanation:** Processes single-end RNA-seq data. Same workflow but without paired-end information. Slightly reduced accuracy compared to paired-end.

### Type specific HLA genes only
**Args:** `arcasHLA genotype --fastq extracted.fastq.gz --genes A B C --outdir specific_results/`
**Explanation:** Genotypes only HLA-A, -B, -C (class I genes). Faster than full typing when class II not needed. Useful for targeted analysis.

### Full class I and II typing
**Args:** `arcasHLA genotype --fastq extracted.fastq.gz --genes A B C DRB1 DQB1 DPB1 --outdir full_results/`
**Explanation:** Complete HLA typing including major class I and class II genes. Most comprehensive typing for transplantation matching.

### Use pre-aligned BAM input
**Args:** `arcasHLA extract --bam aligned.bam --outdir extracted/; arcasHLA genotype --fastq extracted/sample.extracted.fastq.gz --outdir typing/`
**Explanation:** Uses pre-aligned BAM file instead of raw FASTQ. Useful when alignment already performed. Extracts HLA reads from BAM.

### Update HLA database
**Args:** `arcasHLA reference --update`
**Explanation:** Updates HLA reference database to latest IMGT/HLA release. Recommended periodically for most accurate typing with newly discovered alleles.

### Generate detailed typing report
**Args:** `arcasHLA genotype --fastq extracted.fastq.gz --outdir results/ --format detailed`
**Explanation:** Outputs detailed report including allele frequencies, confidence scores, and alignment statistics. Useful for quality assessment and validation.