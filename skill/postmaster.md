---
name: postmaster
category: alignment
description: postmaster annotates transcriptome alignments with posterior probabilities.
tags: [postmaster, alignment, transcriptomics, salmon]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/postmaster"
---

## Concepts

- **Tool Overview**: postmaster processes transcriptome data.
- **Core Function**: Alignment probability annotation.
- **Algorithm**: Uses Salmon quantification methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces annotated alignments.
- **Use Case**: RNA-seq analysis, transcript quantification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Quantification Bias**: May have estimation errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `postmaster --help`
**Explanation:** Shows available options and usage instructions.

### Annotate alignments
**Args:** `postmaster -i alignments.bam -q quant.sf -o annotated.bam`
**Explanation:** Annotates alignments with posterior probabilities.

### With parameters
**Args:** `postmaster -i alignments.bam -q quant.sf -p params.yaml -o annotated.bam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `postmaster -v -i alignments.bam -q quant.sf -o annotated.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `postmaster -t 4 -i alignments.bam -q quant.sf -o annotated.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `postmaster -i alignments.bam -q quant.sf -o annotated.sam --sam`
**Explanation:** Outputs in SAM format.

### Generate report
**Args:** `postmaster -i alignments.bam -q quant.sf -o annotated.bam --report report.html`
**Explanation:** Generates HTML report.