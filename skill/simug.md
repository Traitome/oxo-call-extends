---
name: simug
category: variant-analysis
description: simuG - Simulate genome sequences with variants
tags: ["simug", "variant-analysis", "simulation", "genomics"]
author: oxo-call-community
source_url: "https://github.com/yjx1217/simuG"
---

## Concepts

- **Tool Overview**: simuG (v1.0.1) simulates genome sequences with variants.
- **Core Function**: Generates synthetic genomes with pre-defined or random variants.
- **Algorithm**: Uses reference-based simulation with variant injection.
- **Input/Output**: Accepts reference genome and produces simulated genomes.
- **Variant Simulation**: Specialized for variant simulation in genomes.
- **Applications**: Variant calling benchmarking, algorithm testing.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for realistic simulation.
- **Input Quality**: Results depend on reference genome quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Simulate genome
**Args:** `simug -r reference.fasta -o simulated_genome.fasta`
**Explanation:** `-r` reference genome; `-o` output genome.

### With VCF variants
**Args:** `simug -r reference.fasta -v variants.vcf -o simulated_genome.fasta`
**Explanation:** `-v` input VCF with variants.

### With random variants
**Args:** `simug -r reference.fasta -n 1000 -o simulated_genome.fasta`
**Explanation:** `-n 1000` generate 1000 random variants.

### Help command
**Args:** `simug --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simug --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simug -v -r reference.fasta -o simulated_genome.fasta`
**Explanation:** `-v` verbose output.

### With mutation rate
**Args:** `simug -r reference.fasta -m 0.001 -o simulated_genome.fasta`
**Explanation:** `-m 0.001` mutation rate.
