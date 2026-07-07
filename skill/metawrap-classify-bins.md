---
name: metawrap-classify-bins
category: utility
description: MetaWRAP requirements for classify_bins step
tags: [metawrap-classify-bins, utility, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Classify Bins v1.3.0 provides taxonomic classification functionality for metagenomic bins as part of the MetaWRAP pipeline.
- **Core Function**: Classifies metagenomic bins into taxonomic groups.
- **Taxonomic Classification**: Assigns taxonomy to assembled genome bins.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts genome bins; outputs taxonomic assignments.
- **Multiple Databases**: Supports multiple taxonomic databases for classification.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Database Completeness**: Classification accuracy depends on reference database completeness.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Sequence Quality**: Classification quality depends on input sequence quality.

## Examples

### Classify bins
**Args:** `metawrap-classify-bins -i bins/ -o classifications.txt`
**Explanation:** Classifies metagenomic bins into taxonomic groups.

### With custom database
**Args:** `metawrap-classify-bins -i bins/ -d custom_db/ -o classifications.txt`
**Explanation:** Uses custom taxonomic database for classification.

### Detailed output
**Args:** `metawrap-classify-bins -i bins/ -o classifications.txt -v`
**Explanation:** Generates detailed classification report.

### Output in JSON format
**Args:** `metawrap-classify-bins -i bins/ -o classifications.json -f json`
**Explanation:** Outputs classifications in JSON format.

### Batch processing
**Args:** `metawrap-classify-bins -i bins/ -o classifications/`
**Explanation:** Processes multiple bins in batch mode.