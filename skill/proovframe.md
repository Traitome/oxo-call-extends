---
name: proovframe
category: variant-calling
description: proovframe performs frame-shift correction for long read (meta)genomics.
tags: [proovframe, variant-calling, long-reads, frameshift]
author: oxo-call-community
source_url: "https://github.com/thackl/proovframe"
---

## Concepts

- **Tool Overview**: proovframe corrects frame-shifts.
- **Core Function**: Frame-shift correction.
- **Algorithm**: Uses sequence alignment methods.
- **Input Format**: Accepts BAM/FASTA files.
- **Output**: Produces corrected sequences.
- **Use Case**: Long-read sequencing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Correction Accuracy**: May have errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proovframe --help`
**Explanation:** Shows available options and usage instructions.

### Correct frameshifts
**Args:** `proovframe -i aligned.bam -r reference.fasta -o corrected.bam`
**Explanation:** Corrects frame-shifts in long-read data.

### With parameters
**Args:** `proovframe -i aligned.bam -r reference.fasta -p params.yaml -o corrected.bam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proovframe -v -i aligned.bam -r reference.fasta -o corrected.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proovframe -t 4 -i aligned.bam -r reference.fasta -o corrected.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proovframe -i aligned.bam -r reference.fasta -o corrected.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `proovframe -i aligned.bam -r reference.fasta -o corrected.bam --report report.html`
**Explanation:** Generates HTML report.