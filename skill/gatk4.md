---
name: gatk4
category: variant-calling
description: GATK4 is the industry-standard Genome Analysis Toolkit for variant discovery in high-throughput sequencing data, including SNP/indel calling, genotyping, and variant filtering.
tags: [gatk4, variant-calling, snp, indel, vcf, haplotypecaller, mutect2, bam, germline, somatic, genomics]
author: oxo-call-community
source_url: "https://gatk.broadinstitute.org/"
---

## Concepts

- **Tool Overview**: GATK4 (Genome Analysis Toolkit version 4) is Broad Institute's comprehensive suite for variant discovery in high-throughput sequencing data.
- **Core Function**: Implements industry-standard best practices for germline and somatic SNP/indel discovery, including HaplotypeCaller for germline and Mutect2 for somatic variant calling.
- **Architecture**: GATK4 bundles over 150 tools including Picard toolkit functions, all invoked via `gatk <ToolName>` subcommand architecture.
- **Variant Calling Methods**: HaplotypeCaller uses local de-novo assembly of haplotypes for accurate indel calling. Mutect2 uses matched tumor-normal analysis for somatic variants.
- **GVCF Workflow**: For cohort analysis, HaplotypeCaller produces GVCF files (with reference blocks) enabling efficient joint genotyping across many samples via GenomicsDBImport + GenotypeGVCFs.
- **BQSR**: Base Quality Score Recalibration corrects systematic base-calling errors using known variant sites before variant calling.
- **VQSR**: Variant Quality Score Recalibration uses machine learning to filter variants based on multiple annotation qualities, preferred for large cohorts.
- **Input Formats**: Accepts aligned BAM/SAM files, FASTQ (via Picard), and produces VCF/GVCF outputs.
- **Installation**: `conda install -c bioconda gatk4` or download from GitHub releases

## Pitfalls

- **CRITICAL - Read Groups Required**: BAM files must contain proper @RG headers with SM, PL, LB, PU fields. Missing read groups cause immediate failure.
- **Reference Index Files**: Both `.fai` (samtools) and `.dict` (Picard/CreateSequenceDictionary) must exist for the reference genome.
- **GVCF vs VCF**: GVCF files (`.g.vcf.gz`) contain reference blocks and cannot be used directly with standard VCF tools. Must use GenotypeGVCFs first.
- **Tool Naming Convention**: All tools invoked as `gatk <ToolName>` with CamelCase names (e.g., `HaplotypeCaller`, `Mutect2`). Wrong case causes "tool not found".
- **Interval Specification**: For WES, provide capture kit BED file with `-L targets.bed`. For WGS, scatter by chromosome for parallelization.
- **Somatic vs Germline**: Never use HaplotypeCaller for somatic calling. Use Mutect2 for tumor samples. Confusing these leads to incorrect results.
- **Java Memory**: Large tools like HaplotypeCaller require 4-8GB heap. Set with `--java-options "-Xmx8g"`.

## Examples

### Run HaplotypeCaller in GVCF mode
**Args:** `gatk HaplotypeCaller -R reference.fa -I markdup_bqsr.bam -O sample.g.vcf.gz -ERC GVCF --dbsnp dbsnp.vcf.gz`
**Explanation:** Produces GVCF with reference blocks at all sites. `--dbsnp` annotates known variants. Required for joint genotyping.

### Joint genotype multiple samples
**Args:** `gatk GenomicsDBImport -V sample1.g.vcf.gz -V sample2.g.vcf.gz -L chr1 -R reference.fa --genomicsdb-workspace-path genomicsdb && gatk GenotypeGVCFs -R reference.fa -V gendb://genomicsdb -O cohort.vcf.gz`
**Explanation:** Two-step joint genotyping across samples by chromosome.

### Call somatic variants with Mutect2
**Args:** `gatk Mutect2 -R reference.fa -I tumor.bam -I normal.bam -normal normal_sample -O somatic.vcf.gz --germline-resource af-only-gnomad.vcf.gz --panel-of-normals pon.vcf.gz`
**Explanation:** Tumor-normal mode for somatic SNV/indel calling. Requires contamination estimation and filtering.

### Base Quality Score Recalibration
**Args:** `gatk BaseRecalibrator -R reference.fa -I markdup.bam --known-sites dbsnp.vcf.gz -O recal.table && gatk ApplyBQSR -R reference.fa -I markdup.bam --bqsr-recal-file recal.table -O markdup_bqsr.bam`
**Explanation:** Two-step BQSR: build recalibration table, then apply corrections for improved base quality accuracy.

### Filter variants with hard filters
**Args:** `gatk SelectVariants -V cohort.vcf.gz --select-type-to-include SNP -O snps.vcf.gz && gatk VariantFiltration -V snps.vcf.gz --filter-expression "QD < 2.0 || FS > 60.0 || MQ < 40.0" --filter-name "hard_filter" -O snps_filtered.vcf.gz`
**Explanation:** Hard filtering for small cohorts without VQSR resources.

### List all available tools
**Args:** `gatk --list`
**Explanation:** Displays all 150+ available GATK tools grouped by category.
