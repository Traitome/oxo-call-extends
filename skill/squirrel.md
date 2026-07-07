---
name: squirrel
category: phylogenetics
description: SQUIRREL - Quick reconstruction to resolve evolutionary links
tags: [squirrel, phylogenetics, evolution, reconstruction, phylogeny]
author: oxo-call-community
source_url: "https://github.com/aineniamh/squirrel/blob/1.3.2/README.md"
---

## Concepts

- **Tool Overview**: squirrel (v1.3.2) - An evolutionary reconstruction tool
- **Core Function**: Quickly reconstructs evolutionary links between sequences
- **Input/Output**: Accepts sequence data; outputs evolutionary relationships
- **Algorithm**: Fast evolutionary reconstruction algorithms
- **Installation**: `conda install -c bioconda squirrel`
- **Key Features**: Evolutionary reconstruction, fast processing, phylogenetic analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence data
- **Sequence Quality**: Sequence quality affects reconstruction accuracy
- **Evolutionary Model**: Model choice affects reconstruction results
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Reconstruction Accuracy**: Accuracy depends on sequence quality and model

## Examples

### Display help
**Args:** `squirrel --help`
**Explanation:** Shows available options and usage information.

### Basic evolutionary reconstruction
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt`
**Explanation:** Reconstruct evolutionary links.

### With evolutionary model
**Args:** `squirrel -i sequences.fasta -m jukes-cantor -o evolutionary_links.txt`
**Explanation:** Use specific evolutionary model.

### With distance matrix
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt --distance-matrix`
**Explanation:** Output distance matrix.

### Multiple datasets
**Args:** `squirrel -i seq1.fasta seq2.fasta -o evolutionary_links.txt`
**Explanation:** Reconstruct links from multiple datasets.

### Output detailed results
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt --detailed`
**Explanation:** Output detailed evolutionary information.

### Output tree
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt --tree`
**Explanation:** Output phylogenetic tree.

### Output statistics
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt --stats`
**Explanation:** Output reconstruction statistics.

### Generate report
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt --report`
**Explanation:** Generate evolutionary reconstruction report.

### With threads
**Args:** `squirrel -i sequences.fasta -o evolutionary_links.txt -p 8`
**Explanation:** Use multiple threads for reconstruction.