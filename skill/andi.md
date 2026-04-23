---
name: andi
category: alignment
description: Efficient alignment-free estimation of evolutionary distances between closely related genomes
tags: [evolutionary-distance, alignment-free, phylogeny, anchor-distance, genomes]
author: oxo-call-community
source_url: "https://github.com/evolbioinf/andi"
---

## Concepts

- **Tool Overview**: andi estimates evolutionary distances between closely related genomes using an alignment-free anchor distance method. Orders of magnitude faster than classical alignment-based approaches. Version 1.15.
- **Anchor Distance Method**: Identifies unique word matches (anchors) between genomes and uses their spacing to estimate substitution rates, avoiding full genome alignment.
- **Speed**: Extremely fast compared to alignment-based methods. Can process thousands of bacterial genomes in minutes rather than hours/days.
- **Accuracy**: Superior to other alignment-free methods for closely related genomes. Most accurate for genomes with <0.1 substitutions per site.
- **Phylogenetic Application**: Output distance matrix can be directly used with tree-building programs (e.g., PHYLIP neighbor, FastME) for rapid phylogeny reconstruction.
- **Input Format**: Accepts FASTA format genome sequences. Multiple genomes processed in a single run.
- **Outbreak Monitoring**: Designed for monitoring infectious disease outbreaks where hundreds to thousands of similar genomes accumulate rapidly.

## Pitfalls

- **Closely Related Only**: Accuracy decreases for distantly related genomes (>0.1 substitutions/site). Use traditional alignment methods for distant comparisons.
- **Genome Quality**: Requires complete or near-complete genome assemblies. Fragmented draft assemblies may produce unreliable distances.
- **Recombination**: Recombination between genomes violates model assumptions and may bias distance estimates.
- **Genome Length**: Very short sequences (<10kb) may not provide enough anchors for reliable distance estimation.
- **Output Format**: Outputs PHYLIP distance matrix format. May need conversion for some phylogenetic programs.
- **Thread Usage**: Single-threaded by default. For large datasets, consider splitting into batches.

## Examples

### Basic distance estimation
**Args:** `andi genomes/*.fasta > distances.phylip`
**Explanation:** Estimates pairwise evolutionary distances between all genomes in directory. Outputs PHYLIP distance matrix. Most common usage for rapid phylogeny.

### Distance estimation with FASTA list
**Args:** `andi genome1.fa genome2.fa genome3.fa > distances.phylip`
**Explanation:** Estimates distances between explicitly listed genome files. Useful for specific genome subsets rather than entire directory.

### Verbose output for debugging
**Args:** `andi -v genomes/*.fasta > distances.phylip`
**Explanation:** Verbose mode outputs additional information about anchor detection and distance calculation. Useful for troubleshooting unexpected results.

### Adjust minimum anchor length
**Args:** `andi -m 20 genomes/*.fasta > distances.phylip`
**Explanation:** Sets minimum anchor length to 20bp (default varies by sequence length). Longer anchors increase specificity but may miss matches in more divergent genomes.

### Output for FastME phylogeny
**Args:** `andi genomes/*.fasta | fastme -i - -o tree.nwk`
**Explanation:** Pipes distance matrix directly to FastME for rapid neighbor-joining tree construction. Complete pipeline from genomes to phylogeny in one command.

### Multiple sequence FASTA input
**Args:** `andi all_genomes.fasta > distances.phylip`
**Explanation:** Processes single FASTA file containing multiple genome sequences. Each sequence header defines a separate genome. Alternative to multiple files.

### Compare with reference genome
**Args:** `andi reference.fa query_genomes/*.fasta > ref_distances.phylip`
**Explanation:** Estimates distances between reference genome and all query genomes. Useful for outbreak analysis where reference is known outbreak strain.