---
name: freddie
category: annotation
description: Annotation-independent detection of splicing isoforms using RNA long-reads.
tags: [freddie, alternative splicing, long reads, isoform detection]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/freddie"
---

## Concepts
- **Isoform Detection**: Identifies alternative splicing isoforms from long-read RNA-seq data.
- **Annotation-independent**: Does not require existing gene annotations.
- **Long-read Analysis**: Optimized for PacBio and Oxford Nanopore reads.
- **Splicing Junction Detection**: Identifies novel splice junctions.
- **Isoform Quantification**: Quantifies expression levels of detected isoforms.

## Pitfalls
- **Read Quality**: Requires high-quality long reads.
- **Computational Complexity**: Processing large datasets is computationally intensive.
- **Memory Requirements**: Large memory footprint for genome-scale analysis.
- **False Positives**: May detect spurious isoforms from sequencing errors.
- **Transcript Assembly**: Requires accurate transcript assembly.

## Examples
### Detect isoforms from BAM
**Args:** `freddie detect -i alignments.bam -o isoforms.gtf`
**Explanation:** Detects splicing isoforms from aligned long reads.

### Quantify isoforms
**Args:** `freddie quantify -i alignments.bam -g isoforms.gtf -o expression.txt`
**Explanation:** Quantifies expression levels of detected isoforms.

### Novel junction detection
**Args:** `freddie junctions -i alignments.bam -o junctions.bed`
**Explanation:** Identifies novel splice junctions.

### Compare samples
**Args:** `freddie compare -i sample1.gtf sample2.gtf -o comparison.txt`
**Explanation:** Compares isoform expression between samples.

### Visualize isoforms
**Args:** `freddie plot -i isoforms.gtf -g genome.fa -o isoforms.png`
**Explanation:** Generates visualization of detected isoforms.