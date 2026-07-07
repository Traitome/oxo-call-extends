---
name: peregrine-2021
category: qc
description: Peregrine-2021 assembles genomes from long-read data.
tags: [peregrine-2021, qc, assembly, long-read]
author: oxo-call-community
source_url: "https://github.com/cschin/peregrine-2021"
---

## Concepts

- **Tool Overview**: Peregrine assembles genomes.
- **Core Function**: Assembles from long-read data.
- **Algorithm**: Uses overlap-based assembly.
- **Input Format**: Accepts long-read FASTQ files.
- **Output**: Produces genome assemblies.
- **Use Case**: Genome assembly, long-read analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Read Accuracy**: Requires good read accuracy.
- **Assembly Quality**: Results depend on read quality.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peregrine-2021 --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `peregrine-2021 -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles genome from long reads.

### With parameters
**Args:** `peregrine-2021 -i reads.fastq -p params.yaml -o assembly.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `peregrine-2021 -v -i reads.fastq -o assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peregrine-2021 -t 8 -i reads.fastq -o assembly.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `peregrine-2021 -i reads.fastq -o assembly.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `peregrine-2021 -i reads.fastq -o assembly.fasta --report report.html`
**Explanation:** Generates HTML report.