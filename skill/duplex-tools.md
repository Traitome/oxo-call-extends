---
name: duplex-tools
category: utility
description: Duplex Tools - Utilities for processing Oxford Nanopore duplex sequencing data.
tags: [duplex-tools, utility, nanopore, duplex-sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/duplex-tools"
---

## Concepts

- **Tool Overview**: Duplex Tools provides utilities for processing Oxford Nanopore duplex sequencing data.
- **Core Function**: Assists in identifying and processing duplex reads from Nanopore sequencing runs.
- **Input/Output**: Input: FAST5/FASTQ files from Nanopore sequencing. Output: Duplex calls, consensus sequences.
- **Algorithm**: Uses signal-level analysis to identify duplex reads and generate high-accuracy consensus.
- **Key Features**: Duplex detection, consensus generation, quality filtering, signal analysis, batch processing.
- **Installation**: `conda install -c bioconda duplex-tools`

## Pitfalls

- **Input Requirements**: Requires raw Nanopore data; basecalled reads alone are insufficient.
- **Signal Quality**: Poor signal quality affects duplex detection accuracy.
- **Computation Time**: Signal-level analysis is computationally intensive.
- **Memory Usage**: Processing large FAST5 files requires significant RAM.
- **Basecaller Compatibility**: May require specific basecaller versions for optimal results.
- **Duplex Rate**: Not all reads will form duplex pairs; yields vary by sample and sequencing conditions.

## Examples

### Call duplex reads
**Args:** `duplex-tools call-duplex --input fast5_files/ --output duplex_calls.txt`
**Explanation:** Identifies duplex read pairs from raw Nanopore data.

### Generate consensus
**Args:** `duplex-tools consensus --input duplex_calls.txt --output consensus.fa`
**Explanation:** Generates consensus sequences from duplex read pairs.

### Process basecalled reads
**Args:** `duplex-tools process --input reads.fq --output processed/`
**Explanation:** Processes basecalled reads to extract duplex information.

### With quality filtering
**Args:** `duplex-tools call-duplex --input fast5_files/ --output duplex_calls.txt --min-quality 7`
**Explanation:** Filters duplex calls by minimum quality score.

### Batch processing
**Args:** `duplex-tools call-duplex --input-dir fast5_dir/ --output-dir results/`
**Explanation:** Processes multiple directories of FAST5 files.

### Generate statistics
**Args:** `duplex-tools stats --input duplex_calls.txt --output stats.txt`
**Explanation:** Generates statistics about duplex calling performance.