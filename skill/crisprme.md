---
name: crisprme
category: genome-editing
description: Variant-aware CRISPR off-target analysis tool considering SNPs, indels, and haplotypes for therapeutic genome editing
tags: [crisprme, CRISPR, off-target, SNP, indel, haplotype, population-genomics, therapeutic, guide-RNA, PAM]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPRme"
---

## Concepts

- **Tool Overview**: CRISPRme (v2.1.9+) - A comprehensive tool package for CRISPR experiments assessment and analysis that considers genetic variation (SNVs, indels) across populations and personal genomes.
- **Core Function**: Performs variant-aware off-target site nomination and prioritization. Accounts for single-nucleotide variants (SNVs) and indels, considers bona fide haplotypes, allows for spacer:protospacer mismatches and bulges. Enables population-wide and personal genome analyses for therapeutic gene editing safety.
- **Algorithm**: (1) Builds personal/population genome with variants. (2) Identifies potential off-target sites with variant-adjusted PAMs. (3) Scores each site considering mismatches, bulges, and variant effects on binding. (4) Ranks sites by combined score and population frequency. (5) Generates detailed interactive reports.
- **Input**: Guide RNA sequence(s), reference genome (FASTA), variant files (VCF), optional BAM for experimentally-detected breaks.
- **Output**: Ranked off-target site list with scores, allele frequencies, interactive HTML reports, population-specific risk assessment.
- **Application**: Therapeutic guide RNA selection, clinical trial off-target safety, population genetics in gene editing, personal genome editing analysis.
- **Installation**: `pip install crisprme` or use Docker: `docker pull pinellolab/crisprme`

## Pitfalls

- **Complex Installation**: Has many dependencies - Docker/Singularity recommended for easiest setup.
- **Large Input Files**: Population-scale VCF files can be very large; consider using bgzip compressed files and tabix indexing.
- **Computational Intensity**: Full population analysis is computationally expensive for large cohorts.
- **Variant Annotation**: Requires properly annotated VCF files for accurate haplotype construction.
- **Guide Sequence**: Must provide guide RNA sequence without PAM (PAM is specified separately).
- **Reference Genome**: Ensure reference genome version matches your VCF files (hg19 vs hg38).

## Examples

### Basic off-target search
**Args:** `crisprme search -g GTTTAGA... -r hg38 -o output/`
**Explanation:** Search for off-target sites of a guide RNA in the reference genome.

### Variant-aware analysis
**Args:** `crisprme search -g GTTTAGA... -r hg38 -v variants.vcf.gz -o output/`
**Explanation:** Include population variants to find variant-created or variant-altered off-target sites.

### Population analysis
**Args:** `crisprme population -g GTTTAGA... -r hg38 -v 1000Genomes.vcf.gz -o pop_output/`
**Explanation:** Analyze allele frequencies of off-target sites across a population.

### Personal genome analysis
**Args:** `crisprme personal -g GTTTAGA... -r hg38 -v personal.vcf -o personal_output/`
**Explanation:** Analyze off-targets for a specific individual's genome.

### Mismatch tolerance
**Args:** `crisprme search -g GTTTAGA... -r hg38 -m 4 -o output/`
**Explanation:** Allow up to 4 mismatches between guide and off-target sequences.

### PAM variation analysis
**Args:** `crisprme pam -g GTTTAGA... -r hg38 -v variants.vcf.gz -o pam_output/`
**Explanation:** Find variant-created PAM sites that create new off-target opportunities.

### Generate report
**Args:** `crisprme report -i search_results/ -o html_report/`
**Explanation:** Generate interactive HTML report from analysis results.

### Batch guide analysis
**Args:** `crisprme batch -l guides.txt -r hg38 -v variants.vcf.gz -o batch_output/`
**Explanation:** Process multiple guide RNAs in batch mode.

### Experimental integration
**Args:** `crisprme integrate -g GTTTAGA... -r hg38 -b GUIDEseq.bed -o integrated/`
**Explanation:** Integrate experimentally-detected breaks (GUIDE-seq, CIRCLE-seq) with computational predictions.

### Haplotype-resolved analysis
**Args:** `crisprme haplotype -g GTTTAGA... -r hg38 -v phased.vcf.gz -o hap_output/`
**Explanation:** Resolve off-targets to specific haplotypes for phased genomes.

### Display version
**Args:** `crisprme --version`
**Explanation:** Display installed version.

### Show help
**Args:** `crisprme --help`
**Explanation:** Show all available commands and options.
