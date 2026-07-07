---
name: gap2seq
category: assembly
description: Gap2Seq is a tool for filling gaps between contigs in genome assemblies.
tags: [gap2seq, genome assembly, gap filling, contigs]
author: oxo-call-community
source_url: "https://www.cs.helsinki.fi/u/lmsalmel/Gap2Seq"
---

## Concepts
- **Gap Filling**: Fills gaps between contigs in assemblies.
- **Local Assembly**: Uses seed-and-extend approach.
- **Paired-end Reads**: Utilizes paired-end read information.
- **Scaffold Improvement**: Improves scaffold quality.
- **Assembly Completion**: Helps complete draft assemblies.

## Pitfalls
- **Read Coverage**: Requires sufficient read coverage in gaps.
- **Complex Regions**: May struggle with complex repetitive regions.
- **Assembly Quality**: Results depend on initial assembly quality.
- **Short Gaps**: Better for filling shorter gaps.
- **Computational Time**: Can be time-consuming for large genomes.

## Examples
### Fill gaps
**Args:** `gap2seq -graph assembly.gfa -reads reads.fastq -output filled.gfa`
**Explanation:** Fills gaps in assembly graph.

### With reads file
**Args:** `gap2seq -graph assembly.gfa -reads1 reads_1.fastq -reads2 reads_2.fastq -output filled.gfa`
**Explanation:** Uses paired-end reads for gap filling.

### Specify gap size
**Args:** `gap2seq -graph assembly.gfa -reads reads.fastq -min 10 -max 1000 -output filled.gfa`
**Explanation:** Fills gaps between 10-1000bp.

### Set iterations
**Args:** `gap2seq -graph assembly.gfa -reads reads.fastq -iter 3 -output filled.gfa`
**Explanation:** Runs 3 iterations of gap filling.

### Validate results
**Args:** `gap2seq -graph filled.gfa -validate -o validation.txt`
**Explanation:** Validates gap-filled assembly.