---
name: hmftools-rose
category: variant-calling
description: ROSE makes an actionability summary of clinical relevant genomic events and signatures from the Hartwig pipeline.
tags: [hmftools-rose, clinical, actionability, genomic-events, signatures, hartwig, hmf]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/rose/README.md"
---

## Concepts

- **Tool Overview**: ROSE (v1.3) generates an actionability summary of clinical relevant genomic events and signatures as determined by the Hartwig pipeline. It synthesizes outputs from PURPLE, SAGE, GRIPSS, and other HMF tools into a structured clinical report for the Netherlands healthcare context.

- **Clinical Actionability Framework**: Maps genomic alterations to therapeutic implications based on Dutch clinical guidelines and available therapies. Classifies alterations into actionable, potentially actionable, and non-actionable categories.

- **Genomic Event Summarization**: Consolidates SNVs, indels, copy number alterations, structural variants, and gene fusions into a unified event catalog. Prioritizes events by clinical relevance and evidence strength.

- **Mutational Signature Analysis**: Analyzes mutational signatures to infer underlying mutagenic processes such as tobacco exposure, UV damage, or DNA repair deficiency. Links signatures to potential therapeutic vulnerabilities.

- **Evidence Level Classification**: Assigns evidence levels based on FDA approvals, clinical trial data, case reports, and preclinical evidence. Higher evidence levels support stronger therapeutic recommendations.

- **Trial Eligibility Assessment**: Evaluates patient genomic profile against clinical trial inclusion/exclusion criteria. Generates matched trial list based on specific gene alterations and cancer type.

## Pitfalls

- **Netherlands-Specific Context**: ROSE is designed for the Dutch healthcare system. Clinical trial matching and evidence levels are specific to trials available in the Netherlands. International users may need custom configuration.

- **Complete Pipeline Required**: ROSE requires outputs from multiple HMF pipeline components including PURPLE, SAGE, GRIPSS, LINX, and signature analysis. Running on incomplete pipeline outputs produces partial or misleading summaries.

- **Reference Genome Consistency**: All input files must use consistent reference genome (GRCh37 or GRCh38). Mixing genome versions across tools produces invalid event catalogs.

- **Configuration File Updates**: Trial matching and evidence levels require up-to-date configuration files. Outdated configs may miss relevant trials or assign incorrect evidence levels.

- **Memory for Large Cohorts**: Processing multiple samples simultaneously requires 4GB+ heap memory per sample. Use `-Xmx8G` when running batch analysis.

- **Sample ID Consistency**: Sample identifiers across all input directories must match exactly. Case sensitivity and whitespace differences cause silent failures in event matching.

## Examples

### Run ROSE with complete HMF pipeline outputs
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -ref_genome GRCh37_hmf`
**Explanation:** Standard ROSE run combining copy number (PURPLE), variants (SAGE), structural variants (GRIPSS), and fusion data (LINX). Produces clinical actionability summary with therapeutic recommendations.

### Generate report with trial matching
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -ref_genome GRCh37_hmf -match_trials`
**Explanation:** Enables clinical trial matching based on genomic alterations. Outputs list of potentially eligible trials with corresponding inclusion/exclusion criteria matches.

### Include signature analysis
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -signatures signatures.tsv -ref_genome GRCh37_hmf`
**Explanation:** Integrates mutational signature analysis for additional clinical insights. Signature-based evidence can indicate specific treatment sensitivities such as PARP inhibitors for BRCA-deficient tumors.

### Run on GRCh38 reference
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -ref_genome GRCh38_hmf`
**Explanation:** Uses GRCh38 reference genome. All HMF pipeline outputs must be generated using GRCh38 reference. GRCh38 provides improved gene annotation and additional alt contigs.

### Specify output format
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -ref_genome GRCh37_hmf -output_format json`
**Explanation:** Generates machine-readable JSON output in addition to human-readable summary. JSON format enables integration with hospital information systems and automated clinical reporting.

### High-memory batch processing
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -ref_genome GRCh37_hmf -Xmx16G`
**Explanation:** Allocates 16GB heap memory for samples with complex genomic profiles. Recommended for heavily mutated tumors or samples with many structural variants.

### Run with custom evidence configuration
**Args:** `rose -sample tumor1 -output_dir ./rose/ -purple_dir ./purple/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -evidence_config custom_evidence.tsv -ref_genome GRCh37_hmf`
**Explanation:** Uses custom evidence configuration file to override default Netherlands-specific evidence levels. Useful for research studies or international collaborations with different evidence frameworks.
