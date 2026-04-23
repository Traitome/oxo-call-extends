---
name: assembly_uploader
category: expression
description: Python scripts to upload primary metagenome and metatranscriptome assemblies to ENA on a per-study basis. The scripts generate xmls to register a new study and create manifests necessary for submission with webin-cli.
tags: [assembly_uploader, expression]
author: oxo-call-community
source_url: "https://github.com/EBI-Metagenomics/assembly_uploader/blob/main/README.md"
---

## Concepts

- **Tool Overview**: assembly_uploader (v1.3.5) - Python scripts to upload primary metagenome and metatranscriptome assemblies to ENA on a per-study basis. The scripts generate xmls to register a new study and create manifests necessary for submission with webin-cli.
- **Core Function**: Python scripts to upload primary metagenome and metatranscriptome assemblies to ENA on a per-study basis. The scripts generate xmls to register a new study and create manifests necessary for submission with webin-cli.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda assembly_uploader`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
