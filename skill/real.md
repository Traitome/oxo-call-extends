---
name: real
category: alignment
description: REAL (REad ALigner) is an aligner for next-generation sequencing reads with high accuracy.
tags: [real, alignment, read-alignment, ngs]
author: oxo-call-community
source_url: "https://nms.kcl.ac.uk/informatics/projects/real/?id=man"
---

## Concepts

- **Tool Overview**: real aligns reads.
- **Core Function**: Read alignment.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces alignments.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects alignment.
- **Parameters**: Must be configured.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `real --help`
**Explanation:** Shows available options and usage instructions.

### Align reads
**Args:** `real align -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Aligns reads to reference.

### With parameters
**Args:** `real align -i reads.fastq -p params.yaml -o alignments.sam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `real -v align -i reads.fastq -o alignments.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `real -t 4 align -i reads.fastq -o alignments.sam`
**Explanation:** Uses 4 threads for parallel processing.

### With sensitivity
**Args:** `real align -i reads.fastq -s high -o alignments.sam`
**Explanation:** Uses high sensitivity.

### Generate report
**Args:** `real align -i reads.fastq -o alignments.sam --report report.html`
**Explanation:** Generates HTML report.