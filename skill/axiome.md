---
name: axiome
category: metagenomics
description: AXIOME2 - Automation Extension and Integration of Microbial Ecology
tags: [microbial-ecology, automation, qiime, 16s, amplicon]
author: oxo-call-community
source_url: "https://github.com/neufeld/AXIOME2"
---

## Concepts

- **Tool Overview**: AXIOME2 automates microbial ecology analyses, integrating QIIME and other tools for 16S rRNA amplicon sequencing workflows.

- **QIIME Integration**: Wraps QIIME functionality in automated, reproducible workflows.

- **Amplicon Focus**: Designed for 16S rRNA gene amplicon sequencing data analysis.

- **Reproducibility**: Generates analysis reports and tracks parameters for reproducible research.

## Pitfalls

- **QIIME Dependency**: Requires QIIME installation. Version compatibility is important.

- **Parameter Defaults**: Default parameters may not suit all datasets. Review and adjust.

- **Reference Database**: Requires appropriate 16S reference database (e.g., Greengenes, SILVA).

## Examples

### Basic 16S analysis
**Args:** `axiome --input fastqs/ --mapping-file mapping.tsv --output results/`
**Explanation:** Runs complete 16S amplicon analysis workflow.

### Custom reference database
**Args:** `axiome --input fastqs/ --mapping-file mapping.tsv --reference silva --output results/`
**Explanation:** Uses SILVA reference database instead of default.

### Specify analysis steps
**Args:** `axiome --input fastqs/ --mapping-file mapping.tsv --steps pick_otus,pick_rep_set,assign_taxonomy --output results/`
**Explanation:** Runs only specified analysis steps instead of full pipeline.
