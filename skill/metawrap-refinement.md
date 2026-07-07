---
name: metawrap-refinement
category: utility
description: MetaWRAP requirements for bin_refinement step
tags: [metawrap-refinement, utility, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Bin Refinement v1.3.0 provides bin refinement functionality as part of the MetaWRAP pipeline.
- **Core Function**: Refines and improves metagenomic genome bins.
- **Bin Improvement**: Enhances bin quality through multiple refinement strategies.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts genome bins; outputs refined, higher-quality bins.
- **Quality Filtering**: Filters out low-quality bins and improves existing ones.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Bin Quality**: Refinement quality depends on initial bin quality.
- **Complex Communities**: May struggle with highly complex microbial communities.

## Examples

### Refine bins
**Args:** `metawrap-refinement -i bins/ -o refined/`
**Explanation:** Refines and improves metagenomic bins.

### With quality threshold
**Args:** `metawrap-refinement -i bins/ -o refined/ -q 90`
**Explanation:** Uses minimum quality threshold of 90%.

### Multiple iterations
**Args:** `metawrap-refinement -i bins/ -o refined/ -n 3`
**Explanation:** Performs 3 iterations of refinement.

### Generate report
**Args:** `metawrap-refinement -i bins/ -o refined/ -r report.html`
**Explanation:** Generates refinement quality report.

### Batch processing
**Args:** `metawrap-refinement -i bins/ -o refined/`
**Explanation:** Processes multiple bins in batch mode.