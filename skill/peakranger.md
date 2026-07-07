---
name: peakranger
category: utility
description: PeakRanger provides multi-purpose NGS data analysis suite.
tags: [peakranger, utility, ngs, peak-calling]
author: oxo-call-community
source_url: "http://ranger.sourceforge.net"
---

## Concepts

- **Tool Overview**: PeakRanger analyzes NGS data.
- **Core Function**: Provides peak calling and analysis.
- **Algorithm**: Uses multiple peak detection methods.
- **Input Format**: Accepts BAM/SAM alignments.
- **Output**: Produces peak calls and reports.
- **Use Case**: ChIP-seq, peak calling, NGS analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Peak Definition**: Different methods give different results.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peakranger --help`
**Explanation:** Shows available options and usage instructions.

### Call peaks
**Args:** `peakranger call -i alignments.bam -o peaks.bed`
**Explanation:** Calls peaks from alignments.

### With control
**Args:** `peakranger call -i alignments.bam -c control.bam -o peaks.bed`
**Explanation:** Uses control sample for peak calling.

### Verbose mode
**Args:** `peakranger -v call -i alignments.bam -o peaks.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peakranger call -t 4 -i alignments.bam -o peaks.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peakranger call -i alignments.bam -o peaks.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `peakranger report -i alignments.bam -o report.html`
**Explanation:** Generates HTML report.