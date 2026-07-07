---
name: read2tree
category: utility
description: Read2Tree builds phylogenetic trees directly from sequencing reads without assembly.
tags: [read2tree, utility, phylogenetics, read-based]
author: oxo-call-community
source_url: "https://github.com/DessimozLab/read2tree"
---

## Concepts

- **Tool Overview**: read2tree builds trees.
- **Core Function**: Read-based phylogeny.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects tree building.
- **Parameters**: Must be configured.
- **Runtime**: Tree building may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `read2tree --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `read2tree build -i reads.fastq -o tree.newick`
**Explanation:** Builds phylogenetic tree.

### With parameters
**Args:** `read2tree build -i reads.fastq -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `read2tree -v build -i reads.fastq -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `read2tree -t 4 build -i reads.fastq -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `read2tree build -i reads.fastq -r reference.fasta -o tree.newick`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `read2tree build -i reads.fastq -o tree.newick --report report.html`
**Explanation:** Generates HTML report.