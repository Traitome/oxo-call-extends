---
name: mity
category: variant-calling
description: Mity is a bioinformatic analysis pipeline designed to call mitochondrial SNV and INDEL variants from Whole Genome Sequencing (WGS) data.
tags: [mity, variant-calling]
author: oxo-call-community
source_url: "https://github.com/KCCG/mity"
---

## Concepts

- **Tool Overview**: mity v2.0.1 - *Mity* can: - identify very low-heteroplasmy variants, even <1% heteroplasmy when there is sufficient read-depth (eg >1000x) - filter out common artefacts that arise from high-depth sequencing - easily integrate with existing nuclear DNA analysis pipelines (mity merge) - provide an annotated report, designed for clinicians and researchers to interrogate.
- **Core Function**: Mity is a bioinformatic analysis pipeline designed to call mitochondrial SNV and INDEL variants from Whole Genome Sequencing (WGS) data.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mity`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
