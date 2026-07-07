---
name: haslr
category: bioinformatics
description: HASLR is a fast tool for hybrid genome assembly combining long and short reads.
tags: [haslr, genome-assembly, hybrid-assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/haslr"
---

## Concepts

- **Hybrid Assembly**: HASLR combines long and short reads for assembly.

- **Long Read Data**: Uses long read sequencing data.

- **Short Read Data**: Uses short read sequencing data.

- **Fast Assembly**: Optimized for speed and efficiency.

- **Genome Assembly**: Assembles complete genomes.

- **Error Correction**: Corrects sequencing errors.

## Pitfalls

- **Read Quality**: Low-quality reads may affect assembly.

- **Coverage Depth**: Requires sufficient sequencing coverage.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large genomes may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Assemble genome
**Args:** `haslr --short short_reads.fastq --long long_reads.fastq --output assembly.fasta`
**Explanation:** Assembles genome using hybrid approach.

### With reference
**Args:** `haslr --short short_reads.fastq --long long_reads.fastq --reference reference.fasta --output assembly.fasta`
**Explanation:** Uses reference-guided assembly.

### Batch processing
**Args:** `for f in *.fastq; do haslr --short $f --long long_reads.fastq --output ${f%.fastq}_assembly.fasta; done`
**Explanation:** Processes multiple short read files.

### Generate statistics
**Args:** `haslr --short short_reads.fastq --long long_reads.fastq --stats --output stats.txt`
**Explanation:** Generates assembly statistics.

### Quality filtering
**Args:** `haslr --short short_reads.fastq --long long_reads.fastq --min-quality 20 --output assembly.fasta`
**Explanation:** Filters reads by quality score.

### Help command
**Args:** `haslr --help`
**Explanation:** Shows available options and usage information.