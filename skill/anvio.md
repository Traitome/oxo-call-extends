---
name: anvio
category: metagenomics
description: Anvi'o - Interactive analysis and visualization platform for multi-omics data including metagenomics, pangenomics, and phylogenomics
tags: [metagenomics, visualization, pangenomics, binning, phylogenomics, multi-omics, interactive]
author: oxo-call-community
source_url: "https://github.com/merenlab/anvio"
---

## Concepts

- **Tool Overview**: Anvi'o is an open-source, community-driven platform for integrated analysis and visualization of microbiome data: metagenomics, metatranscriptomics, pangenomics, phylogenomics, and population genetics. Version 9.
- **Interactive Interface**: Web-based interactive visualization for manual binning refinement, genome quality assessment, comparative analysis, and data exploration.
- **Core Workflows**: Contig clustering/binning, genome refinement, pangenome analysis, metabolic pathway reconstruction, phylogenomic tree visualization.
- **Data Integration**: Combines multiple data types: assembly, coverage, taxonomy, functional annotation, phylogeny, and metabolic pathways into unified visualizations.
- **Program Collection**: Over 100 command-line programs (anvi-*) for specific tasks: profiling, annotation, binning, comparison, visualization.
- **Snakemake Workflows**: Automated workflows for common analyses (metagenomics, pangenomics) with reproducible pipeline execution.
- **Community Support**: Active community with tutorials, cookbook examples, and developer documentation at anvio.org.

## Pitfalls

- **Installation Complexity**: Many dependencies make installation challenging. Recommended to use conda or Docker/Singularity containers.
- **Memory Requirements**: Large datasets (multiple genomes, deep metagenomes) require substantial RAM (64GB+ recommended).
- **Learning Curve**: Extensive feature set requires time to learn. Start with tutorials at anvio.org/learn/ before complex analyses.
- **Database Downloads**: Functional annotation requires downloading external databases (COGs, KEGG, Pfam) which can be large.
- **Contig Naming**: Contig names must be consistent across all input files. Name mismatches cause integration failures.
- **Profile Database**: Creating profile databases from BAM files is memory-intensive. Use appropriate threads and memory allocation.

## Examples

### Generate contig database
**Args:** `anvi-gen-contigs-database -f contigs.fa -o contigs.db -n project_name`
**Explanation:** Creates contig database from assembly FASTA. Stores sequences, gene calls, and functional annotations. Foundation for all subsequent analyses.

### Profile BAM files
**Args:** `anvi-profile -i sample1.bam sample2.bam -c contigs.db -o profiles/ -T 12`
**Explanation:** Creates profile database from BAM alignments with 12 threads. Stores coverage, variability, and detection statistics per sample. Required for binning.

### Merge multiple profiles
**Args:** `anvi-merge profiles/*/PROFILE.db -o merged_profile.db -c contigs.db`
**Explanation:** Combines multiple sample profiles into single database for comparative analysis. Enables multi-sample binning and visualization.

### Interactive binning visualization
**Args:** `anvi-interactive -c contigs.db -p merged_profile.db -b bins.txt`
**Explanation:** Launches interactive web interface for manual bin refinement. Visualizes contigs by coverage, taxonomy, GC content. Refine bins manually.

### Run automated binning
**Args:** `anvi-cluster-contigs -c contigs.db -p merged_profile.db -C CONCOCT -k 20`
**Explanation:** Automated binning using CONCOCT algorithm with k=20 clusters. Alternative algorithms: METABAT2, MAXBIN2. Good starting point for binning.

### Calculate genome completeness
**Args:** `anvi-summarize -c contigs.db -p merged_profile.db -C bins_collection -o summary/`
**Explanation:** Generates summary report with completeness/redundancy estimates (using CheckM), taxonomy, and statistics per bin. Quality assessment.

### Pangenome analysis
**Args:** `anvi-gen-genomes-storage -c contigs.db -e external_genomes.txt -o genomes-storage.db; anvi-pan-genome -g genomes-storage.db -o pangenome/`
**Explanation:** Creates pangenome from multiple genomes. Visualizes gene clusters, core/accessory genes, and phylogenomic relationships.

### Estimate metabolic pathways
**Args:** `anvi-estimate-metabolic-completeness -c contigs.db -p merged_profile.db -C bins_collection`
**Explanation:** Estimates KEGG module completeness for each bin. Identifies metabolic capabilities of recovered genomes. Requires KEGG annotation.

### Run metagenomics workflow
**Args:** `anvi-run-workflow -w metagenomics -c config.json`
**Explanation:** Executes automated Snakemake metagenomics workflow from configuration file. Handles assembly, annotation, profiling, binning automatically.