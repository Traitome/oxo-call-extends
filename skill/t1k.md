---
name: t1k
category: variant-calling
description: T1K genotypes highly polymorphic genes (KIR, HLA) with RNA-seq, WGS or WES data.
tags: [t1k, hla-typing, kir-typing, genotyping]
author: oxo-call-community
source_url: "https://github.com/mourisl/T1K/blob/v1.0.9/README.md"
---

## Concepts

- **Tool Overview**: t1k (v1.0.9) is a versatile tool for genotyping polymorphic genes.
- **Core Function**: Genotypes highly polymorphic genes like HLA and KIR from sequencing data.
- **Algorithm**: Uses mapping-based approach for accurate typing.
- **Input/Output**: Input: BAM/FASTQ; Output: Genotype calls.
- **Applications**: HLA/KIR typing for transplantation, disease association studies.
- **Installation**: `conda install -c bioconda t1k` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing can be slow for complex regions.
- **Parameter Tuning**: Incorrect parameters affect typing accuracy.
- **Data Quality**: Requires high-quality sequencing data.
- **Reference Database**: Depends on up-to-date reference sequences.
- **Heterogeneity**: Complex gene families may be challenging.

## Examples

### Display help
**Args:** `t1k --help`
**Explanation:** Shows available options and usage information.

### Basic HLA typing
**Args:** `t1k -i sample.bam -r reference.fasta -o hla_types.txt -t hla`
**Explanation:** Perform HLA typing from BAM file.

### KIR typing
**Args:** `t1k -i sample.bam -r reference.fasta -o kir_types.txt -t kir`
**Explanation:** Perform KIR typing from BAM file.

### Verbose mode
**Args:** `t1k -i sample.bam -r reference.fasta -o types.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `t1k -i sample.bam -r reference.fasta -o types.txt --stats`
**Explanation:** Generate statistics about typing.

### Batch processing
**Args:** `for f in bams/*.bam; do t1k -i $f -r ref.fasta -o results/${f%.bam}.txt; done`
**Explanation:** Process multiple BAM files.

### Filter by quality
**Args:** `t1k -i sample.bam -r reference.fasta -o types.txt -q 20`
**Explanation:** Filter by minimum quality score.

### Include phasing
**Args:** `t1k -i sample.bam -r reference.fasta -o types.txt --phase`
**Explanation:** Include phasing information.

### Generate report
**Args:** `t1k -i sample.bam -r reference.fasta -o types.txt --report`
**Explanation:** Generate comprehensive typing report.
