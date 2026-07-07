---
name: aardvark
category: variant-calling
description: Aardvark compares and merges variant call sets using haplotype-based comparison, supporting small variants, structural variants, and tandem repeats.
tags: [aardvark, variant-calling, benchmarking, vcf, pacbio, haplotype]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/aardvark"
---

## Concepts

- **Tool Overview**: Aardvark (v0.10.5) compares and merges variant call sets, building haplotype sequences for base-pair level comparison regardless of variant type representation.
- **Core Function**: Benchmarks query variants against truth sets and merges variants from multiple callers using haplotype-aware comparison.
- **Input/Output**: Input is VCF files (query and truth sets); output includes summary statistics, annotated VCFs, and merged variant sets.
- **Installation**: Install via bioconda: `conda install -c bioconda aardvark`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **Haplotype-Based Comparison**: Constructs haplotype sequences to compare variants at base-pair level, avoiding issues with different variant representations (e.g., MNV vs SNP+indel).
- **Two Main Modes**: `compare` (benchmarking query vs truth) and `merge` (combine multiple call sets).
- **Variant Types**: Supports SNVs, indels, structural variants (<=10 kbp), and tandem repeats.
- **Performance**: Runs approximately 16x faster than hap.py with similar accuracy.

## Pitfalls

- **VCF Normalization**: Input VCFs should be normalized (left-aligned, split) for best results. Different representations can cause comparison errors.
- **Reference Consistency**: All input VCFs must use the same reference genome.
- **Memory Usage**: Large genomes with many variants require substantial memory for haplotype construction.
- **Version Changes**: In v0.6.0, `--confidence-regions` was replaced with `--regions`.
- **Variant Trimming**: By default, REF/ALT sequences are trimmed at identical tails. Use `--disable-variant-trimming` to disable.

## Examples

### Display help information
**Args:** `aardvark --help`
**Explanation:** Shows all available subcommands, options, and usage information.

### Compare query variants against truth set
**Args:** `aardvark compare --query calls.vcf --truth truth.vcf --reference ref.fa --regions confident.bed -o results/`
**Explanation:** Compares query variant calls against a truth set within specified regions. Outputs summary statistics and annotated VCF with true/false positive/negative labels.

### Merge multiple variant call sets
**Args:** `aardvark merge --inputs caller1.vcf caller2.vcf caller3.vcf --reference ref.fa -o merged.vcf`
**Explanation:** Merges variants from three different callers using haplotype-aware comparison. Resolves different variant representations automatically.

### Compare with stratifications for detailed statistics
**Args:** `aardvark compare --query query.vcf --truth truth.vcf --reference ref.fa --regions regions.bed --stratifications strat.bed -o results/`
**Explanation:** Adds stratification annotations to the output summary, providing statistics for each stratified region.

### Disable variant trimming
**Args:** `aardvark compare --query query.vcf --truth truth.vcf --reference ref.fa --disable-variant-trimming -o results/`
**Explanation:** Disables the default REF/ALT tail trimming behavior. Useful when working with variant representations that shouldn't be normalized.

### Output annotated VCF with comparison results
**Args:** `aardvark compare --query query.vcf --truth truth.vcf --reference ref.fa --output-vcf annotated.vcf -o stats/`
**Explanation:** Produces an annotated VCF where each variant is labeled with its benchmark status (TP, FP, FN) for detailed analysis.

### Merge with output summary statistics
**Args:** `aardvark merge --inputs caller1.vcf caller2.vcf --reference ref.fa -o merged.vcf --output-summary merge_stats.tsv`
**Explanation:** Merges variant call sets and generates a summary TSV file with merge statistics.

### Compare with weighted haplotype scoring
**Args:** `aardvark compare --query query.vcf --truth truth.vcf --reference ref.fa --scoring-mode WEIGHTED_HAP -o results/`
**Explanation:** Uses weighted haplotype scoring where variants are weighted by their length. Longer variants have increased weight in the scoring.