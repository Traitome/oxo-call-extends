---
name: svaba
category: variant-calling
description: Structural variation and indel detection by local assembly from sequencing data.
tags: [svaba, structural-variants, indel-detection, local-assembly]
author: oxo-call-community
source_url: "https://github.com/walaj/svaba"
---

## Concepts

- **Tool Overview**: svaba (v1.2.0) detects structural variations and indels using local assembly.
- **Core Function**: Identifies structural variants through de novo assembly of reads.
- **Algorithm**: Uses local assembly approach for sensitive SV and indel detection.
- **Input/Output**: Input: BAM file, reference genome; Output: VCF with SV calls.
- **Applications**: Structural variant calling, cancer genomics, population genetics.
- **Installation**: `conda install -c bioconda svaba` or download from GitHub.

## Pitfalls

- **Read Quality**: Poor quality reads affect assembly accuracy.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Local assembly can be computationally intensive.
- **Parameter Tuning**: Incorrect parameters affect detection sensitivity.
- **Reference Genome**: Requires high-quality reference genome.
- **Assembly Complexity**: Complex regions may cause assembly issues.

## Examples

### Display help
**Args:** `svaba --help`
**Explanation:** Shows available options and usage information.

### Basic SV calling
**Args:** `svaba run -t tumor.bam -n normal.bam -r reference.fasta -o svaba_results`
**Explanation:** Detect SVs and indels from tumor-normal pair.

### Tumor-only calling
**Args:** `svaba run -t tumor.bam -r reference.fasta -o svaba_results`
**Explanation:** Detect SVs without matched normal.

### Verbose mode
**Args:** `svaba run -t tumor.bam -n normal.bam -r reference.fasta -o svaba_results -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svaba run -t tumor.bam -n normal.bam -r reference.fasta -o svaba_results --stats`
**Explanation:** Generate statistics about SV calling.

### Batch processing
**Args:** `svaba run -t bams/tumor/ -n bams/normal/ -r reference.fasta -o results/`
**Explanation:** Process multiple sample pairs together.

### Filter by quality
**Args:** `svaba run -t tumor.bam -n normal.bam -r reference.fasta -o svaba_results -q 20`
**Explanation:** Filter variants by quality score.

### Include somatic calls
**Args:** `svaba run -t tumor.bam -n normal.bam -r reference.fasta -o svaba_results --somatic`
**Explanation:** Call somatic variants specifically.

### Generate report
**Args:** `svaba run -t tumor.bam -n normal.bam -r reference.fasta -o svaba_results --report`
**Explanation:** Generate comprehensive HTML report.
