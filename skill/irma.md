---
name: irma
category: variant-calling
description: IRMA (Iterative Refinement Meta-Assembler) for robust assembly, variant calling, and phasing of highly variable RNA viruses.
tags: [irma, RNA virus, genome assembly, variant calling, phasing, influenza]
author: oxo-call-community
source_url: "https://wonder.cdc.gov/amd/flu/irma/"
---

## Concepts

- **Iterative Refinement**: IRMA (v1.2.0) uses iterative reference editing based on observed read data to assemble highly variable RNA viruses.
- **Multi-virus Support**: Modules available for influenza (FLU A/B/C/D), coronaviruses (CoV), RSV, and ebolaviruses.
- **Consensus Generation**: Produces plurality consensus sequences that represent the most frequent allele at each position.
- **Variant Phasing**: Performs phase assignment for mixed infections and minor variant detection.
- **Parallel Processing**: Supports both cluster computing (SGE) and single-node multi-core parallelization.
- **Amended Consensus**: Generates modified consensus sequences with base ambiguation for mixed alleles and quality filtering.

## Pitfalls

- **Module Selection**: Must specify correct organism module (FLU, CoV, RSV, EBOLA) for accurate results.
- **Reference Dependencies**: Performance depends on the quality and appropriateness of reference sequences.
- **Read Quality**: Requires high-quality sequencing reads; low-quality data may produce unreliable assemblies.
- **Memory Requirements**: Large datasets or complex genomes may require significant memory allocation.
- **Configuration Complexity**: Multiple configuration files (global, module-specific, run-specific) require careful setup.
- **Commercial Restrictions**: SAM and BLAT binaries have non-commercial use restrictions.

## Examples

### Basic influenza assembly
**Args:** `irma --module FLU --input /path/to/fastq/ --output /path/to/output/`
**Explanation:** Runs IRMA with the FLU module to assemble influenza sequences from FASTQ files.

### Coronavirus analysis
**Args:** `irma --module CoV --input /path/to/sars-cov2/ --output cov_results/`
**Explanation:** Processes SARS-CoV-2 sequencing data using the coronavirus module.

### With custom configuration
**Args:** `irma --module FLU --input /path/to/data/ --output results/ --external-config custom.sh`
**Explanation:** Uses an external configuration file to override default parameters.

### Parallel processing on single node
**Args:** `irma --module FLU --input /path/to/data/ --output results/ --local-procs 16`
**Explanation:** Runs IRMA using 16 CPU cores for parallel processing.

### Generate amended consensus
**Args:** `irma --module FLU --input /path/to/data/ --output results/ --amended-consensus`
**Explanation:** Generates additional amended consensus sequences with quality filtering and base ambiguation.

### Long-read assembly
**Args:** `irma --module FLU --input /path/to/longreads/ --output results/ --minimap2`
**Explanation:** Uses minimap2 instead of BLAT for long-read sequence alignment.