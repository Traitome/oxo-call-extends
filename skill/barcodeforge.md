---
name: barcodeforge
category: utility
description: BarcodeForge - Generate pathogen-specific barcodes for Freyja variant tracking
tags: [barcodeforge, utility, freyja, pathogen, variant-tracking]
author: oxo-call-community
source_url: "https://andersen-lab.github.io/Freyja/src/wiki/custom_barcodes.html"
---

## Concepts

- **Tool Overview**: BarcodeForge (v1.1.5) is a CLI tool for generating pathogen-specific barcodes for use with Freyja, a tool for tracking viral variants.
- **Core Function**: Generates custom barcodes for pathogen variant tracking in Freyja.
- **Barcode Generation**: Creates barcodes specific to pathogen genomes for variant identification.
- **Freyja Integration**: Designed to work seamlessly with Freyja variant tracking pipeline.
- **Pathogen Specific**: Supports various pathogens including viruses like SARS-CoV-2.
- **Input/Output**: Accepts reference sequences and variant data; outputs barcode definitions.
- **Installation**: `conda install -c bioconda barcodeforge`.

## Pitfalls

- **Freyja Compatibility**: Barcodes are specifically designed for Freyja workflow.
- **Reference Quality**: Requires high-quality reference genome for accurate barcode generation.
- **Variant Database**: May require up-to-date variant database for optimal results.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Generate barcodes from reference
**Args:** `barcodeforge -r reference.fasta -o barcodes.json`
**Explanation:** Generates barcodes from reference genome sequence.

### Include variant information
**Args:** `barcodeforge -r reference.fasta -v variants.vcf -o barcodes.json`
**Explanation:** Incorporates known variants into barcode generation.

### Specify pathogen type
**Args:** `barcodeforge -r reference.fasta --pathogen sars-cov-2 -o barcodes.json`
**Explanation:** Uses pathogen-specific settings for barcode generation.

### Custom barcode length
**Args:** `barcodeforge -r reference.fasta -l 20 -o barcodes.json`
**Explanation:** Generates barcodes with custom length of 20 nucleotides.

### Output for Freyja
**Args:** `barcodeforge -r reference.fasta --freyja-format -o freyja_barcodes.tsv`
**Explanation:** Outputs barcodes in Freyja-compatible format.

### Batch processing
**Args:** `barcodeforge -i references.txt -o barcodes_dir/`
**Explanation:** Processes multiple reference sequences in batch mode.

### Display help
**Args:** `barcodeforge --help`
**Explanation:** Shows all available command-line options and usage information.