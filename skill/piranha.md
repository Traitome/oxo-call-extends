---
name: piranha
category: utility
description: piranha is a peak-caller for CLIP- and RIP-Seq data.
tags: [piranha, utility, clip-seq, rip-seq]
author: oxo-call-community
source_url: "http://smithlabresearch.org/software/piranha/"
---

## Concepts

- **Tool Overview**: piranha calls peaks from CLIP/RIP-Seq.
- **Core Function**: Peak calling for sequencing data.
- **Algorithm**: Uses statistical peak detection methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces peak calling results.
- **Use Case**: RNA binding site analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Peak Detection**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piranha --help`
**Explanation:** Shows available options and usage instructions.

### Call peaks
**Args:** `piranha -i clip_seq.bam -o peaks.txt`
**Explanation:** Calls peaks from CLIP-Seq data.

### With parameters
**Args:** `piranha -i clip_seq.bam -p params.yaml -o peaks.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piranha -v -i clip_seq.bam -o peaks.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piranha -t 4 -i clip_seq.bam -o peaks.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `piranha -i clip_seq.bam -o peaks.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `piranha -i clip_seq.bam -o peaks.txt --report report.html`
**Explanation:** Generates HTML report.