---
name: ragout
category: assembly
description: Ragout performs chromosome-level scaffolding using multiple reference genomes for improved assembly.
tags: [ragout, assembly, scaffolding, chromosome-level]
author: oxo-call-community
source_url: "https://github.com/fenderglass/Ragout"
---

## Concepts

- **Tool Overview**: ragout scaffolds assemblies.
- **Core Function**: Chromosome-level scaffolding.
- **Algorithm**: Uses reference genomes.
- **Input Format**: Accepts contigs/scaffolds.
- **Output**: Produces improved scaffolds.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Reference Quality**: Affects scaffolding.
- **Parameters**: Must be configured.
- **Runtime**: Scaffolding may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ragout --help`
**Explanation:** Shows available options and usage instructions.

### Run scaffolding
**Args:** `ragout scaffold -i contigs.fasta -r references.txt -o scaffolds.fasta`
**Explanation:** Scaffolds contigs using references.

### With parameters
**Args:** `ragout scaffold -i contigs.fasta -p params.yaml -o scaffolds.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ragout -v scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ragout -t 4 scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Multiple references
**Args:** `ragout scaffold -i contigs.fasta -r ref1.fasta,ref2.fasta -o scaffolds.fasta`
**Explanation:** Uses multiple reference genomes.

### Generate report
**Args:** `ragout scaffold -i contigs.fasta -o scaffolds.fasta --report report.html`
**Explanation:** Generates HTML report.