---
name: dms
category: annotation
description: DMS - Deep Mutational Scanning analysis tools.
tags: [dms, annotation, deep-mutational-scanning, variant, protein, fitness]
author: oxo-call-community
source_url: "https://github.com/jbloomlab/dms_tools"
---

## Concepts

- **Tool Overview**: DMS tools provide analysis functions for deep mutational scanning experiments.
- **Core Function**: Analyzes high-throughput mutagenesis data to assess variant fitness effects.
- **Input/Output**: Input: Sequencing counts from DMS experiments. Output: Variant fitness scores, statistical analysis.
- **Algorithm**: Uses statistical methods to quantify variant fitness from sequencing data.
- **Key Features**: Fitness calculation, error modeling, statistical testing, visualization, multiple experiment comparison.
- **Installation**: `conda install -c bioconda dms`

## Pitfalls

- **Input Requirements**: Requires deep mutational scanning count data.
- **Experimental Design**: Proper controls are essential for accurate fitness measurements.
- **Sequencing Depth**: Requires sufficient sequencing depth.
- **Normalization**: Appropriate normalization is critical.
- **Batch Effects**: Batch effects can confound results.

## Examples

### Analyze DMS data
**Args:** `dms analyze --counts counts.tsv --output fitness.tsv`
**Explanation:** Analyzes deep mutational scanning data to calculate fitness scores.

### With controls
**Args:** `dms analyze --counts counts.tsv --controls controls.tsv --output fitness.tsv`
**Explanation:** Include control samples for normalization.

### Statistical testing
**Args:** `dms analyze --counts counts.tsv --output fitness.tsv --test`
**Explanation:** Perform statistical testing on fitness differences.

### Generate visualization
**Args:** `dms analyze --counts counts.tsv --output fitness.tsv --plot fitness.png`
**Explanation:** Generate visualization of fitness landscape.

### Compare experiments
**Args:** `dms compare --experiments exp1.tsv exp2.tsv --output comparison.tsv`
**Explanation:** Compare fitness scores across multiple experiments.