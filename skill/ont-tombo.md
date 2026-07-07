---
name: ont-tombo
category: utility
description: ONT Tombo detects modified bases from raw nanopore sequencing data.
tags: [ont-tombo, utility, modified-bases, nanopore]
author: oxo-call-community
source_url: "https://nanoporetech.github.io/tombo/"
---

## Concepts

- **Tool Overview**: Tombo analyzes raw nanopore signals for base modifications.
- **Core Function**: Detects modified DNA/RNA bases from raw data.
- **Algorithm**: Uses statistical models for signal analysis.
- **Input Format**: Accepts fast5 raw data files.
- **Output**: Produces modification probabilities and annotations.
- **Use Case**: Epigenomics, RNA modification analysis, and base modification detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Signal Quality**: Results depend on sequencing quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **False Positives**: May report false modifications.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `tombo --help`
**Explanation:** Shows available options and usage instructions.

### Resquiggle reads
**Args:** `tombo resquiggle raw_reads.fast5 reference.fasta`
**Explanation:** Re-annotates raw signal to reference.

### Detect modifications
**Args:** `tombo detect_modifications --input-path raw_reads.fast5 --output-path modifications.txt`
**Explanation:** Detects modified bases from raw data.

### Compare samples
**Args:** `tombo compare_samples --control-path control.fast5 --treatment-path treated.fast5`
**Explanation:** Compares modification patterns between samples.

### Plot modifications
**Args:** `tombo plot modifications.txt --output plot.png`
**Explanation:** Visualizes modification results.

### Export results
**Args:** `tombo export --input modifications.txt --output modifications.bed`
**Explanation:** Exports results in BED format.

### Verbose mode
**Args:** `tombo detect_modifications --input-path raw_reads.fast5 -v`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `tombo batch --input-dir fast5_dir/ --output-dir results/`
**Explanation:** Processes multiple fast5 files.