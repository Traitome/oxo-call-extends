---
name: akgwas
category: assembly
description: AKmerGWAS - k-mer based genome-wide association studies pipeline supporting multiple input formats
tags: [akgwas, gwas, k-mer, snakemake, association, genomics]
author: oxo-call-community
source_url: "https://github.com/suzkami/Aseembly_GWAS"
---

## Concepts

- **Tool Overview**: AKmerGWAS is a Snakemake-based pipeline for k-mer based genome-wide association studies (GWAS) that accepts multiple input formats including short reads, assemblies, and genomes.
- **Core Function**: Performs k-mer based association analysis by constructing k-mer matrices, running GWAS with GEMMA, and aligning significant k-mers to reference genomes.
- **Input Formats**: Supports short reads (FASTQ), assembled genomes (FASTA), and complete genome assemblies as input.
- **Workflow Modules**: Includes k-mer matrix construction, GWAS analysis using GEMMA, k-mer alignment to reference genome, and post-GWAS analysis.
- **Dependencies**: Relies on snakemake, kmtricks, bwa, samtools, gemma, plink, parallel, and rush.
- **Installation**: Install via bioconda: `conda install -c bioconda akgwas`
- **Output**: Association results, significant k-mers, aligned k-mer locations, and summary statistics.

## Pitfalls

- **Computational Resources**: k-mer counting and GWAS analysis can be memory and computationally intensive for large datasets.
- **K-mer Size**: Appropriate k-mer size must be chosen - too small may lack specificity, too large may reduce sensitivity.
- **Reference Genome**: High-quality reference genome required for k-mer alignment and annotation.
- **Sample Size**: Sufficient sample size needed for statistical power in GWAS analysis.
- **Multiple Testing**: Proper multiple testing correction required due to large number of k-mers tested.

## Examples

### Display help information
**Args:** `akgwas --help`
**Explanation:** Shows available commands and options for the AKmerGWAS pipeline.

### Run with short read input
**Args:** `akgwas --input-type reads --reads-dir reads/ --phenotype phenotypes.tsv --output results/`
**Explanation:** Runs k-mer GWAS using short read sequencing data as input.

### Run with assembled genomes
**Args:** `akgwas --input-type assembly --assemblies-dir assemblies/ --phenotype phenotypes.tsv --output results/`
**Explanation:** Runs k-mer GWAS using assembled genome sequences as input.

### Run with complete genomes
**Args:** `akgwas --input-type genome --genomes-dir genomes/ --phenotype phenotypes.tsv --output results/`
**Explanation:** Runs k-mer GWAS using complete genome sequences as input.

### Specify k-mer size
**Args:** `akgwas --input-type reads --reads-dir reads/ --phenotype phenotypes.tsv --kmer-size 31 --output results/`
**Explanation:** Uses k-mer size of 31 for the analysis instead of default.

### Set minimum k-mer count threshold
**Args:** `akgwas --input-type reads --reads-dir reads/ --phenotype phenotypes.tsv --min-count 5 --output results/`
**Explanation:** Filters out k-mers with count less than 5 across all samples.

### Specify reference genome for alignment
**Args:** `akgwas --input-type assembly --assemblies-dir assemblies/ --phenotype phenotypes.tsv --reference ref.fa --output results/`
**Explanation:** Aligns significant k-mers to specified reference genome for annotation.

### Custom configuration file
**Args:** `akgwas --config config.yaml`
**Explanation:** Runs pipeline using custom configuration file with all parameters specified.

### Run with specific Snakemake options
**Args:** `akgwas --input-type reads --reads-dir reads/ --phenotype phenotypes.tsv --snakemake-args "--cores 32 --use-conda" --output results/`
**Explanation:** Runs pipeline with custom Snakemake options for parallel execution.

### Enable post-GWAS analysis
**Args:** `akgwas --input-type reads --reads-dir reads/ --phenotype phenotypes.tsv --post-gwas --output results/`
**Explanation:** Enables post-GWAS analysis to identify genomic locations and context of trait-associated k-mers.

### Generate summary statistics
**Args:** `akgwas --input-type reads --reads-dir reads/ --phenotype phenotypes.tsv --summary-stats --output results/`
**Explanation:** Generates comprehensive summary statistics for the GWAS analysis.
