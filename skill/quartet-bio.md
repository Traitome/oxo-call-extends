---
name: quartet-bio
category: assembly
description: Quartet-bio is a telomere-to-telomere toolkit for gap-free genome assembly and centromeric repeat identification.
tags: [quartet-bio, assembly, genome-assembly, centromere]
author: oxo-call-community
source_url: "https://github.com/aaranyue/quarTeT/blob/main/README.md"
---

## Concepts

- **Tool Overview**: quartet-bio assembles genomes.
- **Core Function**: Gap-free assembly.
- **Algorithm**: Uses assembly methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces genome assemblies.
- **Use Case**: Genome sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Read Quality**: Affects assembly.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quartet-bio --help`
**Explanation:** Shows available options and usage instructions.

### Run assembly
**Args:** `quartet-bio assemble -i reads.fastq -o assembly/`
**Explanation:** Assembles gap-free genome.

### With parameters
**Args:** `quartet-bio assemble -i reads.fastq -p params.yaml -o assembly/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quartet-bio -v assemble -i reads.fastq -o assembly/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quartet-bio -t 4 assemble -i reads.fastq -o assembly/`
**Explanation:** Uses 4 threads for parallel processing.

### Identify repeats
**Args:** `quartet-bio repeats -i assembly.fasta -o repeats.txt`
**Explanation:** Identifies centromeric repeats.

### Generate report
**Args:** `quartet-bio assemble -i reads.fastq -o assembly/ --report report.html`
**Explanation:** Generates HTML report.