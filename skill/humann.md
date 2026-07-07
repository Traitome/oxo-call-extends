---
name: humann
category: metagenomics
description: HUMAnN 3 for functional profiling of microbial communities
tags: [humann, metagenomics, functional profiling, pathways, bioBakery]
author: oxo-call-community
source_url: "http://huttenhower.sph.harvard.edu/humann"
---

## Concepts

- **Tool Overview**: HUMAnN 3 is the latest version of the HMP Unified Metabolic Analysis Network, enabling efficient and accurate functional profiling of microbial communities.
- **MetaPhlAn 3 Integration**: Designed in tandem with MetaPhlAn 3 for improved taxonomic profiling and species-level functional resolution.
- **Expanded Databases**: Includes 2x more species pangenomes and 3x more gene families compared to HUMAnN 2, based on UniProt/UniRef 2019_01.
- **MetaCyc Integration**: Incorporates MetaCyc v24.0 pathway definitions for comprehensive metabolic pathway analysis.
- **Tiered Search Architecture**: Combines nucleotide-level pangenome mapping with translated search for unclassified reads.
- **Installation**: `conda install -c biobakery humann`

## Pitfalls

- **Database Download**: Initial database setup requires downloading large files (~50GB+); use `humann_databases` command for efficient management.
- **Memory Requirements**: Full database analyses require significant memory; consider using smaller database subsets for resource-limited environments.
- **Version Compatibility**: HUMAnN 3 uses MetaPhlAn 3; ensure MetaPhlAn 2 is not installed in the same environment.
- **DIAMOND Version**: HUMAnN 3.6+ requires specific DIAMOND versions to avoid alignment errors.
- **Pangenome Coverage**: Pangenome sequences must be covered at >50% of sites to be reported; adjust threshold if needed.
- **Output File Size**: Functional profiles can be large; plan storage accordingly.

## Examples

### Basic HUMAnN 3 analysis
**Args:** `humann -i input.fastq -o output_dir`
**Explanation:** Runs complete functional profiling pipeline on metagenomic data.

### Download/update databases
**Args:** `humann_databases --download chocophlan full /path/to/databases --update-config yes`
**Explanation:** Downloads the full ChocoPhlAn pangenome database and updates configuration.

### With translated search only
**Args:** `humann -i input.fastq -o output_dir --bypass-nucleotide-index`
**Explanation:** Skips nucleotide-level mapping and performs only translated search.

### Generate stratified output
**Args:** `humann -i input.fastq -o output_dir --stratified-output`
**Explanation:** Generates species-stratified functional profiles for detailed analysis.

### Run on metatranscriptomic data
**Args:** `humann -i rna_seq.fastq -o output_dir --rna`
**Explanation:** Processes metatranscriptomic data for gene expression-based functional profiling.