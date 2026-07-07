---
name: purge_haplotigs
category: hpc
description: purge_haplotigs curates heterozygous diploid genome assemblies by removing alternate haplotypes.
tags: [purge_haplotigs, hpc, genome-assembly, haplotype-curation]
author: oxo-call-community
source_url: "https://bitbucket.org/mroachawri/purge_haplotigs/"
---

## Concepts

- **Tool Overview**: purge_haplotigs curates genome assemblies.
- **Core Function**: Haplotype removal.
- **Algorithm**: Uses mapping-based approach.
- **Input Format**: Accepts assembly and BAM files.
- **Output**: Produces curated assembly.
- **Use Case**: Diploid genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Heterozygosity Level**: Affects accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `purge_haplotigs --help`
**Explanation:** Shows available options and usage instructions.

### Curate assembly
**Args:** `purge_haplotigs curate -i assembly.fasta -b alignments.bam -o curated.fasta`
**Explanation:** Curates heterozygous assembly.

### With parameters
**Args:** `purge_haplotigs curate -i assembly.fasta -b alignments.bam -p params.yaml -o curated.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `purge_haplotigs -v curate -i assembly.fasta -b alignments.bam -o curated.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `purge_haplotigs -t 4 curate -i assembly.fasta -b alignments.bam -o curated.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Assess coverage
**Args:** `purge_haplotigs assess -i assembly.fasta -b alignments.bam -o coverage_stats.txt`
**Explanation:** Assesses coverage statistics.

### Generate report
**Args:** `purge_haplotigs curate -i assembly.fasta -b alignments.bam -o curated.fasta --report report.html`
**Explanation:** Generates HTML report.