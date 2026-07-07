---
name: decifer
category: expression
description: DeCiFer - simultaneous mutation multiplicity selection and SNV clustering by descendant cell fractions.
tags: [decifer, expression, cancer-evolution, SNV-clustering, subclonal-structure]
author: oxo-call-community
source_url: "https://github.com/raphael-group/decifer"
---

## Concepts

- **Tool Overview**: decifer (v2.1.4+) is an algorithm for analyzing cancer evolution that simultaneously selects mutation multiplicities and clusters SNVs by their corresponding descendant cell fractions (DCF). It infers subclonal structures from multi-sample sequencing data.
- **Core Function**: Analyzes somatic mutations across multiple cancer samples to infer subclonal populations, mutation multiplicities, and evolutionary relationships.
- **Input/Output**: Input: VCF files with somatic mutations, read counts. Output: Clustered mutations, DCF values, subclonal structure.
- **Algorithm**: Uses statistical modeling to simultaneously infer mutation multiplicities and cluster mutations by their DCF, accounting for copy number variations and tumor purity.
- **Key Features**: Multi-sample analysis, accounts for copy number variation, handles tumor purity, provides confidence estimates, visualization support.
- **Installation**: `conda install -c bioconda decifer`

## Pitfalls

- **Sample Quality**: Requires high-quality sequencing data with sufficient depth.
- **Copy Number**: Accurate copy number profiles are essential.
- **Purity Estimation**: Tumor purity estimates affect results.
- **Computational Time**: Complex analyses may be computationally intensive.
- **Parameter Tuning**: Requires careful parameter selection for optimal results.

## Examples

### Run DeCiFer analysis
**Args:** `decifer -i mutations.vcf -o results/`
**Explanation:** Analyze somatic mutations to infer subclonal structure.

### With copy number data
**Args:** `decifer -i mutations.vcf -c copy_number.txt -o results/`
**Explanation:** Include copy number information for improved clustering.

### Specify purity
**Args:** `decifer -i mutations.vcf --purity 0.8 -o results/`
**Explanation:** Specify tumor purity for analysis.