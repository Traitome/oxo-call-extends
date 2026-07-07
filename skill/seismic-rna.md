---
name: seismic-rna
category: rna-analysis
description: seismic-rna - SEISMIC-RNA software for RNA structure analysis
tags: ["seismic-rna", "rna-analysis", "RNA-structure", "SHAPE"]
author: oxo-call-community
source_url: "https://rouskinlab.github.io/seismic-rna"
---

## Concepts

- **Tool Overview**: seismic-rna (v0.24.4) analyzes RNA secondary structure using SHAPE data.
- **Core Function**: Predicts RNA structure and performs structural analysis.
- **Algorithm**: Uses SHAPE chemical probing data for structure prediction.
- **Input/Output**: Accepts SHAPE data and produces RNA structure predictions.
- **SHAPE Integration**: Integrates experimental SHAPE data for improved predictions.
- **Applications**: RNA structure analysis, riboswitch research, and ncRNA characterization.

## Pitfalls

- **Experimental Data**: Requires SHAPE experimental data.
- **Memory Usage**: High memory requirements for large RNA molecules.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Sequence Length**: May have limitations on sequence length.
- **Data Quality**: Results depend on input data quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Predict structure
**Args:** `seismic-rna predict -i rna.fasta -s shape.dat -o structure.dot`
**Explanation:** `-i` input FASTA; `-s` SHAPE data; `-o` output structure.

### Analyze structure
**Args:** `seismic-rna analyze -i structure.dot -o analysis.txt`
**Explanation:** Analyzes predicted structure.

### Refine structure
**Args:** `seismic-rna refine -i structure.dot -s shape.dat -o refined.dot`
**Explanation:** Refines structure using SHAPE data.

### Verbose logging
**Args:** `seismic-rna predict -i rna.fasta -v -o structure.dot`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seismic-rna --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seismic-rna --version`
**Explanation:** Shows current version.

### Energy calculation
**Args:** `seismic-rna energy -i structure.dot -o energy.txt`
**Explanation:** Calculates folding energy.