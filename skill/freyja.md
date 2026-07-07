---
name: freyja
category: annotation
description: Freyja recovers relative lineage abundances from mixed SARS-CoV-2 samples and provides functionality to analyze lineage dynamics.
tags: [freyja, SARS-CoV-2, variant analysis, lineage tracking]
author: oxo-call-community
source_url: "https://github.com/andersen-lab/Freyja"
---

## Concepts
- **Lineage Abundance**: Recovers relative abundances of SARS-CoV-2 lineages from mixed samples.
- **Variant Calling**: Identifies genetic variants from sequencing data.
- **Lineage Assignment**: Assigns reads to specific viral lineages.
- **Dynamics Analysis**: Analyzes lineage dynamics over time.
- **Visualization**: Generates visualizations of lineage frequencies.

## Pitfalls
- **SARS-CoV-2 Specific**: Designed specifically for SARS-CoV-2 analysis.
- **Reference Dependence**: Requires up-to-date reference database.
- **Mixture Detection**: May struggle with very low-frequency variants.
- **Sequencing Depth**: Requires sufficient sequencing depth for accurate detection.
- **Database Updates**: Needs regular updates to reference database.

## Examples
### Recover lineage abundances
**Args:** `freyja demix --reads reads.fastq --output abundances.txt`
**Explanation:** Recovers relative lineage abundances from sequencing data.

### Update reference database
**Args:** `freyja update`
**Explanation:** Updates the lineage reference database.

### Analyze time series
**Args:** `freyja timecourse --input samples.txt --output dynamics.txt`
**Explanation:** Analyzes lineage dynamics over time.

### Generate lineage plot
**Args:** `freyja plot --input abundances.txt --output plot.png`
**Explanation:** Generates visualization of lineage frequencies.

### Export to JSON
**Args:** `freyja export --input abundances.txt --output data.json`
**Explanation:** Exports results in JSON format for downstream analysis.