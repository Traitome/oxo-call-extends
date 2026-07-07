---
name: gapfiller
category: assembly
description: GapFiller is a seed-and-extend local assembler to fill the gap within paired reads.
tags: [gapfiller, genome assembly, gap filling, paired reads]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/gapfiller"
---

## Concepts
- **Gap Closure**: Closes gaps in genome assemblies.
- **Seed-and-Extend**: Uses seed-and-extend algorithm.
- **Paired-end Analysis**: Utilizes paired-end read information.
- **Local Assembly**: Performs local de novo assembly.
- **Scaffold Extension**: Extends scaffolds to close gaps.

## Pitfalls
- **Coverage Requirements**: Requires high coverage in gap regions.
- **Repeat Complexity**: Struggles with repetitive gap regions.
- **Computational Time**: Can be slow for large genomes.
- **Memory Usage**: Requires significant memory.
- **Initial Assembly**: Depends on initial assembly quality.

## Examples
### Fill gaps in scaffolds
**Args:** `gapfiller -i scaffolds.fasta -b reads.bam -o filled_scaffolds.fasta`
**Explanation:** Fills gaps using read alignments.

### Set iterations
**Args:** `gapfiller -i scaffolds.fasta -b reads.bam -t 5 -o filled_scaffolds.fasta`
**Explanation:** Runs up to 5 fill iterations.

### Gap size threshold
**Args:** `gapfiller -i scaffolds.fasta -b reads.bam -g 10 -G 2000 -o filled_scaffolds.fasta`
**Explanation:** Only fills gaps between 10-2000bp.

### With library info
**Args:** `gapfiller -i scaffolds.fasta -b reads.bam -l library.txt -o filled_scaffolds.fasta`
**Explanation:** Uses library information for better results.

### Save log
**Args:** `gapfiller -i scaffolds.fasta -b reads.bam -o filled_scaffolds.fasta -log gapfiller.log`
**Explanation:** Saves detailed log file.