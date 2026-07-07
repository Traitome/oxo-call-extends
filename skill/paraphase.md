---
name: paraphase
category: qc
description: ParaHapCaller is a HiFi-based caller for highly homologous genes.
tags: [paraphase, qc, hifi, haplotype]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/paraphase"
---

## Concepts

- **Tool Overview**: ParaHapCaller calls variants in highly homologous gene families.
- **Core Function**: Identifies haplotypes in duplicated genes.
- **Algorithm**: Uses HiFi sequencing data for accurate variant calling.
- **Input Format**: Accepts BAM files and gene annotations.
- **Output**: Produces haplotype-resolved variant calls.
- **Use Case**: Haplotype analysis, gene family variation, phasing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Homology Complexity**: Complex gene families may affect accuracy.
- **Read Quality**: Results depend on HiFi read quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paraphase --help`
**Explanation:** Shows available options and usage instructions.

### Call haplotypes
**Args:** `paraphase -i reads.bam -g genome.fasta -a genes.gff -o haplotypes.vcf`
**Explanation:** Calls haplotypes for homologous genes.

### With reference haplotypes
**Args:** `paraphase -i reads.bam -r reference_haplotypes.fasta -o haplotypes.vcf`
**Explanation:** Uses reference haplotypes.

### Verbose mode
**Args:** `paraphase -v -i reads.bam -g genome.fasta -o haplotypes.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `paraphase -t 8 -i reads.bam -g genome.fasta -o haplotypes.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `paraphase -c 10 -i reads.bam -g genome.fasta -o haplotypes.vcf`
**Explanation:** Sets minimum coverage threshold.

### Output format
**Args:** `paraphase -i reads.bam -g genome.fasta -o haplotypes.json --json`
**Explanation:** Outputs in JSON format.