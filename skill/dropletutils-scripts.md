---
name: dropletutils-scripts
category: programming
description: "CLI scripts for the DropletUtils package"
tags: [dropletutils-scripts, programming]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/dropletutils-scripts"
---

## Concepts
- **Tool Overview**: A set of wrappers for operations associated with Aaron Lun's DropletUtils  package. Functions in R packages are hard to call when building workflows outside of R, so this package adds a set of simple wrappers with robust argument parsing. Intermediate steps are currently mainly serialized R objects, but the ultimate objective is to have language-agnostic intermediate formats allowing composite workflows using a variety of software packages.
- **Core Function**: CLI scripts for the DropletUtils package
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda dropletutils-scripts`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
