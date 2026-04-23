---
name: callstate
category: variant-calling
description: Replacement for GATK3 CallableLoci for identifying callable genomic regions
tags: [callstate, callable, loci, gatk, coverage]
author: oxo-call-community
source_url: "https://github.com/LuobinY/Callstate"
---

## Concepts

- **Tool Overview**: Callstate identifies callable genomic regions as a replacement for GATK3 CallableLoci.
- **Core Function**: Determines which genomic regions have sufficient coverage for variant calling.
- **Input**: Aligned BAM file and reference genome.
- **Output**: BED file with callable region classifications.
- **Application**: Quality control for variant calling pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda callstate`

## Pitfalls

- **BAM Required**: Requires sorted and indexed BAM file.
- **Coverage Threshold**: Adjust minimum coverage based on variant calling needs.
- **Reference Match**: Must use same reference as alignment.

## Examples

### Identify callable regions
**Args:** `callstate -b aligned.bam -r reference.fa -o callable.bed`
**Explanation:** Identifies genomic regions with sufficient coverage for variant calling.

### Set minimum coverage
**Args:** `callstate -b aligned.bam -r reference.fa -c 10 -o callable.bed`
**Explanation:** Requires minimum 10x coverage for callable classification.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
