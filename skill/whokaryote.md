---
name: whokaryote
category: bioinformatics
description: WhoKaryote - Genome assembly tool.
tags: [whokaryote, genome-assembly, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/whokaryote/"
---

## Concepts

- **Tool Overview**: WhoKaryote - Genome assembly tool.
- **Core Function**: Assembles genomes.
- **Input**: Sequencing reads.
- **Output**: Assembled contigs.
- **Installation**: Install via conda or source
- **Use Case**: Genome assembly, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Assemble genome
**Args:** `whokaryote -i reads.fastq -o assembly/`
**Explanation:** Assemble genome.

### With options
**Args:** `whokaryote -i reads.fastq -o assembly/ -t 8`
**Explanation:** Use 8 threads.
