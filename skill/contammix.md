---
name: contammix
category: assembly
description: Estimate mtDNA contamination from potential contaminant genomes
tags: [contammix, contamination, mtdna, assembly, quality-control]
author: oxo-call-community
source_url: "https://github.com/plfjohnson/contamMix"
---

## Concepts

- **Tool Overview**: ContamMix is a tool for estimating mitochondrial DNA (mtDNA) contamination from a set of potential contaminant genomes, commonly used in ancient DNA and modern mtDNA studies.
- **Core Function**: Quantifies contamination levels by comparing sample mtDNA sequences against a database of potential contaminant sequences.
- **Algorithm**: Uses Bayesian statistical methods to estimate contamination proportions from sequence alignments.
- **Input**: Aligned mtDNA reads in BAM format, contaminant reference sequences.
- **Output**: Contamination estimates with confidence intervals.
- **Application**: Ancient DNA quality control, mtDNA sequencing validation, and contamination assessment.
- **Installation**: Install via bioconda: `conda install -c bioconda contammix`

## Pitfalls

- **Reference Panel**: Contamination estimates depend on contaminant reference panel completeness.
- **Coverage Requirements**: Requires sufficient mtDNA coverage for accurate estimates.
- **Endogenous Damage**: Ancient DNA damage patterns may affect contamination estimation.
- **Population Specificity**: Contaminant panel should match potential contamination sources.
- **Threshold Interpretation**: Low contamination levels may be difficult to distinguish from noise.

## Examples

### Estimate mtDNA contamination
**Args:** `contammix -i sample.bam -r contaminant_refs.fasta -o contamination_estimate.txt`
**Explanation:** Estimates mtDNA contamination from aligned reads.

### With posterior sampling
**Args:** `contammix -i sample.bam -r contaminant_refs.fasta -n 10000 -o contamination_estimate.txt`
**Explanation:** Uses 10,000 posterior samples for estimation.

### With prior specification
**Args:** `contammix -i sample.bam -r contaminant_refs.fasta --prior 0.01 -o contamination_estimate.txt`
**Explanation:** Sets prior contamination rate to 1%.

### Display help
**Args:** `contammix --help`
**Explanation:** Shows all available options and usage information.