---
name: pbdagcon
category: alignment
description: pbDAGCon generates consensus sequences using directed acyclic graphs.
tags: [pbdagcon, alignment, consensus, dag]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbdagcon"
---

## Concepts

- **Tool Overview**: pbDAGCon generates consensus sequences.
- **Core Function**: Uses DAG-based multiple sequence alignment.
- **Algorithm**: Uses directed acyclic graphs for consensus.
- **Input Format**: Accepts FASTA or BAM files.
- **Output**: Produces consensus sequences.
- **Use Case**: Sequence polishing, consensus generation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Results depend on input alignments.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbdagcon --help`
**Explanation:** Shows available options and usage instructions.

### Generate consensus
**Args:** `pbdagcon -i reads.fasta -r reference.fasta -o consensus.fasta`
**Explanation:** Generates consensus sequence.

### With BAM input
**Args:** `pbdagcon -b alignments.bam -o consensus.fasta`
**Explanation:** Uses BAM alignment file.

### Verbose mode
**Args:** `pbdagcon -v -i reads.fasta -r reference.fasta -o consensus.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbdagcon -t 4 -i reads.fasta -r reference.fasta -o consensus.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbdagcon -i reads.fasta -r reference.fasta -o consensus.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Quality threshold
**Args:** `pbdagcon -q 30 -i reads.fasta -r reference.fasta -o consensus.fasta`
**Explanation:** Sets minimum quality threshold.