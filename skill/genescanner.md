---
name: genescanner
category: variant-analysis
description: GeneScanner - Mutation analysis on nucleotide/protein alignments with Excel reports.
tags: [genescanner, mutation-analysis, alignment, variant-detection]
author: oxo-call-community
source_url: "https://github.com/jeju2486/GeneScanner/wiki/GeneScanner"
---

## Concepts
- **Mutation Analysis**: Analyzes mutations in sequence alignments.
- **Alignment Comparison**: Compares multiple sequence alignments.
- **Variant Detection**: Identifies variants in nucleotide/protein sequences.
- **Report Generation**: Generates Excel reports for analysis results.
- **Quality Assessment**: Assesses sequence quality and coverage.

## Pitfalls
- **Alignment Quality**: Depends on high-quality sequence alignments.
- **Mutation Calling**: May miss low-frequency mutations.
- **False Positives**: May detect false mutations.
- **Report Interpretation**: Requires careful interpretation of results.
- **Format Compatibility**: Requires specific input formats.

## Examples
### Analyze mutations
**Args:** `genescanner -i alignment.fasta -o mutations.xlsx`
**Explanation:** Analyzes mutations in sequence alignment and generates Excel report.

### Compare multiple alignments
**Args:** `genescanner -i align1.fasta align2.fasta -o comparison.xlsx`
**Explanation:** Compares multiple sequence alignments.

### Filter by quality
**Args:** `genescanner -i alignment.fasta -q 20 -o mutations.xlsx`
**Explanation:** Filters variants by quality score.

### Generate summary
**Args:** `genescanner -i alignment.fasta -s -o summary.txt`
**Explanation:** Generates summary statistics of mutations.

### Batch processing
**Args:** `genescanner -i ./alignments/ -o ./reports/`
**Explanation:** Processes multiple alignment files in batch.