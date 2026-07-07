---
name: peakzilla
category: expression
description: Peakzilla identifies TF binding sites from ChIP-seq/ChIP-exo data.
tags: [peakzilla, expression, chip-seq, peak-calling]
author: oxo-call-community
source_url: "http://stark.imp.ac.at/data/peakzilla"
---

## Concepts

- **Tool Overview**: Peakzilla calls TF binding peaks.
- **Core Function**: Identifies TF binding sites at high resolution.
- **Algorithm**: Uses high-accuracy peak detection.
- **Input Format**: Accepts ChIP-seq alignments.
- **Output**: Produces peak calls.
- **Use Case**: ChIP-seq, ChIP-exo, TF binding analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Peak Resolution**: Resolution depends on data type.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peakzilla --help`
**Explanation:** Shows available options and usage instructions.

### Call peaks
**Args:** `peakzilla -i chip.bam -c control.bam -o peaks.bed`
**Explanation:** Calls TF binding peaks.

### With input
**Args:** `peakzilla -i chip.bam -c control.bam -g genome.fasta -o peaks.bed`
**Explanation:** Uses genome for peak calling.

### Verbose mode
**Args:** `peakzilla -v -i chip.bam -c control.bam -o peaks.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peakzilla -t 4 -i chip.bam -c control.bam -o peaks.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peakzilla -i chip.bam -c control.bam -o peaks.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `peakzilla -i chip.bam -c control.bam -o peaks.bed --report report.html`
**Explanation:** Generates HTML report.