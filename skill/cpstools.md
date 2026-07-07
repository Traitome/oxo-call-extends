---
name: cpstools
category: utility
description: Python package for analyzing chloroplast genome sequences - gene annotation, IR boundaries, SSR, Pi, and codon usage analysis
tags: [cpstools, chloroplast, genome-analysis, plant, ssr, polymorphism, codon-usage, ir-boundary]
author: oxo-call-community
source_url: "https://github.com/Xwb7533/CPStools"
---

## Concepts

- **Tool Overview**: CPStools is a Python package for comprehensive chloroplast genome sequence analysis, providing multiple analysis modules for plant genomics research.
- **Core Function**: Analyzes chloroplast genome sequences for gene annotation checking, IR boundary detection, nucleotide diversity (Pi), simple sequence repeats (SSR), codon usage (RSCU), and collinearity analysis.
- **Algorithm**: Processes GenBank/FASTA formatted chloroplast genomes using Biopython for sequence handling and pandas for statistical analysis.
- **Input**: chloroplast genome sequences in GenBank (.gb) or FASTA format.
- **Output**: Analysis results including gene statistics, IR regions, SSR locations, Pi values, RSCU values, and collinearity plots.
- **Application**: Plant phylogenomics, chloroplast genome evolution, population genetics, plant species identification, DNA barcoding.
- **Installation**: `pip install cpstools` or `conda install -c bioconda cpstools` (requires Python >= 3.9)

## Pitfalls

- **Python Version**: Requires Python >= 3.9 (does not support Python 4.x)
- **File Format**: GenBank files must end with `.gb` extension for proper parsing
- **IR Detection**: IR regions must exceed 1,000 bp to be identified
- **Biopython Dependency**: Strongly required for sequence parsing and GenBank handling
- **MAFFT for Pi**: Multiple sequence alignment using MAFFT may be needed for Pi calculations

## Examples

### Display help
**Args:** `cpstools -h`
**Explanation:** Shows all available subcommands and their descriptions.

### Check GenBank annotation
**Args:** `cpstools gbcheck -i input_file.gb`
**Explanation:** Self-check mode verifies gene annotation quality, checking start/stop codons and product labels.

### Compare two GenBank files
**Args:** `cpstools gbcheck -i test_file.gb -r ref_file.gb`
**Explanation:** Compares gene counts and differences between two chloroplast genome annotations.

### Get genome statistics
**Args:** `cpstools info -i chloroplast.gb`
**Explanation:** Generates statistics on gene types and gene numbers in the chloroplast genome.

### Find IR boundaries
**Args:** `cpstools IR -i chloroplast.gb`
**Explanation:** Identifies the four regions (LSC, SSC, IRa, IRb) in chloroplast sequences. IR regions must be >1,000 bp.

### Adjust sequence to LSC start
**Args:** `cpstools Seq -d work_dir -f info.txt -m LSC`
**Explanation:** Adjusts all sequences to start at the 1st bp of LSC region. Results saved in LSC directory.

### Adjust SSC forward
**Args:** `cpstools Seq -d work_dir -f info.txt -m SSC`
**Explanation:** Adjusts SSC region to forward orientation. Results saved in SSC directory.

### Adjust to reverse complement
**Args:** `cpstools Seq -d work_dir -f info.txt -m RP`
**Explanation:** Adjusts sequences to reverse complement and LSC 1bp start. Results saved in RP directory.

### Nucleotide diversity (Pi) analysis
**Args:** `cpstools Pi -d work_dir`
**Explanation:** Extracts shared gene regions and calculates nucleotide diversity across multiple chloroplast genomes.

### SSR detection
**Args:** `cpstools SSR -i chloroplast.fasta`
**Explanation:** Identifies and locates simple sequence repeats (microsatellites) in chloroplast genome.

### Codon usage (RSCU) analysis
**Args:** `cpstools RSCU -d work_dir`
**Explanation:** Analyzes codon usage bias using RSCU (Relative Synonymous Codon Usage) method.
