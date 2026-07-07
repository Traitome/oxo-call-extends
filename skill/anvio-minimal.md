---
name: anvio-minimal
category: metagenomics
description: Minimal version of Anvi'o - interactive analysis and visualization platform for omics data with reduced dependencies
tags: [anvio-minimal, anvio, metagenomics, pangenomics, visualization, interactive, minimal]
author: oxo-call-community
source_url: "https://merenlab.org/software/anvio/"
---

## Concepts

- **Tool Overview**: anvio-minimal (v9) - A minimal version of the Anvi'o platform for integrated analysis and visualization of microbiome data, with reduced dependencies for easier installation.
- **Core Function**: Provides essential anvi'o functionality including contig database generation, profile analysis, binning, pangenome analysis, and interactive visualization with fewer dependencies than the full version.
- **Key Features**:
  - **Contig Database**: Create and manage contig databases from genome/metagenome assemblies
  - **Profile Analysis**: Process BAM files to generate coverage and variability profiles
  - **Binning**: Support for automated binning algorithms (CONCOCT, METABAT2, MAXBIN2)
  - **Pangenome Analysis**: Comparative genomics with core/accessory gene visualization
  - **Interactive Interface**: Web-based visualization for manual bin refinement and data exploration
  - **Reduced Dependencies**: Excludes some optional dependencies like Prodigal, CheckM, etc.
- **Installation**: `conda install -c bioconda anvio-minimal`

## Pitfalls

- **Limited Functionality**: Missing some features of full anvio like certain annotation databases and advanced analysis modules
- **Dependency Version Constraints**: Specific pinned versions for numpy, pandas, scikit-learn for compatibility
- **Memory Requirements**: Still requires significant RAM for large datasets
- **Learning Curve**: Same steep learning curve as full anvio; tutorials recommended
- **External Tools**: May need to install additional tools like Prodigal separately for gene calling

## Examples

### Generate contig database
**Args:** `anvi-gen-contigs-database -f contigs.fa -o contigs.db -n project_name`
**Explanation:** Creates a contig database from assembly FASTA file, storing sequences and gene calls.

### Profile BAM files
**Args:** `anvi-profile -i sample.bam -c contigs.db -o profile/ -T 8`
**Explanation:** Creates profile database from BAM alignment with 8 threads, storing coverage statistics.

### Merge multiple profiles
**Args:** `anvi-merge profiles/*/PROFILE.db -o merged.db -c contigs.db`
**Explanation:** Combines multiple sample profiles into single database for comparative analysis.

### Interactive visualization
**Args:** `anvi-interactive -c contigs.db -p merged.db`
**Explanation:** Launches web-based interactive interface for exploring contigs and bins.

### Run automated binning
**Args:** `anvi-cluster-contigs -c contigs.db -p merged.db -C CONCOCT`
**Explanation:** Performs automated binning using CONCOCT algorithm.

### Pangenome analysis
**Args:** `anvi-pan-genome -g genomes-storage.db -o pangenome/`
**Explanation:** Creates pangenome from multiple genomes stored in database.

### Reformat FASTA
**Args:** `anvi-script-reformat-fasta -i input.fa -o output.fa --seq-type NT -l 1000`
**Explanation:** Filters and reformats FASTA file, keeping sequences >= 1000 bp.