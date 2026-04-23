---
name: kma
category: alignment
description: KMA is a mapping method designed to map raw reads directly against redundant databases, in an ultra-fast manner using seed and extend.
tags: [kma, alignment]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/kma"
---

## Concepts

- **Tool Overview**: kma v1.6.10 - KMA is a mapping method designed to map raw reads directly against redundant databases, in an ultra-fast manner using seed and extend..
- **Core Function**: KMA is a mapping method designed to map raw reads directly against redundant databases, in an ultra-fast manner using seed and extend.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kma`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Index database
**Args:** `kma -i reference.fasta -o dbname -t 4`
**Explanation:** Creates KMA index from reference sequences.

### Map reads
**Args:** `kma -i reads.fastq -o output -t_db dbname -t 4`
**Explanation:** Maps reads against indexed database using 4 threads.

