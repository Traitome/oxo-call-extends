---
name: nextpolish
category: assembly
description: NextPolish is a fast and accurate genome polishing tool for noisy long-read assemblies.
tags: [nextpolish, assembly, polishing, long-reads, nanopore]
author: oxo-call-community
source_url: "https://github.com/Nextomics/NextPolish"
---

## Concepts

- **Tool Overview**: NextPolish polishes genome assemblies using short or long reads.
- **Core Function**: Corrects errors in draft assemblies using sequencing reads.
- **Algorithm**: Uses iterative mapping and consensus calling.
- **Input Format**: Accepts FASTA assembly and sequencing reads.
- **Output**: Produces polished genome assembly.
- **Use Case**: Improving draft genome assemblies from long-read sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Quality**: Results depend on input read quality.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Polishing can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Complex Genomes**: Highly repetitive genomes may need special handling.

## Examples

### Display help
**Args:** `nextPolish --help`
**Explanation:** Shows available options and usage instructions.

### Basic polishing
**Args:** `nextPolish genome.fasta reads.fastq > polished.fasta`
**Explanation:** Polishes genome assembly.

### Paired-end reads
**Args:** `nextPolish genome.fasta reads_1.fastq reads_2.fastq > polished.fasta`
**Explanation:** Uses paired-end reads for polishing.

### Quality filtering
**Args:** `nextPolish -q 20 genome.fasta reads.fastq > polished.fasta`
**Explanation:** Filters reads by quality score.

### Iterations
**Args:** `nextPolish -i 3 genome.fasta reads.fastq > polished.fasta`
**Explanation:** Runs 3 polishing iterations.

### Threads
**Args:** `nextPolish -t 8 genome.fasta reads.fastq > polished.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Output stats
**Args:** `nextPolish -s genome.fasta reads.fastq > polished.fasta`
**Explanation:** Outputs polishing statistics.