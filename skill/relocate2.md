---
name: relocate2
category: alignment
description: RelocaTE2 is a high-resolution transposable element insertion site mapping tool for population resequencing.
tags: [relocate2, alignment, transposable-elements, insertion-sites]
author: oxo-call-community
source_url: "https://github.com/stajichlab/RelocaTE2"
---

## Concepts

- **Tool Overview**: relocate2 maps insertions.
- **Core Function**: TE insertion mapping.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces insertion sites.
- **Use Case**: Population genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects mapping.
- **Parameters**: Must be configured.
- **Runtime**: Mapping may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `relocate2 --help`
**Explanation:** Shows available options and usage instructions.

### Map insertions
**Args:** `relocate2 map -i reads.fastq -r reference.fasta -o insertions.bed`
**Explanation:** Maps transposable element insertions.

### With parameters
**Args:** `relocate2 map -i reads.fastq -p params.yaml -o insertions.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `relocate2 -v map -i reads.fastq -o insertions.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `relocate2 -t 4 map -i reads.fastq -o insertions.bed`
**Explanation:** Uses 4 threads for parallel processing.

### With TE library
**Args:** `relocate2 map -i reads.fastq -t te_library.fasta -o insertions.bed`
**Explanation:** Uses custom TE library.

### Generate report
**Args:** `relocate2 map -i reads.fastq -o insertions.bed --report report.html`
**Explanation:** Generates HTML report.