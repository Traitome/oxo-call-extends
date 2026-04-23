---
name: tpp
category: expression
description: The Trans-Proteomic Pipeline (TPP) is a collection of integrated tools for MS/MS proteomics developed at the Seattle Proteome Center. The Bioconda package includes the command-line versions of the TPP toolset. These programs include tools for validation (PeptideProphet, iProphet, ProteinProphet, Mayu) and quantification (XPRESS, ASAPRatio, Libra) as well as a number of parsers and converters (Out2XML, Mascot2XML, Tandem2XML, etc).
tags: [tpp, expression]
author: oxo-call-community
source_url: "http://tools.proteomecenter.org/wiki/index.php?title=Software:TPP"
---

## Concepts

- **Tool Overview**: tpp (v5.0.0) - The Trans-Proteomic Pipeline (TPP) is a collection of integrated tools for MS/MS proteomics developed at the Seattle Proteome Center. The Bioconda package includes the command-line versions of the TPP toolset. These programs include tools for validation (PeptideProphet, iProphet, ProteinProphet, Mayu) and quantification (XPRESS, ASAPRatio, Libra) as well as a number of parsers and converters (Out2XML, Mascot2XML, Tandem2XML, etc).
- **Core Function**: The Trans-Proteomic Pipeline (TPP) is a collection of integrated tools for MS/MS proteomics developed at the Seattle Proteome Center. The Bioconda package includes the command-line versions of the TPP toolset. These programs include tools for validation (PeptideProphet, iProphet, ProteinProphet, Mayu) and quantification (XPRESS, ASAPRatio, Libra) as well as a number of parsers and converters (Out2XML, Mascot2XML, Tandem2XML, etc).
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda tpp`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
