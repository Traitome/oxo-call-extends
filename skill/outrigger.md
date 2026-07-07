---
name: outrigger
category: utility
description: Outrigger detects de novo exons and quantifies their percent spliced-in.
tags: [outrigger, utility, splicing, rna-seq]
author: oxo-call-community
source_url: "https://yeolab.github.io/outrigger"
---

## Concepts

- **Tool Overview**: Outrigger analyzes alternative splicing events.
- **Core Function**: Detects novel exons and quantifies PSI values.
- **Algorithm**: Uses junction analysis and statistical modeling.
- **Input Format**: Accepts BAM files and annotation files.
- **Output**: Produces PSI values and splicing events.
- **Use Case**: RNA-seq analysis, alternative splicing, transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Annotation Dependencies**: Requires gene annotations.
- **Coverage Requirements**: Needs sufficient sequencing depth.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `outrigger --help`
**Explanation:** Shows available options and usage instructions.

### Detect exons
**Args:** `outrigger detect -i alignments.bam -a annotation.gtf -o events.txt`
**Explanation:** Detects de novo exons.

### Quantify PSI
**Args:** `outrigger quantify -i alignments.bam -e events.txt -o psi.txt`
**Explanation:** Quantifies percent spliced-in values.

### Visualization
**Args:** `outrigger plot -i psi.txt -o splicing_plot.png`
**Explanation:** Creates visualization of splicing events.

### Verbose mode
**Args:** `outrigger detect -i alignments.bam -v -o events.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `outrigger batch -d bams/ -o results/`
**Explanation:** Processes multiple samples.

### Filter events
**Args:** `outrigger filter -i events.txt -p 0.05 -o filtered.txt`
**Explanation:** Filters events by significance.