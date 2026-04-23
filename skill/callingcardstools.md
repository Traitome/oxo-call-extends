---
name: callingcardstools
category: epigenomics
description: Command line tools for Calling Cards sequencing data analysis
tags: [callingcardstools, calling-cards, transposon, epigenomics]
author: oxo-call-community
source_url: "https://github.com/cmatKhan/callingCardsTools"
---

## Concepts

- **Tool Overview**: CallingCardsTools processes Calling Cards transposon sequencing data.
- **Core Function**: Analyzes transposon insertion data to identify transcription factor binding sites.
- **Input**: FASTQ files from Calling Cards experiments.
- **Output**: Transposon insertion sites and binding peak calls.
- **Application**: Transcription factor binding site identification.
- **Installation**: Install via bioconda: `conda install -c bioconda callingcardstools`

## Pitfalls

- **Protocol Specific**: Designed for Calling Cards protocol data.
- **Reference Genome**: Requires matching reference genome.
- **Barcode Handling**: Proper barcode demultiplexing is critical.

## Examples

### Process Calling Cards data
**Args:** `callingcardstools process -i reads.fq -r reference.fa -o results/`
**Explanation:** Processes Calling Cards sequencing data for insertion site detection.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
