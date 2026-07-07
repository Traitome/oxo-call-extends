---
name: chum
category: capture
description: Evaluate the effectiveness of baits in a hybrid selection panel
tags: [chum, capture, bait-design, target-enrichment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/clintval/chum/blob/0.2.0/README.md"
---

## Concepts

- **Tool Overview**: CHUM evaluates the effectiveness of RNA or DNA baits in hybrid selection/capture panels.
- **Core Function**: Assesses bait performance by analyzing capture efficiency, coverage, and specificity.
- **Features**: Bait design validation, coverage analysis, and performance metrics calculation.
- **Input**: Bait sequences, target regions, and sequencing data.
- **Output**: Bait performance metrics and coverage statistics.
- **Application**: Targeted sequencing panel design, bait optimization, and capture efficiency assessment.
- **Installation**: Install via bioconda: `conda install -c bioconda chum`

## Pitfalls

- **Bait Design**: Bait performance depends on careful design and specificity.
- **Target Regions**: Requires well-defined target regions for accurate evaluation.
- **Sequencing Depth**: Results depend on sufficient sequencing depth.
- **Repeat Regions**: May have issues with repetitive regions in targets.
- **Off-Target Effects**: May capture unintended sequences.

## Examples

### Evaluate bait panel
**Args:** `chum -b baits.fasta -t targets.bed -o bait_evaluation.txt`
**Explanation:** Evaluates bait effectiveness for target regions.

### With sequencing data
**Args:** `chum -b baits.fasta -t targets.bed -s reads.bam -o evaluation.txt`
**Explanation:** Evaluates bait performance using sequencing data.

### Generate report
**Args:** `chum -b baits.fasta -t targets.bed --report -o report.html`
**Explanation:** Generates HTML report of bait evaluation.

### Display help
**Args:** `chum --help`
**Explanation:** Shows all available options and usage information.