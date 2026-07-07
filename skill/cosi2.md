---
name: cosi2
category: population-genomics
description: Efficient coalescent simulator with selection and population structure support
tags: [cosi2, coalescent-simulation, population-genetics, selection, recombination]
author: oxo-call-community
source_url: "https://www.broadinstitute.org/mpg/cosi2/"
---

## Concepts

- **Tool Overview**: cosi2 is an efficient coalescent simulator that supports selection, population structure, variable recombination rates, and gene conversion, with both exact and approximate simulation modes.
- **Core Function**: Simulates genetic variation under the coalescent model with various evolutionary forces.
- **Algorithm**: Implements coalescent theory with extensions for selection, recombination, gene conversion, and population structure.
- **Input**: Configuration file defining population parameters, demographic history, and simulation settings.
- **Output**: Simulated genetic sequences, variant data in various formats (FASTA, VCF, etc.).
- **Application**: Population genetics research, testing statistical methods, generating benchmark datasets.
- **Installation**: Install via bioconda: `conda install -c bioconda cosi2`

## Pitfalls

- **Parameter Complexity**: Requires careful specification of demographic and selection parameters.
- **Computational Time**: Exact simulation mode can be slow for large populations.
- **Memory Usage**: May require significant memory for complex simulations.
- **Approximation Accuracy**: Approximate mode trades accuracy for speed.
- **Model Assumptions**: Results depend on correct specification of evolutionary model.

## Examples

### Basic simulation
**Args:** `cosi2 -c config.txt -o output.vcf`
**Explanation:** Runs simulation using configuration file and outputs VCF.

### Approximate mode
**Args:** `cosi2 -c config.txt -a -o output.vcf`
**Explanation:** Uses approximate simulation mode for faster results.

### Output FASTA format
**Args:** `cosi2 -c config.txt -f fasta -o output.fasta`
**Explanation:** Outputs simulated sequences in FASTA format.

### Multiple replicates
**Args:** `cosi2 -c config.txt -r 10 -o output_`
**Explanation:** Runs 10 simulation replicates.

### Display help
**Args:** `cosi2 --help`
**Explanation:** Shows all available options and usage information.