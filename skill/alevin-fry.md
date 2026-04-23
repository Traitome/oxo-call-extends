---
name: alevin-fry
category: expression
description: Efficient tool for processing single-cell RNA-seq data from RAD files produced by alevin/salmon
tags: [single-cell, scrna-seq, quantification, umi, salmon]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/alevin-fry"
---

## Concepts

- **Tool Overview**: alevin-fry is a fast, accurate, and memory-efficient tool for quantifying single-cell and single-nucleus RNA-seq data from RAD files.
- **Core Function**: Processes RAD files from alevin/salmon to generate permit lists, quantify gene expression, and resolve UMI collisions.
- **Input/Output**: Input: RAD files from alevin. Output: Gene count matrices, permit lists, quantification reports.
- **Resolution Methods**: Supports multiple UMI resolution methods: cr-like, cr-like-em, parsimony, parsimony-em, for different accuracy/speed tradeoffs.
- **Installation**: Install via bioconda: `conda install -c bioconda alevin-fry`

## Pitfalls

- **RAD Input Required**: Must use alevin/salmon output in RAD format - standard BAM/FASTQ not supported.
- **Permit List Generation**: Must generate permit list before quantification - barcode filtering is critical for accurate results.
- **Memory vs Speed**: Different resolution methods have different memory requirements - parsimony is fastest, parsimony-em most accurate.
- **Chemistry Protocol**: Specify correct chemistry (10x v2/v3, dropseq, etc.) for proper barcode handling.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available subcommands and options.

### Generate permit list
**Args:** `generate-permit-list -i rad_dir/ -o permit_list/ -k 10`
**Explanation:** Generates barcode permit list with expected cell count of 10.

### Quantify with cr-like method
**Args:** `quant -i permit_list/ -r rad_dir/ -o quant_output/ -m cr-like`
**Explanation:** Quantifies using Cell Ranger-like resolution method.

### Quantify with parsimony-em
**Args:** `quant -i permit_list/ -r rad_dir/ -o quant_output/ -m parsimony-em`
**Explanation:** Uses parsimony-EM method for most accurate UMI resolution.

### Generate permit list from expected cells
**Args:** `generate-permit-list -i rad_dir/ -o permit_list/ --expect-cells 5000`
**Explanation:** Uses expected cell count of 5000 for barcode filtering.

### Map transcripts to genes
**Args:** `quant -i permit_list/ -r rad_dir/ -o output/ -t transcript2gene.tsv`
**Explanation:** Uses custom transcript-to-gene mapping file for quantification.

### Process with chemistry specification
**Args:** `generate-permit-list -i rad_dir/ -o permit_list/ --chemistry 10x_v3`
**Explanation:** Specifies 10x v3 chemistry for proper barcode length and structure.

### Output in different formats
**Args:** `quant -i permit_list/ -r rad_dir/ -o output/ --output-format alevin`
**Explanation:** Outputs in alevin-compatible format for downstream tools.
