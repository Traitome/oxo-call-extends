---
name: sniffles
category: variant-analysis
description: Sniffles - Structural variation caller for long-read sequencing (PacBio/Oxford Nanopore)
tags: [sniffles, variant-analysis, structural-variants, long-reads, pacbio, nanopore]
author: oxo-call-community
source_url: "https://github.com/fritzsedlazeck/Sniffles"
---

## Concepts

- **Tool Overview**: sniffles (v2.7.5) - A structural variant caller for long-read sequencing
- **Core Function**: Detects structural variants from PacBio or Oxford Nanopore data
- **Input/Output**: Accepts aligned BAM files; outputs VCF with SV calls
- **Algorithm**: Analyzes read alignments to identify insertions, deletions, inversions, duplications
- **Installation**: `conda install -c bioconda sniffles`
- **Key Features**: Long-read SV calling, multiple SV types, high accuracy

## Pitfalls

- **Input Requirements**: Requires properly aligned long-read BAM files
- **Read Depth**: Requires sufficient read depth for reliable SV calling
- **Reference Genome**: Must use compatible reference genome
- **Minimum Support**: Minimum read support threshold affects sensitivity
- **Memory Usage**: Large BAM files require significant memory
- **SV Types**: Different SV types have different detection accuracy

## Examples

### Display help
**Args:** `sniffles --help`
**Explanation:** Shows available options and usage information.

### Basic SV calling
**Args:** `sniffles -i aligned.bam -o sv_calls.vcf`
**Explanation:** Call structural variants from aligned BAM.

### With reference genome
**Args:** `sniffles -i aligned.bam -r reference.fasta -o sv_calls.vcf`
**Explanation:** Use reference genome for SV calling.

### Set minimum support
**Args:** `sniffles -i aligned.bam -o sv_calls.vcf --min_support 5`
**Explanation:** Set minimum reads supporting each SV.

### Filter by length
**Args:** `sniffles -i aligned.bam -o sv_calls.vcf --min_length 50`
**Explanation:** Filter SVs by minimum length.

### Generate summary
**Args:** `sniffles -i aligned.bam -o sv_calls.vcf --summary`
**Explanation:** Generate summary statistics.

### Multi-sample calling
**Args:** `sniffles -i sample1.bam sample2.bam -o combined_svs.vcf --combine`
**Explanation:** Call SVs from multiple samples.

### With genotyping
**Args:** `sniffles -i aligned.bam -o sv_calls.vcf --genotype`
**Explanation:** Perform genotyping on SV calls.