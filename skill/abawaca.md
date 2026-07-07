---
name: abawaca
category: metagenomics
description: abawaca (A Binning Algorithm Without A Cool Acronym) is a binning program for metagenomics that utilizes differential coverage and DNA signature information.
tags: [abawaca, metagenomics, binning, contigs, clustering]
author: oxo-call-community
source_url: "https://github.com/CK7/abawaca"
---

## Concepts

- **Tool Overview**: abawaca (A Binning Algorithm Without A Cool Acronym) is a metagenomic binning program. Version 1.00.
- **Core Function**: Bins metagenomic contigs into putative genome bins using differential coverage and DNA signature information.
- **Input/Output**: Input is assembled contigs (FASTA) with coverage information; output is genome bins.
- **Installation**: Install via bioconda: `conda install -c bioconda abawaca`
- **Platform Support**: Linux (C++ compiled)
- **Algorithm**: Uses composition-based binning with coverage information for improved binning accuracy.

## Pitfalls

- **Under Development**: The program is currently under development and not fully supported.
- **Documentation**: Limited documentation available; check the GitHub repository for updates.
- **Input Requirements**: Requires coverage information for optimal binning performance.
- **Citation**: If using this tool in published research, cite the original publication (doi:10.1038/nature14486).

## Examples

### Display usage information
**Args:** `abawaca`
**Explanation:** Shows basic usage information and available options.

### Basic binning with coverage file
**Args:** `-i contigs.fasta -c coverage.txt -o output_bins/`
**Explanation:** Bins contigs based on composition and coverage information into the output directory.

### Run with minimum contig length filter
**Args:** `-i contigs.fasta -c coverage.txt -m 1000 -o bins/`
**Explanation:** Filters out contigs shorter than 1000 bp before binning.

### Specify number of bins
**Args:** `-i contigs.fasta -c coverage.txt -k 10 -o bins/`
**Explanation:** Attempts to create exactly 10 genome bins from the input contigs.

### Run in verbose mode
**Args:** `-i contigs.fasta -c coverage.txt -v -o bins/`
**Explanation:** Runs with verbose output to monitor the binning process.