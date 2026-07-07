---
name: gneiss
category: metagenomics
description: QIIME 2 plugin for differential abundance analysis using compositional data analysis with balances and hierarchical clustering.
tags: [gneiss, metagenomics, differential-abundance, qiime2, compositional-data, balances]
author: oxo-call-community
source_url: "https://qiime2.org"
---

## Concepts

- **Compositional Data Analysis**: gneiss addresses the compositional nature of microbiome data where relative abundances sum to 1. Standard differential abundance methods can fail because changes in one taxon affect the apparent abundances of others. gneiss uses balances (log-ratios between groups of taxa) to handle this properly.

- **Balance Calculation**: Balances are calculated using the formula b_i = sqrt(rs/(r+s)) * log(g(x_r)/g(x_s)), where g(x) is the geometric mean, x_r and x_s are the numerator and denominator taxa sets, and r and s are the number of taxa in each set.

- **Correlation Clustering**: When no prior knowledge exists about how taxa should be grouped, gneiss uses correlation clustering to group taxa based on their co-occurrence patterns across samples. Taxa that frequently appear together in the same samples are grouped.

- **Gradient Clustering**: When a numeric metadata gradient exists (e.g., pH, temperature, time), gradient clustering groups taxa based on their abundance patterns across that gradient. This reveals how taxa respond to environmental gradients.

- **Statistical Analysis**: After computing balances, standard statistical methods (ANOVA, linear regression) can be applied to identify differentially abundant taxa. The hierarchical tree structure controls for variation by restricting comparisons within balances.

## Pitfalls

- **Numeric Gradient Requirement**: The gradient-clustering command requires a numeric metadata column. Categorical variables will cause errors. For categorical gradients, convert to numeric values (e.g., Low=1, Medium=2, High=3) or use correlation-clustering instead.

- **Missing Values**: Metadata columns used for gradient clustering cannot contain missing (NA) values. Ensure complete metadata before running gradient-clustering.

- **Sample Size Requirements**: Balance-based methods work best with adequate sample sizes. Very small sample sizes may lead to unreliable balance estimates and inflated false positive rates.

- **Taxonomic Hierarchy Alignment**: The input phylogenetic tree must have tips that match the feature IDs in your feature table. Mismatches will cause errors or missing results.

- **Compositional Assumption**: gneiss methods assume compositional data (proportions summing to 1). Raw count data should be converted to relative abundances or compositions before analysis using QIIME 2's appropriate methods.

## Examples

### Create hierarchy using correlation clustering
**Args:** `qiime gneiss correlation-clustering --i-table feature-table.qza --o-clustering hierarchy.qza`
**Explanation:** This basic command creates a hierarchical clustering of taxa based on their co-occurrence patterns across all samples. The resulting hierarchy.qza file defines how taxa will be grouped into balances for downstream analysis.

### Gradient clustering with a numeric metadata column
**Args:** `qiime gneiss gradient-clustering --i-table feature-table.qza --m-gradient-file metadata.tsv --m-gradient-column pH --o-clustering gradient-hierarchy.qza`
**Explanation:** When you have a numeric gradient (like pH), gradient clustering groups taxa that respond similarly to that gradient. This example creates a hierarchy based on how taxa vary across the pH gradient in your samples.

### Calculate balances from hierarchy
**Args:** `qiime gneiss ilr-hierarchical --i-table feature-table.qza --i-hierarchy hierarchy.qza --o-balances balances.qza`
**Explanation:** The ilr-hierarchical command computes isometric log-ratio (ILR) balances from the feature table and hierarchy. These balances transform the compositional data into values that can be used with standard statistical tests.

### Visualize balances with heatmap
**Args:** `qiime gneiss dendrogram-heatmap --i-table feature-table.qza --i-hierarchy hierarchy.qza --m-metadata-file metadata.tsv --o-visualization heatmap.qzv`
**Explanation:** The dendrogram-heatmap visualization shows how balances vary across samples with a dendrogram showing the taxonomic hierarchy and a heatmap showing abundance patterns. This helps identify which balances differ between sample groups.

### Perform differential abundance testing with ANOVA
**Args:** `qiime gneiss ols-regression --p-formula "treatment" --i-balances balances.qza --m-metadata-file metadata.tsv --o-visualization regression.qzv`
**Explanation:** After computing balances, use ols-regression (ordinary least squares) to test for associations between balances and metadata variables. This example tests whether balances differ between treatment groups.

### Run regression with multiple covariates
**Args:** `qiime gneiss ols-regression --p-formula "treatment + age + BMI" --i-balances balances.qza --m-metadata-file metadata.tsv --o-visualization multivariable.qzv`
**Explanation:** The regression framework supports multiple covariates to control for confounders. This example tests the treatment effect while adjusting for age and BMI, providing more robust differential abundance estimates.
