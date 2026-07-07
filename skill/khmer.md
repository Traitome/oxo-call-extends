---
name: khmer
category: programming
description: khmer k-mer counting library for bioinformatics analysis.
tags: [khmer, programming, k-mer, bioinformatics, Python]
author: oxo-call-community
source_url: "https://khmer.readthedocs.io"
---

## Concepts

- **Tool Overview**: khmer (v3.0.0a3) - Python library for k-mer counting and analysis.
- **k-mer Counting**: Efficiently counts k-mers in sequence data.
- **Streaming**: Processes data in streaming mode for memory efficiency.
- **Error Correction**: Includes error correction capabilities.
- **Digital Normalization**: Reduces dataset complexity.
- **Assembly**: Supports de novo assembly tasks.

## Pitfalls

- **Memory Management**: Large datasets require careful memory management.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Python Version**: Requires specific Python version.
- **Installation**: May have complex dependencies.
- **Performance**: Python overhead may affect performance.
- **Documentation**: Some features have limited documentation.

## Examples

### Count k-mers
**Args:** `khmer count -i reads.fastq -k 21 -o counts.ct`
**Explanation:** Counts 21-mers in FASTQ file.

### Digital normalization
**Args:** `khmer normalize -i reads.fastq -o normalized.fastq -k 21 -C 20`
**Explanation:** Normalizes reads to coverage of 20.

### Error correction
**Args:** `khmer correct -i reads.fastq -o corrected.fastq -k 21`
**Explanation:** Corrects sequencing errors using k-mers.

### Filter low-abundance k-mers
**Args:** `khmer filter-abund -i reads.fastq -o filtered.fastq -k 21 -C 3`
**Explanation:** Filters reads with low-abundance k-mers.

### Merge k-mer counts
**Args:** `khmer merge -i counts1.ct counts2.ct -o merged.ct`
**Explanation:** Merges multiple k-mer count files.

### Use in Python script
**Args:** `from khmer import Countgraph; c = Countgraph(21); c.consume_fasta("genome.fasta")`
**Explanation:** Use khmer in Python code.