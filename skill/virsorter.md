---
name: virsorter
category: bioinformatics
description: VirSorter - Viral sequence identification.
tags: [virsorter, viral-genomics, sequence-identification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/srouxjgi/virsorter"
---

## Concepts

- **Tool Overview**: VirSorter - Identifies viral sequences.
- **Core Function**: Detects viral sequences in metagenomics data.
- **Input**: Contig sequences.
- **Output**: Viral sequence predictions.
- **Installation**: Install via conda or source
- **Use Case**: Virus discovery, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **False Positives**: May report false positives.

## Examples

### Identify viruses
**Args:** `virsorter run -i contigs.fasta -o results/`
**Explanation:** Identify viral sequences.

### With options
**Args:** `virsorter run -i contigs.fasta -o results/ --threads 8`
**Explanation:** Use 8 threads.
