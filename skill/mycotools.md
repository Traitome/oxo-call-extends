---
name: mycotools
category: utility
description: Mycotools - Comparative genomics automation and standardization software
tags: [mycotools, comparative-genomics, automation, standardization, fungi, fungal]
author: oxo-call-community
source_url: "https://github.com/xonq/mycotools"
---

## Concepts

- **Tool Overview**: Mycotools v1.0.0 is an automated and scalable platform for comparative genomics, specifically designed for fungal genomics. It provides modules to automate routine-complex comparative genomics workflows including phylogenetic analysis, orthology calling, and genome comparison.
- **Core Function**: Automates comparative genomics analyses from genome assemblies to finished analyses. Handles the full workflow from genome input through orthology assignment, phylogenetic analysis, and result visualization.
- **Modules**: Includes multiple subcommands for different genomics tasks: genome comparison, orthology calling, phylogenetics, synteny analysis, and data standardization across fungal genomes.
- **Input Format**: Accepts genome assemblies in FASTA format, gene annotations in standard formats (GFF3, GenBank), and sequence data for comparative analysis.
- **Output**: Produces analysis results including ortholog clusters, phylogenetic trees, synteny maps, and standardized comparative genomics datasets.
- **Use Case**: Fungal genomics research, fungal pathogen studies, evolutionary genomics of fungi, and comparative analysis across fungal species or strains.

## Pitfalls

- **Genome Quality**: Low-quality genome assemblies with many contigs or gaps will affect comparative analysis quality. Consider QC filtering before analysis.
- **Gene Annotation**: Accurate gene annotations are essential for orthology and functional comparative analyses. Ensure annotations are consistent across all genomes being compared.
- **Computational Resources**: Whole-genome comparative analyses can be computationally intensive. Large fungal genomes or many species require substantial CPU and memory.
- **Database Dependencies**: Some modules may require external databases (e.g., for orthology assignment) that need to be downloaded and configured.
- **Reference Selection**: Choosing an appropriate reference genome for comparative analyses affects downstream interpretation. Select a well-annotated reference genome.
- **Version Stability**: As a relatively new tool (v1.0.0), some subcommands and options may change between versions.

## Examples

### Run full comparative analysis pipeline
**Args:** `-i genomes_dir -o output_dir -p analysis_prefix`
**Explanation:** Standard workflow running the complete comparative genomics pipeline on input genomes.

### Identify ortholog clusters
**Args:** `orthologs -i genomes/ -o ortho_results/ -c 0.5`
**Explanation:** Identifies orthologous gene clusters across fungal genomes with specified similarity threshold.

### Build phylogenetic tree
**Args:** `phylogeny -i orthologs/ -o tree.nwk -m RAxML`
**Explanation:** Constructs a phylogenetic tree from ortholog alignments using specified method (RAxML).

### Display help and available commands
**Args:** `--help`
**Explanation:** Shows all available subcommands and options for the mycotools suite.

### Check installation and dependencies
**Args:** `check`
**Explanation:** Verifies that all required dependencies are installed and accessible.
