---
name: fastkit
category: formatting
description: "Routine pre-processing of biological data e.g. FASTA/FASTQ files"
tags: [fastkit, formatting, FASTA, FASTQ, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/neoformit/fastkit"
---

## Concepts

- **Tool Overview**: fastkit is a collection of tools for routine pre-processing of biological sequence data including FASTA and FASTQ files.
- **Core Function**: Provides utilities for sequence data preprocessing and manipulation.
- **Input/Output**: Input: FASTA/FASTQ files. Output: Processed sequences, statistics.
- **Algorithm**: Implements various sequence processing algorithms.
- **Key Features**: Sequence preprocessing, format conversion, quality filtering, statistics generation, batch processing.
- **Installation**: `conda install -c bioconda fastkit`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **Format Compatibility**: Requires standard input formats.
- **Sequence Quality**: Poor quality sequences may affect results.
- **Processing Order**: May affect output order.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Convert FASTA to FASTQ
**Args:** `fastkit fasta2fastq -i input.fasta -o output.fastq`
**Explanation:** Converts FASTA to FASTQ format.

### Quality filtering
**Args:** `fastkit filter -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** Filters reads by quality score.

### Reverse complement
**Args:** `fastkit revcomp -i input.fasta -o revcomp.fasta`
**Explanation:** Reverse complements sequences.

### Sequence statistics
**Args:** `fastkit stats -i input.fasta -o stats.txt`
**Explanation:** Generates sequence statistics.

### Batch processing
**Args:** `fastkit batch -i fastq_files/ -o output/ --operation filter`
**Explanation:** Processes multiple files in batch mode.