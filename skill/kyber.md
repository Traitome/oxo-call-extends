---
name: kyber
category: qc
description: Length-accuracy heatmap generator for Oxford Nanopore reads from BAM/CRAM files
tags: [kyber, qc, nanopore, BAM, CRAM, quality-control, heatmap]
author: oxo-call-community
source_url: "https://github.com/wdecoster/kyber"
---

## Concepts

- **Accuracy Heatmap**: Creates length-accuracy heatmaps from read data
- **Nanopore Support**: Designed for Oxford Nanopore sequencing data
- **BAM/CRAM Input**: Accepts BAM and CRAM alignment files
- **Read Quality**: Visualizes read quality distributions
- **Length Analysis**: Analyzes read length accuracy relationship
- **Quality Control**: Provides QC metrics for nanopore runs

## Pitfalls

- **Alignment Required**: Requires aligned BAM/CRAM files
- **Basecalling Quality**: Results depend on basecalling quality
- **Reference Selection**: Reference genome affects alignment quality
- **Coverage Depth**: Low coverage gives unreliable metrics
- **Aligner Choice**: Different aligners may give different results
- **Samtools Dependency**: Requires samtools for CRAM processing

## Examples

### Generate heatmap
**Args:** `kyber -i alignments.bam -o heatmap.pdf`
**Explanation:** Creates length-accuracy heatmap from BAM file.

### Specify reference
**Args:** `kyber -i alignments.bam -r reference.fasta -o heatmap.pdf`
**Explanation:** Uses specific reference genome for analysis.

### CRAM input
**Args:** `kyber -i alignments.cram -r reference.fasta -o heatmap.pdf`
**Explanation:** Processes CRAM format alignment file.

### Set read length bins
**Args:** `kyber -i alignments.bam --length-bins 1000 -o heatmap.pdf`
**Explanation:** Uses 1kb read length bins.

### Quality threshold
**Args:** `kyber -i alignments.bam --min-qscore 7 -o heatmap.pdf`
**Explanation:** Only includes reads with Q score >= 7.

### Batch processing
**Args:** `kyber batch -d bams/ -o results/`
**Explanation:** Creates heatmaps for multiple BAM files.