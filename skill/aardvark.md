---
name: aardvark
category: variant-calling
description: A tool for sniffing out the differences in vari-Ants - benchmarks and merges variant call sets.
tags: [aardvark, variant-calling, benchmarking, vcf, pacbio]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/aardvark"
---

## Concepts

- **Tool Overview**: Aardvark compares and merges variant call sets, building haplotype sequences for base-pair level comparison regardless of variant type. Version 0.10.5.
- **Core Function**: Benchmarks query variants against truth sets and merges variants from multiple callers, handling different variant representations through haplotype context.
- **Input/Output**: Input is VCF files (query and truth sets); output includes summary statistics, annotated VCFs, and merged variant sets.
- **Installation**: Install via bioconda: `conda install -c bioconda aardvark`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **Haplotype-Based Comparison**: Constructs haplotype sequences to compare variants at base-pair level, avoiding issues with different variant representations (e.g., MNV vs SNP+indel).
- **Two Main Modes**: Benchmarking (query vs truth) and merging (combine multiple call sets with various strategies).
- **Genotype Assessment**: Supports strict exact match scoring for genotype evaluation.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Confidence Regions**: Requires BED file of confidence regions for accurate benchmarking. Results depend heavily on these regions.
- **VCF Normalization**: Input VCFs should be normalized (left-aligned, split) for best results. Different representations can cause comparison errors.
- **Memory Usage**: Large genomes with many variants require substantial memory for haplotype construction.
- **Reference Consistency**: All input VCFs must use the same reference genome.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available subcommands, options, and usage information.

### Benchmark variants against truth set
**Args:** `benchmark --query calls.vcf --truth truth.vcf --reference ref.fa --confidence-regions confident.bed -o results/`
**Explanation:** Compares query variant calls against a truth set within specified confidence regions. Outputs summary statistics and annotated VCF with true/false positive/negative labels.

### Merge multiple variant call sets
**Args:** `merge --inputs caller1.vcf caller2.vcf caller3.vcf --reference ref.fa -o merged.vcf`
**Explanation:** Merges variants from three different callers using haplotype-aware comparison. Resolves different variant representations automatically.

### Benchmark with specific merge strategy
**Args:** `benchmark --query calls.vcf --truth truth.vcf --reference ref.fa --strategy majority -o results/`
**Explanation:** Uses majority voting strategy for merging conflicting variant representations. Alternative strategies include strict exact match.

### Output annotated VCF with comparison results
**Args:** `benchmark --query query.vcf --truth truth.vcf --reference ref.fa --output-vcf annotated.vcf -o stats/`
**Explanation:** Produces an annotated VCF where each variant is labeled with its benchmark status (TP, FP, FN) for detailed analysis.
