---
name: tortoize
category: qc
description: Application to calculate ramachandran z-scores.
tags: [tortoize, qc]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/tortoize/blob/trunk/doc/tortoize.pdf"
---

## Concepts

- **Tool Overview**: tortoize (v2.0.16) - Tortoize validates protein structure models by checking the Ramachandran plot and side-chain rotamer distributions. Quality Z-scores are given at the residue level and at the model level (ramachandran-z and torsions-z). Higher scores are better. To compare models or to describe the reliability of the model Z-scores jackknife- based standard deviations are also reported (ramachandran-jackknife-sd and torsion-jackknife-sd).
- **Core Function**: Application to calculate ramachandran z-scores.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda tortoize`

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
