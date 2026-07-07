---
name: seqyclean
category: qc
description: seqyclean - Pre-process NGS data for downstream analysis
tags: ["seqyclean", "qc", "preprocessing", "NGS"]
author: oxo-call-community
source_url: "https://github.com/ibest/seqyclean"
---

## Concepts

- **Tool Overview**: seqyclean (v1.10.09) pre-processes NGS data for downstream analysis.
- **Core Function**: Cleans and prepares sequencing data for analysis.
- **Algorithm**: Implements quality filtering, trimming, and adapter removal.
- **Input/Output**: Accepts FASTQ files and produces cleaned sequences.
- **Preprocessing**: Focuses on NGS data cleaning and preparation.
- **Applications**: Sequence quality control, data preprocessing, and NGS analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large FASTQ files.
- **Input Format**: Requires correct FASTQ format.
- **Performance**: May be slow for extremely large files.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Clean reads
**Args:** `seqyclean -i input.fastq -o output.fastq`
**Explanation:** Cleans and filters FASTQ file.

### Paired-end
**Args:** `seqyclean -1 reads_1.fastq -2 reads_2.fastq -o output/`
**Explanation:** `-1/-2` paired-end reads.

### With adapter
**Args:** `seqyclean -i input.fastq -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -o output.fastq`
**Explanation:** `-a` adapter sequence.

### Verbose logging
**Args:** `seqyclean -v -i input.fastq -o output.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqyclean --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqyclean --version`
**Explanation:** Shows current version.

### Quality threshold
**Args:** `seqyclean -i input.fastq -q 20 -o output.fastq`
**Explanation:** `-q 20` minimum quality score.