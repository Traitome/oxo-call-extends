---
name: ray
category: hpc
description: Ray performs parallel genome assemblies for parallel DNA sequencing using distributed computing.
tags: [ray, hpc, assembly, parallel-computing]
author: oxo-call-community
source_url: "http://denovoassembler.sourceforge.net/index.html"
---

## Concepts

- **Tool Overview**: ray assembles genomes.
- **Core Function**: Parallel genome assembly.
- **Algorithm**: Uses distributed methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces contigs/scaffolds.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects assembly.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ray --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `ray assemble -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles genome.

### With parameters
**Args:** `ray assemble -i reads.fastq -p params.yaml -o assembly.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ray -v assemble -i reads.fastq -o assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ray -t 4 assemble -i reads.fastq -o assembly.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `ray assemble -i reads.fastq -k 21 -o assembly.fasta`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `ray assemble -i reads.fastq -o assembly.fasta --report report.html`
**Explanation:** Generates HTML report.