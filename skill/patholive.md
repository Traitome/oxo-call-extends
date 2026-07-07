---
name: patholive
category: metagenomics
description: PathoLive performs real-time pathogen diagnostics from metagenomic sequencing data.
tags: [patholive, metagenomics, pathogen-detection, real-time]
author: oxo-call-community
source_url: "https://gitlab.com/SimonHTausch/PathoLive"
---

## Concepts

- **Tool Overview**: PathoLive detects pathogens in real-time from sequencing.
- **Core Function**: Identifies pathogens from metagenomic data.
- **Algorithm**: Uses rapid classification algorithms.
- **Input Format**: Accepts Illumina sequencing reads.
- **Output**: Produces real-time pathogen identification.
- **Use Case**: Clinical diagnostics, outbreak response.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Latency**: Real-time processing requires optimization.
- **Sensitivity**: Depends on sequencing depth.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `patholive --help`
**Explanation:** Shows available options and usage instructions.

### Run diagnostics
**Args:** `patholive -i reads.fastq -o results/`
**Explanation:** Performs real-time pathogen detection.

### Real-time mode
**Args:** `patholive -i reads.fastq -o results/ --stream`
**Explanation:** Processes data in streaming mode.

### Verbose mode
**Args:** `patholive -v -i reads.fastq -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `patholive -t 8 -i reads.fastq -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `patholive -i reads.fastq -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `patholive -i reads.fastq -o results/ -r report.html`
**Explanation:** Generates HTML report.