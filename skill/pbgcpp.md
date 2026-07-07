---
name: pbgcpp
category: utility
description: pbgcpp provides C++ implementation of GenomicConsensus.
tags: [pbgcpp, utility, consensus, c++]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbgcpp implements GenomicConsensus.
- **Core Function**: Generates consensus sequences from alignments.
- **Algorithm**: Uses statistical consensus calling.
- **Input Format**: Accepts BAM/SAM alignments.
- **Output**: Produces consensus sequences.
- **Use Case**: Sequence polishing, variant calling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Results depend on input alignments.
- **Dependency Management**: Requires C++ environment.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbgcpp --help`
**Explanation:** Shows available options and usage instructions.

### Generate consensus
**Args:** `pbgcpp -i alignments.bam -o consensus.fasta`
**Explanation:** Generates consensus sequence.

### With reference
**Args:** `pbgcpp -i alignments.bam -r reference.fasta -o consensus.fasta`
**Explanation:** Uses reference genome for consensus.

### Verbose mode
**Args:** `pbgcpp -v -i alignments.bam -o consensus.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbgcpp -t 8 -i alignments.bam -o consensus.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pbgcpp -i alignments.bam -o consensus.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Quality threshold
**Args:** `pbgcpp -q 30 -i alignments.bam -o consensus.fasta`
**Explanation:** Sets minimum quality threshold.