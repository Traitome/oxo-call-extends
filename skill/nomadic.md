---
name: nomadic
category: alignment
description: Nomadic provides real-time sequencing analysis with interactive dashboard for nanopore data.
tags: [nomadic, alignment, nanopore, real-time]
author: oxo-call-community
source_url: "https://jasonahendry.github.io/nomadic/"
---

## Concepts

- **Tool Overview**: Nomadic enables real-time bioinformatics analysis during nanopore sequencing.
- **Core Function**: Performs read mapping, quality control, and variant calling in real-time.
- **Algorithm**: Processes streaming sequencing data with interactive visualization.
- **Input Format**: Accepts FASTQ reads from nanopore sequencing.
- **Output**: Produces real-time analysis results and dashboard.
- **Use Case**: Real-time sequencing analysis, rapid diagnostics, and quality monitoring.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Requirements**: Requires network for real-time updates.
- **Memory Usage**: Real-time processing requires memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Data Rate**: Limited by sequencing speed.
- **Accuracy**: Real-time results may be preliminary.

## Examples

### Display help
**Args:** `nomadic --help`
**Explanation:** Shows available options and usage instructions.

### Start real-time analysis
**Args:** `nomadic run -i /path/to/reads -o output/`
**Explanation:** Starts real-time sequencing analysis.

### With reference
**Args:** `nomadic run -i /path/to/reads -r reference.fasta -o output/`
**Explanation:** Uses reference genome for mapping.

### Variant calling
**Args:** `nomadic run -i /path/to/reads -r reference.fasta --call-variants -o output/`
**Explanation:** Enables real-time variant calling.

### Dashboard only
**Args:** `nomadic dashboard -d /path/to/data`
**Explanation:** Starts dashboard for existing data.

### Threads
**Args:** `nomadic run -i /path/to/reads -t 8 -o output/`
**Explanation:** Uses 8 threads for parallel processing.

### Quiet mode
**Args:** `nomadic run -i /path/to/reads -q -o output/`
**Explanation:** Runs with minimal output.