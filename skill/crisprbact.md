---
name: crisprbact
category: genome-editing
description: Design and analyze CRISPRi experiments for bacterial functional genomics
tags: [crisprbact, CRISPRi, bacteria, functional-genomics, gene-knockdown, sgRNA, essential-genes, screen-analysis]
author: oxo-call-community
source_url: "https://gitlab.pasteur.fr/dbikard/crisprbact"
---

## Concepts

- **Tool Overview**: crisprbact (v1.3.1) - A Python toolkit for designing and analyzing CRISPR interference (CRISPRi) experiments in bacteria.
- **Core Function**: Provides tools for designing sgRNA libraries targeting bacterial genomes, analyzing CRISPRi screen data to identify gene essentiality and genetic interactions, and predicting sgRNA efficiency.
- **Algorithm**: Implements rules-based sgRNA design for dCas9-based transcriptional repression in bacteria, integrates with screen analysis pipelines for depletion/enrichment profiling.
- **Input**: Bacterial genome sequence (FASTA), gene annotations (GFF), condition-specific sequencing data (FASTQ) from CRISPRi screens.
- **Output**: Designed sgRNA sequences, screen analysis results (gene scores, hit identification), visualization plots.
- **Application**: Bacterial essential gene mapping, genetic interaction screening, drug target identification, metabolic engineering, microbial community analysis.
- **Installation**: `pip install crisprbact` or `conda install -c bioconda crisprbact`

## Pitfalls

- **Species-specific Design**: sgRNA design rules are optimized for specific bacterial species - may not work well across all bacteria.
- ** PAM Requirements**: dCas9 from different species has different PAM requirements - ensure compatible PAM for your target organism.
- **Multiple dCas9 Versions**: Supports different dCas9 versions (S. pyogenes, S. aureus) - choose appropriate version for your experiment.
- **Library Complexity**: Large sgRNA libraries can be expensive and difficult to clone efficiently.
- **Screen Depth**: Requires sufficient sequencing depth to detect moderate depletion/enrichment signals.

## Examples

### Design sgRNAs for a genome
**Args:** `crisprbact design -g genome.fasta -a annotations.gff -o sgRNAs.csv`
**Explanation:** Design sgRNAs for all protein-coding genes in a bacterial genome.

### Design targeted sgRNA library
**Args:** `crisprbact design -g genome.fasta -a annotations.gff -t "geneA,geneB,geneC" -o targeted.csv`
**Explanation:** Design sgRNAs targeting only specific genes of interest.

### Analyze CRISPRi screen
**Args:** `crisprbact analyze -i counts.tsv -o analysis_results/`
**Explanation:** Analyze screen count data to identify essential genes or genetic interactions.

### Calculate gene scores
**Args:** `crisprbact score -i counts.tsv -o scores.csv --method rho`
**Explanation:** Calculate gene-level scores from sgRNA count data using specified method (rho, beta, etc.).

### Predict sgRNA efficiency
**Args:** `crisprbact predict -s ATGCGATCGATCGATCGA -o predictions.csv`
**Explanation:** Predict the knock-down efficiency of a specific sgRNA sequence.

### Generate library for cloning
**Args:** `crisprbact library -g genome.fasta -a annotations.gff -n 4 -o library.fa`
**Explanation:** Generate a sgRNA library with N sgRNAs per gene for cloning into CRISPRi vector.

### Visualize screen results
**Args:** `crisprbact plot -i scores.csv -o volcano.pdf --type volcano`
**Explanation:** Generate volcano plot or other visualizations of screen results.

### Essential gene analysis
**Args:** `crisprbact essential -i counts_initial.tsv counts_final.tsv -o essential_genes.csv`
**Explanation:** Identify essential genes by comparing initial and final sgRNA abundances after selection.

### Find genetic interactions
**Args:** `crisprbact interactions -s scores_condition1.csv -s scores_condition2.csv -o interactions.csv`
**Explanation:** Identify genetic interactions by comparing gene scores across different conditions.

### Export for downstream tools
**Args:** `crisprbact export -i analysis_results/ -f MAGECK -o mageck_input.csv`
**Explanation:** Export data in formats compatible with other screen analysis tools like MAGECK.
