---
name: taxtastic
category: annotation
description: Tools for taxonomic naming and annotation of phylogenetic trees, including reference package creation for pplacer.
tags: [taxtastic, phylogenetics, annotation, pplacer, phylogenetic-placement, taxonomy]
author: oxo-call-community
source_url: "https://github.com/fhcrc/taxtastic"
---

## Concepts

- **Tool Overview**: taxtastic (v0.12.0+) - A suite of tools for working with taxonomically annotated phylogenetic trees. Primarily used to create "reference packages" (refpkgs) containing reference sequences, trees, and taxonomic information for phylogenetic placement using pplacer.
- **Core Function**: Main tool is `taxit` which creates and manipulates reference packages with taxonomic annotations for phylogenetic analysis.
- **Key Commands**: `taxit create` builds reference packages; `taxit new_database` downloads NCBI taxonomy; `taxit taxtable` extracts taxonomy subsets; `taxit composition` shows taxonomic composition.
- **Reference Packages**: Self-contained packages (`.refpkg`) containing aligned sequences, Newick tree, tree stats, and taxonomy - used by pplacer for read placement.
- **Installation**: `conda install -c bioconda taxtastic` or `pip install taxtastic`
- **Database**: Uses NCBI Taxonomy database (downloaded automatically or from existing taxdump files).

## Pitfalls

- **NCBI Taxonomy Download**: `taxit new_database` downloads full NCBI taxonomy (~600MB) on first run - requires stable internet and time.
- **Sequence Name Matching**: Sequence names in FASTA files must match exactly with names in seq_info.csv for proper taxonomic annotation.
- **Taxid Validity**: All taxids used must exist in the NCBI taxonomy database or be added manually via `taxit add_nodes`.
- **Tree Building Software**: The `--tree-stats` file format depends on the tree builder used (FastTree, RAxML, or phyml).
- **Type Strains**: The `is_type` field in seq_info.csv is important for accurate phylogenetic placement - set to TRUE for designated type strain sequences.
- **Reference Package Versioning**: Keep track of refpkg versions when working with collaborators to ensure consistency.

## Examples

### Create reference package
**Args:** `taxit create -l 16s_rRNA -P my.refpkg --aln-fasta seqs.fasta --tree-stats tree_stats.txt --tree-file tree.nwk`
**Explanation:** Build a basic reference package from aligned sequences, tree, and tree stats file. This is the minimal required input.

### Download NCBI taxonomy
**Args:** `taxit new_database taxonomy.db`
**Explanation:** Download and create local NCBI taxonomy database. Required once before using taxonomy features.

### Extract taxonomy subset
**Args:** `taxit taxtable taxonomy.db -f tax_ids.txt -o taxa.csv`
**Explanation:** Extract minimal taxonomy containing only the taxids in the input file. Creates CSV for use in refpkg creation.

### Full taxonomically-annotated refpkg
**Args:** `taxit create -l locus_name -P my.refpkg --taxonomy taxa.csv --aln-fasta seqs.fasta --seq-info seq_info.csv --tree-stats tree_stats.txt --tree-file tree.nwk`
**Explanation:** Create reference package with full taxonomic annotation including lineage information.

### Check reference package
**Args:** `taxit check my.refpkg`
**Explanation:** Verify integrity and contents of a reference package before use in phylogenetic placement.

### Show composition
**Args:** `taxit composition -t taxa.csv my.refpkg`
**Explanation:** Display taxonomic composition of sequences in a reference package by rank.

### Add custom nodes to taxonomy
**Args:** `taxit add_nodes taxonomy.db new_nodes.yaml`
**Explanation:** Add custom taxonomic nodes (like novel lineages) to the local taxonomy database using YAML format.

### List refpkg contents
**Args:** `taxit info my.refpkg`
**Explanation:** Display metadata and contents of a reference package including sequences, tree, and taxonomy data.
