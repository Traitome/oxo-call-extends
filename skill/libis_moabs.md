---
name: libis_moabs
category: methylation
description: MOABS-based low-input bisulfite sequencing alignment
tags: [libis_moabs, methylation, bisulfite-seq, MOABS, alignment]
author: oxo-call-community
source_url: "https://github.com/Dangertrip/LiBis"
---

## Concepts

- **MOABS Integration**: Built on MOABS aligner
- **Low-input Sequencing**: Optimized for low-input bisulfite data
- **Methylation Calling**: Accurate methylation state detection
- **Bisulfite Alignment**: Specialized alignment for bisulfite reads
- **Quality Control**: Built-in quality control metrics
- **Efficiency**: Optimized for performance

## Pitfalls

- **MOABS Dependencies**: Requires MOABS installation
- **Input Requirements**: Specific input format required
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: Alignment may take significant time
- **Parameter Tuning**: Requires careful parameter optimization
- **Reference Compatibility**: Requires compatible reference genome

## Examples

### Align with MOABS
**Args:** `libis_moabs align -i reads.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Aligns reads using MOABS algorithm.

### Call methylation
**Args:** `libis_moabs call -i aligned.bam -o methylation.bed`
**Explanation:** Calls methylation states from aligned reads.

### Single-end alignment
**Args:** `libis_moabs align -f reads.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Processes single-end data.

### Paired-end alignment
**Args:** `libis_moabs align -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Processes paired-end data.

### Generate report
**Args:** `libis_moabs report -i aligned.bam -o report.pdf`
**Explanation:** Generates QC report.

### Filter reads
**Args:** `libis_moabs filter -i reads.fastq -q 20 -o filtered.fastq`
**Explanation:** Filters low-quality reads.