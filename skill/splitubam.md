---
name: splitubam
category: alignment
description: SplitUBAM - Split unaligned BAM files per line
tags: [splitubam, alignment, bam, splitting, utility]
author: oxo-call-community
source_url: "https://github.com/fellen31/splitubam"
---

## Concepts

- **Tool Overview**: splitubam (v0.1.1) - A BAM splitting tool
- **Core Function**: Splits unaligned BAM files into multiple files per line
- **Input/Output**: Accepts unaligned BAM files; outputs split BAM files
- **Algorithm**: Line-by-line BAM splitting
- **Installation**: `conda install -c bioconda splitubam`
- **Key Features**: BAM splitting, unaligned reads, fast processing

## Pitfalls

- **Input Requirements**: Requires properly formatted unaligned BAM files
- **BAM Format**: BAM must be unaligned format
- **Memory Usage**: Large BAM files require significant memory
- **Output Format**: Output format depends on configuration
- **Splitting Accuracy**: Accuracy depends on BAM file integrity
- **File Management**: Multiple output files require disk space

## Examples

### Display help
**Args:** `splitubam --help`
**Explanation:** Shows available options and usage information.

### Basic BAM splitting
**Args:** `splitubam -i input.bam -o output_prefix`
**Explanation:** Split unaligned BAM file per line.

### With output directory
**Args:** `splitubam -i input.bam -o output_prefix --output-dir output/`
**Explanation:** Set output directory for split files.

### With compression
**Args:** `splitubam -i input.bam -o output_prefix --compress`
**Explanation:** Compress output BAM files.

### Output detailed results
**Args:** `splitubam -i input.bam -o output_prefix --detailed`
**Explanation:** Output detailed splitting information.

### Output statistics
**Args:** `splitubam -i input.bam -o output_prefix --stats`
**Explanation:** Output splitting statistics.

### Generate report
**Args:** `splitubam -i input.bam -o output_prefix --report`
**Explanation:** Generate splitting report.

### With threads
**Args:** `splitubam -i input.bam -o output_prefix -p 8`
**Explanation:** Use multiple threads for splitting.

### Batch processing
**Args:** `splitubam -i bam1.bam bam2.bam -o output_prefix`
**Explanation:** Split multiple BAM files.