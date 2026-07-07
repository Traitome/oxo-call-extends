---
name: sideretro
category: variant-analysis
description: sideRETRO - Somatic insertion of de novo retrotransposon detection
tags: ["sideretro", "variant-analysis", "retrotransposon", "somatic"]
author: oxo-call-community
source_url: "https://github.com/galantelab/sideRETRO"
---

## Concepts

- **Tool Overview**: sideRETRO (v1.1.6) detects somatic retrotransposon insertions from sequencing data.
- **Core Function**: Identifies de novo retrotransposon insertions in cancer genomes.
- **Algorithm**: Uses split-read and read-pair approaches for detection.
- **Input/Output**: Accepts BAM files and produces insertion calls.
- **Retrotransposon Analysis**: Specialized for LINE-1, Alu, and SVA elements.
- **Applications**: Cancer genomics, somatic mutation analysis, and mobile element research.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Genome**: Requires appropriate reference genome.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Detect insertions
**Args:** `sideretro -i tumor.bam -n normal.bam -o insertions.vcf`
**Explanation:** `-i` tumor BAM; `-n` normal BAM; `-o` output VCF.

### With reference
**Args:** `sideretro -i tumor.bam -n normal.bam -r reference.fasta -o insertions.vcf`
**Explanation:** `-r` reference genome.

### With repeatmasker
**Args:** `sideretro -i tumor.bam -n normal.bam -m repeats.bed -o insertions.vcf`
**Explanation:** `-m` RepeatMasker annotations.

### Help command
**Args:** `sideretro --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sideretro --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sideretro -v -i tumor.bam -n normal.bam -o insertions.vcf`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sideretro -t 8 -i tumor.bam -n normal.bam -o insertions.vcf`
**Explanation:** `-t 8` uses 8 threads.
