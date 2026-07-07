---
name: targetfinder
category: ncrna-analysis
description: Plant small RNA target prediction tool.
tags: [targetfinder, mirna, small-rna, plant]
author: oxo-call-community
source_url: "https://github.com/carringtonlab/TargetFinder"
---

## Concepts

- **Tool Overview**: targetfinder (v1.7) predicts small RNA targets in plants.
- **Core Function**: Identifies mRNA targets of small RNAs.
- **Algorithm**: Uses complementarity-based target prediction.
- **Input/Output**: Input: Small RNA and mRNA sequences; Output: Target predictions.
- **Applications**: Plant miRNA research, gene regulation studies.
- **Installation**: `conda install -c bioconda targetfinder` or download from GitHub.

## Pitfalls

- **Seed Region**: Prediction depends on seed region complementarity.
- **Energy Threshold**: Incorrect thresholds affect accuracy.
- **Plant Specificity**: Optimized for plant small RNAs.
- **Multiple Hits**: May predict multiple targets per small RNA.
- **False Positives**: May include non-functional targets.
- **Sequence Quality**: Poor quality affects prediction.

## Examples

### Display help
**Args:** `targetfinder --help`
**Explanation:** Shows available options and usage information.

### Basic target prediction
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt`
**Explanation:** Predict small RNA targets.

### With scoring
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt -sc 4`
**Explanation:** Use scoring threshold of 4.

### Verbose mode
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt --stats`
**Explanation:** Generate statistics about predictions.

### Batch processing
**Args:** `for f in sRNA/*.fasta; do targetfinder -s $f -t mrnas.fasta -o results/${f%.fasta}_targets.txt; done`
**Explanation:** Process multiple small RNA files.

### With energy cutoff
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt -e -15`
**Explanation:** Maximum folding energy of -15 kcal/mol.

### Generate report
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt --report`
**Explanation:** Generate comprehensive target report.

### Include alignments
**Args:** `targetfinder -s small_rnas.fasta -t mrnas.fasta -o targets.txt --alignments`
**Explanation:** Include target alignments.
