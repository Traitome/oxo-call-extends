---
name: brass
category: variant-calling
description: BRASS (Breakpoint via Assembly) for detecting somatic structural rearrangements
tags: [brass, sv, structural-variant, somatic, rearrangement]
author: oxo-call-community
source_url: "https://github.com/cancerit/BRASS"
---

## Concepts

- **Tool Overview**: BRASS detects somatic structural rearrangements using assembly-based approach.
- **Core Function**: Identifies breakpoints and structural variants from paired-end sequencing data.
- **Algorithm**: Uses local assembly around discordant read pairs for precise breakpoint detection.
- **Input**: Tumor and normal BAM files from paired-end sequencing.
- **Output**: Structural rearrangement calls with assembled breakpoint sequences.
- **Installation**: Install via bioconda: `conda install -c bioconda brass`

## Pitfalls

- **Paired Samples**: Requires matched tumor-normal pairs for somatic calling.
- **Memory Usage**: Assembly step requires significant memory for complex regions.
- **Reference Genome**: Must use the same reference as alignment.
- **Coverage**: Low coverage regions may have reduced sensitivity.

## Examples

### Run somatic SV detection
**Args:** `brass -r reference.fa -t tumor.bam -n normal.bam -o results/`
**Explanation:** Detects somatic structural rearrangements between tumor and normal samples.

### Set minimum supporting reads
**Args:** `brass -r reference.fa -t tumor.bam -n normal.bam -m 3 -o results/`
**Explanation:** Requires minimum 3 supporting reads for SV call.

### Specify output directory
**Args:** `brass -r reference.fa -t tumor.bam -n normal.bam -o brass_output/`
**Explanation:** Writes all output files to specified directory.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
