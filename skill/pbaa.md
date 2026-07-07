---
name: pbaa
category: qc
description: pbAA clusters HiFi reads and generates high-quality consensus sequences.
tags: [pbaa, qc, pacbio, hifi]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbAA"
---

## Concepts

- **Tool Overview**: pbAA processes PacBio HiFi sequencing data.
- **Core Function**: Clusters reads and generates consensus sequences.
- **Algorithm**: Uses clustering and consensus calling.
- **Input Format**: Accepts HiFi reads in FASTQ format.
- **Output**: Produces high-quality consensus sequences.
- **Use Case**: Long-read sequencing, consensus generation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on input read quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbaa --help`
**Explanation:** Shows available options and usage instructions.

### Generate consensus
**Args:** `pbaa -i reads.fastq -o consensus.fasta`
**Explanation:** Clusters reads and generates consensus.

### With clustering
**Args:** `pbaa -i reads.fastq -c -o consensus.fasta`
**Explanation:** Performs clustering before consensus.

### Verbose mode
**Args:** `pbaa -v -i reads.fastq -o consensus.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbaa -t 8 -i reads.fastq -o consensus.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pbaa -i reads.fastq -o consensus.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Quality filtering
**Args:** `pbaa -q 30 -i reads.fastq -o consensus.fasta`
**Explanation:** Filters reads by quality score.