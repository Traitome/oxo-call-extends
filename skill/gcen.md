---
name: gcen
category: expression
description: An easy-to-use toolkit for Gene Co-Expression Network analysis and lncRNAs annotation
tags: [gcen, expression, co-expression, network, lncRNA, RNA-seq, WGCNA]
author: oxo-call-community
source_url: "https://www.biochen.org/gcen"
---

## Concepts

- **Tool Overview**: GCEN (Gene Co-Expression Network analysis) is a command-line toolkit for building gene co-expression networks and predicting gene function, particularly optimized for lncRNA annotation from RNA-Seq data. It implements a complete pipeline: data pretreatment, network construction, module identification, and function annotation.
- **Core Modules**: (1) data_norm - normalizes expression data using upper quartile, TPM, or DESeq2 methods. (2) data_filter - removes low-expression genes based on configurable thresholds. (3) network_build - constructs co-expression networks using Pearson or Spearman correlation. (4) module_identify - identifies modules (clusters) of co-expressed genes. (5) annotate - performs GO and KEGG enrichment for network/module annotation. (6) rwr - runs Random Walk with Restart for gene function prediction.
- **Input Format**: Tab-separated gene expression matrix with first column as gene IDs and subsequent columns as sample expression values. Accepts output from RSEM, StringTie, Salmon, FeatureCounts, and similar quantification tools.
- **Correlation Methods**: network_build supports Pearson correlation (fast, good for linear relationships) and Spearman correlation (slower, captures monotonic relationships, more robust to outliers). Choose Spearman for non-normally distributed data.
- **Multiple Testing Correction**: GCEN applies Bonferroni and FDR corrections for multiple testing when calculating correlation significance. The -p parameter sets the p-value threshold for significant correlations.
- **Random Walk with Restart (RWR)**: The rwr module implements Random Walk with Restart algorithm for gene function prediction. Given a set of "seed" genes with known functions, it identifies other genes likely to share those functions based on network topology.
- **Threading**: All modules support multi-threading via the -t parameter, significantly accelerating processing of large RNA-Seq datasets (10,000+ genes).
- **Installation**: Download precompiled binaries from biochen.org or install via Bioconda (`conda install -c bioconda gcen`). Add both bin/ and util/ directories to PATH.

## Pitfalls

- **Gene ID Mismatch**: Input expression matrices must have consistent gene ID formats across all samples. Mixing different ID types (Entrez, Ensembl, gene symbols) will cause incorrect network construction. Always verify ID consistency before analysis.
- **Low Expression Threshold**: Setting -p too high in data_filter may remove legitimate low-expression genes important for your biological question. For lncRNA analysis, be conservative as lncRNAs often have lower expression than protein-coding genes.
- **Sample Size Requirements**: Co-expression network analysis requires sufficient sample size (minimum 3-5 biological replicates recommended). With too few samples, correlation estimates are unreliable and networks may be artifacts.
- **Memory Usage**: network_build computes pairwise correlations across all genes, which scales O(n²) with gene number. For genomes with 20,000+ genes, ensure 8GB+ RAM available.
- **Software Dependencies**: GCEN itself does not require R or Python, but the annotation module requires GO (Gene Ontology) files in OBO format and KEGG pathway files. Download these separately from GO and KEGG databases.
- **Java Memory for RWR**: The rwr module requires Java Runtime Environment and may need increased heap size for large networks. Use `java -Xmx2g -jar rwr.jar` for networks with 10,000+ genes.

## Examples

### Basic expression data normalization
**Args:** `data_norm -i gene_expr.tsv -o gene_expr_norm.tsv -m upqt -t 8`
**Explanation:** Normalizes expression data using the upper quartile method, which scales each sample's gene expression by the 75th percentile. The -t 8 enables 8-threaded processing for faster execution on multi-core systems.

### Filter low-expression genes
**Args:** `data_filter -i gene_expr_norm.tsv -o gene_expr_filtered.tsv -p 0.75 -t 8`
**Explanation:** Removes genes where expression is below the 75th percentile in more than 25% of samples. This reduces noise from lowly-expressed genes that may represent background or sequencing artifacts, improving downstream network quality.

### Build co-expression network with Spearman correlation
**Args:** `network_build -i gene_expr_filtered.tsv -o coexpr.network -m spearman -p 0.001 -c 0.8 -f -t 8`
**Explanation:** Constructs a co-expression network using Spearman correlation (more robust for expression data), p-value threshold of 0.001 (highly significant correlations only), correlation coefficient threshold of 0.8 (strong correlations), and enables Fisher's z-transformation for correlation aggregation across samples. Output is an edge list with gene pairs and correlation statistics.

### Identify modules in the network
**Args:** `module_identify -i coexpr.network -o modules.txt -s 0.5 -t 8`
**Explanation:** Identifies modules (clusters) of tightly co-expressed genes using a similarity threshold of 0.5 (genes in the same module have pairwise similarity above this value). Higher thresholds produce more, smaller modules; lower thresholds produce fewer, larger modules.

### Annotate network with GO enrichment
**Args:** `annotate -g go-basic.obo -a gene_go.assoc -n coexpr.network -o network_go_annotation -t 8`
**Explanation:** Performs Gene Ontology enrichment analysis on the entire co-expression network. The -g file is the GO ontology in OBO format, -a is a tab-separated file mapping gene IDs to GO terms. Output includes enriched GO terms with p-values and the genes supporting each enrichment.

### Annotate specific module with KEGG pathways
**Args:** `annotate -k ko00001.tsv -a gene_kegg.assoc -m modules.txt -o module_kegg_annotation -t 8`
**Explanation:** Performs KEGG pathway enrichment for each module identified by module_identify. The -k file is the KEGG hierarchy (ko00001), -a maps genes to KEGG orthologs. This identifies which biological pathways are enriched in each co-expression module.

### Predict gene function using Random Walk with Restart
**Args:** `rwr -n coexpr.network -g interested_genes.list -o rwr_predictions.tsv`
**Explanation:** Uses Random Walk with Restart to predict functions for genes in interested_genes.list based on network topology. Genes are scored by their connectivity to known functional genes in the network. Output is a ranked list of genes most likely to share functions with the input seed genes.
