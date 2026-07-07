---
name: gfold
category: differential-expression
description: gfold - Find differentially expressed genes from RNA-seq data using generalized fold changes.
tags: [gfold, differential-expression, RNA-seq, bioinformatics]
author: oxo-call-community
source_url: "http://compbio.tongji.edu.cn/~fengjx/GFOLD/gfold.html"
---

## Concepts
- **Differential Expression**: Identifies differentially expressed genes.
- **Generalized Fold Change**: Uses generalized fold change metric.
- **RNA-seq Analysis**: Analyzes RNA-seq data.
- **Statistical Significance**: Computes statistical significance.
- **Few Replicates**: Works with few biological replicates.

## Pitfalls
- **Replicate Number**: Designed for few replicates.
- **Read Count**: Requires accurate read counts.
- **Normalization**: Requires proper normalization.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Validation**: Results should be validated.

## Examples
### Run differential expression
**Args:** `gfold diff -s1 treatment.txt -s2 control.txt -o results.txt`
**Explanation:** Finds differentially expressed genes.

### With options
**Args:** `gfold diff -s1 treatment.txt -s2 control.txt -s 0.05 -o results.txt`
**Explanation:** Uses significance threshold of 0.05.

### Generate ranking
**Args:** `gfold rank -s treatment.txt -o ranking.txt`
**Explanation:** Ranks genes by expression.

### Batch processing
**Args:** `gfold diff -l samples.txt -o ./results/`
**Explanation:** Processes multiple sample pairs.

### Generate report
**Args:** `gfold diff -s1 treatment.txt -s2 control.txt -r -o report.html`
**Explanation:** Generates analysis report.