---
name: strcount
category: variant-calling
description: Count the number of repeats in Short Tandem Repeat Expansions from long reads.
tags: [strcount, str-analysis, long-reads, repeat-counting]
author: oxo-call-community
source_url: "https://github.com/sabiqali/strcount"
---

## Concepts

- **Tool Overview**: strcount (v0.1.1) is a tool for counting repeat units in Short Tandem Repeat (STR) expansions from long-read sequencing data.
- **Core Function**: Determines the number of repeat units in STR expansions using long reads.
- **Algorithm**: Uses alignment and pattern matching to count repeat units in expanded regions.
- **Input/Output**: Input: Long-read BAM file, STR coordinates; Output: Repeat count estimates.
- **Applications**: Genetic disease diagnosis, STR expansion analysis, research into repeat disorders.
- **Installation**: `conda install -c bioconda strcount` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect repeat counting accuracy.
- **Repeat Complexity**: Complex repeat patterns are hard to count.
- **Read Coverage**: Insufficient coverage affects accuracy.
- **Alignment Quality**: Poor alignment produces incorrect counts.
- **Repeat Size**: Very large expansions may be miscalled.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `strcount --help`
**Explanation:** Shows available options and usage information.

### Basic repeat counting
**Args:** `strcount -i reads.bam -r reference.fasta -o counts.txt`
**Explanation:** Count STR repeats from long-read alignment.

### With STR bed file
**Args:** `strcount -i reads.bam -r reference.fasta -s strs.bed -o counts.txt`
**Explanation:** Use custom STR coordinates for counting.

### Verbose mode
**Args:** `strcount -i reads.bam -r reference.fasta -o counts.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output confidence
**Args:** `strcount -i reads.bam -r reference.fasta -o counts.txt --confidence`
**Explanation:** Output confidence scores for repeat counts.

### Custom thresholds
**Args:** `strcount -i reads.bam -r reference.fasta -o counts.txt -c 0.9`
**Explanation:** Minimum confidence threshold of 0.9.

### Batch processing
**Args:** `strcount -i batch/ -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `strcount -i reads.bam -r reference.fasta -o counts.txt -q 20`
**Explanation:** Filter reads by mapping quality.

### Generate report
**Args:** `strcount -i reads.bam -r reference.fasta -o counts.txt --report`
**Explanation:** Generate comprehensive HTML report.
