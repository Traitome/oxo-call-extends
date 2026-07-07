---
name: metawrap-quant-bins
category: utility
description: MetaWRAP requirements for quant_bins step
tags: [metawrap-quant-bins, utility, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Quant Bins v1.3.0 provides quantification functionality for metagenomic bins as part of the MetaWRAP pipeline.
- **Core Function**: Quantifies the abundance of metagenomic bins.
- **Abundance Estimation**: Estimates the relative abundance of each genome bin.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts genome bins and sequencing reads; outputs abundance estimates.
- **Coverage Calculation**: Calculates coverage depth for each bin.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Sequence Quality**: Quantification accuracy depends on input sequence quality.
- **Reference Bias**: May have bias towards well-characterized genomes.

## Examples

### Quantify bins
**Args:** `metawrap-quant-bins -i bins/ -r reads.fastq -o abundances.txt`
**Explanation:** Quantifies abundance of metagenomic bins.

### With multiple samples
**Args:** `metawrap-quant-bins -i bins/ -r sample1.fastq sample2.fastq -o abundances.txt`
**Explanation:** Quantifies bins across multiple samples.

### Generate coverage report
**Args:** `metawrap-quant-bins -i bins/ -r reads.fastq -o abundances.txt -c coverage.txt`
**Explanation:** Generates coverage report along with abundances.

### Detailed output
**Args:** `metawrap-quant-bins -i bins/ -r reads.fastq -o abundances.txt -v`
**Explanation:** Generates detailed quantification report.

### Batch processing
**Args:** `metawrap-quant-bins -i bins/ -r fastq/ -o abundances/`
**Explanation:** Processes multiple samples in batch mode.