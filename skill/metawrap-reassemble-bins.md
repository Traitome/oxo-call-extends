---
name: metawrap-reassemble-bins
category: assembly
description: MetaWRAP requirements for reassemble_bins step
tags: [metawrap-reassemble-bins, assembly, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Reassemble Bins v1.3.0 provides reassembly functionality for metagenomic bins as part of the MetaWRAP pipeline.
- **Core Function**: Reassembles and improves metagenomic genome bins.
- **Bin Improvement**: Enhances the quality of existing genome bins through reassembly.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts genome bins; outputs improved, reassembled bins.
- **Error Correction**: Corrects sequencing errors in assembled contigs.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Reassembly of complex genomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Sequence Quality**: Reassembly quality depends on input sequence quality.

## Examples

### Reassemble bins
**Args:** `metawrap-reassemble-bins -i bins/ -o reassembled/`
**Explanation:** Reassembles and improves metagenomic bins.

### With coverage information
**Args:** `metawrap-reassemble-bins -i bins/ -c coverage.txt -o reassembled/`
**Explanation:** Uses coverage information for improved reassembly.

### Error correction
**Args:** `metawrap-reassemble-bins -i bins/ -o reassembled/ --correct`
**Explanation:** Performs error correction during reassembly.

### Detailed output
**Args:** `metawrap-reassemble-bins -i bins/ -o reassembled/ -v`
**Explanation:** Generates detailed reassembly report.

### Batch processing
**Args:** `metawrap-reassemble-bins -i bins/ -o reassembled/`
**Explanation:** Processes multiple bins in batch mode.