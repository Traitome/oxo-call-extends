---
name: gmap
category: alignment
description: gmap - Genomic mapping and alignment program for mRNA and EST sequences.
tags: [gmap, alignment, mRNA, EST, splice-alignment]
author: oxo-call-community
source_url: "http://research-pub.gene.com/gmap"
---

## Concepts
- **Splice Alignment**: Aligns mRNA/EST to genome.
- **GMAP Algorithm**: Uses GMAP alignment algorithm.
- **Intron Detection**: Detects splice sites.
- **Genome Indexing**: Indexes reference genome.
- **Polymorphism Handling**: Handles polymorphisms.

## Pitfalls
- **Genome Indexing**: Index building is time-consuming.
- **Memory Usage**: Large genomes require memory.
- **Splice Detection**: May miss unusual splice sites.
- **Parameter Tuning**: May require parameter adjustment.
- **Quality Control**: Results require QC.

## Examples
### Build index
**Args:** `gmap_build -d genome -D ./indexes genome.fasta`
**Explanation:** Builds genome index.

### Align mRNA
**Args:** `gmap -d genome -D ./indexes -t 4 -f sam mrna.fasta > aligned.sam`
**Explanation:** Aligns mRNA sequences.

### Align EST
**Args:** `gmap -d genome -D ./indexes -t 4 -f sam est.fasta > aligned.sam`
**Explanation:** Aligns EST sequences.

### Batch processing
**Args:** `gmap -d genome -D ./indexes -t 4 -f sam -B batch.txt > aligned.sam`
**Explanation:** Processes multiple batches.

### Generate report
**Args:** `gmap -d genome -D ./indexes -t 4 -f sam mrna.fasta -r > report.txt`
**Explanation:** Generates alignment report.