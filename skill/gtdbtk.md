---
name: gtdbtk
category: bioinformatics
description: GTDB-Tk provides objective taxonomic classification for bacterial and archaeal genomes using the Genome Taxonomy Database.
tags: [gtdbtk, taxonomy, bacterial-classification, bioinformatics]
author: oxo-call-community
source_url: "https://ecogenomics.github.io/GTDBTk"
---

## Concepts

- **Taxonomic Classification**: GTDB-Tk assigns taxonomic classifications to genomes.

- **Genome Taxonomy Database**: Uses the GTDB reference database for classification.

- **Phylogenetic Placement**: Places genomes in a phylogenetic context.

- **Marker Genes**: Uses conserved marker genes for classification.

- **Automatic Assignment**: Automatically assigns taxonomy from domain to species.

- **Quality Control**: Provides quality metrics for genome assemblies.

## Pitfalls

- **Database Download**: Requires downloading large reference databases.

- **Memory Usage**: Processing many genomes may require significant memory.

- **Genome Quality**: Low-quality genomes may produce unreliable classifications.

- **Taxonomic Changes**: GTDB taxonomy is regularly updated.

- **Computational Time**: Classification can be computationally intensive.

## Examples

### Classify genomes
**Args:** `gtdbtk classify_wf --genome_dir genomes/ --out_dir results/`
**Explanation:** Runs the complete classification workflow.

### Identify marker genes
**Args:** `gtdbtk identify --genome_dir genomes/ --out_dir markers/`
**Explanation:** Identifies marker genes in input genomes.

### Align marker genes
**Args:** `gtdbtk align --identify_dir markers/ --out_dir alignments/`
**Explanation:** Aligns identified marker genes.

### Infer phylogeny
**Args:** `gtdbtk infer --align_dir alignments/ --out_dir tree/`
**Explanation:** Infers phylogenetic tree from alignments.

### Classify single genome
**Args:** `gtdbtk classify --genome input.fasta --out_dir result/`
**Explanation:** Classifies a single genome.

### Check database version
**Args:** `gtdbtk check_install`
**Explanation:** Verifies installation and database status.

### Help command
**Args:** `gtdbtk --help`
**Explanation:** Shows available options and usage information.