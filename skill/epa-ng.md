---
name: epa-ng
category: annotation
description: "Massively parallel phylogenetic placement of genetic sequences"
tags: [epa-ng, annotation, phylogenetics, tree-inference, sequence-placement]
author: oxo-call-community
source_url: "https://github.com/Pbdas/epa-ng"
---

## Concepts

- **Tool Overview**: EPA-ng (Evolutionary Placement Algorithm - Next Generation) is a tool for massively parallel phylogenetic placement of genetic sequences onto a reference tree.
- **Core Function**: Places query sequences onto an existing phylogenetic tree, determining their evolutionary relationships with known taxa.
- **Input/Output**: Input: Reference tree (Newick format), reference alignment (FASTA), query sequences (FASTA). Output: Placement results (JPLACE format), statistical support values.
- **Algorithm**: Uses maximum likelihood-based placement algorithm with parallel computing for efficient placement of large sequence datasets.
- **Key Features**: Massively parallel processing, high accuracy, support for large datasets, JPLACE output format, statistical support estimation.
- **Installation**: `conda install -c bioconda epa-ng`

## Pitfalls

- **Reference Tree Quality**: Placement accuracy depends on reference tree quality.
- **Alignment Quality**: Poor alignments may lead to incorrect placements.
- **Computation Resources**: Large datasets require significant computational resources.
- **Memory Usage**: May require substantial RAM for large reference trees.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic phylogenetic placement
**Args:** `epa-ng -t reference_tree.nwk -s reference_alignment.fasta -q queries.fasta -o placements.jplace`
**Explanation:** Places query sequences onto reference tree.

### With bootstrap support
**Args:** `epa-ng -t reference_tree.nwk -s reference_alignment.fasta -q queries.fasta -o placements.jplace --bootstrap`
**Explanation:** Calculates bootstrap support values for placements.

### Parallel processing
**Args:** `epa-ng -t reference_tree.nwk -s reference_alignment.fasta -q queries.fasta -o placements.jplace -T 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output detailed results
**Args:** `epa-ng -t reference_tree.nwk -s reference_alignment.fasta -q queries.fasta -o placements.jplace --verbose`
**Explanation:** Outputs verbose placement information.

### Filter low-confidence placements
**Args:** `epa-ng -t reference_tree.nwk -s reference_alignment.fasta -q queries.fasta -o placements.jplace --min-support 0.7`
**Explanation:** Filters placements with support below 0.7.