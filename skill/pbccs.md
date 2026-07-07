---
name: pbccs
category: qc
description: pbCCS generates Highly Accurate Single-Molecule Consensus Reads (HiFi Reads).
tags: [pbccs, qc, pacbio, hifi]
author: oxo-call-community
source_url: "https://ccs.how"
---

## Concepts

- **Tool Overview**: pbCCS generates HiFi consensus reads.
- **Core Function**: Processes subreads into consensus sequences.
- **Algorithm**: Uses circular consensus sequencing.
- **Input Format**: Accepts PacBio subreads.
- **Output**: Produces HiFi consensus reads.
- **Use Case**: Long-read sequencing, high-quality variant calling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on input quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ccs --help`
**Explanation:** Shows available options and usage instructions.

### Generate HiFi reads
**Args:** `ccs subreads.bam hifi_reads.bam`
**Explanation:** Generates HiFi consensus reads.

### With multiple threads
**Args:** `ccs -j 8 subreads.bam hifi_reads.bam`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ccs -v subreads.bam hifi_reads.bam`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `ccs --output-format fastq subreads.bam hifi_reads.fastq`
**Explanation:** Outputs in FASTQ format.

### Quality threshold
**Args:** `ccs --min-rq 0.9 subreads.bam hifi_reads.bam`
**Explanation:** Sets minimum read quality threshold.

### Generate report
**Args:** `ccs --report report.json subreads.bam hifi_reads.bam`
**Explanation:** Generates JSON report.