---
name: dipcall
category: variant-calling
description: dipcall - Reference-based variant calling for phased haplotype assemblies.
tags: [dipcall, variant-calling, haplotype, phased, assembly]
author: oxo-call-community
source_url: "https://github.com/lh3/dipcall"
---

## Concepts

- **Tool Overview**: dipcall (v0.3+) is a variant calling pipeline for diploid genomes from phased haplotype assemblies.
- **Core Function**: Calls small variants and long indels from phased assembly alignments against a reference genome.
- **Input/Output**: Input: Phased haplotype FASTA files, reference genome. Output: VCF with variant calls, statistics.
- **Algorithm**: Aligns phased haplotypes to reference and calls variants using mapping information.
- **Key Features**: Phased variant calling, long indel detection, high accuracy, fast execution, VCF output.
- **Installation**: `conda install -c bioconda dipcall`

## Pitfalls

- **Input Requirements**: Requires phased haplotype assemblies (not raw reads).
- **Reference Genome**: Must use same reference genome used for assembly.
- **Phasing Quality**: Variant calling quality depends on input haplotype phasing accuracy.
- **Assembly Quality**: Poor assembly quality affects variant calling.
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Call variants from phased assemblies
**Args:** `-g ref.fa -o output/ hap1.fa hap2.fa`
**Explanation:** Calls variants from phased haplotype assemblies against reference.

### With pre-aligned BAM
**Args:** `-g ref.fa -o output/ --bam aligned.bam hap1.fa hap2.fa`
**Explanation:** Use pre-aligned BAM file for variant calling.

### Generate statistics
**Args:** `-g ref.fa -o output/ --stats stats.tsv hap1.fa hap2.fa`
**Explanation:** Generate variant calling statistics.

### Filter by quality
**Args:** `-g ref.fa -o output/ --min-q 30 hap1.fa hap2.fa`
**Explanation:** Filter variants by minimum quality score.

### Large genome mode
**Args:** `-g ref.fa -o output/ --large hap1.fa hap2.fa`
**Explanation:** Use large genome mode for improved memory efficiency.