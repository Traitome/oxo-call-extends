---
name: strling
category: variant-calling
description: STRling detects large STR expansions from short-read sequencing data.
tags: [strling, str-analysis, short-reads, variant-detection]
author: oxo-call-community
source_url: "https://github.com/quinlan-lab/STRling"
---

## Concepts

- **Tool Overview**: strling (v0.6.0) is a method to detect large STR expansions from short-read sequencing data.
- **Core Function**: Identifies expanded short tandem repeats using short-read data.
- **Algorithm**: Uses read depth and split read analysis to detect STR expansions.
- **Input/Output**: Input: BAM file with aligned reads; Output: STR expansion calls with sizes.
- **Applications**: Genetic disease diagnosis, STR expansion analysis, research into repeat disorders.
- **Installation**: `conda install -c bioconda strling` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect detection accuracy.
- **Repeat Complexity**: Complex repeat patterns are hard to detect.
- **Read Coverage**: Insufficient coverage affects sensitivity.
- **Alignment Quality**: Poor alignment produces false calls.
- **Repeat Size**: Very large expansions may be missed.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `strling --help`
**Explanation:** Shows available options and usage information.

### Basic STR expansion detection
**Args:** `strling -i reads.bam -r reference.fasta -o results.vcf`
**Explanation:** Detect STR expansions from short-read alignment.

### With STR bed file
**Args:** `strling -i reads.bam -r reference.fasta -s strs.bed -o results.vcf`
**Explanation:** Use custom STR coordinates for targeted detection.

### Verbose mode
**Args:** `strling -i reads.bam -r reference.fasta -o results.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `strling -i reads.bam -r reference.fasta -o results.vcf --stats`
**Explanation:** Generate statistics about STR calls.

### Batch processing
**Args:** `strling -i batch/ -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `strling -i reads.bam -r reference.fasta -o results.vcf -q 20`
**Explanation:** Filter variants by quality score.

### Include flanking regions
**Args:** `strling -i reads.bam -r reference.fasta -o results.vcf -f 100`
**Explanation:** Include 100bp flanking regions in analysis.

### Generate report
**Args:** `strling -i reads.bam -r reference.fasta -o results.vcf --report`
**Explanation:** Generate comprehensive HTML report.
