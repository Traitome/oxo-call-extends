---
name: survindel2
category: variant-calling
description: A CNV caller for Illumina paired-end whole-genome sequencing data.
tags: [survindel2, cnv-calling, wgs, structural-variants]
author: oxo-call-community
source_url: "https://github.com/kensung-lab/SurVIndel2"
---

## Concepts

- **Tool Overview**: survindel2 (v1.1.4) is a CNV caller for Illumina paired-end WGS data.
- **Core Function**: Detects copy number variations from whole-genome sequencing data.
- **Algorithm**: Uses read depth and paired-end information for CNV detection.
- **Input/Output**: Input: BAM file, reference genome; Output: VCF with CNV calls.
- **Applications**: Copy number variation analysis, cancer genomics, population genetics.
- **Installation**: `conda install -c bioconda survindel2` or download from GitHub.

## Pitfalls

- **Input Quality**: Poor quality BAM files affect detection accuracy.
- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Analysis of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect CNV calling.
- **Reference Genome**: Requires matched reference genome.
- **Coverage Depth**: Low coverage affects detection sensitivity.

## Examples

### Display help
**Args:** `survindel2 --help`
**Explanation:** Shows available options and usage information.

### Basic CNV calling
**Args:** `survindel2 -i sample.bam -r reference.fasta -o cnv.vcf`
**Explanation:** Detect CNVs from WGS BAM file.

### With paired control
**Args:** `survindel2 -i tumor.bam -c normal.bam -r reference.fasta -o cnv.vcf`
**Explanation:** Use matched normal sample as control.

### Verbose mode
**Args:** `survindel2 -i sample.bam -r reference.fasta -o cnv.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `survindel2 -i sample.bam -r reference.fasta -o cnv.vcf --stats`
**Explanation:** Generate statistics about CNV calling.

### Batch processing
**Args:** `survindel2 -i bams/ -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `survindel2 -i sample.bam -r reference.fasta -o cnv.vcf -q 20`
**Explanation:** Filter CNVs by quality score.

### Include somatic calls
**Args:** `survindel2 -i tumor.bam -c normal.bam -r reference.fasta -o cnv.vcf --somatic`
**Explanation:** Call somatic CNVs in tumor-normal pairs.

### Generate report
**Args:** `survindel2 -i sample.bam -r reference.fasta -o cnv.vcf --report`
**Explanation:** Generate comprehensive HTML report.
