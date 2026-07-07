---
name: ngsep
category: variant-calling
description: NGSEP is a comprehensive platform for variant detection and analysis from NGS data.
tags: [ngsep, variant-calling, snv, indel, cnv]
author: oxo-call-community
source_url: "https://github.com/NGSEP/NGSEPcore"
---

## Concepts

- **Tool Overview**: NGSEP provides variant detection and downstream analysis for NGS data.
- **Core Function**: Detects SNVs, indels, STRs, inversions, and CNVs from sequencing data.
- **Algorithm**: Uses probabilistic models for variant calling and genotyping.
- **Input Format**: Accepts BAM files and reference genomes.
- **Output**: Produces VCF files with variant calls and annotations.
- **Use Case**: Variant analysis, population genetics, and genome-wide association studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require significant memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Reference Genome**: Requires indexed reference genome.
- **Output Size**: VCF files can be large.

## Examples

### Display help
**Args:** `NGSEP --help`
**Explanation:** Shows available options and usage instructions.

### Variant calling
**Args:** `NGSEP -i alignment.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from aligned reads.

### Genotype calling
**Args:** `NGSEP -i alignment.bam -r reference.fasta -g genotypes.vcf -o output/`
**Explanation:** Performs joint genotyping.

### CNV calling
**Args:** `NGSEP -i alignment.bam -r reference.fasta --cnv -o cnv.vcf`
**Explanation:** Detects copy number variants.

### STR calling
**Args:** `NGSEP -i alignment.bam -r reference.fasta --str -o str.vcf`
**Explanation:** Calls short tandem repeats.

### Annotation
**Args:** `NGSEP -v variants.vcf --annotate -o annotated.vcf`
**Explanation:** Annotates variants with functional information.

### Filtering
**Args:** `NGSEP -v variants.vcf --filter -o filtered.vcf`
**Explanation:** Filters variants by quality criteria.