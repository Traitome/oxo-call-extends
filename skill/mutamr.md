---
name: mutamr
category: variant-calling
description: Stripped down tool for generation of annotated vcf from paired-end reads in a CPHL.
tags: [mutamr, variant-calling, vcf, annotation, paired-end, wgs, clinical]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/mutamr"
---

## Concepts

- **Tool Overview**: MutAMR v0.0.2 is a variant calling pipeline designed for clinical public health laboratory (CPHL) settings. It processes paired-end sequencing reads to generate annotated Variant Call Format (VCF) files, with focus on producing clinically relevant variant annotations.
- **Core Function**: Takes paired-end FASTQ or BAM files, aligns to a reference genome, calls variants, and generates annotated VCF output. Designed for bacterial whole-genome sequencing but can work with other organisms.
- **Workflow**: Typically combines alignment (BWA/similar), variant calling (freebayes or similar), and annotation (SnpEff or similar) into a streamlined pipeline.
- **Input Format**: Accepts gzipped or uncompressed FASTQ files (paired-end), or pre-aligned BAM files. Requires a reference genome in FASTA format.
- **Output**: Produces an annotated VCF file with functional annotations including variant effect (synonymous, missense, etc.), amino acid changes, and gene annotations.
- **Clinical Focus**: Designed with clinical laboratory workflows in mind, emphasizing reliable variant detection, comprehensive annotation, and standardized output formats.

## Pitfalls

- **Paired-End Requirement**: MutAMR is designed for paired-end reads. Single-end data may work but is not the primary use case and may reduce variant detection accuracy.
- **Reference Quality**: Output quality depends heavily on reference genome quality. Ensure the reference is appropriate (correct species, assembly version).
- **Coverage Requirements**: Low coverage regions may result in false negatives. MutAMR will call variants in low-coverage regions but with lower confidence.
- **Annotation Database**: Annotations depend on having current reference databases. Gene names, IDs, and effect predictions require up-to-date annotation files.
- **Bioinformatics Expertise**: While designed to be straightforward, users should have basic understanding of VCF format and variant calling concepts.
- **Memory and Runtime**: Whole bacterial genome sequencing (typical for MutAMR use case) is fast, but large eukaryotic genomes require more resources.

## Examples

### Basic variant calling from FASTQ
**Args:** `-1 reads_R1.fastq -2 reads_R2.fastq -r reference.fasta -o output.vcf`
**Explanation:** Standard MutAMR workflow. Takes paired FASTQ files, aligns reads, calls variants, and outputs annotated VCF.

### Use pre-aligned BAM input
**Args:** `-b aligned.bam -r reference.fasta -o output.vcf`
**Explanation:** If reads are already aligned, provide a BAM file directly. Skips alignment step and proceeds to variant calling.

### Specify output directory
**Args:** `-1 R1.fq.gz -2 R2.fq.gz -r ref.fa -o results/ -t 8`
**Explanation:** Use `-o` to specify output directory. `-t` sets thread count for parallel processing during alignment and variant calling.

### Include quality filtering
**Args:** `-1 R1.fq -2 R2.fq -r ref.fa -o variants.vcf -q 20 -d 10`
**Explanation:** Sets minimum mapping quality (`-q`) of 20 and minimum read depth (`-d`) of 10 for variant calls.

### Generate HTML report
**Args:** `-1 R1.fq -2 R2.fq -r ref.fa -o results.vcf --report`
**Explanation:** The `--report` flag generates an HTML summary report alongside the VCF, useful for clinical review.
