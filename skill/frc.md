---
name: frc
category: formatting
description: Computes FRC (Fragment Length Coverage) from SAM/BAM file.
tags: [frc, assembly evaluation, FRC, SAM/BAM]
author: oxo-call-community
source_url: "https://github.com/vezzi/FRC_align"
---

## Concepts
- **Fragment Length Coverage**: Computes FRC metric for assembly evaluation.
- **Alignment-based**: Uses SAM/BAM alignment files as input.
- **Quality Assessment**: Evaluates assembly quality using FRC curves.
- **Coverage Analysis**: Analyzes fragment coverage across the genome.
- **Visualization**: Generates FRC plots for quality assessment.

## Pitfalls
- **Alignment Dependence**: Requires high-quality alignments.
- **Reference Genome**: Needs a reference genome for alignment.
- **Memory Usage**: Processing large BAM files requires significant memory.
- **Output Interpretation**: Requires understanding of FRC metrics.
- **Format Requirements**: Strict input format requirements.

## Examples
### Compute FRC from BAM
**Args:** `frc -i alignments.bam -o frc.txt`
**Explanation:** Computes FRC metrics from alignment file.

### Generate FRC plot
**Args:** `frc -i alignments.bam -o frc.txt --plot frc.png`
**Explanation:** Computes FRC and generates visualization.

### With reference genome
**Args:** `frc -i alignments.bam -r genome.fa -o frc.txt`
**Explanation:** Uses reference genome for improved analysis.

### Multiple BAM files
**Args:** `frc -i align1.bam align2.bam -o frc.txt`
**Explanation:** Computes combined FRC from multiple alignments.

### Detailed output
**Args:** `frc -i alignments.bam -o frc.txt --detailed`
**Explanation:** Generates detailed FRC statistics.