---
name: diphase
category: variant-calling
description: Diphase - Diploid genome phasing tool.
tags: [diphase, variant-calling, phasing, diploid, haplotype]
author: oxo-call-community
source_url: "https://github.com/zhangjuncsu/Diphase"
---

## Concepts

- **Tool Overview**: Diphase (v1.0.3+) is a tool for phasing diploid genome assemblies.
- **Core Function**: Separates haplotype phases in diploid genome assemblies using variant information.
- **Input/Output**: Input: Diploid assembly FASTA, variant calls (VCF). Output: Phased haplotype sequences.
- **Algorithm**: Uses variant information to phase diploid assemblies into separate haplotypes.
- **Key Features**: Diploid phasing, haplotype separation, variant-aware phasing, high accuracy, fast execution.
- **Installation**: `conda install -c bioconda diphase`

## Pitfalls

- **Input Requirements**: Requires diploid assembly and variant information.
- **Variant Quality**: Phasing accuracy depends on variant call quality.
- **Assembly Completeness**: Incomplete assemblies affect phasing results.
- **Memory Usage**: May require significant memory for large genomes.
- **Phasing Errors**: Switch errors may occur in repetitive regions.

## Examples

### Phase diploid assembly
**Args:** `diphase --assembly diploid.fa --variants variants.vcf --output phased/`
**Explanation:** Phases diploid genome assembly into haplotypes.

### With quality filtering
**Args:** `diphase --assembly diploid.fa --variants variants.vcf --output phased/ --min-q 30`
**Explanation:** Use minimum quality threshold for variants.

### Phase specific region
**Args:** `diphase --assembly diploid.fa --variants variants.vcf --output phased/ --region chr1:1-1000000`
**Explanation:** Phase only specific genomic region.

### Generate statistics
**Args:** `diphase --assembly diploid.fa --variants variants.vcf --output phased/ --stats stats.tsv`
**Explanation:** Generate phasing statistics and metrics.

### Compare with known phases
**Args:** `diphase --assembly diploid.fa --variants variants.vcf --output phased/ --truth truth.vcf`
**Explanation:** Compare phasing results with known truth.