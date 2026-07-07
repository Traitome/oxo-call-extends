---
name: scoary
category: population-genomics
description: Scoary - Microbial pan-GWAS using the output from Roary
tags: ["scoary", "population-genomics", "pan-genomics", "GWAS"]
author: oxo-call-community
source_url: "https://github.com/AdmiralenOla/Scoary"
---

## Concepts

- **Tool Overview**: Scoary (v1.6.16) is a tool for microbial pan-GWAS using the output from Roary.
- **Core Function**: Identifies genes associated with phenotypic traits in microbial populations.
- **Algorithm**: Uses statistical tests to identify gene-trait associations in pan-genome data.
- **Input/Output**: Accepts Roary output and phenotype data, produces association results.
- **Pan-Genomics**: Analyzes the entire gene repertoire of a microbial population.
- **Applications**: Microbial genomics, gene-trait association, and population genetics.

## Pitfalls

- **Data Quality**: Results depend on input data quality and annotation.
- **Statistical Significance**: Requires careful interpretation of statistical results.
- **Multiple Testing**: May require correction for multiple testing.
- **Computational Resources**: May require significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Roary Dependency**: Requires Roary output as input.

## Examples

### Basic pan-GWAS
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv -o results/`
**Explanation:** `-g` gene presence/absence; `-t` traits; `-o` output directory.

### With significance threshold
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv -p 0.05 -o results/`
**Explanation:** `-p 0.05` sets significance threshold.

### Multiple traits
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv --multi-trait -o results/`
**Explanation:** `--multi-trait` analyzes multiple traits simultaneously.

### Verbose logging
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv -v -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Filter genes
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv -m 10 -o results/`
**Explanation:** `-m 10` requires minimum 10 occurrences per gene.

### Output plots
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv --plot -o results/`
**Explanation:** `--plot` generates visualization plots.

### Custom annotation
**Args:** `scoary -g gene_presence_absence.csv -t traits.csv -a annotations.csv -o results/`
**Explanation:** `-a` provides gene annotations.