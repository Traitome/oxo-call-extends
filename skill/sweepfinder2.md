---
name: sweepfinder2
category: population-genetics
description: Program for detecting recent selective sweeps in genomic data.
tags: [sweepfinder2, selective-sweeps, population-genetics, natural-selection]
author: oxo-call-community
source_url: "https://degiorgiogroup.fau.edu/sf2.html"
---

## Concepts

- **Tool Overview**: sweepfinder2 (v1.0) detects recent selective sweeps in populations.
- **Core Function**: Identifies regions under positive selection in genomes.
- **Algorithm**: Uses composite likelihood ratio test for sweep detection.
- **Input/Output**: Input: SNP data, recombination map; Output: Sweep scores.
- **Applications**: Population genetics, evolutionary biology, selection detection.
- **Installation**: `conda install -c bioconda sweepfinder2` or download from website.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Analyzing large genomes can be slow.
- **Parameter Tuning**: Incorrect parameters affect detection.
- **Input Quality**: Requires high-quality SNP data.
- **Recombination Map**: Requires accurate recombination rate estimates.
- **Population Structure**: May be affected by population structure.

## Examples

### Display help
**Args:** `sweepfinder2 --help`
**Explanation:** Shows available options and usage information.

### Basic sweep detection
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt`
**Explanation:** Detect selective sweeps from SNP data.

### With window size
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt -w 10000`
**Explanation:** Use window size of 10kb.

### Verbose mode
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt --stats`
**Explanation:** Generate statistics about sweep detection.

### Batch processing
**Args:** `for chr in chr1 chr2 chr3; do sweepfinder2 -i ${chr}_snps.txt -r recombination.txt -o ${chr}_scores.txt; done`
**Explanation:** Process multiple chromosomes.

### Filter by significance
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt -p 0.05`
**Explanation:** Filter by p-value threshold.

### Include neutral regions
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt -n neutral.txt`
**Explanation:** Use neutral regions for normalization.

### Generate report
**Args:** `sweepfinder2 -i snps.txt -r recombination.txt -o scores.txt --report`
**Explanation:** Generate comprehensive HTML report.
