---
name: clonalframeml
category: population-genomics
description: Efficient inference of recombination in bacterial genomes
tags: [clonalframeml, recombination, bacterial-genomics, phylogenetics, population-genomics]
author: oxo-call-community
source_url: "https://github.com/xavierdidelot/ClonalFrameML"
---

## Concepts

- **Tool Overview**: ClonalFrameML is a maximum likelihood method for bacterial recombination detection, identifying regions where recombination has altered the phylogenetic signal.
- **Core Function**: Identifies recombination events in bacterial genomes by comparing observed patterns to expected clonal inheritance, improving phylogenetic accuracy.
- **Input/Output**: Input: Multiple sequence alignment (FASTA) and phylogenetic tree (Newick). Output: Recombination events, corrected tree, and summary statistics.
- **Recombination Detection**: Detects imported regions where sequence patterns differ from clonal expectation, marking them as recombinant.
- **Tree Correction**: Produces a recombination-corrected tree that reflects true clonal relationships by excluding recombinant regions.
- **Statistical Framework**: Uses maximum likelihood to estimate recombination rates, import lengths, and identify specific recombination events.

## Pitfalls

- **Tree Required**: Must provide an initial phylogenetic tree. Use FastTree or RAxML to generate tree first.
- **Alignment Format**: Expects FASTA format alignment. Ensure sequences are aligned and same length.
- **Recombination Hotspots**: May miss short recombination events. Adjust parameters for different bacterial species.
- **Computational Cost**: Large datasets (>100 genomes) can be slow. Use `-r` to limit regions analyzed.
- **Core Genome**: Best used on core genome alignment. Remove accessory genome regions before analysis.

## Examples

### Basic recombination analysis
**Args:** `-x alignment.fasta -t tree.nwk -o output_prefix`
**Explanation:** Detects recombination events in the alignment using the provided tree, outputs results with specified prefix.

### Analyze specific region
**Args:** `-x alignment.fasta -t tree.nwk -o output -r start:end`
**Explanation:** Limits analysis to a specific genomic region (start to end position), useful for large alignments.

### Estimate recombination parameters only
**Args:** `-x alignment.fasta -t tree.nwk -o output --estimate_r`
**Explanation:** Estimates recombination rate parameters without identifying individual events, faster for parameter exploration.

### Output recombination-corrected tree
**Args:** `-x alignment.fasta -t tree.nwk -o output --output_tree corrected_tree.nwk`
**Explanation:** Produces a phylogenetic tree with recombination events removed, reflecting true clonal relationships.

### Specify import length
**Args:** `-x alignment.fasta -t tree.nwk -o output --import_length 500`
**Explanation:** Sets expected import length to 500bp, useful when recombination tract length is known.

### Use multiple threads
**Args:** `-x alignment.fasta -t tree.nwk -o output --threads 4`
**Explanation:** Uses 4 threads for parallel computation, speeds up analysis of large datasets.
