---
name: isoformcheck
category: comparative
description: Protein sequence comparison between de novo genome assemblies, identifying consistent and divergent isoforms.
tags: [isoformcheck, comparative genomics, protein isoforms, genome assembly]
author: oxo-call-community
source_url: "https://github.com/maickrau/IsoformCheck/blob/v1.0.0/README.md"
---

## Concepts

- **Isoform Comparison**: Compares protein sequences across multiple de novo genome assemblies to identify common and unique isoforms.
- **Assembly Validation**: Validates gene predictions by comparing them against known protein sequences or orthologous sequences from related species.
- **Alternative Splicing Analysis**: Identifies potential alternative splicing events by comparing transcript isoforms across assemblies.
- **Conservation Assessment**: Evaluates the conservation of protein sequences and domain architectures across different genome assemblies.
- **Quality Control**: Provides quality metrics for genome assemblies based on protein sequence consistency.
- **Ortholog Detection**: Identifies orthologous protein sequences across different species or strains.

## Pitfalls

- **Assembly Completeness**: Incomplete genome assemblies may lead to missing or truncated protein sequences.
- **Annotation Quality**: Poor gene prediction can introduce false positives or negatives in isoform comparison.
- **Sequence Divergence**: Highly divergent sequences may not be properly aligned or compared.
- **Transcriptome Data**: Lack of RNA-seq data may limit accurate isoform identification.
- **Computational Resources**: Comparing large numbers of assemblies can be computationally intensive.
- **Reference Bias**: Results may be biased towards the reference assembly used as the baseline.

## Examples

### Basic isoform comparison
**Args:** `isoformcheck --assemblies assembly1.fasta assembly2.fasta --output comparison.csv`
**Explanation:** Compares protein sequences between two genome assemblies.

### Multiple assembly comparison
**Args:** `isoformcheck --assemblies *.fasta --output multi_comparison.csv`
**Explanation:** Compares protein sequences across multiple genome assemblies.

### With reference database
**Args:** `isoformcheck --assemblies assemblies/ --reference ref_proteins.fasta --output results.csv`
**Explanation:** Compares assembly proteins against a reference protein database.

### Domain analysis
**Args:** `isoformcheck --assemblies assembly1.fasta assembly2.fasta --domain-analysis --output domains.csv`
**Explanation:** Performs protein domain architecture comparison between assemblies.

### Generate report
**Args:** `isoformcheck --assemblies assemblies/ --output results.csv --report report.pdf`
**Explanation:** Generates a comprehensive PDF report with comparison statistics.

### Filter by similarity
**Args:** `isoformcheck --assemblies a1.fasta a2.fasta --min-identity 90 --output filtered.csv`
**Explanation:** Filters results to only include proteins with at least 90% sequence identity.