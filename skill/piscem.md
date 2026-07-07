---
name: piscem
category: alignment
description: piscem is a de Bruijn graph-based indexer and mapper.
tags: [piscem, alignment, de-bruijn, indexer]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/piscem"
---

## Concepts

- **Tool Overview**: piscem indexes and maps sequences.
- **Core Function**: Sequence mapping using de Bruijn graph.
- **Algorithm**: Uses compacted colored de Bruijn graph.
- **Input Format**: Accepts genome sequence files.
- **Output**: Produces mapping results.
- **Use Case**: Sequence alignment, read mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Index Building**: May take significant time.
- **Mapping Accuracy**: May have mapping errors.
- **Runtime**: Mapping may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piscem --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `piscem index -i reference.fasta -o index/`
**Explanation:** Builds de Bruijn graph index.

### Map reads
**Args:** `piscem map -i reads.fastq -x index/ -o mappings.sam`
**Explanation:** Maps reads to reference.

### With parameters
**Args:** `piscem map -i reads.fastq -x index/ -p params.yaml -o mappings.sam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piscem map -v -i reads.fastq -x index/ -o mappings.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piscem map -t 4 -i reads.fastq -x index/ -o mappings.sam`
**Explanation:** Uses 4 threads for parallel processing.

### Generate report
**Args:** `piscem map -i reads.fastq -x index/ -o mappings.sam --report report.html`
**Explanation:** Generates HTML report.