---
name: reparation_blast
category: formatting
description: REPARATION_blast detects novel open reading frames with ribosome profiling data for bacteria.
tags: [reparation_blast, formatting, orf-detection, ribosome-profiling]
author: oxo-call-community
source_url: "https://github.com/RickGelhausen/REPARATION_blast"
---

## Concepts

- **Tool Overview**: reparation_blast detects ORFs.
- **Core Function**: Open reading frame detection.
- **Algorithm**: Uses BLAST methods.
- **Input Format**: Accepts ribosome profiling data.
- **Output**: Produces ORF predictions.
- **Use Case**: Gene prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reparation_blast --help`
**Explanation:** Shows available options and usage instructions.

### Detect ORFs
**Args:** `reparation_blast detect -i riboseq.bam -g genome.fasta -o orfs.txt`
**Explanation:** Detects novel open reading frames.

### With parameters
**Args:** `reparation_blast detect -i riboseq.bam -p params.yaml -o orfs.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reparation_blast -v detect -i riboseq.bam -o orfs.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reparation_blast -t 4 detect -i riboseq.bam -o orfs.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With BLAST database
**Args:** `reparation_blast detect -i riboseq.bam -d blast_db -o orfs.txt`
**Explanation:** Uses custom BLAST database.

### Generate report
**Args:** `reparation_blast detect -i riboseq.bam -o orfs.txt --report report.html`
**Explanation:** Generates HTML report.