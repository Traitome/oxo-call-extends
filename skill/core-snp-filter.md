---
name: core-snp-filter
category: alignment
description: Filtering sites in FASTA-format whole-genome pseudo-alignment
tags: [core-snp-filter, alignment, fasta, snp-filtering, genomics]
author: oxo-call-community
source_url: "https://github.com/rrwick/Core-SNP-filter"
---

## Concepts

- **Tool Overview**: Core-SNP-Filter is a tool for filtering sites (columns) in a FASTA-format whole-genome pseudo-alignment, specifically designed for SNP-based phylogenetic analysis.
- **Core Function**: Filters alignment columns based on quality metrics, missing data, and SNP characteristics.
- **Algorithm**: Examines each column in the alignment and applies filters based on user-defined criteria.
- **Input**: FASTA format whole-genome pseudo-alignment.
- **Output**: Filtered FASTA alignment with only high-quality SNP sites.
- **Application**: SNP calling, phylogenetic analysis, core genome alignment refinement.
- **Installation**: Install via bioconda: `conda install -c bioconda core-snp-filter`

## Pitfalls

- **Input Quality**: Requires high-quality input alignment for meaningful filtering.
- **Missing Data**: Excessive missing data can reduce alignment utility.
- **Filter Stringency**: Over-filtering may remove biologically relevant SNPs.
- **Alignment Format**: Only works with FASTA format pseudo-alignments.
- **Ambiguous Bases**: Ns and ambiguous bases can affect filtering decisions.

## Examples

### Basic filtering
**Args:** `core-snp-filter -i alignment.fasta -o filtered.fasta`
**Explanation:** Filters alignment using default parameters.

### With minimum coverage
**Args:** `core-snp-filter -i alignment.fasta -c 0.9 -o filtered.fasta`
**Explanation:** Requires 90% coverage at each site.

### Remove invariant sites
**Args:** `core-snp-filter -i alignment.fasta --remove-invariant -o filtered.fasta`
**Explanation:** Removes columns with no variation.

### Custom gap threshold
**Args:** `core-snp-filter -i alignment.fasta -g 0.1 -o filtered.fasta`
**Explanation:** Allows maximum 10% gaps per site.

### Display help
**Args:** `core-snp-filter --help`
**Explanation:** Shows all available options and usage information.