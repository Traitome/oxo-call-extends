---
name: deconveil
category: utility
description: DeConveil - extension of PyDESeq2/DESeq2 designed to account for genome aneuploidy.
tags: [deconveil, utility, DESeq2, differential-expression, aneuploidy]
author: oxo-call-community
source_url: "https://github.com/caravagnalab/DeConveil"
---

## Concepts

- **Tool Overview**: deconveil (v0.2.0+) is an extension of PyDESeq2/DESeq2 that accounts for genome aneuploidy in differential expression analysis. It adjusts expression counts to account for copy number variations that affect gene expression measurements.
- **Core Function**: Performs differential expression analysis while accounting for genome aneuploidy, improving accuracy in cancer and other aneuploid samples.
- **Input/Output**: Input: Gene expression matrix, copy number data, sample annotations. Output: Differential expression results, adjusted counts, visualization plots.
- **Algorithm**: Extends DESeq2's negative binomial model by incorporating copy number information to adjust expression levels before differential analysis.
- **Key Features**: Aneuploidy-aware, extends DESeq2/PyDESeq2, improved accuracy for cancer data, integrates copy number data, visualization support.
- **Installation**: `conda install -c bioconda deconveil`

## Pitfalls

- **Copy Number Quality**: Requires accurate copy number profiles.
- **Ploidy Estimation**: Incorrect ploidy estimates affect results.
- **Baseline Selection**: Requires appropriate baseline for comparison.
- **Normalization**: Standard normalization may not be appropriate.
- **Data Requirements**: Requires matched copy number and expression data.

## Examples

### Run DeConveil analysis
**Args:** `deconveil -i counts.csv -c copy_number.csv -o results/`
**Explanation:** Perform differential expression analysis accounting for aneuploidy.

### With sample annotations
**Args:** `deconveil -i counts.csv -c copy_number.csv -a annotations.csv -o results/`
**Explanation:** Include sample annotations for group comparisons.

### Generate visualization
**Args:** `deconveil -i counts.csv -c copy_number.csv -o results/ --plot`
**Explanation:** Generate diagnostic plots for the analysis.