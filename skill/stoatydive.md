---
name: stoatydive
category: chip-seq
description: StoatyDive evaluates and classifies predicted peak profiles to assess the binding specificity of a protein to its targets.
tags: [stoatydive, chip-seq, peak-analysis, binding-specificity]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/StoatyDive"
---

## Concepts

- **Tool Overview**: stoatydive (v1.1.1) is a tool for evaluating and classifying ChIP-seq peak profiles to assess protein-DNA binding specificity.
- **Core Function**: Analyzes peak shapes and patterns to distinguish specific from non-specific binding events.
- **Algorithm**: Uses machine learning to classify peaks based on shape features and binding characteristics.
- **Input/Output**: Input: Peak calls (BED/BAM), genome annotation; Output: Classification scores and specificity metrics.
- **Applications**: ChIP-seq quality control, identifying true binding sites, filtering false positives.
- **Installation**: `conda install -c bioconda stoatydive` or download from GitHub.

## Pitfalls

- **Peak Quality**: Poor quality peaks affect classification accuracy.
- **Training Data**: Model trained on specific data may not generalize to all datasets.
- **Threshold Selection**: Incorrect thresholds affect sensitivity/specificity.
- **Genome Version**: Incorrect genome assembly affects annotation matching.
- **Batch Effects**: Batch effects between samples affect comparison.
- **Memory Requirements**: Large peak sets require significant memory.

## Examples

### Display help
**Args:** `stoatydive --help`
**Explanation:** Shows available options and usage information.

### Basic peak classification
**Args:** `stoatydive -i peaks.bed -g genome.fasta -o results.txt`
**Explanation:** Classify peaks to assess binding specificity.

### With annotation
**Args:** `stoatydive -i peaks.bed -g genome.fasta -a annotation.gtf -o results.txt`
**Explanation:** Incorporate gene annotation for better classification.

### Verbose mode
**Args:** `stoatydive -i peaks.bed -g genome.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `stoatydive -i peaks.bed -g genome.fasta -o results.txt --plot`
**Explanation:** Generate visualization of peak profiles.

### Custom model
**Args:** `stoatydive -i peaks.bed -g genome.fasta -o results.txt -m custom_model.pkl`
**Explanation:** Use custom-trained classification model.

### Batch processing
**Args:** `stoatydive -i batch/ -g genome.fasta -o results/`
**Explanation:** Process multiple peak files together.

### Filter by confidence
**Args:** `stoatydive -i peaks.bed -g genome.fasta -o results.txt -c 0.8`
**Explanation:** Filter peaks with confidence below 0.8.

### Generate report
**Args:** `stoatydive -i peaks.bed -g genome.fasta -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
