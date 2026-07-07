---
name: metawrap-annotate-bins
category: annotation
description: MetaWRAP requirements for annotate_bins step
tags: [metawrap-annotate-bins, annotation, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Annotate Bins v1.3.0 provides annotation functionality for metagenomic bins as part of the MetaWRAP pipeline.
- **Core Function**: Annotates genes and functions within metagenomic bins.
- **Gene Annotation**: Identifies and annotates genes in assembled contigs.
- **Functional Annotation**: Provides functional descriptions for predicted genes.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts genome bins; outputs annotated features and functional information.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Sequence Quality**: Annotation quality depends on input sequence quality.
- **Database Completeness**: Annotation quality depends on reference database completeness.
- **False Positives**: May predict false positive genes.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Memory Requirements**: Processing large datasets may require significant memory.

## Examples

### Annotate bins
**Args:** `metawrap-annotate-bins -i bins/ -o annotations/`
**Explanation:** Annotates genes in metagenomic bins.

### With custom database
**Args:** `metawrap-annotate-bins -i bins/ -d custom_db/ -o annotations/`
**Explanation:** Uses custom annotation database.

### Detailed annotation
**Args:** `metawrap-annotate-bins -i bins/ -o annotations/ -v`
**Explanation:** Generates detailed annotations with verbose output.

### Output GFF format
**Args:** `metawrap-annotate-bins -i bins/ -o annotations.gff -f gff`
**Explanation:** Outputs annotations in GFF format.

### Batch processing
**Args:** `metawrap-annotate-bins -i bins/ -o annotations/`
**Explanation:** Processes multiple bins in batch mode.