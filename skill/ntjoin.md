---
name: ntjoin
category: assembly
description: ntJoin is a genome assembly scaffolder using minimizer graphs for improved contiguity.
tags: [ntjoin, assembly, scaffolding, minimizer]
author: oxo-call-community
source_url: "https://github.com/BirolLab/ntJoin"
---

## Concepts

- **Tool Overview**: ntJoin scaffolds genome assemblies using minimizer-based approaches.
- **Core Function**: Links contigs into larger scaffolds using minimizer graphs.
- **Algorithm**: Uses minimizer-based graph construction for scaffolding.
- **Input Format**: Accepts FASTA contigs and reference sequences.
- **Output**: Produces scaffolded assemblies.
- **Use Case**: Genome assembly scaffolding, improving contiguity, and genome finishing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Minimizer Selection**: Requires careful minimizer parameter selection.
- **Reference Quality**: Results depend on reference quality.
- **Computational Cost**: Scaffolding can be computationally intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntjoin --help`
**Explanation:** Shows available options and usage instructions.

### Scaffold assembly
**Args:** `ntjoin -i contigs.fasta -r reference.fasta -o scaffolded.fasta`
**Explanation:** Scaffolds contigs using reference.

### With reads
**Args:** `ntjoin -i contigs.fasta -r reference.fasta -f reads.fastq -o scaffolded.fasta`
**Explanation:** Uses reads for additional scaffolding information.

### Minimum length
**Args:** `ntjoin -i contigs.fasta -r reference.fasta -m 1000 -o scaffolded.fasta`
**Explanation:** Sets minimum contig length to 1000.

### Threads
**Args:** `ntjoin -i contigs.fasta -r reference.fasta -t 8 -o scaffolded.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Gap size
**Args:** `ntjoin -i contigs.fasta -r reference.fasta -g 500 -o scaffolded.fasta`
**Explanation:** Sets estimated gap size to 500.

### Verbose mode
**Args:** `ntjoin -i contigs.fasta -r reference.fasta -v -o scaffolded.fasta`
**Explanation:** Runs with verbose output.