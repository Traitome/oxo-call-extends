---
name: meraculous
category: assembly
description: Whole genome assembler for large genomes using hybrid k-mer/read-based approach.
tags: [meraculous, genome-assembly, large-genomes]
author: oxo-call-community
source_url: "https://jgi.doe.gov/data-and-tools/meraculous/"
---

## Concepts

- **Tool Overview**: Meraculous assembles large genomes using Illumina sequencing data.
- **Core Function**: Whole genome assembly for large eukaryotic genomes.
- **Hybrid Approach**: Combines k-mer and read-based assembly strategies.
- **Parallel Processing**: Multi-threaded parallelization for performance.
- **Error Correction**: Implicit error correction during assembly.
- **Installation**: `conda install -c bioconda meraculous`

## Pitfalls

- **Memory Requirements**: High memory for large genomes.
- **Computation Time**: Slow for very large datasets.
- **Parameter Tuning**: Requires careful k-mer selection.
- **Input Quality**: Depends on high-quality Illumina data.
- **Assembly Fragmentation**: May produce fragmented assemblies.
- **Cluster Requirements**: Requires HPC cluster for large genomes.

## Examples

### Assemble genome
**Args:** `Meraculous.pl -config config.txt`
**Explanation:** Runs genome assembly with configuration file.

### Create config
**Args:** `Meraculous.pl -prepare -output config.txt`
**Explanation:** Creates assembly configuration file.

### Run specific stage
**Args:** `Meraculous.pl -config config.txt -stage 2`
**Explanation:** Runs specific assembly stage.

### With multiple k-mers
**Args:** `Meraculous.pl -config config.txt -kmer 21,33,55`
**Explanation:** Uses multiple k-mer sizes.

### Help documentation
**Args:** `Meraculous.pl --help`
**Explanation:** Displays available options.
