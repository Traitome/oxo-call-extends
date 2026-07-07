---
name: sr2silo
category: formatting
description: SR2SILO - Short-read to SILO format converter
tags: [sr2silo, formatting, short-read, silo, conversion]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/sr2silo/blob/v1.8.1/README.md"
---

## Concepts

- **Tool Overview**: sr2silo (v1.8.1) - A format conversion tool
- **Core Function**: Converts short-read data to SILO format
- **Input/Output**: Accepts short-read files; outputs SILO format files
- **Algorithm**: Format conversion algorithms
- **Installation**: `conda install -c bioconda sr2silo`
- **Key Features**: Format conversion, short-read, SILO format

## Pitfalls

- **Input Requirements**: Requires properly formatted short-read files
- **Format Compatibility**: Not all formats are compatible
- **Conversion Accuracy**: Conversion may lose information
- **Memory Usage**: Large files require significant memory
- **Output Format**: Output format depends on configuration
- **SILO Format**: SILO format has specific requirements

## Examples

### Display help
**Args:** `sr2silo --help`
**Explanation:** Shows available options and usage information.

### Basic format conversion
**Args:** `sr2silo -i reads.fastq -o output.silo`
**Explanation:** Convert short-read to SILO format.

### With quality scores
**Args:** `sr2silo -i reads.fastq -o output.silo --quality`
**Explanation:** Include quality scores in conversion.

### With metadata
**Args:** `sr2silo -i reads.fastq -m metadata.txt -o output.silo`
**Explanation:** Include metadata in SILO format.

### Multiple files
**Args:** `sr2silo -i reads1.fastq reads2.fastq -o output.silo`
**Explanation:** Convert multiple short-read files.

### Output detailed results
**Args:** `sr2silo -i reads.fastq -o output.silo --detailed`
**Explanation:** Output detailed conversion information.

### Output statistics
**Args:** `sr2silo -i reads.fastq -o output.silo --stats`
**Explanation:** Output conversion statistics.

### Generate report
**Args:** `sr2silo -i reads.fastq -o output.silo --report`
**Explanation:** Generate conversion report.

### With threads
**Args:** `sr2silo -i reads.fastq -o output.silo -p 8`
**Explanation:** Use multiple threads for conversion.