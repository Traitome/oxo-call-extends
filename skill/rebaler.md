---
name: rebaler
category: utility
description: Rebaler performs reference-based long read assemblies of bacterial genomes.
tags: [rebaler, utility, long-read-assembly, bacterial-genomics]
author: oxo-call-community
source_url: "https://github.com/rrwick/Rebaler"
---

## Concepts

- **Tool Overview**: rebaler assembles genomes.
- **Core Function**: Reference-based assembly.
- **Algorithm**: Uses assembly methods.
- **Input Format**: Accepts long reads.
- **Output**: Produces assemblies.
- **Use Case**: Bacterial genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects assembly.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rebaler --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `rebaler assemble -i long_reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Assembles bacterial genome.

### With parameters
**Args:** `rebaler assemble -i long_reads.fastq -p params.yaml -o assembly.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rebaler -v assemble -i long_reads.fastq -o assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rebaler -t 4 assemble -i long_reads.fastq -o assembly.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `rebaler assemble -i long_reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `rebaler assemble -i long_reads.fastq -o assembly.fasta --report report.html`
**Explanation:** Generates HTML report.