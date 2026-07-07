---
name: skder
category: assembly
description: skDER - Microbial genome dereplication
tags: ["skder", "assembly", "dereplication", "microbial"]
author: oxo-call-community
source_url: "https://github.com/raufs/skDER"
---

## Concepts

- **Tool Overview**: skDER (v1.3.4) performs efficient dereplication of microbial genomes.
- **Core Function**: Identifies and removes redundant genome sequences.
- **Algorithm**: Uses k-mer based clustering for dereplication.
- **Input/Output**: Accepts FASTA sequences and produces non-redundant set.
- **Genome Dereplication**: Specialized for microbial genome clustering.
- **Applications**: Metagenomics, genome collection curation, redundancy removal.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Dereplicate genomes
**Args:** `skder -i genomes/ -o dereplicated/`
**Explanation:** `-i` input directory; `-o` output directory.

### With CiDDER mode
**Args:** `skder -i genomes/ -c -o dereplicated/`
**Explanation:** `-c` use CiDDER algorithm.

### With threshold
**Args:** `skder -i genomes/ -t 0.99 -o dereplicated/`
**Explanation:** `-t 0.99` similarity threshold.

### Help command
**Args:** `skder --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `skder --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `skder -v -i genomes/ -o dereplicated/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `skder -t 8 -i genomes/ -o dereplicated/`
**Explanation:** `-t 8` uses 8 threads.
