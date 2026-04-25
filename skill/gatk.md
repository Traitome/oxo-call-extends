---
name: gatk
category: variant-calling
description: Genome Analysis Toolkit — the industry-standard suite for variant discovery in high-throughput sequencing data, including SNP/indel calling, genotyping, and variant filtering.
tags: [gatk, variant-calling, snp, indel, vcf, haplotypecaller, mutect2, bam, germline, somatic]
author: oxo-call-community
source_url: "https://gatk.broadinstitute.org/hc/en-us/categories/360002369672"
---

## Concepts

- **Tool Overview**: GATK (Genome Analysis Toolkit) is Broad Institute's suite for variant discovery. GATK4 bundles Picard tools and uses a subcommand architecture. Version 4.5.0.
- **CRITICAL - Tool-as-Subcommand**: All GATK4 tools are invoked as `gatk <ToolName> [options]`. Tool names are CamelCase (e.g., `HaplotypeCaller`, `Mutect2`, `GenotypeGVCFs`). `gatk --HaplotypeCaller` is WRONG.
- **GATK Best Practices Germline Pipeline**: (1) FastqToSam → (2) BWA-MEM align → (3) MergeBamAlignment → (4) MarkDuplicates → (5) BaseQualityScoreRecalibration (BQSR) → (6) HaplotypeCaller → (7) GenomicsDBImport + GenotypeGVCFs → (8) VQSR or hard filtering.
- **HaplotypeCaller vs Mutect2**: `HaplotypeCaller` is for germline variants (diploid). `Mutect2` is for somatic variants (tumor vs normal) or tumor-only calling. Never use HaplotypeCaller for somatic calling.
- **GVCF Mode**: For joint genotyping of multiple samples, run `HaplotypeCaller -ERC GVCF` per sample to produce GVCFs, then combine with `GenomicsDBImport` and jointly genotype with `GenotypeGVCFs`. This is the recommended approach for cohorts.
- **Required Reference Files**: GATK requires (1) indexed FASTA (`.fai`), (2) sequence dictionary (`.dict`), and (3) sorted BAM with read groups. Create with `samtools faidx ref.fa` and `gatk CreateSequenceDictionary -R ref.fa`.
- **Known Variants Resources**: BQSR and VQSR require known variant databases (dbSNP, 1000G, Mills & Gold). Download from GATK Resource Bundle at `gs://gatk-best-practices/`.
- **Installation**: `conda install -c bioconda gatk4`

## Pitfalls

- **CRITICAL - Read Groups Required**: GATK aborts if the BAM lacks proper @RG (read group) headers with SM, PL, LB, PU fields. Add with `picard AddOrReplaceReadGroups` or BWA-MEM's `-R` flag before running GATK.
- **Reference Dict and FAI**: GATK requires both `.dict` (Picard dictionary) and `.fai` (samtools index) for the reference. Missing either causes immediate failure with a cryptic error.
- **GVCF Not a VCF**: GVCFs (`.g.vcf.gz`) are NOT standard VCFs; they contain reference blocks and are only useful as input to `GenotypeGVCFs`. Do not analyze GVCFs directly with standard VCF tools.
- **Genome Intervals**: GATK processes one genomic region at a time with `-L chr1` (or `-L chr1:1-10000`). For WGS, parallelize by chromosome or use scatter-gather. For WES, provide capture kit BED with `-L targets.bed`.
- **Strand Bias and Low Coverage**: HaplotypeCaller uses local assembly, which can cause false positives in low-coverage regions or highly repetitive sequences. Apply hard filters or VQSR to remove low-quality variants.
- **Mutect2 Contamination**: For somatic calling, estimate contamination with `GetPileupSummaries` + `CalculateContamination` and pass results to `FilterMutectCalls` to reduce false positives.

## Examples

### Germline SNP/indel calling with HaplotypeCaller (single sample)
**Args:** `HaplotypeCaller -R reference.fa -I markdup_bqsr.bam -O sample.g.vcf.gz -ERC GVCF --dbsnp dbsnp.vcf.gz`
**Explanation:** `-ERC GVCF` produces a GVCF with all sites including reference blocks; `--dbsnp` adds rs IDs to known sites. For single-sample VCF output, omit `-ERC GVCF` and add `-O sample.vcf.gz`.

### Joint genotyping from multiple GVCFs
**Args:** `GenomicsDBImport --genomicsdb-workspace-path genomicsdb_chr1 -L chr1 -V sample1.g.vcf.gz -V sample2.g.vcf.gz -V sample3.g.vcf.gz && gatk GenotypeGVCFs -R reference.fa -V gendb://genomicsdb_chr1 -O cohort_chr1.vcf.gz`
**Explanation:** Two-step joint genotyping: (1) `GenomicsDBImport` combines GVCFs by chromosome into a database; (2) `GenotypeGVCFs` jointly calls variants from all samples. Scale by splitting across chromosomes.

### Base Quality Score Recalibration (BQSR)
**Args:** `BaseRecalibrator -R reference.fa -I markdup.bam --known-sites dbsnp.vcf.gz --known-sites 1000g_gold_standard.vcf.gz -O recal.table && gatk ApplyBQSR -R reference.fa -I markdup.bam --bqsr-recal-file recal.table -O markdup_bqsr.bam`
**Explanation:** BQSR adjusts systematic base quality errors. Step 1: build recalibration table using known variants; Step 2: apply corrections to produce the final analysis-ready BAM. Required before HaplotypeCaller in the GATK best practices pipeline.

### Somatic variant calling with Mutect2
**Args:** `Mutect2 -R reference.fa -I tumor.bam -I normal.bam -normal normal_sample_name -O somatic.vcf.gz --germline-resource af-only-gnomad.vcf.gz --panel-of-normals pon.vcf.gz`
**Explanation:** Tumor-normal mode: `-I tumor.bam -I normal.bam` with `-normal` specifying the normal sample name from the BAM's @RG SM field. `--germline-resource` provides allele frequencies; `--panel-of-normals` filters systematic artifacts.

### Hard filter variants (for small cohorts without VQSR)
**Args:** `SelectVariants -R reference.fa -V cohort.vcf.gz --select-type-to-include SNP -O snps_raw.vcf.gz && gatk VariantFiltration -R reference.fa -V snps_raw.vcf.gz --filter-expression "QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0" --filter-name "basic_snp_filter" -O snps_filtered.vcf.gz`
**Explanation:** Two-step hard filtering: (1) extract SNPs with SelectVariants; (2) apply GATK hard filter thresholds recommended for small cohorts (<30 samples). Apply similar filters for INDELs with different thresholds (QD<2, FS>200, ReadPosRankSum<-20).

### Check GATK version and list available tools
**Args:** `--version && gatk --list`
**Explanation:** `--version` prints GATK version and Java info; `--list` lists all available tools grouped by category. Use this to discover available subcommands.

### Genotype given alleles at known positions
**Args:** `HaplotypeCaller -R reference.fa -I sample.bam -O forced_genotype.vcf.gz --genotyping-mode GENOTYPE_GIVEN_ALLELES --alleles known_variants.vcf.gz -L known_variants.vcf.gz`
**Explanation:** Forces GATK to genotype specific alleles from `--alleles` VCF, even if not detected by assembly. Useful for population studies where you want genotype calls at pre-specified sites.
