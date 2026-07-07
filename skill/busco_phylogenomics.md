---
name: busco_phylogenomics
category: population-genomics
description: Pipeline to construct species phylogenies using BUSCO single-copy orthologs from multiple species
tags: [busco, phylogenomics, phylogeny, ortholog, supermatrix]
author: oxo-call-community
source_url: "https://github.com/jamiemcg/BUSCO_phylogenomics"
---

## Concepts

- **Tool Overview**: BUSCO_phylogenomics is a pipeline to construct species phylogenies from BUSCO proteins. It works directly from BUSCO output directories and generates concatenated supermatrix alignments and individual gene trees of BUSCO families.
- **Core Workflow**: Identifies BUSCO proteins that are complete and single-copy in all (or a percentage of) input samples → individually aligns each BUSCO family → trims alignments → concatenates into a supermatrix → builds phylogenetic tree. Also generates individual gene trees for each BUSCO family.
- **Input**: A directory containing completed BUSCO output directories (one per species). The pipeline looks for BUSCO's `full_table.tsv` and protein FASTA files in each subdirectory.
- **Output**: Concatenated alignment in FASTA and Phylip format, partition file in NEXUS format, and individual gene trees (Newick). Stored in the specified output directory.
- **Alignment Methods**: Supports MAFFT (default, via `--mafft`) and MUSCLE (via `--muscle`) for multiple sequence alignment. Trimal is used for alignment trimming with configurable strategies.
- **Tree Building**: Gene trees built with FastTree (default) or IQ-TREE (via `--gene_tree_program iqtree`). The supermatrix tree is typically built externally by the user with their preferred method (RAxML, IQ-TREE, etc.) using the provided partition file.
- **Missing Data Handling**: The `--percent_single_copy` (`-psc`) parameter allows including BUSCOs that are complete and single-copy in at least a specified percentage of species, filling gaps with a missing character (`?` by default).
- **Dependencies**: python, biopython, muscle, mafft, trimal, fasttree, iqtree, tqdm — all must be in `$PATH`.
- **Installation**: `conda create -n BUSCO_phylogenomics -c bioconda -c conda-forge busco_phylogenomics` (installs `BUSCO_phylogenomics.py` and `count_buscos.py`).

## Pitfalls

- **BUSCO Prerequisite**: Requires completed BUSCO runs for all species. BUSCO must be run separately first (with protein or genome mode), and the output directories must be placed in a single input directory. The pipeline does not run BUSCO itself.
- **Nucleotide Mode Incompatibility**: The `--nt` flag (align nucleotide sequences) does NOT work if miniprot was used to identify BUSCOs, because miniprot only outputs amino acid sequences. Use protein mode (default) when BUSCO was run with miniprot.
- **BUSCO Version 3 Output Structure**: BUSCO v3 has a slightly different output structure than v4/v5. Use `--busco_version_3` flag when working with v3 outputs, otherwise the pipeline will fail to locate the required files.
- **Missing Data Quality**: Using low `--percent_single_copy` values (e.g., 50%) increases missing data in the supermatrix, which can reduce phylogenetic accuracy. Use `count_buscos.py` to inspect BUSCO presence/absence before choosing a cutoff.
- **Single Node Execution**: The pipeline is designed for a single node/machine. It parallelizes alignment/trimming/phylogeny jobs across `-t` threads, but does not support distributed cluster execution natively. For large datasets, consider running on a high-core-count server.
- **Gene Tree Minimum Species**: Gene trees are only built for BUSCOs that are complete and single-copy in at least 4 samples (`--min_species_gene_tree`, default=4). Adjust this threshold for datasets with few species.

## Examples

### Basic phylogenomic reconstruction
**Args:** `BUSCO_phylogenomics.py -i BUSCO_results -o output_phylogenomics -t 8`
**Explanation:** Looks in `BUSCO_results/` for completed BUSCO runs, aligns all complete single-copy proteins found in ALL samples with MAFFT, trims with trimal, concatenates into a supermatrix (FASTA + Phylip + NEXUS partitions), and builds gene trees with FastTree. Runs 8 parallel alignment/trimming/phylogeny jobs.

### Use MUSCLE instead of MAFFT for alignment
**Args:** `BUSCO_phylogenomics.py -i BUSCO_results -o output -t 8 --muscle`
**Explanation:** Uses MUSCLE for multiple sequence alignment instead of the default MAFFT. Both aligners should produce similar results, but MUSCLE may be faster for small protein sets.

### Allow missing data (70% single-copy threshold)
**Args:** `BUSCO_phylogenomics.py -i BUSCO_results -o output -t 8 --percent_single_copy 70`
**Explanation:** Includes BUSCO families that are complete and single-copy in at least 70% of samples. Missing taxa are represented by `?` characters in the concatenated alignment. Use `count_buscos.py -i BUSCO_results` first to determine an appropriate cutoff.

### Supermatrix only (skip gene trees)
**Args:** `BUSCO_phylogenomics.py -i BUSCO_results -o output -t 8 --supermatrix_only`
**Explanation:** Only generates the concatenated supermatrix alignment and partition file, skipping individual gene tree construction. Faster when only a species tree is needed.

### Gene trees only with IQ-TREE
**Args:** `BUSCO_phylogenomics.py -i BUSCO_results -o output -t 8 --gene_trees_only --gene_tree_program iqtree`
**Explanation:** Only generates individual gene trees using IQ-TREE (instead of default FastTree). Useful for gene tree/species tree reconciliation methods like ASTRAL or ASTRID.

### Subsample markers for large datasets
**Args:** `BUSCO_phylogenomics.py -i BUSCO_results -o output -t 8 --max_markers 500 --random_seed 42`
**Explanation:** Randomly subsamples 500 complete single-copy BUSCO families for the supermatrix workflow. `--random_seed 42` ensures reproducible subsampling across runs. Useful for reducing compute time on datasets with thousands of BUSCOs.

### Count BUSCOs across samples to determine cutoff
**Args:** `count_buscos.py -i BUSCO_runs`
**Explanation:** Reports how many BUSCOs are complete and single-copy in what percentage of samples, and prints a presence/absence table for each BUSCO family. Use this to decide the `--percent_single_copy` threshold before running the full pipeline.
