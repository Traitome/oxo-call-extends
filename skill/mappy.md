---
name: mappy
category: alignment
description: Minimap2 Python binding
tags: [mappy, alignment, minimap2, python]
author: oxo-call-community
source_url: "https://github.com/lh3/minimap2"
---

## Concepts

- **Tool Overview**: mappy v2.30 - Python binding for minimap2, a fast and versatile sequence alignment tool.
- **Core Function**: Provides Python API for minimap2 sequence alignment functionality.
- **Input/Output**: Input: Sequence data (FASTA/FASTQ); Output: Alignments in various formats.
- **Installation**: `conda install -c bioconda mappy`
- **Minimap2 Integration**: Directly interfaces with minimap2 for fast alignment.
- **Python API**: Provides convenient Python interface for sequence alignment.

## Pitfalls

- **Version Compatibility**: Requires compatible minimap2 version.
- **Memory Usage**: Large sequences require significant memory.
- **Parameter Knowledge**: Requires understanding of minimap2 parameters.
- **Output Parsing**: Output formats require proper parsing.
- **Index Building**: Large reference genomes require time to index.
- **Python Version**: Requires compatible Python version.

## Examples

### Basic alignment
**Args:** `import mappy; a = mappy.Aligner("ref.fa"); hits = list(a.map("read.fastq"))`
**Explanation:** Aligns reads to reference using Python API.

### Create index
**Args:** `import mappy; mappy.fastq_read("reads.fastq")`
**Explanation:** Reads FASTQ file using mappy.

### Multiple alignments
**Args:** `import mappy; a = mappy.Aligner("ref.fa", preset="sr"); hits = [h for h in a.map("read.fastq")]`
**Explanation:** Performs short-read alignment.

### Custom parameters
**Args:** `import mappy; a = mappy.Aligner("ref.fa", k=15, w=5)`
**Explanation:** Creates aligner with custom k-mer and window size.

### SAM output
**Args:** `import mappy; a = mappy.Aligner("ref.fa"); print(a.map("read.fastq", fmt="sam"))`
**Explanation:** Outputs alignments in SAM format.

### Chaining mode
**Args:** `import mappy; a = mappy.Aligner("ref.fa", preset="map-pb"); hits = list(a.map("read.fastq"))`
**Explanation:** Uses PacBio mapping preset.