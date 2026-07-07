---
name: aodp
category: sequencing
description: Automated Oligonucleotide Design Pipeline - Cluster oligonucleotide signatures for rapid identification by sequencing
tags: [aodp, oligonucleotide, primer-design, metabarcoding, sequencing]
author: oxo-call-community
source_url: "https://github.com/peterk87/aodp"
---

## Concepts

- **Tool Overview**: AODP (Automated Oligonucleotide Design Pipeline) v2.5.0.2 - A tool for clustering oligonucleotide signatures for rapid identification by sequencing.
- **Core Function**: Design and optimize oligonucleotide primers for metabarcoding and sequence-based identification. Identifies conserved DNA markers and mutations distinguishing close relatives.
- **Key Features**:
  - Cluster oligonucleotide signatures from sequence alignments
  - Design species-specific primers and probes
  - Identify diagnostic SNPs and mutations between closely related taxa
  - Optimize primer sets for PCR amplification and sequencing
  - Generate signatures for rapid identification workflows
- **Applications**: 
  - Metabarcoding analysis
  - Phytopathogen detection and identification
  - Species discrimination in environmental samples
  - High-resolution microbial community profiling
- **Installation**: `conda install -c bioconda aodp`

## Pitfalls

- **Perl Dependencies**: Requires Perl and BioPerl modules
- **Reference Database Quality**: Results depend on the quality and completeness of input reference sequences
- **Computational Resources**: May require significant memory for large datasets
- **Alignment Requirements**: Input sequences must be properly aligned
- **Version Compatibility**: Options and output format may vary between versions

## Examples

### Basic primer design
**Args:** `aodp -i input.fasta -o output_prefix`
**Explanation:** Runs AODP on input FASTA file to design oligonucleotide signatures.

### With specific parameters
**Args:** `aodp -i aligned_sequences.fasta -o results -k 3 -m 100`
**Explanation:** Designs oligonucleotides with specific k-mer size (-k) and minimum score threshold (-m).

### Generate diagnostic markers
**Args:** `aodp -i ref_sequences.fasta -o diagnostic_markers -d -t species_list.txt`
**Explanation:** Identifies diagnostic SNPs and mutations distinguishing between species in the input list.

### Batch processing
**Args:** `aodp -i batch_input/ -o batch_output/ -b`
**Explanation:** Processes multiple FASTA files in batch mode from input directory.

### Help documentation
**Args:** `aodp --help`
**Explanation:** Shows available options and parameters.