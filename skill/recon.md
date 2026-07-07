---
name: recon
category: containerization
description: RECON performs de novo identification and classification of repeat sequence families from genomic sequences.
tags: [recon, containerization, repeat-detection, genomic-repeats]
author: oxo-call-community
source_url: "http://eddylab.org/software/recon"
---

## Concepts

- **Tool Overview**: recon identifies repeats.
- **Core Function**: Repeat family detection.
- **Algorithm**: Uses clustering methods.
- **Input Format**: Accepts genomic sequences.
- **Output**: Produces repeat families.
- **Use Case**: Repeat analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Sequence Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recon --help`
**Explanation:** Shows available options and usage instructions.

### Identify repeats
**Args:** `recon identify -i genome.fasta -o repeat_families.txt`
**Explanation:** Identifies repeat families.

### With parameters
**Args:** `recon identify -i genome.fasta -p params.yaml -o repeat_families.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recon -v identify -i genome.fasta -o repeat_families.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recon -t 4 identify -i genome.fasta -o repeat_families.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Classify repeats
**Args:** `recon classify -i repeat_families.txt -o classified_repeats.txt`
**Explanation:** Classifies repeat families.

### Generate report
**Args:** `recon identify -i genome.fasta -o repeat_families.txt --report report.html`
**Explanation:** Generates HTML report.