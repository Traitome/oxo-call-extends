---
name: pplacer
category: alignment
description: pplacer places query sequences on reference phylogenetic trees.
tags: [pplacer, alignment, phylogenetics, tree]
author: oxo-call-community
source_url: "http://matsen.fredhutch.org/pplacer"
---

## Concepts

- **Tool Overview**: pplacer performs phylogenetic placement.
- **Core Function**: Sequence placement on trees.
- **Algorithm**: Uses likelihood/posterior methods.
- **Input Format**: Accepts FASTA/tree files.
- **Output**: Produces placement results.
- **Use Case**: Phylogenetics, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Data Quality**: Results depend on sequence quality.
- **Placement Accuracy**: May have misplacement.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pplacer --help`
**Explanation:** Shows available options and usage instructions.

### Place sequences
**Args:** `pplacer -i queries.fasta -t reference.tree -a reference.aln -o placements.jplace`
**Explanation:** Places sequences on phylogenetic tree.

### With parameters
**Args:** `pplacer -i queries.fasta -t reference.tree -a reference.aln -p params.yaml -o placements.jplace`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pplacer -v -i queries.fasta -t reference.tree -a reference.aln -o placements.jplace`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pplacer -j 4 -i queries.fasta -t reference.tree -a reference.aln -o placements.jplace`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pplacer -i queries.fasta -t reference.tree -a reference.aln -o placements.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `pplacer -i queries.fasta -t reference.tree -a reference.aln -o placements.jplace --report report.html`
**Explanation:** Generates HTML report.