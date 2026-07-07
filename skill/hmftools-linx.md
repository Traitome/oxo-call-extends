---
name: hmftools-linx
category: variant-calling
description: LINX is an annotation, interpretation and visualisation tool for structural variants.
tags: [hmftools-linx, variant-calling, structural-variants, sv, annotation, visualization, circos]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/linx"
---

## Concepts

- **Tool Overview**: LINX (v2.2) is a Java-based structural variant annotation, interpretation and visualisation tool from Hartwig Medical Foundation. It processes GRIDSS/GRIPSS output to annotate breakpoints, gene fusions, and copy number changes with biological context.

- **Visualization Engine**: LINX uses Circos for circular genome visualization, generating publication-quality plots showing structural variant breakpoints, genes, and chromosomal bands. Requires R packages including ggplot2, dplyr, tidyr, cowplot, and magick.

- **Breakpoint Annotation**: Annotates SV breakpoints with overlapping genes, strand orientation, breakend type (deletion, duplication, inversion, translocation), and genomic coordinates. Identifies frameshift and in-frame gene fusions.

- **Fusion Classification**: Classifies gene fusions into categories: in-frame, frameshift, splice-affecting, read-through, and intergenic. Provides fusion partner information and functional impact assessment.

- **Helianthalike Repeat Detection**: Detects homopolymer and microsatellite instability regions near breakpoints that may affect SV detection accuracy.

- **Driver Event Identification**: Identifies known cancer driver events including kinase fusions, tumor suppressor gene disruptions, and amplification patterns characteristic of oncogene activation.

## Pitfalls

- **Circos Dependency**: LINX requires Circos (>=0.69.6) and multiple R packages (ggplot2, dplyr, tidyr, cowplot, magick, bioconductor-gviz). Installation via conda handles most dependencies but Circos may require additional configuration on some systems.

- **Reference Genome Compatibility**: Resource files must match the reference genome build (GRCh37 or GRCh38). Using wrong genome version results in incorrect annotations or runtime errors.

- **GRIPSS Input Requirement**: LINX requires GRIPSS output as input, not raw GRIDSS VCF. GRIPSS filters and normalizes GRIDSS calls, providing higher quality breakpoints for annotation.

- **Memory Configuration**: Large genomes or samples with many SVs (500+) may require increased JVM heap memory. Use `-Xmx8G` or higher for WGS samples.

- **File Path Limitations**: Circos has strict limitations on special characters in input paths. Avoid spaces, quotes, and non-ASCII characters in file paths.

## Examples

### Run LINX on GRIPSS output
**Args:** `linx -sample tumor1 -gripss_vcf gripss_somatic.vcf -ref_genome GRCh37_hmf -output_dir ./linx/`
**Explanation:** Runs standard LINX annotation on GRIPSS VCF. Produces breakpoint annotations, fusion calls, and visualization plots. The ref_genome must match the GRIPSS reference.

### Generate Circos visualizations
**Args:** `linx -sample tumor1 -breakend_annotations annotations.tsv -output_dir ./linx/plots/ -vis`
**Explanation:** Generates Circos visualization plots from pre-computed annotations. Requires annotated breakpoint file from a previous LINX run.

### Run with explicit reference data paths
**Args:** `linx -sample tumor1 -gripss_vcf somatic.sv.vcf -ref_genome GRCh38_hmf -ref_data_dir /path/to/hmf_refs/ -output_dir ./linx/`
**Explanation:** Specifies explicit paths to reference data files. Required when reference data is not in standard location or when using custom gene annotations.

### Multi-sample batch processing
**Args:** `linx -sample batch1 -gripss_vcf batch1.sv.vcf -ref_genome GRCh37_hmf -output_dir ./linx_batch1/`
**Explanation:** Processes multiple samples independently. Each sample should have its own GRIPSS VCF and output directory. Batch naming helps organize large cohorts.

### Run with specific threads for large samples
**Args:** `linx -sample tumor1 -gripss_vcf somatic.vcf -ref_genome GRCh37_hmf -output_dir ./linx/ -threads 8`
**Explanation:** Uses 8 threads for parallel processing of large VCF files. Thread count affects only the Java application; Circos visualization runs single-threaded.

### Generate fusion report
**Args:** `linx -sample tumor1 -gripss_vcf gripss.vcf -ref_genome GRCh37_hmf -output_dir ./linx/ -fusion`
**Explanation:** Generates a specific fusion report in addition to standard annotations. Fusion output includes partner genes, orientation, and predicted functional impact.
