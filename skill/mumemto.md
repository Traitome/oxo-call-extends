---
name: mumemto
category: utility
description: Mumemto finds maximal unique matches (multi-MUMs) across pangenome collections for alignment and structural variation detection.
tags: [mumemto, pangenome, multi-mum, genome-alignment, structural-variation, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/vikshiv/mumemto"
---

## Concepts

- **Tool Overview**: Mumemto v1.3.4 is a tool for finding maximal unique matches (multi-MUMs and multi-MEMs) across collections of genome sequences, such as pangenomes. It uses prefix-free parsing (PFP) for efficient computation at scale.
- **Core Function**: Computes multi-MUMs, multi-MEMs, and partial-MUMs across large genome collections. Enables pangenome alignment, synteny visualization, and structural variation detection.
- **Algorithm**: Uses prefix-free parsing (PFP) with streaming enhanced suffix arrays (SA), Burrows-Wheeler transform (BWT), and longest common prefix (LCP) arrays. 7-15x faster than MUMmer4 on core genome alignment.
- **Input Format**: Accepts multi-FASTA files representing different genome assemblies. Works with haploid, diploid, and polyploid genome collections.
- **Output**: Produces MUM/MEM coordinates in tab-delimited format, GFA-style graphs for pangenome visualization, and statistics on genome conservation and structural variation.
- **Scale**: Can process 320 human genomes (960GB) in 25.7 hours with 800GB memory. Scales to population-level pangenome analysis.

## Pitfalls

- **Memory Requirements**: Large pangenome analysis requires substantial RAM (hundreds of GB for human-scale analysis). Ensure adequate memory before running on large collections.
- **Sequence Quality**: Assemblies with contiguity issues produce fragmented matches. High-quality, chromosome-level assemblies produce more interpretable results.
- **MUM Length**: Short MUMs may be numerous but biologically uninformative. Use minimum length thresholds to filter noise (typical: 21-100bp depending on analysis goals).
- **Duplicated Regions**: Genomes with many segmental duplications produce fewer unique matches. Consider hard-masking repeat regions before analysis.
- **Index Construction**: Building the PFP index for large genomes takes significant time upfront. Plan for index construction in workflow design.
- **Output Format**: Default output is coordinate-based. Use visualization tools (included or external) to interpret synteny patterns and structural variants.

## Examples

### Compute multi-MUMs across genomes
**Args:** `mumemto genomes/ --min-length 21 --output mums.tsv`
**Explanation:** Finds all multi-MUMs of at least 21bp across genomes in the directory. Output contains chromosome, start, end, and participating genomes.

### Identify structural variations
**Args:** `mumemto genomes/ --min-length 100 --detect-sv --output sv_analysis/`
**Explanation:** Uses longer MUMs to identify structural variations like insertions, deletions, and inversions between genomes. Results in BEDPE-like format.

### Visualize pangenome synteny
**Args:** `mumemto genomes/ --visualize --output synteny_plots/`
**Explanation:** Generates synteny visualization plots showing matching regions across genomes. Includes dot plots and syntenic region diagrams.

### Compare two genome collections
**Args:** `mumemto population1/ population2/ --min-length 50 --output comparison/`
**Explanation:** Finds MUMs present in both populations for divergence analysis. Useful for population genetics and selection scans.

### Generate GFA graph
**Args:** `mumemto genomes/ --graph-format gfa --output pangenome.gfa`
**Explanation:** Exports pangenome structure as GFA format for use with pangenome graph tools like minigraph or pggg. Enables integration with graph-based pangenome workflows.

### Parallel execution on cluster
**Args:** `mumemto genomes/ --min-length 31 --threads 64 --chunk-size 10000000 --output mums/`
**Explanation:** Uses 64 threads with chunked processing for large genomes. Splits work into 10Mbp chunks for efficient cluster scheduling.
