---
name: psiclass
category: expression
description: psiclass performs simultaneous multi-sample transcript assembly from RNA-seq data.
tags: [psiclass, expression, transcript-assembly, RNA-seq]
author: oxo-call-community
source_url: "https://github.com/splicebox/PsiCLASS/blob/v1.0.3/README.md"
---

## Concepts

- **Tool Overview**: psiclass assembles transcripts from RNA-seq.
- **Core Function**: Multi-sample transcript assembly.
- **Algorithm**: Uses splice-aware methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces transcript models.
- **Use Case**: RNA-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Sample Heterogeneity**: May affect assembly.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psiclass --help`
**Explanation:** Shows available options and usage instructions.

### Assemble transcripts
**Args:** `psiclass -i sample1.bam sample2.bam -o transcripts.gtf`
**Explanation:** Performs multi-sample transcript assembly.

### With parameters
**Args:** `psiclass -i *.bam -p params.yaml -o transcripts.gtf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psiclass -v -i *.bam -o transcripts.gtf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psiclass -t 4 -i *.bam -o transcripts.gtf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psiclass -i *.bam -o transcripts.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `psiclass -i *.bam -o transcripts.gtf --report report.html`
**Explanation:** Generates HTML report.