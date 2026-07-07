---
name: piranha-polio
category: qc
description: piranha-polio analyzes poliovirus nanopore haplotypes.
tags: [piranha-polio, qc, poliovirus, nanopore]
author: oxo-call-community
source_url: "https://github.com/polio-nanopore/piranha"
---

## Concepts

- **Tool Overview**: piranha-polio analyzes poliovirus haplotypes.
- **Core Function**: Nanopore haplotype analysis.
- **Algorithm**: Uses haplotype calling methods.
- **Input Format**: Accepts nanopore sequencing files.
- **Output**: Produces haplotype analysis results.
- **Use Case**: Poliovirus surveillance, haplotyping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on nanopore quality.
- **Haplotype Calling**: May have calling errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piranha-polio --help`
**Explanation:** Shows available options and usage instructions.

### Analyze haplotypes
**Args:** `piranha-polio -i nanopore_data.fastq -o haplotypes.txt`
**Explanation:** Analyzes poliovirus haplotypes.

### With parameters
**Args:** `piranha-polio -i nanopore_data.fastq -p params.yaml -o haplotypes.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piranha-polio -v -i nanopore_data.fastq -o haplotypes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piranha-polio -t 4 -i nanopore_data.fastq -o haplotypes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `piranha-polio -i nanopore_data.fastq -o haplotypes.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `piranha-polio -i nanopore_data.fastq -o haplotypes.txt --report report.html`
**Explanation:** Generates HTML report.