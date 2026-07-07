---
name: doubletd
category: utility
description: "doubletD is a method to detect doublets in single-cell DNA sequencing data"
tags: [doubletd, utility, single-cell, DNA-seq, doublet-detection]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/doubletD"
---

## Concepts

- **Tool Overview**: doubletD is a computational method for detecting doublets in single-cell DNA sequencing data.
- **Core Function**: Identifies cells containing DNA from two different individuals in scDNA-seq experiments.
- **Input/Output**: Input: VCF file with variant calls, cell barcodes. Output: Doublet probabilities and classifications.
- **Algorithm**: Uses haplotype-based phasing and statistical modeling to detect mixed-genotype cells.
- **Key Features**: Works with low-coverage data, handles heterogeneous populations, scalable to large datasets.
- **Installation**: `conda install -c bioconda doubletd`

## Pitfalls

- **Variant Call Quality**: Accurate doublet detection depends on high-quality variant calls.
- **Coverage Depth**: Very low coverage may reduce detection sensitivity.
- **Population Structure**: Admixed populations can complicate doublet detection.
- **Contamination**: Sample contamination can produce false doublet signals.
- **Phasing Quality**: Poor phasing can affect doublet classification accuracy.

## Examples

### Basic doublet detection
**Args:** `--vcf variants.vcf --cells barcodes.txt --output doublets.txt`
**Explanation:** Detects doublets from variant calls and cell barcodes.

### With phasing information
**Args:** `--vcf variants.vcf --cells barcodes.txt --phased --output doublets.txt`
**Explanation:** Uses pre-phased genotypes for improved doublet detection.

### Custom confidence threshold
**Args:** `--vcf variants.vcf --cells barcodes.txt --threshold 0.8 --output doublets.txt`
**Explanation:** Sets a custom confidence threshold (0.8) for calling doublets.

### Batch processing
**Args:** `--vcf batch1.vcf batch2.vcf --cells barcodes.txt --output combined.txt --batch`
**Explanation:** Processes multiple VCF files from different batches together.

### Generate summary report
**Args:** `--vcf variants.vcf --cells barcodes.txt --output doublets.txt --report summary.html`
**Explanation:** Produces an HTML summary report with doublet statistics.