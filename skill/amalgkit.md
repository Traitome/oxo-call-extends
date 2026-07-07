---
name: amalgkit
category: expression
description: Toolkit for integrating RNA-seq data from NCBI SRA and private FASTQ files for large-scale evolutionary transcriptomics
tags: [amalgkit, RNA-seq, transcriptomics, expression, SRA, cross-species]
author: oxo-call-community
source_url: "https://github.com/kfuku52/amalgkit"
---

## Concepts

- **Tool Overview**: AMALGKIT is a toolkit to integrate RNA-seq data from the NCBI SRA database and private FASTQ files to generate unbiased cross-species transcript abundance datasets for large-scale evolutionary gene expression analysis.
- **Core Function**: Provides a complete workflow from metadata retrieval to cross-species normalization, including metadata curation, FASTQ generation, quantification, merging, and quality control.
- **Input/Output**: Inputs: SRA accessions, metadata tables, local FASTQ files; Outputs: curated metadata, transcript abundance tables, normalized expression matrices, quality control reports.
- **Installation**: Available via Bioconda (`conda install -c bioconda amalgkit`) or GitHub (`pip install git+https://github.com/kfuku52/amalgkit`).
- **Modules**: metadata (SRA metadata retrieval), config (configuration file generation), select (SRA entry selection), integrate (local FASTQ integration), getfastq (FASTQ generation), quant (transcript quantification), merge (abundance table generation), cstmm (cross-species TMM normalization), curate (outlier removal), csca (correlation analysis), sanity (integrity checking).

## Pitfalls

- **SRA Access**: Requires NCBI SRA Toolkit for downloading data; ensure proper installation and configuration.
- **Metadata Quality**: Poorly curated metadata can affect downstream analysis; use `amalgkit sanity` to check integrity.
- **Resource Requirements**: Large-scale analyses require significant storage and computational resources; consider parallel processing options.
- **Reference Genome**: Ensure consistent reference genome/transcriptome across all samples in cross-species analysis.
- **Normalization**: Cross-species normalization using `cstmm` requires single-copy genes; ensure proper gene set selection.

## Examples

### Retrieve SRA metadata
**Args:** `amalgkit metadata --query "Homo sapiens[Organism] AND RNA-seq[Strategy]" --output metadata.tsv`
**Explanation:** Retrieves metadata for human RNA-seq experiments from NCBI SRA and saves to a TSV file.

### Generate configuration files
**Args:** `amalgkit config --metadata metadata.tsv --output-dir configs/`
**Explanation:** Creates configuration files for downstream analysis based on the provided metadata table.

### Select SRA entries for analysis
**Args:** `amalgkit select --metadata metadata.tsv --config configs/sample_config.json --output selected.tsv`
**Explanation:** Filters and selects specific SRA entries based on criteria defined in the configuration file.

### Download FASTQ files from SRA
**Args:** `amalgkit getfastq --metadata selected.tsv --output-dir fastq/ --threads 8`
**Explanation:** Downloads and converts SRA files to FASTQ format using 8 threads for parallel processing.

### Quantify transcript abundance
**Args:** `amalgkit quant --metadata selected.tsv --fastq-dir fastq/ --transcriptome ref_transcripts.fasta --output quant/`
**Explanation:** Performs transcript-level quantification using Salmon or Kallisto and generates abundance estimates.

### Merge abundance tables
**Args:** `amalgkit merge --quant-dir quant/ --metadata selected.tsv --output merged_abundance.tsv`
**Explanation:** Combines individual quantification results into a single transcript abundance matrix.

### Cross-species TMM normalization
**Args:** `amalgkit cstmm --abundance merged_abundance.tsv --single-copy-genes single_copy_genes.txt --output normalized.tsv`
**Explanation:** Applies cross-species TMM normalization using single-copy orthologs for unbiased comparison.

### Curate and remove outliers
**Args:** `amalgkit curate --abundance normalized.tsv --metadata selected.tsv --output curated.tsv`
**Explanation:** Automatically detects and removes outlier samples and unwanted batch effects from the dataset.