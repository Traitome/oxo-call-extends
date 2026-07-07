---
name: ntlink
category: assembly
description: ntLink is a genome assembly scaffolder using long reads and minimizers for improved assembly contiguity.
tags: [ntlink, assembly, scaffolding, long-reads]
author: oxo-call-community
source_url: "https://github.com/BirolLab/ntLink"
---

## Concepts

- **Tool Overview**: ntLink scaffolds genome assemblies using long reads and minimizer technology.
- **Core Function**: Links contigs into scaffolds using long-read information.
- **Algorithm**: Uses minimizer-based approach for long-read scaffolding.
- **Input Format**: Accepts FASTA contigs and long-read sequencing data.
- **Output**: Produces scaffolded assemblies with improved contiguity.
- **Use Case**: Genome assembly scaffolding, long-read integration, and genome finishing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Long Read Quality**: Results depend on long-read quality.
- **Minimizer Selection**: Requires careful parameter selection.
- **Computational Cost**: Long-read processing can be intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntlink --help`
**Explanation:** Shows available options and usage instructions.

### Scaffold with long reads
**Args:** `ntlink -i contigs.fasta -l long_reads.fastq -o scaffolded.fasta`
**Explanation:** Scaffolds contigs using long reads.

### With minimizer size
**Args:** `ntlink -i contigs.fasta -l long_reads.fastq -k 21 -o scaffolded.fasta`
**Explanation:** Sets minimizer k-mer size to 21.

### Minimum length
**Args:** `ntlink -i contigs.fasta -l long_reads.fastq -m 1000 -o scaffolded.fasta`
**Explanation:** Sets minimum contig length to 1000.

### Threads
**Args:** `ntlink -i contigs.fasta -l long_reads.fastq -t 8 -o scaffolded.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Gap size
**Args:** `ntlink -i contigs.fasta -l long_reads.fastq -g 1000 -o scaffolded.fasta`
**Explanation:** Sets estimated gap size to 1000.

### Verbose mode
**Args:** `ntlink -i contigs.fasta -l long_reads.fastq -v -o scaffolded.fasta`
**Explanation:** Runs with verbose output.