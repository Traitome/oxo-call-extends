---
name: msmc2
category: population-genomics
description: Infer population size history and separation history from whole genome sequencing data.
tags: [msmc2, population-genomics, genetics]
author: oxo-call-community
source_url: "https://github.com/stschiff/msmc2"
---

## Concepts

- **Tool Overview**: MSMC2 v2.1.4 infers population history from WGS data.
- **Core Function**: Reconstructs population size and separation history.
- **Coalescent Theory**: Uses multiple sequentially Markovian coalescent methods.
- **Whole Genome**: Works with whole genome sequencing data.
- **Time Estimation**: Estimates population history over time.
- **Input/Output**: Accepts phased genomes; outputs population history curves.

## Pitfalls

- **Phased Data**: Requires phased haplotype data.
- **Memory Requirements**: Memory usage depends on genome coverage.
- **Parameter Tuning**: May require parameter adjustment for analysis.
- **Data Quality**: Results depend on sequencing quality and depth.
- **Computational Resources**: Large genomes may require significant resources.
- **Sample Requirements**: Requires multiple samples for population inference.

## Examples

### Infer population history
**Args:** `msmc2 -o output input1.bam input2.bam`
**Explanation:** Infers population history from two haplotypes.

### With multiple samples
**Args:** `msmc2 -o output hap1_1.bam hap1_2.bam hap2_1.bam hap2_2.bam`
**Explanation:** Uses four haplotypes from two individuals.

### Generate time trajectory
**Args:** `msmc2 -o output -t 30 input1.bam input2.bam`
**Explanation:** Generates time trajectory with 30 time points.

### Generate interval file
**Args:** `msmc2 -o output -I input1.bam input2.bam`
**Explanation:** Outputs intermediate interval files.

### Cross-coalescent rates
**Args:** `msmc2 -o output input1_1.bam input1_2.bam input2_1.bam input2_2.bam`
**Explanation:** Calculates cross-coalescent rates between populations.