---
name: hmftools-neo
category: expression
description: Identification of neoepitope and calculation of allele specific neoepitope binding and presentation likelihood.
tags: [hmftools-neo, expression, neoantigen, epitope, HLA, immunotherapy, cancer]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/neo"
---

## Concepts

- **Neoepitope Prediction Pipeline**: NEO (v1.2.1) identifies neoepitopes (tumor-specific antigens) by combining somatic variant calls with HLA binding prediction. It processes SNVs, indels, and gene fusions to predict which peptides will be presented on MHC molecules.

- **HLA Binding Prediction**: Integrates with NetMHCpan and similar tools to predict peptide-MHC binding affinities. Calculates allele-specific binding scores for each neoepitope candidate across all HLA alleles.

- **Variant Effect on Peptides**: Translates coding variants into altered peptide sequences and assesses their uniqueness to tumor cells. Frameshift and nonsense variants produce longer neoepitope candidates than missense variants.

- **Transcript Expression Integration**: Combines expression data (from Isofox or similar) with variant predictions to prioritize neoepitopes from expressed mutations. Only expressed mutations can be processed into presented peptides.

- **Tumor vs Normal Discrimination**: Filters out variants present in matched normal samples to ensure neoepitopes are truly tumor-specific. Germline variants cannot produce neoepitopes.

- **Neoantigen Ranking**: Ranks neoepitopes by predicted binding affinity, expression level, and tumor mutational burden. Higher-ranked candidates are more likely to elicit T-cell immune responses.

## Pitfalls

- **HLA Typing Prerequisite**: Requires accurate HLA typing from samples (using HLA-LA, HLApology, or similar). Poor HLA typing accuracy directly impacts neoepitope prediction reliability.

- **NetMHCpan Dependency**: The tool requires NetMHCpan or NetMHCIIpan for binding prediction. These must be licensed separately and installed. Binding prediction is computationally expensive.

- **Indel Handling Complexity**: Frameshift indels produce longer peptide sequences that require special handling. NetMHCpan may perform poorly on unusual peptide lengths.

- **Fusion Neoepitopes**: Gene fusions can produce novel junction peptides but are harder to predict. Not all fusion breakpoints generate viable neoepitopes.

- **Expression Data Requirement**: Without RNA-seq expression data, NEO cannot determine which variants are expressed. All variants are treated equally, potentially overestimating neoepitope load.

- **Multiple HLA Alleles**: Patients with heterozygous HLA loci have more allele-specific predictions to compute. A typical heterozygous patient with 6 HLA Class I alleles requires 6x the binding predictions.

## Examples

### Run NEO on somatic variants with HLA types
**Args:** `neo -sample patient1 -somatic_vcf somatic_variants.vcf -hla_types hla_types.txt -ref_genome GRCh37_hmf -output_dir ./neo/`
**Explanation:** Runs standard neoepitope prediction using somatic VCF and pre-computed HLA types. Produces ranked list of neoepitope candidates with binding predictions.

### Include gene fusion data
**Args:** `neo -sample patient1 -somatic_vcf variants.vcf -fusions linx_fusions.tsv -hla_types hla.txt -ref_genome GRCh37_hmf -output_dir ./neo/`
**Explanation:** Includes gene fusion predictions from LINX to identify fusion-junction neoepitopes. Fusion peptides span the breakpoint and may be tumor-specific.

### Run with expression data
**Args:** `neo -sample patient1 -somatic_vcf somatic.vcf -hla_types hla.txt -expression isofox_expression.tsv -ref_genome GRCh37_hmf -output_dir ./neo/`
**Explanation:** Uses expression data to prioritize neoepitopes from highly expressed mutations. Only expressed variants above expression threshold are included.

### Tumor-normal paired analysis
**Args:** `neo -sample tumor1 -tumor_vcf tumor.vcf -normal_vcf normal.vcf -hla_types hla.txt -ref_genome GRCh37_hmf -output_dir ./neo/`
**Explanation:** Uses matched normal VCF to filter germline variants. Only tumor-specific variants are used for neoepitope prediction.

### Specify binding prediction thresholds
**Args:** `neo -sample patient1 -somatic_vcf variants.vcf -hla_types hla.txt -ref_genome GRCh37_hmf -binding_threshold 500 -output_dir ./neo/`
**Explanation:** Sets IC50 binding threshold to 500nM (less stringent than default 50nM). Includes more neoepitope candidates but with lower predicted binding.

### Run on GRCh38 reference
**Args:** `neo -sample patient1 -somatic_vcf somatic.vcf -hla_types hla.txt -ref_genome GRCh38_hmf -output_dir ./neo/`
**Explanation:** Uses GRCh38 reference genome and annotation. Required when variant calling was performed against GRCh38.
