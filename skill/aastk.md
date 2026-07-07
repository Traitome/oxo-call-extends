---
name: aastk
category: utility
description: Amino acid sequence toolkit for analyzing protein sequences from the GlobDB genome database.
tags: [aastk, utility, protein, amino-acid, sequence-analysis, globdb, pasr, cugo]
author: oxo-call-community
source_url: "https://github.com/dspeth/aastk/"
---

## Concepts

- **Tool Overview**: AASTK (Amino Acid Sequence Toolkit) is a suite of tools for constructing and analyzing protein sequence datasets from the GlobDB genomes. Version 0.1.1.
- **Core Function**: Provides utilities for amino acid sequence analysis, including Protein Alignment Score Ratio (PASR) analysis and Colocalized Unidirectional Gene Organization (CUGO) visualization.
- **GlobDB Integration**: Designed to leverage GlobDB, a comprehensive genomic resource of species-representative microbial genomes of Bacteria and Archaea.
- **SQL Database**: Uses a precomputed SQL database containing protein sequences, genomic context, functional annotations (KEGG, COG, PFAM), and genome metadata.
- **Installation**: Install via bioconda: `conda install -c bioconda aastk`
- **Platform Support**: Platform-independent (noarch), Python-based

## Pitfalls

- **Active Development**: AASTK is currently in active development and may not be ready for broad public use. API may change.
- **GlobDB Dependency**: Requires the GlobDB SQL database for full functionality. Download from https://globdb.org/downloads.
- **Input Format**: Ensure input sequences are in FASTA format and are amino acid sequences, not nucleotide.
- **Documentation**: Limited documentation available. Check `aastk --help` for each subcommand.

## Examples

### Display help information
**Args:** `aastk --help`
**Explanation:** Shows all available subcommands and their options.

### Run PASR analysis
**Args:** `aastk pasr --input proteins.fasta --output pasr_results/`
**Explanation:** Performs Protein Alignment Score Ratio (PASR) analysis on the input amino acid sequences. PASR helps identify functionally important residues.

### Run CUGO visualization
**Args:** `aastk cugo --input gene_coordinates.gff --output cugo_plot.png`
**Explanation:** Generates a Colocalized Unidirectional Gene Organization (CUGO) visualization showing gene orientation patterns in genomic regions.

### PASR analysis with custom parameters
**Args:** `aastk pasr --input proteins.fasta --min-identity 0.3 --max-evalue 1e-10 -o results/`
**Explanation:** Runs PASR analysis with custom sequence identity threshold (0.3) and e-value cutoff (1e-10).

### CUGO with multiple regions
**Args:** `aastk cugo --input regions.gff --window-size 10 --output cugo_analysis/`
**Explanation:** Analyzes multiple genomic regions with a sliding window size of 10 genes to identify co-localized gene organization patterns.