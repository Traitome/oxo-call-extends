---
name: polap
category: qc
description: polap assembles plant organelle genomes from long reads.
tags: [polap, qc, assembly, plant]
author: oxo-call-community
source_url: "https://github.com/goshng/polap"
---

## Concepts

- **Tool Overview**: polap assembles organelle genomes.
- **Core Function**: Plant organelle long-read assembly.
- **Algorithm**: Uses assembly and polishing methods.
- **Input Format**: Accepts long-read sequencing data.
- **Output**: Produces organelle genome assemblies.
- **Use Case**: Plant mitochondrial/chloroplast genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Assembly Accuracy**: May have assembly errors.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `polap --help`
**Explanation:** Shows available options and usage instructions.

### Assemble organelle genome
**Args:** `polap -i reads.fastq -o assembly/`
**Explanation:** Assembles plant organelle genome.

### With parameters
**Args:** `polap -i reads.fastq -p params.yaml -o assembly/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `polap -v -i reads.fastq -o assembly/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `polap -t 4 -i reads.fastq -o assembly/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `polap -i reads.fastq -o assembly.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `polap -i reads.fastq -o assembly/ --report report.html`
**Explanation:** Generates HTML report.