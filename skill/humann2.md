---
name: humann2
category: metagenomics
description: "HUMAnN2: The HMP Unified Metabolic Analysis Network 2"
tags: [humann2, metagenomics, functional profiling, pathways]
author: oxo-call-community
source_url: "http://huttenhower.sph.harvard.edu/humann2"
---
## Concepts

- **Tool Overview**: HUMAnN2 is a pipeline for functional profiling of microbial communities from metagenomic or metatranscriptomic sequencing data.
- **Tiered Search Strategy**: Combines MetaPhlAn2 for taxonomic profiling, ChocoPhlAn pangenome mapping, and Diamond for translated search.
- **Gene Family Quantification**: Maps reads to UniRef gene families (UniRef90/UniRef50) for functional annotation.
- **Pathway Analysis**: Uses MetaCyc pathway definitions and MinPath for pathway reconstruction and quantification.
- **Species-level Resolution**: Provides organism-specific functional profiles by stratifying contributions from known and uncharacterized species.
- **Installation**: `conda install -c bioconda humann2`

## Pitfalls

- **Database Requirements**: Requires large reference databases (ChocoPhlAn, UniRef); download may take time and require significant disk space.
- **Memory Usage**: Diamond alignment can require substantial memory (16GB+ recommended for full UniRef90 database).
- **MetaPhlAn Dependency**: Requires MetaPhlAn2 for initial taxonomic profiling; ensure compatible versions.
- **Input Quality**: Low-quality reads can affect mapping accuracy; preprocess reads with quality filtering before analysis.
- **Run Time**: Comprehensive functional profiling is computationally intensive; expect long run times for large datasets.
- **Output Interpretation**: Functional profiles require careful interpretation; consider using companion tools like STAMP for statistical analysis.

## Examples

### Basic functional profiling
**Args:** `humann2 --input input.fastq --output output_dir`
**Explanation:** Runs HUMAnN2 on a metagenomic FASTQ file and generates functional profiles.

### With pre-computed taxonomic profile
**Args:** `humann2 --input input.fastq --output output_dir --taxonomic-profile metaphlan_output.tsv`
**Explanation:** Uses a pre-computed MetaPhlAn2 profile to skip taxonomic profiling step.

### Specify output format
**Args:** `humann2 --input input.fastq --output output_dir --output-format tsv`
**Explanation:** Outputs results in tab-separated value format for easier downstream analysis.

### Adjust translated search sensitivity
**Args:** `humann2 --input input.fastq --output output_dir --search-mode sensitive`
**Explanation:** Uses sensitive search mode for Diamond translated alignment.

### Generate pathway coverage report
**Args:** `humann2 --input input.fastq --output output_dir --pathway-coverage`
**Explanation:** Generates additional pathway coverage information along with abundance profiles.