---
name: zol
category: comparative-genomics
description: Large-scale targeted detection and evolutionary investigation of gene clusters
tags: [zol, gene-cluster, comparative-genomics, evolution, phylogenomics]
author: oxo-call-community
source_url: "https://github.com/Kalan-Lab/zol"
---

## Concepts

- **Tool Overview**: Zol (and its companion tool fai) enables large-scale targeted detection and evolutionary analysis of gene clusters
- **Gene Cluster Detection**: Identifies homologous/orthologous gene cluster instances across multiple genomes
- **PrepTG Database**: Creates indexed databases of target genomes for efficient searching
- **Comparative Analysis**: Performs comparative analysis of gene clusters across species
- **Visualization**: Generates tree-heatmap figures and pan-gene-cluster network visuals
- **Installation**: `conda install -c bioconda zol`

## Pitfalls

- **Database Preparation**: Requires preprocessing of target genomes with prepTG before searching
- **Computational Resources**: Large-scale analyses may require significant computational resources
- **Genome Format**: Supports FASTA and GenBank formats; ensure correct format for input
- **Checkpoint Files**: Results are partially cached; delete checkpoint files for complete rerun

## Examples

### Prepare target genome database
**Args:** `prepTG -g genomes/ -o target_db/`
**Explanation:** Use prepTG with -g for genome directory and -o for output database directory.

### Search for gene clusters
**Args:** `fai search -q query_cluster.fasta -d target_db/ -o results/`
**Explanation:** Use fai search with -q for query cluster, -d for database, and -o for output results.

### Generate evolutionary report
**Args:** `zol analyze -i results/ -o report.tsv --species-tree tree.nwk`
**Explanation:** Use zol analyze with -i for input results, -o for output file, and --species-tree for phylogenetic context.

### Compare gene clusters across samples
**Args:** `zol compare -d sample1_dir sample2_dir -o comparison.tsv`
**Explanation:** Use zol compare with -d for multiple sample directories and -o for output comparison file.

### Create pan-gene-cluster network visualization
**Args:** `cgcg -i results/ -o network.png --clade-specific`
**Explanation:** Use cgcg tool with -i for input results, -o for output visualization, and --clade-specific for highlighting clade patterns.

### Manual selection of gene cluster instances
**Args:** `zol manual-select -i results/fai_output.tsv -o selected_instances.tsv`
**Explanation:** Use manual-select with -i for fai output file and -o for manually curated selection file.

### Run complete analysis pipeline
**Args:** `zol pipeline -g genomes/ -q query.fasta -o final_results/ --species-tree tree.nwk`
**Explanation:** Use pipeline command with -g for genomes, -q for query, -o for output, and --species-tree for evolutionary context.