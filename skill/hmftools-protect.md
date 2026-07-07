---
name: hmftools-protect
category: variant-calling
description: PROTECT determines the clinical evidence applicable for a particular tumor sample based on all genomic events and signatures.
tags: [hmftools-protect, clinical, evidence, tumor-sample, hartwig, hmf]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/protect/README.md"
---

## Concepts

- **Tool Overview**: PROTECT (v2.3) determines the clinical evidence applicable for a particular tumor sample based on all genomic events and signatures that are determined by the Hartwig pipeline. It integrates variant calls, copy number profiles, structural variants, and mutational signatures to identify clinically relevant biomarkers.

- **Clinical Evidence Matching**: Matches genomic findings to known therapeutic options, clinical trials, and resistance mechanisms. Produces evidence strings linking specific biomarkers to targeted therapies or trial eligibility.

- **Multi-modal Integration**: Combines outputs from SAGE (small variants), PURPLE (copy number), GRIPSS (structural variants), and signature analysis tools into a unified clinical interpretation.

- **Evidence Tier Classification**: Classifies evidence into tiers based on clinical relevance: Tier I (FDA-approved biomarkers), Tier II (clinical evidence), Tier III (preclinical or biological evidence), and Tier IV (hypothetical or exploratory).

- **Trial Matching**: Cross-references patient biomarkers with active clinical trials based on inclusion/exclusion criteria. Requires trial configuration files specifying gene-alteration pairs.

- **Resistance Biomarker Detection**: Identifies known resistance mechanisms to targeted therapies, such as EGFR T790M for osimertinib or KRAS G12C reversion mutations.

## Pitfalls

- **Complete Pipeline Dependency**: PROTECT requires outputs from multiple HMF pipeline components (SAGE, PURPLE, GRIPSS, LINX). Running PROTECT in isolation without prior pipeline completion will fail or produce incomplete results.

- **Reference Genome Consistency**: All input files must use the same reference genome build (GRCh37 or GRCh38). Mixing genome versions across tools produces invalid matches.

- **Trial Configuration Updates**: Trial eligibility criteria require regular updates as new trials open and close. Outdated configuration files may miss relevant trials or include ineligible ones.

- **Memory Requirements**: Large cohorts with high mutational burden require 4GB+ heap memory. Use `-Xmx8G` for samples with extensive genomic alterations.

- **Sample ID Matching**: Sample identifiers across all input files must match exactly. Case sensitivity and whitespace differences cause silent failures in evidence matching.

## Examples

### Run PROTECT with complete HMF pipeline outputs
**Args:** `protect -sample tumor1 -output_dir ./protect/ -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -ref_genome GRCh37_hmf`
**Explanation:** Standard PROTECT run combining copy number (PURPLE), BAF (AMBER), small variants (SAGE), and structural variants (GRIPSS). Produces clinical evidence report with therapeutic recommendations.

### Generate evidence for clinical trial matching
**Args:** `protect -sample tumor1 -output_dir ./protect/ -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -ref_genome GRCh37_hmf -trial_config trials_hmf.tsv`
**Explanation:** Runs PROTECT with explicit trial configuration file specifying which gene alterations match which clinical trials. Output includes matched trial IDs and eligibility details.

### Run with signature analysis output
**Args:** `protect -sample tumor1 -output_dir ./protect/ -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -signatures signatures.tsv -ref_genome GRCh37_hmf`
**Explanation:** Includes mutational signature analysis for additional evidence. Signature-based evidence can indicate specific carcinogen exposures or DNA repair deficiencies.

### Specify output formats
**Args:** `protect -sample tumor1 -output_dir ./protect/ -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -ref_genome GRCh37_hmf -output_format json`
**Explanation:** Generates machine-readable JSON output in addition to human-readable reports. JSON format enables integration with LIMS systems and automated reporting pipelines.

### Run on GRCh38 reference
**Args:** `protect -sample tumor1 -output_dir ./protect/ -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -ref_genome GRCh38_hmf`
**Explanation:** Uses GRCh38 reference genome. All input files must be aligned to GRCh38. GRCh38 provides improved reference assembly with additional alt loci.

### High-memory mode for complex samples
**Args:** `protect -sample tumor1 -output_dir ./protect/ -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -ref_genome GRCh37_hmf -Xmx16G`
**Explanation:** Allocates 16GB heap memory for heavily mutated samples. Recommended for samples with high neoantigen burden or complex genomic rearrangements.
