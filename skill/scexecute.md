---
name: scexecute
category: alignment
description: SCExecute - Generate cell-barcode specific BAM files from aggregate single-cell sequencing data
tags: ["scexecute", "alignment", "single-cell", "BAM"]
author: oxo-call-community
source_url: "https://horvathlab.github.io/NGS/SCExecute"
---

## Concepts

- **Tool Overview**: SCExecute (v1.3.3) generates cell-barcode specific BAM files from aligned, aggregate single-cell sequencing data.
- **Core Function**: Stratifies aggregate BAM files by cell barcodes and executes commands on each.
- **Algorithm**: Uses barcode information to separate reads into cell-specific BAM files.
- **Input/Output**: Accepts aggregate BAM file and produces cell-specific BAM files.
- **Barcode Processing**: Handles cell barcode extraction and stratification.
- **Applications**: Single-cell sequencing data processing, parallel analysis of individual cells.

## Pitfalls

- **Barcode Quality**: Results depend on barcode quality and completeness.
- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **File Size**: Generates many individual BAM files.
- **Barcode Whitelist**: Requires proper barcode whitelist for accurate cell identification.

## Examples

### Basic execution
**Args:** `scexecute -i aggregate.bam -b barcodes.txt -o cell_bams/`
**Explanation:** `-i` input BAM; `-b` barcode whitelist; `-o` output directory.

### With custom command
**Args:** `scexecute -i aggregate.bam -b barcodes.txt -c "samtools view -F 4" -o filtered_bams/`
**Explanation:** `-c` executes custom command on each cell BAM.

### Multiple barcodes
**Args:** `scexecute -i aggregate.bam -b barcodes1.txt barcodes2.txt -o cell_bams/`
**Explanation:** Processes multiple barcode files.

### Verbose logging
**Args:** `scexecute -i aggregate.bam -b barcodes.txt -v -o cell_bams/`
**Explanation:** `-v` enables verbose output for debugging.

### Quality filtering
**Args:** `scexecute -i aggregate.bam -b barcodes.txt -q 30 -o cell_bams/`
**Explanation:** `-q 30` filters reads with quality below 30.

### Output statistics
**Args:** `scexecute -i aggregate.bam -b barcodes.txt -s stats.txt -o cell_bams/`
**Explanation:** `-s` outputs processing statistics.

### Batch processing
**Args:** `scexecute -i aggregate.bam -b barcodes.txt --batch 100 -o cell_bams/`
**Explanation:** `--batch` processes cells in batches of 100.