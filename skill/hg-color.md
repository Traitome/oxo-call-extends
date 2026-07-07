---
name: hg-color
category: bioinformatics
description: HG-CoLoR is a hybrid method for error correction of long reads using accurate short read assemblies.
tags: [hg-color, error-correction, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pierre-morisse/HG-CoLoR"
---

## Concepts

- **Long Read Correction**: HG-CoLoR corrects long read sequencing errors.

- **Hybrid Approach**: Uses both long and short reads.

- **Short Read Assembly**: Assembles accurate short reads.

- **Error Correction**: Improves long read accuracy.

- **Sequence Polishing**: Polishes long read sequences.

- **Hybrid Assembly**: Combines data from different sequencing technologies.

## Pitfalls

- **Data Requirements**: Requires both long and short reads.

- **Assembly Quality**: Results depend on short read assembly quality.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Correct long reads
**Args:** `HG-CoLoR -l long_reads.fastq -s short_reads.fastq -o corrected.fastq`
**Explanation:** Corrects long reads using short reads.

### With assembly
**Args:** `HG-CoLoR -l long_reads.fastq -a assembly.fasta -o corrected.fastq`
**Explanation:** Uses existing assembly for correction.

### Batch processing
**Args:** `for f in *_long.fastq; do HG-CoLoR -l $f -s ${f%_long.fastq}_short.fastq -o ${f%_long.fastq}_corrected.fastq; done`
**Explanation:** Processes multiple read pairs.

### Quality filtering
**Args:** `HG-CoLoR -l long_reads.fastq -s short_reads.fastq -q 20 -o corrected.fastq`
**Explanation:** Filters by quality score.

### Help command
**Args:** `HG-CoLoR --help`
**Explanation:** Shows available options and usage information.