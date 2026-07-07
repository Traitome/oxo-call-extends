---
name: domainator
category: annotation
description: Domainator - Domain-based gene neighborhood and protein analysis suite.
tags: [domainator, annotation, protein-domains, gene-neighborhood, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/nebiolabs/domainator"
---

## Concepts

- **Tool Overview**: Domainator is a flexible suite for analyzing protein domains and gene neighborhoods.
- **Core Function**: Identifies and analyzes protein domains, domain architectures, and gene neighborhood patterns.
- **Input/Output**: Input: Protein sequences (FASTA), genome annotations (GFF). Output: Domain annotations, neighborhood analysis.
- **Algorithm**: Uses profile HMMs and sequence comparison for domain identification.
- **Key Features**: Domain prediction, gene neighborhood analysis, architecture comparison, visualization support.
- **Installation**: `conda install -c bioconda domainator`

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence and annotation files.
- **Database Dependencies**: Relies on domain databases (Pfam, InterPro) for predictions.
- **Sequence Quality**: Poor quality sequences affect domain prediction accuracy.
- **Memory Usage**: Analyzing many sequences simultaneously requires significant RAM.
- **Computation Time**: Comprehensive analysis can be time-consuming.
- **Output Size**: Detailed output can be large for genome-scale analysis.

## Examples

### Analyze protein domains
**Args:** `domainator --input proteins.fa --output domains.tsv`
**Explanation:** Identifies protein domains in input sequences.

### With custom database
**Args:** `domainator --input proteins.fa --output domains.tsv --database custom.hmm`
**Explanation:** Uses a custom HMM database for domain prediction.

### Gene neighborhood analysis
**Args:** `domainator --input genome.gff --output neighborhoods.tsv --neighborhood`
**Explanation:** Analyzes gene neighborhoods and domain co-occurrence.

### Architecture comparison
**Args:** `domainator --input proteins.fa --output comparison.tsv --compare`
**Explanation:** Compares domain architectures across proteins.

### Include visualization
**Args:** `domainator --input proteins.fa --output domains.tsv --plot domains.png`
**Explanation:** Generates visualization of domain architectures.

### Batch processing
**Args:** `domainator --input-dir fasta_files/ --output-dir results/`
**Explanation:** Processes multiple sequence files in batch mode.