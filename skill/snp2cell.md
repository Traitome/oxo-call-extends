---
name: snp2cell
category: analysis
description: SNP2Cell - Find enriched regulatory networks from GWAS and single-cell data
tags: [snp2cell, analysis, gwas, single-cell, regulatory-networks]
author: oxo-call-community
source_url: "https://github.com/Teichlab/snp2cell"
---

## Concepts

- **Tool Overview**: snp2cell (v0.3.0) - A tool for integrating GWAS with single-cell data
- **Core Function**: Identifies enriched regulatory networks from genetic associations
- **Input/Output**: Accepts GWAS SNPs and single-cell data; outputs enriched networks
- **Algorithm**: Integrates genetic variants with single-cell expression patterns
- **Installation**: `conda install -c bioconda snp2cell`
- **Key Features**: GWAS integration, single-cell analysis, network enrichment

## Pitfalls

- **Input Requirements**: Requires properly formatted GWAS and single-cell data
- **Data Integration**: Requires matching cell types and SNP annotations
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for large networks
- **Interpretation**: Results require biological interpretation
- **Multiple Testing**: Requires proper correction for multiple testing

## Examples

### Display help
**Args:** `snp2cell --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -o results/`
**Explanation:** Run SNP to cell type enrichment analysis.

### With network
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -n network.txt -o results/`
**Explanation:** Use regulatory network for analysis.

### With annotations
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -a annotations.gff -o results/`
**Explanation:** Use SNP annotations for analysis.

### Set threshold
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -o results/ --threshold 0.05`
**Explanation:** Set enrichment threshold.

### Generate report
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -o results/ --report`
**Explanation:** Generate analysis report.

### Export network
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -o results/ --export-network`
**Explanation:** Export enriched regulatory network.

### With visualization
**Args:** `snp2cell -g gwas_snps.txt -c cell_data.h5ad -o results/ --visualize`
**Explanation:** Generate visualizations of results.