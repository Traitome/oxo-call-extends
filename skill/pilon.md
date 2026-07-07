---
name: pilon
category: assembly
description: pilon improves genome assemblies and detects variants.
tags: [pilon, assembly, variant-detection, genome]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/pilon/"
---

## Concepts

- **Tool Overview**: pilon improves genome assemblies.
- **Core Function**: Assembly polishing and variant detection.
- **Algorithm**: Uses alignment-based methods.
- **Input Format**: Accepts genome and alignment files.
- **Output**: Produces improved assembly results.
- **Use Case**: Genome assembly, variant calling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Assembly Errors**: May introduce errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pilon --help`
**Explanation:** Shows available options and usage instructions.

### Improve assembly
**Args:** `pilon -i genome.fasta -b alignment.bam -o polished_genome.fasta`
**Explanation:** Improves genome assembly.

### With parameters
**Args:** `pilon -i genome.fasta -b alignment.bam -p params.yaml -o polished_genome.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pilon -v -i genome.fasta -b alignment.bam -o polished_genome.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pilon -t 4 -i genome.fasta -b alignment.bam -o polished_genome.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pilon -i genome.fasta -b alignment.bam -o polished_genome.vcf --vcf`
**Explanation:** Outputs variants in VCF format.

### Generate report
**Args:** `pilon -i genome.fasta -b alignment.bam -o polished_genome.fasta --report report.html`
**Explanation:** Generates HTML report.