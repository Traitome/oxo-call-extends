---
name: visceral-evaluatesegmentation
category: utility
description: EvaluateSegmentation is a tool that compares two volumes (a test segmentation and a ground truth segmentation) using 22 different metrics that were selected as a result of a comprehensive research into the metrics used in the medical volume segmentations.
tags: [visceral-evaluatesegmentation, utility]
author: oxo-call-community
source_url: "https://github.com/Visceral-Project/EvaluateSegmentation"
---

## Concepts

- **Tool Overview**: visceral-evaluatesegmentation (v2021.03.25) - EvaluateSegmentation is a tool that compares two volumes (a test segmentation and a ground truth segmentation) using 22 different metrics that were selected as a result of a comprehensive research into the metrics used in the medical volume segmentations.
- **Core Function**: EvaluateSegmentation is a tool that compares two volumes (a test segmentation and a ground truth segmentation) using 22 different metrics that were selected as a result of a comprehensive research into the metrics used in the medical volume segmentations.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda visceral-evaluatesegmentation`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
