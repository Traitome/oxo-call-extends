---
name: roadies
category: phylogenetics
description: Reference-free, Orthology-free, Alignment-free, Discordance-aware Estimation of Species trees from whole-genome sequencing data, using a k-mer Jaccard distance and a coalescent-aware summary.
tags: ["roadies", "species-tree", "alignment-free", "k-mer", "phylogenomics", "core-genome"]
author: oxo-call-community
source_url: "https://turakhia.ucsd.edu/ROADIES"
---

## Concepts

- **Tool Overview**: ROADIES (v0.1.10, Turakhia lab / UCSD) is a tool for inferring species trees from whole-genome sequencing data without requiring a reference genome, ortholog identification, or multiple-sequence alignment. It uses a k-mer Jaccard distance matrix and a coalescent-aware maximum-likelihood summary method, and is the first method designed to be robust to gene-tree discordance caused by ILS, HGT, and duplication.
- **Core Function**: Takes a set of unassembled or assembled genomes (FASTA) and outputs a Newick species tree. Internally, it (1) sketches each genome with a hash-based k-mer counter, (2) computes pairwise Jaccard distances, (3) builds a tree via neighbor-joining and refines it with a maximum-likelihood search under a coalescent model that explicitly models discordance.
- **Algorithm**: A multi-resolution MinHash-like sketch is computed per genome; pairwise Jaccard distances are derived from the sketch intersection; the distance matrix is the input to a species-tree estimator that uses a coalescent model with a per-branch concordance factor (similar to ASTRAL's quartet scores). A bootstrap support value is reported for every internal branch.
- **Input Format**: A directory of FASTA files (one per genome) or a multi-FASTA with one contig per genome. Assemblies (`.fasta`, `.fa`) and unassembled reads (`*.fastq.gz`) are both accepted; the latter are pre-sketched without assembly. Genomes should be at least 100 kbp.
- **Output Format**: A Newick species tree (`species.nwk`), a per-pair distance matrix (`distances.tsv`), a per-branch bootstrap support file (`bootstrap.txt`), and a per-genome sketch file (`sketch.txt`) for incremental additions. The Newick is drawn with branch lengths in substitutions per site (or per-kmer, configurable).
- **Use Case**: Building a species tree for a set of newly sequenced bacterial isolates (the canonical use case), reconciling trees from WGS data with trees from 16S, MLST, or core-SNP pipelines, screening for HGT candidates (genomes with anomalously long branches), and producing a tree directly from clinical metagenomic reads without assembly.

## Pitfalls

- **CRITICAL — K-mer size must be chosen relative to genome divergence**: The default k=21 works for closely related species (ANI > 95%) but loses signal for distantly related bacteria. For 80–95% ANI, use k=15; for 60–80% ANI, use k=11. Run `roadies --auto-k` (if available) to let the tool choose.
- **CRITICAL — Contamination in the input FASTA produces phantom branches**: A single contaminated contig adds a long branch; a contaminated genome adds a clade that looks real. Run `Kraken2` or `ConFindr` on each input FASTA first.
- **The sketch size affects memory and accuracy**: A larger sketch (e.g., `--sketch-size 10000`) is more accurate but uses more RAM (~1 GB per 1000 genomes). The default is fine for 100–500 genomes.
- **Bootstrap support values are NOT the same as ASTRAL's**: ROADIES's bootstrap is a nonparametric bootstrap on the k-mer Jaccard distances; an internal branch with 80% ROADIES bootstrap is comparable to ~95% in ASTRAL. Calibrate empirically on a known tree.
- **Outgroup rooting requires explicit input**: ROADIES produces an unrooted tree by default; pass `--outgroup genome_X` to root the tree on the outgroup genome.
- **Long-read assemblies need `--assembler-error-rate`**: A long-read assembly with ~10% errors produces a k-mer profile biased by errors. Set `--assembler-error-rate 0.10` (or whatever the assembler reports) so the sketch can compensate.

## Examples

### Basic species tree from a directory of genomes
**Args:** `roadies -i genome_dir/ -o tree_out/`
**Explanation:** `-i` is the directory of FASTA files, `-o` is the output directory. Produces `tree_out/species.nwk`, `tree_out/distances.tsv`, and `tree_out/bootstrap.txt`. The default k-mer size is 21.

### Specify k-mer size for more distant species
**Args:** `roadies -i genome_dir/ -o tree_out/ -k 15`
**Explanation:** `-k 15` reduces the k-mer size to 15, suitable for species with 80–95% ANI. For very distant comparisons (60–80% ANI), use `-k 11` (slower, more memory).

### Build a tree from unassembled reads
**Args:** `roadies -i reads_dir/ -o tree_out/ --input-type fastq`
**Explanation:** `--input-type fastq` tells ROADIES to read FASTQ files instead of assembled FASTA. Useful for direct metagenomic-read-based species trees. Requires ~10× more sequencing depth than assemblies.

### Root the tree with an outgroup
**Args:** `roadies -i genome_dir/ -o tree_out/ --outgroup outgroup_genome.fa`
**Explanation:** `--outgroup` specifies the outgroup FASTA. The resulting Newick is rooted on this genome. Without an outgroup, the tree is unrooted.

### Increase bootstrap replicates
**Args:** `roadies -i genome_dir/ -o tree_out/ -b 100`
**Explanation:** `-b 100` runs 100 bootstrap replicates (default 10). The bootstrap support values are written to `tree_out/bootstrap.txt`. Higher bootstrap counts are slower but more accurate; the trade-off plateaus around 100–200.

### Adjust the sketch size for large cohorts
**Args:** `roadies -i genome_dir/ -o tree_out/ --sketch-size 5000`
**Explanation:** `--sketch-size 5000` reduces the per-genome sketch size from the default 10000 to 5000, halving the memory usage. For 1000+ genomes, this is recommended.

### Output the distance matrix only
**Args:** `roadies -i genome_dir/ -o tree_out/ --no-tree`
**Explanation:** `--no-tree` skips the tree-building step and writes only the pairwise distance matrix. Useful for downstream analyses (PCA, hierarchical clustering) that take a distance matrix.
