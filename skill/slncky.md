---
name: slncky
category: qc
description: slncky is a tool for lncRNA discovery from RNA-Seq data. slncky filters a high-quality set of noncoding transcripts, discovers lncRNA orthologs, and characterizes conserved lncRNA evolution. slncky was developed as a collaboration between the Garber Lab at UMass Medical and the Regev Lab at the Broad Institute.
tags: [slncky, qc]
author: oxo-call-community
source_url: "https://github.com/slncky/slncky"
---

## Concepts

- **Tool Overview**: slncky (v1.0.4) - slncky is a tool for lncRNA discovery from RNA-Seq data. slncky filters a high-quality set of noncoding transcripts, discovers lncRNA orthologs, and characterizes conserved lncRNA evolution. slncky was developed as a collaboration between the Garber Lab at UMass Medical and the Regev Lab at the Broad Institute.
- **Core Function**: slncky is a tool for lncRNA discovery from RNA-Seq data. slncky filters a high-quality set of noncoding transcripts, discovers lncRNA orthologs, and characterizes conserved lncRNA evolution. slncky was developed as a collaboration between the Garber Lab at UMass Medical and the Regev Lab at the Broad Institute.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda slncky`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `slncky -i <input.fastq> -o <output_dir>`
**Explanation:** Run slncky with typical input and output options.
