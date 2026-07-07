---
name: hmftools-gene-utils
category: utility
description: Generate Ensembl-based gene annotation resource files for use by HMF bioinformatics applications.
tags: [hmftools-gene-utils, gene annotation, Ensembl, reference data, HMF pipeline]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/gene-utils"
---

## Concepts

- **Tool Overview**: hmftools-gene-utils (v1.3) provides routines to generate gene annotation resource files from Ensembl for use by various Hartwig Medical Foundation applications.
- **Ensembl Integration**: Downloads and processes Ensembl gene annotations (GTF/GFF files) to create HMF-specific resource formats required by downstream tools.
- **Resource File Generation**: Produces various annotation files including gene lists, transcript information, and genomic coordinates needed by HMF tools like SAGE, PURPLE, and LINX.
- **Version Compatibility**: Handles different Ensembl versions (v74 for GRCh37, v104 for GRCh38) ensuring compatibility with reference genomes.
- **Pipeline Support**: Essential for setting up HMF analysis pipelines by generating the correct gene annotation resources before running variant calling or copy number analysis.
- **Single Tool Multiple Functions**: gene-utils is actually a collection of utilities, each generating specific resource files for different HMF applications.

## Pitfalls

- **Ensembl Version Matching**: Must use Ensembl annotations matching the reference genome version; using v38 annotations with v37 genome causes coordinate mismatches.
- **Network Dependency**: Downloads data from Ensembl servers; requires internet connectivity and proper HTTP access for data retrieval.
- **Disk Space**: Full Ensembl downloads can be several GB; ensure adequate storage for gene annotation files.
- **Java Version Requirements**: Requires Java 8+ (OpenJDK >=8,<=21); incompatible Java versions may cause parsing errors.
- **Periodic Updates**: Ensembl releases new versions quarterly; outdated gene annotations may miss newer transcripts or genes.

## Examples

### Generate gene annotation files for GRCh38
**Args:** `gene-utils -ensembl_version 104 -ref_genome GRCh38 -output_dir ./ref_data/`
**Explanation:** Downloads Ensembl v104 annotations and generates HMF-compatible gene resource files for GRCh38 reference genome.

### Generate resources for GRCh37 (Ensembl v75)
**Args:** `gene-utils -ensembl_version 75 -ref_genome GRCh37 -output_dir ./hmf_ref/`
**Explanation:** Creates gene annotation resources using Ensembl v75 which is compatible with GRCh37. Required for older reference setups.

### List available gene-utils subcommands
**Args:** `gene-utils -help`
**Explanation:** Displays all available subcommands and options. gene-utils contains multiple utilities for generating different resource file types.

### Generate transcript annotation file
**Args:** `gene-utils -mode transcript_annotation -ensembl_version 104 -ref_genome GRCh38 -output_dir ./output`
**Explanation:** Creates transcript-specific annotation files including transcript IDs, gene names, and biotype information for downstream RNA analysis tools.

### Batch generate for both genome versions
**Args:** `for build in GRCh37 GRCh38; do for version in 75 104; do gene-utils -ensembl_version $version -ref_genome $build -output_dir ./refs/$build; done; done`
**Explanation:** Generates resource files for both GRCh37 and GRCh38 with their corresponding Ensembl versions. Useful for labs supporting multiple reference builds.

### Validate generated resource files
**Args:** `gene-utils -mode validate -resource_dir ./ref_data -ref_genome GRCh38`
**Explanation:** Validates that generated resource files are complete and properly formatted before using them in HMF pipelines.
