---
name: ancestry_hmm-s
category: population-genomics
description: Ancestry_HMM-S - Inferring adaptive introgression from genomic data using hidden Markov models
tags: [adaptive-introgression, selection, hmm, population-genetics, introgression]
author: oxo-call-community
source_url: "https://github.com/jesvedberg/Ancestry_HMM-S"
---

## Concepts

- **Tool Overview**: Ancestry_HMM-S is a hidden Markov model-based method for identifying genes undergoing adaptive introgression and quantifying the strength of selection acting on them. Version 0.9.0.2.
- **Core Function**: Identifies loci that have increased in frequency due to selection and quantifies the strength of selection. Specifically designed to detect adaptive introgression from population genomic data.
- **Adaptive Introgression**: The flow of adaptive genetic variation between species or populations, implicated in adaptation from pesticide resistance and immunity to local adaptation.
- **HMM-Based Approach**: Uses hidden Markov models to simultaneously infer ancestry and detect signatures of positive selection on introgressed regions.
- **Selection Quantification**: Quantifies the strength of selection acting on introgressed loci, providing insights into adaptive evolution.
- **Population Genomics**: Applied to admixed populations to identify beneficial genetic variants acquired through introgression.
- **Installation**: Available via Bioconda (`conda install -c bioconda ancestry_hmm-s`).

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for genomic data. Requires properly formatted VCF or genotype files.
- **Population Structure**: Requires admixed population data with clear source populations.
- **Reference Data**: Needs appropriate reference populations for ancestry inference.
- **Computational Requirements**: HMM inference can be computationally intensive for large datasets.
- **Model Assumptions**: Assumes specific demographic and selection models; violations may affect accuracy.

## Examples

### Display help
**Args:** `ancestry_hmm-s --help`
**Explanation:** Shows available options and usage information.

### Basic adaptive introgression detection
**Args:** `ancestry_hmm-s -i input.vcf -p pop1.vcf pop2.vcf -o results/`
**Explanation:** Detects adaptive introgression using VCF input and two source population VCFs. Outputs results to specified directory.

### Quantify selection strength
**Args:** `ancestry_hmm-s -i genotypes.vcf -p ref1.vcf ref2.vcf -o output/ --selection`
**Explanation:** Identifies introgressed loci and quantifies selection strength. Provides selection coefficient estimates.

### Use genotype likelihoods
**Args:** `ancestry_hmm-s -l likelihoods.txt -p pop1.freqs pop2.freqs -o results/`
**Explanation:** Uses genotype likelihoods input instead of called genotypes. Useful for low-coverage sequencing data.

### Specify recombination rate
**Args:** `ancestry_hmm-s -i input.vcf -p pop1.vcf pop2.vcf -o output/ -r recombination_map.txt`
**Explanation:** Provides custom recombination rate map for improved HMM accuracy. Important for accurate ancestry tract inference.

### Output detailed statistics
**Args:** `ancestry_hmm-s -i input.vcf -p pop1.vcf pop2.vcf -o output/ --verbose`
**Explanation:** Generates detailed output including posterior probabilities and selection coefficients for each locus.

### Filter by significance
**Args:** `ancestry_hmm-s -i input.vcf -p pop1.vcf pop2.vcf -o output/ --threshold 0.05`
**Explanation:** Filters results by significance threshold, only reporting loci with strong evidence of adaptive introgression.

### Batch processing
**Args:** `ancestry_hmm-s -i batch_input/ -p pop1.vcf pop2.vcf -o batch_output/`
**Explanation:** Processes multiple VCF files in batch mode from input directory.