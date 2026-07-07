---
name: ptgaul
category: assembly
description: ptGAUL assembles plastid genomes using long-read sequencing data.
tags: [ptgaul, assembly, plastid-genome, long-read]
author: oxo-call-community
source_url: "https://github.com/Bean061/ptgaul"
---

## Concepts

- **Tool Overview**: ptgaul assembles plastid genomes.
- **Core Function**: Plastid genome assembly.
- **Algorithm**: Uses long-read assembly.
- **Input Format**: Accepts long-read sequencing data.
- **Output**: Produces plastid genome assembly.
- **Use Case**: Plastid genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Read Length**: Affects assembly quality.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ptgaul --help`
**Explanation:** Shows available options and usage instructions.

### Assemble plastid genome
**Args:** `ptgaul -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Assembles plastid genome from long reads.

### With parameters
**Args:** `ptgaul -i reads.fastq -r reference.fasta -p params.yaml -o assembly.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ptgaul -v -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ptgaul -t 4 -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `ptgaul -i reads.fastq -r reference.fasta -o assembly.gb --genbank`
**Explanation:** Outputs in GenBank format.

### Generate report
**Args:** `ptgaul -i reads.fastq -r reference.fasta -o assembly.fasta --report report.html`
**Explanation:** Generates HTML report.