---
name: attotree
category: utility
description: Attotree - Rapid estimation of phylogenetic trees using genome sketching
tags: [phylogenetics, tree-building, genome-sketching, mash, rapid-analysis]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/attotree"
---

## Concepts

- **Tool Overview**: Attotree rapidly estimates phylogenetic trees directly from FASTA files using sketching approach similar to Mashtree, but with significantly faster computation time.

- **Sketching Approach**: Uses MinHash-based genome sketching to compute pairwise distances between genomes, then builds neighbor-joining tree from distance matrix.

- **Mashtree Compatibility**: With default parameters, produces identical output to Mashtree, allowing direct comparison and validation.

- **Multi-threading**: Supports parallel computation using multiple CPU cores for faster processing of large genome collections.

- **Input Flexibility**: Accepts multiple FASTA files directly, including gzipped files, without requiring preprocessing or alignment.

## Pitfalls

- **K-mer Size**: Default k-mer size (21) may not be optimal for all organisms. Adjust for different genome sizes and diversity levels.

- **Sketch Size**: Larger sketch sizes improve accuracy but increase memory usage and computation time.

- **Tree Method**: Default neighbor-joining may not be optimal for all datasets. Consider alternative methods for specific applications.

- **No Alignment**: Does not perform sequence alignment, so cannot detect fine-scale sequence variations or structural differences.

## Examples

### Basic tree from multiple genomes
**Args:** `attotree genome1.fasta genome2.fasta genome3.fasta > tree.nwk`
**Explanation:** Builds phylogenetic tree from three genome files, outputs in Newick format to stdout.

### Output to file
**Args:** `attotree -o tree.nwk *.fasta`
**Explanation:** Processes all FASTA files in current directory, saves tree to file instead of stdout.

### Multi-threaded processing
**Args:** `attotree -t 8 -o tree.nwk genomes/*.fasta`
**Explanation:** Uses 8 threads for parallel distance computation, significantly faster for large genome collections.

### Custom k-mer and sketch size
**Args:** `attotree -k 31 -s 50000 -o tree.nwk genomes/*.fasta`
**Explanation:** Uses k-mer size 31 and sketch size 50,000 for higher resolution in diverse datasets.

### Process gzipped files
**Args:** `attotree genomes/*.fasta.gz > tree.nwk`
**Explanation:** Automatically detects and processes gzip-compressed FASTA files without decompression.

### Input from file list
**Args:** `attotree -L genome_list.txt > tree.nwk`
**Explanation:** Reads genome file paths from list file instead of command line, useful for large numbers of genomes.

### Custom temporary directory
**Args:** `attotree -d /scratch/tmp -o tree.nwk genomes/*.fasta`
**Explanation:** Uses specified temporary directory for intermediate files, useful when default temp space is limited.

### Debug mode
**Args:** `attotree -D -o tree.nwk genomes/*.fasta`
**Explanation:** Runs in debug mode, preserving temporary files for troubleshooting and verification.

### Verbose output
**Args:** `attotree -V -o tree.nwk genomes/*.fasta`
**Explanation:** Prints detailed progress information during tree building for monitoring large analyses.
