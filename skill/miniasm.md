---
name: miniasm
category: assembly
description: Ultrafast de novo assembly for long noisy reads (though having no consensus step).
tags: [miniasm, assembly, long-read]
author: oxo-call-community
source_url: "https://github.com/lh3/miniasm"
---

## Concepts

- **Tool Overview**: Miniasm v0.3 is an ultrafast assembler for long noisy reads.
- **Core Function**: Assembles long-read sequencing data without consensus step.
- **Overlap Layout Consensus**: Uses OLC approach for assembly.
- **Speed Optimized**: Designed for rapid assembly of long reads.
- **Input/Output**: Accepts long reads; outputs assembly graph.
- **Long-read Assembly**: Optimized for PacBio and Nanopore reads.

## Pitfalls

- **No Consensus**: Does not perform consensus polishing.
- **Long-read Specific**: Designed for long sequencing reads.
- **Computational Resources**: Assembly may require significant resources.
- **Memory Requirements**: Memory usage can be high for large datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assembly accuracy depends on read quality.

## Examples

### Assemble long reads
**Args:** `miniasm -f reference.fasta overlaps.paf > assembly.gfa`
**Explanation:** Assembles long reads into graph format.

### With minimap2 overlaps
**Args:** `minimap2 -x ava-pb reads.fastq reads.fastq | gzip -1 > overlaps.paf.gz && miniasm -f reads.fastq overlaps.paf.gz > assembly.gfa`
**Explanation:** Uses minimap2 to find overlaps first.

### Custom overlap threshold
**Args:** `miniasm -f reads.fastq -s 1000 overlaps.paf > assembly.gfa`
**Explanation:** Uses custom overlap score threshold.

### Batch processing
**Args:** `miniasm -f reads.fastq overlaps/*.paf > assembly.gfa`
**Explanation:** Processes multiple overlap files.

### Simplify graph
**Args:** `miniasm -f reads.fastq -m 100 overlaps.paf > assembly.gfa`
**Explanation:** Merges similar edges in the graph.