---
name: redundans
category: assembly
description: Redundans is a pipeline that assists in assembly of heterozygous/polymorphic genomes.
tags: [redundans, assembly, heterozygous-genomes, polymorphic-genomes]
author: oxo-call-community
source_url: "https://github.com/Gabaldonlab/redundans/"
---

## Concepts

- **Tool Overview**: redundans assembles genomes.
- **Core Function**: Heterozygous genome assembly.
- **Algorithm**: Uses pipeline methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces assembled genomes.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Read Quality**: Affects assembly.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `redundans --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `redundans assemble -i reads.fastq -o assembly_dir`
**Explanation:** Assembles heterozygous genome.

### With parameters
**Args:** `redundans assemble -i reads.fastq -p params.yaml -o assembly_dir`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `redundans -v assemble -i reads.fastq -o assembly_dir`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `redundans -t 4 assemble -i reads.fastq -o assembly_dir`
**Explanation:** Uses 4 threads for parallel processing.

### With paired reads
**Args:** `redundans assemble -i reads1.fastq -j reads2.fastq -o assembly_dir`
**Explanation:** Uses paired-end reads.

### Generate report
**Args:** `redundans assemble -i reads.fastq -o assembly_dir --report report.html`
**Explanation:** Generates HTML report.