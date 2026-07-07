---
name: pecat
category: assembly
description: PECAT provides phased error correction and assembly tool.
tags: [pecat, assembly, error-correction, phased]
author: oxo-call-community
source_url: "https://github.com/lemene/PECAT"
---

## Concepts

- **Tool Overview**: PECAT corrects and assembles reads.
- **Core Function**: Performs phased error correction.
- **Algorithm**: Uses error correction and assembly.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces corrected reads and assemblies.
- **Use Case**: Genome assembly, error correction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on input quality.
- **Phasing Accuracy**: Requires sufficient coverage.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pecat --help`
**Explanation:** Shows available options and usage instructions.

### Correct reads
**Args:** `pecat correct -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects errors in reads.

### Assemble reads
**Args:** `pecat assemble -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles reads into contigs.

### Verbose mode
**Args:** `pecat -v correct -i reads.fastq -o corrected.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pecat -t 8 correct -i reads.fastq -o corrected.fastq`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pecat correct -i reads.fastq -o corrected.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `pecat correct -i reads.fastq -o corrected.fastq --report report.html`
**Explanation:** Generates HTML report.