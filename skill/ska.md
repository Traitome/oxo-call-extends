---
name: ska
category: sequence-analysis
description: SKA - Split Kmer Analysis
tags: ["ska", "sequence-analysis", "k-mer", "comparative"]
author: oxo-call-community
source_url: "https://github.com/simonrharris/SKA/wiki"
---

## Concepts

- **Tool Overview**: SKA (v1.0) performs split k-mer analysis for bacterial genomes.
- **Core Function**: Generates k-mer based alignments and trees.
- **Algorithm**: Uses split k-mers for efficient sequence comparison.
- **Input/Output**: Accepts FASTA sequences and produces alignments.
- **K-mer Analysis**: Specialized for bacterial comparative genomics.
- **Applications**: Phylogenetics, SNP calling, genome comparison.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Legacy software, may have compatibility issues.
- **Documentation**: Limited documentation available.

## Examples

### Build alignment
**Args:** `ska fasta2matrix -i genomes/ -o alignment.fasta`
**Explanation:** `-i` directory with genomes; `-o` output alignment.

### Build tree
**Args:** `ska matrix2tree -i alignment.fasta -o tree.nwk`
**Explanation:** Builds tree from alignment.

### Call SNPs
**Args:** `ska snp -i genomes/ -o snps.vcf`
**Explanation:** Calls SNPs across genomes.

### Help command
**Args:** `ska --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `ska --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `ska -v fasta2matrix -i genomes/ -o alignment.fasta`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `ska -t 8 fasta2matrix -i genomes/ -o alignment.fasta`
**Explanation:** `-t 8` uses 8 threads.
