---
name: caspeak
category: structural-variation
description: Pipeline for finding non-reference mobile element insertions
tags: [caspeak, mobile-element, insertion, structural-variation, meis]
author: oxo-call-community
source_url: "https://github.com/Rye-lxy/CasPeak"
---

## Concepts

- **Tool Overview**: CasPeak identifies non-reference mobile element insertions (MEIs) from sequencing data.
- **Core Function**: Detects mobile element insertions not present in the reference genome.
- **Algorithm**: Uses split-read and paired-end mapping strategies for MEI detection.
- **Input**: Aligned BAM file and reference genome.
- **Output**: Mobile element insertion calls with breakpoints and annotations.
- **Application**: Structural variant discovery and population genetics.
- **Installation**: Install via bioconda: `conda install -c bioconda caspeak`

## Pitfalls

- **BAM Required**: Requires sorted and indexed BAM file.
- **Reference Match**: Must use matching reference genome.
- **MEI Database**: Requires mobile element reference sequences.
- **Low Coverage**: Low coverage regions may miss insertions.

## Examples

### Detect mobile element insertions
**Args:** `caspeak -i aligned.bam -r reference.fa -o mei_calls.vcf`
**Explanation:** Identifies non-reference mobile element insertions from BAM file.

### Specify MEI database
**Args:** `caspeak -i aligned.bam -r reference.fa -d mei_database.fa -o mei_calls.vcf`
**Explanation:** Uses custom mobile element database for detection.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.