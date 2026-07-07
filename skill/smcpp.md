---
name: smcpp
category: population-genomics
description: SMC++ infers population history from whole-genome sequence data using the Sequential Markov Coalescent model
tags: [smcpp, population-genomics, coalescent, demography, population-history]
author: oxo-call-community
source_url: "https://github.com/popgenmethods/smcpp"
---

## Concepts

- **Tool Overview**: smcpp (v1.15.4) - A tool for inferring population demography from whole-genome sequencing data
- **Core Function**: Uses Sequential Markov Coalescent (SMC) model to infer population size changes over time
- **Input/Output**: Accepts VCF or FASTA files; outputs demographic history plots and parameters
- **Algorithm**: Implements the SMC' model for efficient coalescent inference
- **Installation**: `conda install -c bioconda smcpp`
- **Key Features**: Handles large genomes, supports multiple populations, provides visualization tools

## Pitfalls

- **VCF Quality**: Requires high-quality VCF with accurate genotype calls
- **Reference Genome**: Must use properly indexed reference genome
- **Computation Time**: Large datasets can be computationally intensive
- **Memory Usage**: May require significant memory for large genomes
- **Sample Size**: Performance depends on sample size and coverage
- **Model Assumptions**: Assumes neutral evolution and no population structure

## Examples

### Display help
**Args:** `smcpp --help`
**Explanation:** Shows available options and usage information.

### Prepare input data
**Args:** `smcpp vcf2smc -i input.vcf -o output.smc.gz -r reference.fasta`
**Explanation:** Convert VCF to SMC++ input format.

### Infer population size
**Args:** `smcpp estimate -i output.smc.gz -o results/`
**Explanation:** Infer population size history from SMC file.

### Plot results
**Args:** `smcpp plot -i results/model.final.json -o plot.pdf`
**Explanation:** Generate demographic history plot.

### Multi-population analysis
**Args:** `smcpp estimate -i pop1.smc.gz pop2.smc.gz -o results/`
**Explanation:** Compare demographic histories across populations.

### Bootstrap analysis
**Args:** `smcpp bootstrap -i output.smc.gz -o bootstrap_results/ -n 100`
**Explanation:** Perform bootstrap resampling for confidence intervals.

### Specify mutation rate
**Args:** `smcpp estimate -i output.smc.gz -o results/ -m 2.5e-8`
**Explanation:** Set custom mutation rate for analysis.

### Generate report
**Args:** `smcpp report -i results/ -o report.html`
**Explanation:** Generate comprehensive HTML report.