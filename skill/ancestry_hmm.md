---
name: ancestry_hmm
category: population-genomics
description: HMM-based local ancestry inference and admixture time estimation from NGS data with arbitrary ploidy support
tags: [local-ancestry, admixture, hmm, ploidy, population-genetics]
author: oxo-call-community
source_url: "https://github.com/russcd/Ancestry_HMM"
---

## Concepts

- **Tool Overview**: Ancestry_HMM uses a hidden Markov model approach for simultaneously estimating local ancestry and admixture time from next-generation sequencing data. Supports samples of arbitrary ploidy. Version 1.0.2.
- **Genotype Likelihoods**: Models read pileup data directly rather than called genotypes, avoiding biases from genotype calling in low-coverage data.
- **Arbitrary Ploidy**: Generalized to handle any ploidy level (diploid, tetraploid, hexaploid, etc.), not limited to diploid organisms.
- **Simultaneous Estimation**: Estimates both local ancestry tracts and admixture timing in a single analysis, rather than requiring separate steps.
- **Population Sources**: Requires allele frequency data from source populations to infer ancestry at each genomic position.
- **Admixture Time**: Estimates time since admixture event based on ancestry tract length distribution.

## Pitfalls

- **Reference Populations**: Requires accurate allele frequency estimates from source populations. Poor reference data leads to incorrect ancestry calls.
- **Coverage Requirements**: Low-coverage data (<5x) has reduced power for ancestry inference. Higher coverage improves accuracy.
- **Computational Cost**: HMM inference is computationally intensive for large genomes with many samples. Consider chromosome-by-chromosome analysis.
- **Model Assumptions**: Assumes single-pulse admixture model. Multiple admixture events may violate assumptions and produce biased estimates.
- **Ploidy Specification**: Must correctly specify ploidy for each sample. Wrong ploidy causes incorrect ancestry inference.
- **Phasing**: Unphased data may reduce accuracy for polyploid samples. Consider phasing if possible.

## Examples

### Basic local ancestry inference
**Args:** `ancestry_hmm -f input.pileup -p pop1.freqs pop2.freqs -o ancestry_output -n 2`
**Explanation:** Infers local ancestry from pileup data using two source population allele frequencies. Ploidy 2 (diploid). Outputs ancestry tracts and admixture time estimate.

### Tetraploid ancestry inference
**Args:** `ancestry_hmm -f input.pileup -p pop1.freqs pop2.freqs -o tetra_output -n 4`
**Explanation:** Ancestry inference for tetraploid sample (ploidy 4). Handles four allele copies per locus. Important for polyploid species like potato or wheat.

### Three-way admixture
**Args:** `ancestry_hmm -f input.pileup -p pop1.freqs pop2.freqs pop3.freqs -o three_way_output -n 2`
**Explanation:** Three-way admixture model with three source populations. Assigns each position to one of three ancestral sources. Useful for complex admixture scenarios.

### Specify admixture time prior
**Args:** `ancestry_hmm -f input.pileup -p pop1.freqs pop2.freqs -o output -n 2 -t 10`
**Explanation:** Sets admixture time prior to 10 generations. Useful when approximate admixture time is known from historical records. Improves convergence.

### Use VCF input format
**Args:** `ancestry_hmm -v input.vcf -p pop1.freqs pop2.freqs -o vcf_output -n 2`
**Explanation:** Uses VCF format input instead of pileup. Requires genotype likelihoods or called genotypes in VCF. Alternative to pileup-based input.

### Output per-position ancestry probabilities
**Args:** `ancestry_hmm -f input.pileup -p pop1.freqs pop2.freqs -o detailed_output -n 2 --posterior`
**Explanation:** Outputs posterior probabilities for each ancestry state at each position. Useful for assessing confidence in ancestry calls and identifying uncertain regions.