---
name: wgs-assembler
category: bioinformatics
description: WGS-Assembler - Whole-genome shotgun assembler.
tags: [wgs-assembler, genome-assembly, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/wgs-assembler/"
---

## Concepts

- **Tool Overview**: WGS-Assembler - Genome assembly tool.
- **Core Function**: Assembles genomes from shotgun reads.
- **Input**: FASTQ reads.
- **Output**: Assembled contigs.
- **Installation**: Install via conda or source
- **Use Case**: Genome assembly, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Assemble genome
**Args:** `wgs-assembler -i reads.fastq -o assembly/`
**Explanation:** Assemble genome.

### With options
**Args:** `wgs-assembler -i reads.fastq -o assembly/ -t 8`
**Explanation:** Use 8 threads.
