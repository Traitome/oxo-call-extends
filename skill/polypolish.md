---
name: polypolish
category: assembly
description: polypolish polishes genome assemblies using short reads.
tags: [polypolish, assembly, polishing, short-reads]
author: oxo-call-community
source_url: "https://github.com/rrwick/Polypolish"
---

## Concepts

- **Tool Overview**: polypolish improves genome assemblies.
- **Core Function**: Assembly polishing with short reads.
- **Algorithm**: Uses mapping and consensus methods.
- **Input Format**: Accepts assembly and short read files.
- **Output**: Produces polished genome assembly.
- **Use Case**: Genome assembly refinement, polishing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Data Quality**: Results depend on read quality.
- **Polishing Accuracy**: May have refinement errors.
- **Runtime**: Polishing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `polypolish --help`
**Explanation:** Shows available options and usage instructions.

### Polish assembly
**Args:** `polypolish assembly.fasta reads_1.fastq reads_2.fastq -o polished.fasta`
**Explanation:** Polishes genome assembly with short reads.

### With parameters
**Args:** `polypolish assembly.fasta reads_1.fastq reads_2.fastq -p params.yaml -o polished.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `polypolish -v assembly.fasta reads_1.fastq reads_2.fastq -o polished.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `polypolish -t 4 assembly.fasta reads_1.fastq reads_2.fastq -o polished.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `polypolish assembly.fasta reads_1.fastq reads_2.fastq -o polished.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `polypolish assembly.fasta reads_1.fastq reads_2.fastq -o polished.fasta --report report.html`
**Explanation:** Generates HTML report.