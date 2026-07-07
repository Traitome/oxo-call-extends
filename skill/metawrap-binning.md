---
name: metawrap-binning
category: utility
description: MetaWRAP requirements for binning step
tags: [metawrap-binning, utility, metagenomics, binning]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Binning v1.3.0 provides binning functionality as part of the MetaWRAP metagenomic analysis pipeline.
- **Core Function**: Bins metagenomic contigs into genome bins.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Multiple Binning Methods**: Supports multiple binning algorithms for improved results.
- **Input/Output**: Accepts assembled contigs; outputs genome bins.
- **Quality Assessment**: Includes bin quality assessment and refinement.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Contig Quality**: Binning quality depends on input contig quality.
- **Complex Communities**: May struggle with highly complex microbial communities.

## Examples

### Bin metagenome
**Args:** `metawrap-binning -i contigs.fasta -o bins/`
**Explanation:** Bins assembled contigs into genome bins.

### With coverage information
**Args:** `metawrap-binning -i contigs.fasta -c coverage.txt -o bins/`
**Explanation:** Uses coverage information for improved binning.

### Refine bins
**Args:** `metawrap-binning -i contigs.fasta -o bins/ --refine`
**Explanation:** Refines existing genome bins.

### Multiple methods
**Args:** `metawrap-binning -i contigs.fasta -o bins/ --multi`
**Explanation:** Uses multiple binning methods for consensus.

### Quality assessment
**Args:** `metawrap-binning -i contigs.fasta -o bins/ --assess`
**Explanation:** Assesses bin quality and generates statistics.