---
name: portello
category: alignment
description: portello transfers HiFi read mappings from assembly contigs to reference.
tags: [portello, alignment, hifi, mapping]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/portello"
---

## Concepts

- **Tool Overview**: portello processes HiFi sequencing data.
- **Core Function**: Mapping transfer between assemblies.
- **Algorithm**: Uses alignment-based methods.
- **Input Format**: Accepts BAM/FASTA files.
- **Output**: Produces transferred mappings.
- **Use Case**: Genome assembly, variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Mapping Accuracy**: May have alignment errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `portello --help`
**Explanation:** Shows available options and usage instructions.

### Transfer mappings
**Args:** `portello -i reads.bam -c contigs.fasta -r reference.fasta -o mapped.bam`
**Explanation:** Transfers HiFi mappings to reference.

### With parameters
**Args:** `portello -i reads.bam -c contigs.fasta -r reference.fasta -p params.yaml -o mapped.bam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `portello -v -i reads.bam -c contigs.fasta -r reference.fasta -o mapped.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `portello -t 4 -i reads.bam -c contigs.fasta -r reference.fasta -o mapped.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `portello -i reads.bam -c contigs.fasta -r reference.fasta -o mapped.sam --sam`
**Explanation:** Outputs in SAM format.

### Generate report
**Args:** `portello -i reads.bam -c contigs.fasta -r reference.fasta -o mapped.bam --report report.html`
**Explanation:** Generates HTML report.