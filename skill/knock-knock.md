---
name: knock-knock
category: genome-editing
description: Toolkit for analyzing CRISPR knock-in experiments
tags: [knock-knock, genome-editing, CRISPR, knock-in, sequencing]
author: oxo-call-community
source_url: "https://github.com/jeffhussmann/knock-knock"
---

## Concepts

- **CRISPR Analysis**: Analyzes CRISPR-mediated knock-in experiments
- **Knock-in Validation**: Validates successful knock-in events from sequencing data
- **Read Classification**: Classifies reads based on knock-in status
- **Efficiency Estimation**: Estimates knock-in efficiency from sequencing data
- **Large Insert Detection**: Detects large DNA insertions from CRISPR experiments
- **Multiplex Support**: Handles multiplexed knock-in experiments

## Pitfalls

- **Sequencing Depth**: Insufficient coverage affects detection accuracy
- **Read Quality**: Low-quality reads may cause misclassification
- **Insertion Size**: Very large insertions may be difficult to detect
- **Off-target Effects**: May detect off-target insertion events
- **Background Noise**: High background can affect efficiency estimates
- **Sample Preparation**: Library preparation affects read representation

## Examples

### Analyze knock-in experiment
**Args:** `knock-knock analyze -i reads.fastq -o results/`
**Explanation:** Analyzes sequencing data from knock-in experiment.

### Specify target site
**Args:** `knock-knock analyze -i reads.fastq -t target_sequence -o results/`
**Explanation:** Analyzes reads targeting specific genomic site.

### Paired-end analysis
**Args:** `knock-knock analyze -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** Uses paired-end reads for knock-in analysis.

### Estimate efficiency
**Args:** `knock-knock efficiency -i reads.fastq -o efficiency.txt`
**Explanation:** Estimates knock-in efficiency from reads.

### Visualize results
**Args:** `knock-knock visualize -i results/ -o plot.pdf`
**Explanation:** Generates visualization of knock-in analysis results.

### Batch processing
**Args:** `knock-knock batch -d samples/ -o results/`
**Explanation:** Processes multiple knock-in experiments.