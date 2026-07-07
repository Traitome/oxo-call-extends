---
name: megagta
category: assembly
description: HMM-guided metagenomic gene-targeted assembler using iterative de Bruijn graphs.
tags: [megagta, metagenomics, gene-assembly]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/megagta"
---

## Concepts

- **Tool Overview**: MegaGTA assembles target genes from metagenomic data.
- **Core Function**: HMM-guided iterative de Bruijn graph assembly.
- **HMM Guidance**: Uses profile HMMs for gene targeting.
- **Iterative Assembly**: Iteratively builds and refines assemblies.
- **Metagenomic Focus**: Optimized for complex microbial communities.
- **Installation**: `conda install -c bioconda megagta`

## Pitfalls

- **HMM Quality**: Depends on high-quality HMM profiles.
- **Computation Time**: Slow for large metagenomic datasets.
- **Memory Requirements**: High memory for complex graphs.
- **Parameter Tuning**: Requires careful HMM and graph parameters.
- **Gene Abundance**: May miss low-abundance genes.
- **Contamination**: May assemble non-target sequences.

## Examples

### Assemble target genes
**Args:** `megagta -i reads.fastq -h hmm_profiles.hmm -o output/`
**Explanation:** Assembles genes using HMM profiles.

### With multiple HMMs
**Args:** `megagta -i reads.fastq -h gene1.hmm gene2.hmm -o output/`
**Explanation:** Targets multiple gene families.

### Iterative refinement
**Args:** `megagta -i reads.fastq -h hmm.hmm -n 3 -o output/`
**Explanation:** Runs 3 iterations of assembly.

### Verbose mode
**Args:** `megagta -i reads.fastq -h hmm.hmm -v -o output/`
**Explanation:** Shows detailed assembly progress.

### Help documentation
**Args:** `megagta --help`
**Explanation:** Displays available options.
