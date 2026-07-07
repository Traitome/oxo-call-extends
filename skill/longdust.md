---
name: longdust
category: sequence-analysis
description: Longdust - Identify long highly repetitive STRs, VNTRs, satellite DNA and low-complexity regions
tags: [longdust, sequence-analysis, repeat-detection, STRs, VNTRs, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lh3/longdust"
---

## Concepts

- **Repeat Detection**: Identification of repetitive DNA sequences
- **STRs**: Short Tandem Repeats detection
- **VNTRs**: Variable Number Tandem Repeats detection
- **Satellite DNA**: Satellite DNA identification
- **Low-Complexity Regions**: Low-complexity region detection
- **Genome Analysis**: Genome-wide repeat analysis

## Pitfalls

- **False Positives**: May produce false positive repeat calls
- **Memory Usage**: Memory-intensive for large genomes
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Sequence Quality**: Poor quality sequences affect results
- **Repeat Complexity**: Highly complex repeats may be missed

## Examples

### Detect repeats
**Args:** `longdust -i genome.fasta -o repeats.bed`
**Explanation:** Identifies repetitive regions in genome.

### Minimum length
**Args:** `longdust -i genome.fasta -o repeats.bed -l 100`
**Explanation:** Sets minimum repeat length to 100bp.

### Threads
**Args:** `longdust -i genome.fasta -o repeats.bed -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `longdust -i genome.fasta -o repeats.gff -f gff`
**Explanation:** Outputs results in GFF format.

### Verbose output
**Args:** `longdust -i genome.fasta -o repeats.bed -v`
**Explanation:** Provides detailed output.

### Mask repeats
**Args:** `longdust -i genome.fasta -o repeats.bed -m masked.fasta`
**Explanation:** Masks repetitive regions in output.