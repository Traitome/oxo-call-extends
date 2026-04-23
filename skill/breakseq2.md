---
name: breakseq2
category: variant-calling
description: Ultrafast and accurate nucleotide-resolution analysis of structural variants
tags: [breakseq2, sv, structural-variant, breakpoint]
author: oxo-call-community
source_url: "https://github.com/bioinform/breakseq2"
---

## Concepts

- **Tool Overview**: BreakSeq2 performs ultrafast and accurate structural variant analysis at nucleotide resolution.
- **Core Function**: Detects structural variants including deletions, insertions, and inversions.
- **Algorithm**: Uses breakpoint library and split-read evidence for precise SV calling.
- **Input**: Aligned BAM file and reference genome.
- **Output**: Structural variant calls with precise breakpoints.
- **Installation**: Install via bioconda: `conda install -c bioconda breakseq2`

## Pitfalls

- **Breakpoint Library**: Requires or builds breakpoint library for detection.
- **BAM Input**: Requires properly aligned BAM file.
- **Memory Usage**: Large genomes require significant memory.
- **False Positives**: Filter results based on supporting read count.

## Examples

### Detect structural variants
**Args:** `breakseq2 -b aligned.bam -r reference.fa -o svs.vcf`
**Explanation:** Detects structural variants from aligned BAM file.

### Set minimum support
**Args:** `breakseq2 -b aligned.bam -r reference.fa -s 3 -o svs.vcf`
**Explanation:** Requires minimum 3 supporting reads for SV call.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
