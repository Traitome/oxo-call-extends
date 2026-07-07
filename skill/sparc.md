---
name: sparc
category: qc
description: SPARC - Sparsity-based consensus algorithm for long erroneous reads
tags: [sparc, qc, consensus, long-reads, error-correction]
author: oxo-call-community
source_url: "https://github.com/yechengxi/Sparc"
---

## Concepts

- **Tool Overview**: sparc (v20160205) - A long-read consensus tool
- **Core Function**: Generates consensus from erroneous long reads
- **Input/Output**: Accepts long reads; outputs corrected consensus sequences
- **Algorithm**: Sparsity-based consensus algorithm
- **Installation**: `conda install -c bioconda sparc`
- **Key Features**: Consensus generation, error correction, long-read processing

## Pitfalls

- **Input Requirements**: Requires properly formatted long reads
- **Read Coverage**: Requires sufficient coverage for consensus
- **Read Quality**: Read quality affects consensus accuracy
- **Memory Usage**: Large read sets require significant memory
- **Output Format**: Output format depends on configuration
- **Consensus Quality**: Consensus quality depends on input reads

## Examples

### Display help
**Args:** `sparc --help`
**Explanation:** Shows available options and usage information.

### Basic consensus generation
**Args:** `sparc -i reads.fastq -o consensus.fasta`
**Explanation:** Generate consensus from reads.

### With coverage threshold
**Args:** `sparc -i reads.fastq -o consensus.fasta --min-coverage 10`
**Explanation:** Set minimum coverage threshold.

### With quality filter
**Args:** `sparc -i reads.fastq -o consensus.fasta --min-quality 20`
**Explanation:** Filter reads by quality.

### With iteration
**Args:** `sparc -i reads.fastq -o consensus.fasta --iterations 5`
**Explanation:** Set number of consensus iterations.

### Output detailed results
**Args:** `sparc -i reads.fastq -o consensus.fasta --detailed`
**Explanation:** Output detailed consensus information.

### Output statistics
**Args:** `sparc -i reads.fastq -o consensus.fasta --stats`
**Explanation:** Output consensus statistics.

### Generate report
**Args:** `sparc -i reads.fastq -o consensus.fasta --report`
**Explanation:** Generate consensus report.

### With threads
**Args:** `sparc -i reads.fastq -o consensus.fasta -p 8`
**Explanation:** Use multiple threads for consensus.