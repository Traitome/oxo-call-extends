---
name: libshorah
category: variant-calling
description: libshorah - Short reads assembly into haplotypes
tags: [libshorah, variant-calling, haplotypes, short-reads, assembly]
author: oxo-call-community
source_url: "https://github.com/LaraFuhrmann/VILOCA"
---

## Concepts

- **Haplotype Assembly**: Assembles short reads into haplotypes
- **Variant Detection**: Identifies genetic variants from reads
- **Short-read Analysis**: Optimized for short-read sequencing data
- **Error Correction**: Error correction during assembly
- **Consensus Calling**: Generates consensus sequences
- **Population Analysis**: Population-level haplotype analysis

## Pitfalls

- **Read Quality**: Poor quality reads affect assembly
- **Coverage**: Low coverage affects haplotype reconstruction
- **Complex Regions**: Repeat regions may cause issues
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: Assembly may take significant time
- **Parameter Tuning**: Requires careful parameter optimization

## Examples

### Assemble haplotypes
**Args:** `shorah assemble -i reads.fastq -o haplotypes.fasta`
**Explanation:** Assembles short reads into haplotypes.

### Call variants
**Args:** `shorah call -i reads.fastq -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from assembled haplotypes.

### Error correction
**Args:** `shorah correct -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects sequencing errors.

### Consensus sequence
**Args:** `shorah consensus -i haplotypes.fasta -o consensus.fasta`
**Explanation:** Generates consensus sequence.

### Population analysis
**Args:** `shorah population -i samples.txt -o population.txt`
**Explanation:** Analyzes population haplotypes.

### Statistics
**Args:** `shorah stats -i haplotypes.fasta -o stats.txt`
**Explanation:** Shows haplotype statistics.