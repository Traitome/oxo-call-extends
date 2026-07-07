---
name: portcullis
category: qc
description: portcullis analyzes and filters splice junctions from BAM files.
tags: [portcullis, qc, splice-junctions, bam]
author: oxo-call-community
source_url: "https://ei-corebioinformatics.github.io/portcullis"
---

## Concepts

- **Tool Overview**: portcullis processes splice junctions.
- **Core Function**: Junction analysis and filtering.
- **Algorithm**: Uses alignment-based methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces junction calls.
- **Use Case**: RNA-seq analysis, alternative splicing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Junction Detection**: May have false positives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `portcullis --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `portcullis full -i alignments.bam -o junctions/`
**Explanation:** Performs splice junction analysis.

### With parameters
**Args:** `portcullis full -i alignments.bam -p params.yaml -o junctions/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `portcullis -v full -i alignments.bam -o junctions/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `portcullis -t 4 full -i alignments.bam -o junctions/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `portcullis full -i alignments.bam -o junctions.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `portcullis full -i alignments.bam -o junctions/ --report report.html`
**Explanation:** Generates HTML report.