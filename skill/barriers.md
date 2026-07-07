---
name: barriers
category: utility
description: Barriers - Compute local minima and energy barriers of RNA folding landscapes
tags: [barriers, utility, RNA-folding, energy-landscape, bioinformatics]
author: oxo-call-community
source_url: "https://www.tbi.univie.ac.at/RNA/Barriers"
---

## Concepts

- **Tool Overview**: Barriers (v1.8.1) computes local minima and energy barriers of RNA folding landscapes, helping analyze the thermodynamic properties of RNA secondary structures.
- **Core Function**: Identifies local energy minima and calculates energy barriers in RNA folding landscapes.
- **Energy Landscape**: Analyzes the free energy landscape of RNA folding pathways.
- **Local Minima**: Identifies stable RNA secondary structures (local energy minima).
- **Energy Barriers**: Calculates energy barriers between different RNA conformations.
- **Pathway Analysis**: Determines folding pathways between different structural states.
- **Input/Output**: Accepts RNA sequences or secondary structures; outputs energy landscape analysis.
- **Installation**: `conda install -c bioconda barriers`.

## Pitfalls

- **Sequence Length**: Performance may degrade for very long RNA sequences.
- **Computational Complexity**: Energy landscape analysis can be computationally intensive.
- **Parameter Sensitivity**: Results may vary with different temperature and parameter settings.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Analyze RNA folding landscape
**Args:** `barriers -i sequence.fasta -o landscape.txt`
**Explanation:** Computes energy landscape for RNA sequence.

### Specify temperature
**Args:** `barriers -i sequence.fasta -T 37 -o landscape.txt`
**Explanation:** Analyzes folding landscape at 37°C.

### Include secondary structure constraints
**Args:** `barriers -i sequence.fasta -c constraints.txt -o landscape.txt`
**Explanation:** Incorporates structural constraints into analysis.

### Generate dot plot
**Args:** `barriers -i sequence.fasta --dotplot dotplot.ps -o landscape.txt`
**Explanation:** Generates dot plot visualization of folding landscape.

### Maximum number of minima
**Args:** `barriers -i sequence.fasta -m 100 -o landscape.txt`
**Explanation:** Limits analysis to top 100 local minima.

### Detailed output
**Args:** `barriers -i sequence.fasta -v -o landscape.txt`
**Explanation:** Produces verbose output with detailed energy information.

### Display help
**Args:** `barriers --help`
**Explanation:** Shows all available command-line options and usage information.