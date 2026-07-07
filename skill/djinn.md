---
name: djinn
category: utility
description: djinn - Format converter for linked-read sequencing data.
tags: [djinn, utility, linked-read, barcode, format-conversion, 10x]
author: oxo-call-community
source_url: "https://github.com/pdimens/djinn"
---

## Concepts

- **Tool Overview**: djinn (v2.4+) is a format converter for linked-read sequencing data (10x, stLFR, TELLseq).
- **Core Function**: Converts between different linked-read FASTQ formats and barcode styles.
- **Input/Output**: Input: Linked-read FASTQ files. Output: Converted files in target format.
- **Algorithm**: Parses barcode information and reformats according to target specification.
- **Key Features**: Format conversion, barcode reformatting, supports multiple technologies, quality preservation, batch processing.
- **Installation**: `conda install -c bioconda djinn`

## Pitfalls

- **Input Requirements**: Requires linked-read data with specific barcode format.
- **Barcode Compatibility**: Not all barcode formats may be supported.
- **Read Pairing**: Must maintain proper read pairing during conversion.
- **Quality Scores**: Ensure quality scores are preserved during conversion.
- **Large Files**: May require significant memory for large FASTQ files.

## Examples

### Convert linked-read format
**Args:** `djinn convert --input reads.fq --from 10x --to stlfr --output converted.fq`
**Explanation:** Converts linked-read data from 10x to stLFR format.

### Batch conversion
**Args:** `djinn convert --input-dir fastq_files/ --from 10x --to tellseq --output-dir converted/`
**Explanation:** Batch convert multiple FASTQ files.

### Extract barcodes
**Args:** `djinn extract --input reads.fq --output barcodes.tsv`
**Explanation:** Extract barcode information from linked-read data.

### Validate format
**Args:** `djinn validate --input reads.fq --format 10x`
**Explanation:** Validate linked-read file format.

### Reformat barcodes
**Args:** `djinn reformat --input reads.fq --output reformatted.fq --barcode-format hex`
**Explanation:** Reformat barcode representation.