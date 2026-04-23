---
name: blobtk
category: qc
description: Core functionality shared across BlobToolKit tools
tags: [blobtk, blobtoolkit, qc, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/genomehubs/blobtk"
---

## Concepts

- **Tool Overview**: BlobTK provides core functionality for BlobToolKit genome assembly quality assessment.
- **Core Function**: Shared utilities for blobplot generation and assembly analysis.
- **Components**: Taxonomy parsing, coverage calculation, and data formatting.
- **Input**: Assembly FASTA, BAM files, BLAST results.
- **Output**: Processed data files for BlobToolKit visualization.
- **Installation**: Install via bioconda: `conda install -c bioconda blobtk`

## Pitfalls

- **Dependency**: Primarily used as library; command-line interface limited.
- **Taxonomy Database**: Requires NCBI taxonomy database for parsing.
- **File Formats**: Specific input format requirements for compatibility.
- **Memory Usage**: Large assemblies require significant memory.

## Examples

### Parse taxonomy file
**Args:** `blobtk parse-taxonomy -i taxonomy.tsv -o parsed.json`
**Explanation:** Parses taxonomy file for BlobToolKit compatibility.

### Calculate coverage statistics
**Args:** `blobtk coverage -b aligned.bam -o coverage.tsv`
**Explanation:** Calculates coverage statistics from BAM file.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
