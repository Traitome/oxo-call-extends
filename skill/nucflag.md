---
name: nucflag
category: assembly
description: NucFlag identifies misassemblies in genome assemblies using read mapping.
tags: [nucflag, assembly, misassembly-detection, quality-control]
author: oxo-call-community
source_url: "https://github.com/logsdon-lab/NucFlag"
---

## Concepts

- **Tool Overview**: NucFlag detects misassemblies in genome assemblies.
- **Core Function**: Identifies potential misassembly points using read evidence.
- **Algorithm**: Analyzes read mapping patterns to detect inconsistencies.
- **Input Format**: Accepts FASTA assemblies and BAM alignment files.
- **Output**: Produces misassembly flags and coordinates.
- **Use Case**: Assembly quality control, misassembly detection, and genome finishing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Mapping Quality**: Results depend on read mapping quality.
- **Read Coverage**: Requires sufficient sequencing coverage.
- **False Positives**: May report false misassembly flags.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `nucflag --help`
**Explanation:** Shows available options and usage instructions.

### Detect misassemblies
**Args:** `nucflag -a assembly.fasta -b alignments.bam -o misassemblies.txt`
**Explanation:** Detects misassemblies using read mappings.

### Output BED
**Args:** `nucflag -a assembly.fasta -b alignments.bam -o misassemblies.bed --bed`
**Explanation:** Outputs misassembly regions in BED format.

### Minimum coverage
**Args:** `nucflag -a assembly.fasta -b alignments.bam -c 10 -o misassemblies.txt`
**Explanation:** Sets minimum coverage threshold to 10.

### Confidence threshold
**Args:** `nucflag -a assembly.fasta -b alignments.bam -t 0.9 -o misassemblies.txt`
**Explanation:** Sets confidence threshold to 0.9.

### Threads
**Args:** `nucflag -a assembly.fasta -b alignments.bam -t 8 -o misassemblies.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nucflag -a assembly.fasta -b alignments.bam -v -o misassemblies.txt`
**Explanation:** Runs with verbose output.