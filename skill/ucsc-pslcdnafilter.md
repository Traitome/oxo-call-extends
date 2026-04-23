---
name: ucsc-pslcdnafilter
category: alignment
description: Filter cDNA alignments in psl format. Filtering criteria are comparative, selecting near best in genome alignments for each given cDNA and non-comparative, based only on the quality of an individual alignment.
tags: [ucsc-pslcdnafilter, alignment]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-pslcdnafilter (v482) - Filter cDNA alignments in psl format. Filtering criteria are comparative, selecting near best in genome alignments for each given cDNA and non-comparative, based only on the quality of an individual alignment.
- **Core Function**: Filter cDNA alignments in psl format. Filtering criteria are comparative, selecting near best in genome alignments for each given cDNA and non-comparative, based only on the quality of an individual alignment.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-pslcdnafilter`

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
