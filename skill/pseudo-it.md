---
name: pseudo-it
category: alignment
description: pseudo-it performs reference-based genome assembly using iterative mapping.
tags: [pseudo-it, alignment, genome-assembly, iterative-mapping]
author: oxo-call-community
source_url: "https://github.com/goodest-goodlab/pseudo-it"
---

## Concepts

- **Tool Overview**: pseudo-it assembles genomes.
- **Core Function**: Iterative mapping assembly.
- **Algorithm**: Uses iterative alignment.
- **Input Format**: Accepts reads and reference.
- **Output**: Produces assembled contigs.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Reference Quality**: Affects assembly.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pseudo-it --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `pseudo-it -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Performs iterative mapping assembly.

### With parameters
**Args:** `pseudo-it -i reads.fastq -r reference.fasta --params params.yaml -o assembly.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pseudo-it -v -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pseudo-it -t 4 -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Iteration count
**Args:** `pseudo-it -i reads.fastq -r reference.fasta -n 10 -o assembly.fasta`
**Explanation:** Uses 10 iterations.

### Generate report
**Args:** `pseudo-it -i reads.fastq -r reference.fasta -o assembly.fasta --report report.html`
**Explanation:** Generates HTML report.