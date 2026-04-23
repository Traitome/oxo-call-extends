---
name: antismash
category: annotation
description: antiSMASH - Identify, annotate, and analyze secondary metabolite biosynthesis gene clusters in bacterial and fungal genomes
tags: [secondary-metabolite, biosynthesis, gene-cluster, antibiotics, bacteria, fungi]
author: oxo-call-community
source_url: "https://github.com/antismash/antismash"
---

## Concepts

- **Tool Overview**: antiSMASH (Antibiotics and Secondary Metabolite Analysis SHell) identifies and annotates biosynthetic gene clusters (BGCs) for secondary metabolites in bacterial and fungal genomes. Version 8.0.4.
- **Detection Method**: Uses profile Hidden Markov Models (HMMs) to detect known BGC types across 70+ secondary metabolite classes (NRPS, PKS, terpenes, bacteriocins, etc.).
- **Analysis Modules**: Core detection plus optional modules: ClusterBlast (homologous cluster search), SubClusterBlast (subcluster detection), Pfam analysis, smCoG trees (secondary metabolite gene orthology).
- **Input Formats**: Accepts GenBank, FASTA, or EMBL format. Prefers GenBank with existing annotations for best results.
- **Output**: HTML visualization, GenBank annotations, JSON results, cluster boundaries, domain predictions, and compound predictions.
- **Web Server**: Available as web service at antismash.secondarymetabolites.org for small-scale analyses without local installation.
- **Container Support**: Docker and Singularity containers available for reproducible analysis environments.

## Pitfalls

- **Input Annotations**: FASTA-only input provides less accurate domain predictions. GenBank with gene annotations recommended.
- **Runtime**: Full analysis with all modules can take hours for large genomes. Use --minimal for quick detection-only runs.
- **Memory Requirements**: Large genomes (>10Mb) require substantial memory. ClusterBlast module particularly memory-intensive.
- **Database Dependencies**: Requires downloading large databases (ClusterBlast, PFAM, etc.) for full functionality. Use --minimal to skip database-dependent modules.
- **Taxon-specific Models**: Bacterial and fungal versions have different HMM sets. Use appropriate version for organism type.
- **Version Compatibility**: --reuse-results only works with results from same antiSMASH version. Module changes break compatibility.

## Examples

### Basic detection run
**Args:** `antismash genome.gbk --output-dir results/`
**Explanation:** Default run: core detection plus fast analysis modules. Outputs HTML visualization and GenBank with BGC annotations. ~2 min on 4-core machine.

### Minimal detection only
**Args:** `antismash --minimal genome.gbk --output-dir minimal_results/`
**Explanation:** Runs only core BGC detection without additional analysis modules. Fastest option (~1 min). Use for quick screening when detailed analysis not needed.

### Full analysis with all modules
**Args:** `antismash genome.gbk --genefinding-tool prodigal --cb-general --cb-subclusters --pfam2go --smcog-trees --output-dir full_results/`
**Explanation:** Comprehensive analysis: ClusterBlast, SubClusterBlast, Pfam annotations, smCoG phylogenetic trees. Most detailed output but slowest runtime.

### Reuse previous results
**Args:** `antismash --reuse-results previous.json --output-dir new_output/`
**Explanation:** Regenerates output files from previous JSON results. Useful for adding new analysis modules without re-running detection. Must use same antiSMASH version.

### Specify custom output
**Args:** `antismash genome.gbk --output-dir results/ --output-basename my_analysis --html-title "My Strain Analysis" --html-description "Secondary metabolite screening"`
**Explanation:** Custom output naming: base filename, HTML title, and description. Useful for organizing multiple analyses or customizing reports.

### Use with FASTA input
**Args:** `antismash genome.fasta --genefinding-tool prodigal --output-dir fasta_results/`
**Explanation:** Processes FASTA input using Prodigal for gene finding. Less accurate than GenBank input but works for unannotated genomes.

### Run specific detection classes
**Args:** `antismash genome.gbk --detect-only nrps,pks,terpene --output-dir specific_results/`
**Explanation:** Detects only specified BGC classes (NRPS, PKS, terpenes). Faster than full detection when interested in specific metabolite types.

### Display all options
**Args:** `antismash --help-showall`
**Explanation:** Shows complete list of all available command-line options including advanced parameters. Use for discovering specialized features.