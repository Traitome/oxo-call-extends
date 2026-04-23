---
name: clinker
category: expression
description: Clinker is a bioinformatics pipeline that generates a superTranscriptome from popular fusion finder outputs (JAFFA, tophatFusion, SOAP, deFUSE, Pizzly, etc), that can be then be either viewed in genome viewers such as IGV or through the included plotting feature developed with GViz.
tags: [clinker, expression]
author: oxo-call-community
source_url: "https://github.com/Oshlack/Clinker"
---

## Concepts

- **Tool Overview**: clinker (v1.33) - Clinker is a bioinformatics pipeline that generates a superTranscriptome from popular fusion finder outputs (JAFFA, tophatFusion, SOAP, deFUSE, Pizzly, etc), that can be then be either viewed in genome viewers such as IGV or through the included plotting feature developed with GViz.
- **Core Function**: Clinker is a bioinformatics pipeline that generates a superTranscriptome from popular fusion finder outputs (JAFFA, tophatFusion, SOAP, deFUSE, Pizzly, etc), that can be then be either viewed in genome viewers such as IGV or through the included plotting feature developed with GViz.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda clinker`

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
