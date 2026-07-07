---
name: eklipse
category: expression
description: "eKLIPse is a sensitive and specific tool allowing the detection and quantification of large mtDNA rearrangements."
tags: [eklipse, expression, mtDNA, mitochondrial, rearrangements]
author: oxo-call-community
source_url: "https://github.com/dooguypapua/eKLIPse"
---

## Concepts

- **Tool Overview**: eKLIPse is a sensitive and specific bioinformatics tool for detecting and quantifying large mitochondrial DNA (mtDNA) rearrangements from high-throughput sequencing data.
- **Core Function**: Identifies and quantifies mtDNA rearrangements, including deletions, duplications, and other structural variations.
- **Input/Output**: Input: BAM files (aligned reads), mtDNA reference sequence. Output: Rearrangement calls with breakpoints, quantification metrics, visualization plots.
- **Algorithm**: Uses split-read analysis and coverage depth analysis to detect abnormal read alignments indicative of mtDNA rearrangements.
- **Key Features**: High sensitivity for low-abundance rearrangements, breakpoint precision, quantification of heteroplasmy levels, visualization support, batch processing.
- **Installation**: `conda install -c bioconda eklipse`

## Pitfalls

- **Reference Quality**: Requires high-quality mtDNA reference sequence.
- **Coverage Depth**: Low coverage may miss rare rearrangements.
- **PCR Bias**: PCR amplification can introduce artifacts in mtDNA sequencing.
- **Nuclear Mitochondrial Sequences (NUMTs)**: NUMTs can interfere with analysis.
- **Heteroplasmy Threshold**: Default thresholds may need adjustment for specific samples.

## Examples

### Basic mtDNA rearrangement detection
**Args:** `eklipse -b sample.bam -r mtDNA_ref.fasta -o results/`
**Explanation:** Detects mtDNA rearrangements from aligned BAM file.

### With specific minimum coverage
**Args:** `eklipse -b sample.bam -r mtDNA_ref.fasta -o results/ -c 100`
**Explanation:** Sets minimum coverage threshold to 100x.

### Include NUMT filtering
**Args:** `eklipse -b sample.bam -r mtDNA_ref.fasta -o results/ --filter-numts`
**Explanation:** Filters out potential NUMT-derived reads.

### Generate visualization
**Args:** `eklipse -b sample.bam -r mtDNA_ref.fasta -o results/ -p`
**Explanation:** Generates visualization plots of detected rearrangements.

### Batch processing
**Args:** `eklipse -b samples/ -r mtDNA_ref.fasta -o results/ --batch`
**Explanation:** Processes multiple BAM files in batch mode.