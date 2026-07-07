---
name: idba_subasm
category: assembly
description: Fork of IDBA with modifications to perform subassembly for the read cloud metagenomic assembler Athena
tags: [idba_subasm, assembly, metagenomics, read cloud]
author: oxo-call-community
source_url: "https://github.com/abishara/idba"
---

## Concepts

- **Subassembly Strategy**: Specialized fork of IDBA optimized for read cloud sequencing data in metagenomic assembly.
- **Athena Integration**: Designed to work as part of the Athena metagenomic assembler pipeline for read cloud data.
- **De Bruijn Graph Modifications**: Modified graph construction algorithms to handle the unique characteristics of read cloud data.
- **Partitioned Assembly**: Enables subassembly of complex metagenomic communities by partitioning reads into smaller subsets.
- **Hybrid Assembly Support**: Can integrate short and long reads for improved metagenomic assembly.

## Pitfalls

- **Specialized Use Case**: Optimized for read cloud data; may not perform optimally on standard sequencing data.
- **Dependency on Athena**: Best used within the Athena pipeline context; standalone usage may require additional configuration.
- **Limited Documentation**: As a specialized fork, documentation may be less comprehensive than the original IDBA.
- **Version Compatibility**: May have compatibility issues with certain input formats or downstream tools.
- **Resource Requirements**: Metagenomic assembly can be computationally intensive, requiring significant memory and CPU resources.

## Examples

### Basic subassembly run
**Args:** `idba_subasm -r reads.fa -o output_dir`
**Explanation:** Performs subassembly on read cloud sequencing data for metagenomic analysis.

### With paired-end reads
**Args:** `idba_subasm -r short_reads.fa --read_level_2 pe_reads.fa -o output_dir`
**Explanation:** Incorporates paired-end reads at level 2 for improved scaffolding in subassembly.

### Custom k-mer parameters
**Args:** `idba_subasm -r reads.fa -o output_dir --mink 25 --maxk 75 --step 5`
**Explanation:** Customizes k-mer range from 25 to 75 with 5-step increments for metagenomic data.

### Multiple read levels
**Args:** `idba_subasm -r level1.fa --read_level_2 level2.fa --read_level_3 level3.fa -o output_dir`
**Explanation:** Processes reads at multiple levels for hierarchical assembly strategy.

### With long read integration
**Args:** `idba_subasm -r short_reads.fa -l long_reads.fa -o output_dir`
**Explanation:** Combines short and long reads for hybrid metagenomic subassembly.