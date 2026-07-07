---
name: pantax
category: metagenomics
description: PanTax performs strain-level metagenomic profiling using pangenome graphs.
tags: [pantax, metagenomics, strain-level, pangenome]
author: oxo-call-community
source_url: "https://github.com/LuoGroup2023/PanTax"
---

## Concepts

- **Tool Overview**: PanTax profiles metagenomic samples at strain level.
- **Core Function**: Uses pangenome graphs for strain identification.
- **Algorithm**: Maps reads to pangenome graphs for strain-level profiling.
- **Input Format**: Accepts FASTQ reads and pangenome graphs.
- **Output**: Produces strain abundance profiles.
- **Use Case**: Metagenomics, strain tracking, and microbial community analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Pangenome Quality**: Results depend on pangenome quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pantax --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `pantax build -i pangenome.gfa -o index/`
**Explanation:** Creates index for pangenome graph.

### Profile sample
**Args:** `pantax profile -x index/ -i reads.fastq -o profile.txt`
**Explanation:** Profiles metagenomic sample.

### With paired-end reads
**Args:** `pantax profile -x index/ -1 reads_1.fastq -2 reads_2.fastq -o profile.txt`
**Explanation:** Uses paired-end reads for profiling.

### Verbose mode
**Args:** `pantax profile -v -x index/ -i reads.fastq -o profile.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pantax profile -t 16 -x index/ -i reads.fastq -o profile.txt`
**Explanation:** Uses 16 threads for parallel processing.

### Output format
**Args:** `pantax profile -x index/ -i reads.fastq -o profile.json --json`
**Explanation:** Outputs in JSON format.