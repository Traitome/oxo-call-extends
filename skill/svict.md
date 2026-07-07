---
name: svict
category: cancer
description: SViCT detects structural variations from cell-free DNA containing low dilutions of ctDNA.
tags: [svict, liquid-biopsy, ctDNA, cancer-genomics]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/svict"
---

## Concepts

- **Tool Overview**: svict (v1.0.1) detects structural variations from cell-free DNA with low ctDNA dilution.
- **Core Function**: Identifies SVs in cfDNA samples with high sensitivity.
- **Algorithm**: Uses specialized methods for detecting SVs in low-input sequencing data.
- **Input/Output**: Input: BAM file from cfDNA sequencing; Output: VCF with SV calls.
- **Applications**: Liquid biopsy, cancer detection, minimal residual disease monitoring.
- **Installation**: `conda install -c bioconda svict` or download from GitHub.

## Pitfalls

- **Input Quality**: Poor quality cfDNA data affects detection.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Analysis of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.
- **ctDNA Fraction**: Very low ctDNA fractions may be missed.
- **Contamination**: Sample contamination affects results.

## Examples

### Display help
**Args:** `svict --help`
**Explanation:** Shows available options and usage information.

### Basic SV detection
**Args:** `svict -i cfdna.bam -r reference.fasta -o sv.vcf`
**Explanation:** Detect SVs from cfDNA BAM file.

### With matched normal
**Args:** `svict -i cfdna.bam -n normal.bam -r reference.fasta -o sv.vcf`
**Explanation:** Use matched normal for filtering.

### Verbose mode
**Args:** `svict -i cfdna.bam -r reference.fasta -o sv.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svict -i cfdna.bam -r reference.fasta -o sv.vcf --stats`
**Explanation:** Generate statistics about SV detection.

### Batch processing
**Args:** `svict -i bams/ -r reference.fasta -o results/`
**Explanation:** Process multiple cfDNA samples together.

### Filter by quality
**Args:** `svict -i cfdna.bam -r reference.fasta -o sv.vcf -q 20`
**Explanation:** Filter SVs by quality score.

### Include somatic calls
**Args:** `svict -i cfdna.bam -n normal.bam -r reference.fasta -o sv.vcf --somatic`
**Explanation:** Call somatic SVs specifically.

### Generate report
**Args:** `svict -i cfdna.bam -r reference.fasta -o sv.vcf --report`
**Explanation:** Generate comprehensive HTML report.
