---
name: phables
category: metagenomics
description: phables resolves bacteriophage genomes from fragmented assemblies.
tags: [phables, metagenomics, phage, assembly]
author: oxo-call-community
source_url: "https://github.com/Vini2/phables"
---

## Concepts

- **Tool Overview**: phables resolves phage genomes.
- **Core Function**: Assembles high-quality bacteriophage genomes.
- **Algorithm**: Uses phage bubble resolution.
- **Input Format**: Accepts fragmented assembly files.
- **Output**: Produces complete phage genomes.
- **Use Case**: Phage assembly, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Assembly Quality**: Results depend on input quality.
- **Bubble Detection**: May miss complex bubbles.
- **Runtime**: Resolution may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phables --help`
**Explanation:** Shows available options and usage instructions.

### Resolve genomes
**Args:** `phables -i assembly.fasta -o phage_genomes.fasta`
**Explanation:** Resolves phage genomes from assembly.

### With parameters
**Args:** `phables -i assembly.fasta -p params.yaml -o phage_genomes.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phables -v -i assembly.fasta -o phage_genomes.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phables -t 4 -i assembly.fasta -o phage_genomes.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phables -i assembly.fasta -o phage_genomes.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `phables -i assembly.fasta -o phage_genomes.fasta --report report.html`
**Explanation:** Generates HTML report.