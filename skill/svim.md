---
name: svim
category: variant-calling
description: SVIM is a structural variant caller specifically designed for long-read sequencing data.
tags: [svim, structural-variants, long-reads, variant-discovery]
author: oxo-call-community
source_url: "https://github.com/eldariont/svim/wiki"
---

## Concepts

- **Tool Overview**: svim (v2.0.0) is a structural variant caller optimized for long-read sequencing data.
- **Core Function**: Detects structural variants from PacBio or Oxford Nanopore sequencing reads.
- **Algorithm**: Uses read alignment signatures to identify deletions, insertions, inversions, and translocations.
- **Input/Output**: Input: BAM file with aligned reads; Output: VCF with SV calls.
- **Applications**: Long-read SV detection, genome assembly analysis, complex variant discovery.
- **Installation**: `conda install -c bioconda svim` or download from GitHub.

## Pitfalls

- **Read Quality**: Poor quality long reads affect detection accuracy.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing long reads can be computationally intensive.
- **Parameter Tuning**: Incorrect parameters affect sensitivity and specificity.
- **Alignment Quality**: Requires high-quality aligned BAM files.
- **Complex Regions**: Difficult to detect SVs in repetitive or complex genomic regions.

## Examples

### Display help
**Args:** `svim --help`
**Explanation:** Shows available options and usage information.

### Basic SV calling
**Args:** `svim alignment sample.bam reference.fasta output/`
**Explanation:** Detect SVs from aligned long reads.

### Discovery mode
**Args:** `svim discovery reads.fastq reference.fasta output/`
**Explanation:** Discover SVs directly from raw FASTQ reads.

### Verbose mode
**Args:** `svim alignment sample.bam reference.fasta output/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svim alignment sample.bam reference.fasta output/ --stats`
**Explanation:** Generate statistics about SV calling.

### Batch processing
**Args:** `svim alignment bams/ reference.fasta results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svim alignment sample.bam reference.fasta output/ -q 20`
**Explanation:** Filter SVs by quality score.

### Include all SV types
**Args:** `svim alignment sample.bam reference.fasta output/ --all-types`
**Explanation:** Detect all types of structural variants.

### Generate report
**Args:** `svim alignment sample.bam reference.fasta output/ --report`
**Explanation:** Generate comprehensive HTML report.
