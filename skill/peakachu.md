---
name: peakachu
category: variant-calling
description: PEAKachu provides peak calling for CLIP-seq data.
tags: [peakachu, variant-calling, clip-seq, peak-calling]
author: oxo-call-community
source_url: "https://github.com/tbischler/PEAKachu"
---

## Concepts

- **Tool Overview**: PEAKachu calls peaks in CLIP-seq.
- **Core Function**: Identifies binding sites from CLIP-seq.
- **Algorithm**: Uses peak detection algorithms.
- **Input Format**: Accepts CLIP-seq alignments.
- **Output**: Produces peak calls.
- **Use Case**: RNA-binding protein analysis, CLIP-seq.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Peak Definition**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peakachu --help`
**Explanation:** Shows available options and usage instructions.

### Call peaks
**Args:** `peakachu -i alignments.bam -o peaks.bed`
**Explanation:** Calls peaks from CLIP-seq data.

### With control
**Args:** `peakachu -i alignments.bam -c control.bam -o peaks.bed`
**Explanation:** Uses control sample for peak calling.

### Verbose mode
**Args:** `peakachu -v -i alignments.bam -o peaks.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peakachu -t 4 -i alignments.bam -o peaks.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peakachu -i alignments.bam -o peaks.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `peakachu -i alignments.bam -o peaks.bed --report report.html`
**Explanation:** Generates HTML report.