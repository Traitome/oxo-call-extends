---
name: meraculous
category: assembly
description: Meraculous is a whole genome assembler for Next Generation Sequencing data, geared for large genomes. It's hybrid k-mer/read-based approach capitalizes on the high accuracy of Illumina sequence by eschewing an explicit error correction step which we argue to be redundant with the assembly process. Meraculous achieves high performance with large datasets by utilizing lightweight data structures and multi-threaded parallelization, allowing to assemble human-sized genomes on a high-cpu cluster in under a day. The process pipeline implements a highly transparent and portable model of job control and monitoring where different assembly stages can be executed and re-executed separately or in unison on a wide variety of architectures.
tags: [meraculous, assembly]
author: oxo-call-community
source_url: "https://jgi.doe.gov/data-and-tools/meraculous/"
---

## Concepts

- **Tool Overview**: meraculous v2.2.6 - Meraculous is a whole genome assembler for Next Generation Sequencing data, geared for large genomes. It's hybrid k-mer/read-based approach capitalizes on the high accuracy of Illumina sequence by eschewing an explicit error correction step which we argue to be redundant with the assembly process. Meraculous achieves high performance with large datasets by utilizing lightweight data structures and multi-threaded parallelization, allowing to assemble human-sized genomes on a high-cpu cluster in under a day. The process pipeline implements a highly transparent and portable model of job control and monitoring where different assembly stages can be executed and re-executed separately or in unison on a wide variety of architectures..
- **Core Function**: Meraculous is a whole genome assembler for Next Generation Sequencing data, geared for large genomes. It's hybrid k-mer/read-based approach capitalizes on the high accuracy of Illumina sequence by eschewing an explicit error correction step which we argue to be redundant with the assembly process. Meraculous achieves high performance with large datasets by utilizing lightweight data structures and multi-threaded parallelization, allowing to assemble human-sized genomes on a high-cpu cluster in under a day. The process pipeline implements a highly transparent and portable model of job control and monitoring where different assembly stages can be executed and re-executed separately or in unison on a wide variety of architectures.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda meraculous`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
