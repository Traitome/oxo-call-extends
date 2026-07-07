---
name: hmftools-orange
category: utility
description: ORANGE summarizes the key outputs from all algorithms in the Hartwig suite.
tags: [hmftools-orange, utility, WGS, tumor, purity, ploidy, clinical-reporting, hartwig]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/orange/README.md"
---

## Concepts

- **Tool Overview**: ORANGE (v4.1.3) is a comprehensive summary and reporting tool from Hartwig Medical Foundation that integrates outputs from all HMF bioinformatics tools to produce a unified clinical genomics report.

- **Purity and Ploidie Estimation**: Combines copy number (PURPLE), BAF (AMBER), and variant calls to estimate tumor purity and ploidy. These values are critical for interpreting variant allelic frequencies and copy number alterations.

- **Driver Event Catalog**: Identifies and classifies driver mutations including SNVs, indels, copy number alterations, structural variants, and gene fusions. Maps variants to known cancer genes and pathways.

- **Microsatellite Instability Assessment**: Evaluates MSIsensor data to determine microsatellite instability status, important for immunotherapy response prediction.

- **HRD Score Integration**: Incorporates CHORD HRD scores to report homologous recombination deficiency status, relevant for PARP inhibitor therapy selection.

- **Tumor Origin Prediction**: Uses CUPPA DNA/RNA predictions to suggest tissue of origin for cancers of unknown primary, assisting in diagnosis and treatment planning.

## Pitfalls

- **Complete HMF Pipeline Requirement**: ORANGE requires outputs from multiple HMF tools (PURPLE, AMBER, SAGE, GRIPSS, LINX, CHORD, CUPPA). Missing any component may cause partial or failed analysis.

- **Reference Genome Consistency**: All input files must use the same reference genome build (GRCh37 or GRCh38). Mixing genome builds produces incorrect annotations.

- **Sample Metadata Requirements**: Requires correct sample ID, sex, and cohort information for accurate reporting. Wrong metadata affects population frequency calculations and gender-specific interpretations.

- **Large File Processing**: Processing WGS samples with all tool outputs may require significant memory. Reports with many SVs, CNVs, and variants need 8GB+ RAM.

- **Output Interpretation**: ORANGE produces multiple output formats (JSON, TXT, PDF) with different contents. JSON is best for automated downstream processing; PDF is for clinical review.

## Examples

### Run ORANGE with complete HMF pipeline outputs
**Args:** `orange -sample tumor1 -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -ref_genome GRCh37_hmf -output_dir ./orange/`
**Explanation:** Runs standard ORANGE analysis combining PURPLE copy number, AMBER BAF, and SAGE variant calls. Produces clinical summary report with driver events.

### Include structural variant analysis
**Args:** `orange -sample tumor1 -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -gripss_dir ./gripss/ -linx_dir ./linx/ -ref_genome GRCh37_hmf -output_dir ./orange/`
**Explanation:** Adds GRIPSS and LINX outputs for structural variant reporting. Includes fusion calls, breakpoint annotations, and SV-driven driver events.

### Specify sample sex for accurate reporting
**Args:** `orange -sample tumor1 -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -ref_genome GRCh37_hmf -sex female -output_dir ./orange/`
**Explanation:** Specifies female sex for proper handling of sex chromosomes in copy number analysis. Incorrect sex can misestimate chromosome X ploidy.

### Run on GRCh38 reference
**Args:** `orange -sample tumor1 -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -ref_genome GRCh38_hmf -output_dir ./orange/`
**Explanation:** Uses GRCh38 reference genome. All input directories must contain GRCh38-based results.

### Generate only summary text output
**Args:** `orange -sample tumor1 -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -ref_genome GRCh37_hmf -output_dir ./orange/ -output_format txt`
**Explanation:** Generates only text summary file without full JSON and PDF reports. Useful for quick review or pipeline integration.

### Specify output filename prefix
**Args:** `orange -sample patient123 -purple_dir ./purple/ -amber_dir ./amber/ -sage_dir ./sage/ -ref_genome GRCh37_hmf -output_dir ./orange/`
**Explanation:** Uses sample ID as prefix for all output files. Output files will be named patient123.* in the output directory.
