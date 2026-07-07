---
name: colombo
category: annotation
description: Software framework for prediction of genomic islands in prokaryotes
tags: [colombo, genomic-islands, prokaryotes, annotation, bioinformatics]
author: oxo-call-community
source_url: "https://www.uni-goettingen.de/en/research/185810.html"
---

## Concepts

- **Tool Overview**: COLOMBO is a software framework with a graphical user interface (GUI) for predicting genomic islands (GIs) in prokaryotic genomes using multiple prediction algorithms.
- **Core Function**: Identifies genomic islands in prokaryotic genomes by integrating multiple prediction methods through a plugin architecture.
- **Algorithm**: Combines sequence composition-based methods (GC content, codon usage, k-mer frequencies) with comparative genomics approaches.
- **Input**: Prokaryotic genome sequences in FASTA format, optional annotation files.
- **Output**: Predicted genomic island coordinates and confidence scores.
- **Application**: Horizontal gene transfer detection, pathogenicity island identification, and genome evolution studies.
- **Installation**: Install via bioconda: `conda install -c bioconda colombo`

## Pitfalls

- **Plugin Configuration**: Requires proper plugin setup for prediction algorithms.
- **Genome Quality**: Depends on high-quality genome assembly and annotation.
- **Threshold Settings**: May require tuning of prediction thresholds.
- **GUI Dependencies**: GUI mode requires graphical environment.
- **Computational Resources**: Multiple prediction methods increase resource requirements.

## Examples

### Predict genomic islands
**Args:** `colombo -i genome.fasta -o predictions.gff`
**Explanation:** Predicts genomic islands in prokaryotic genome.

### With custom plugins
**Args:** `colombo -i genome.fasta -p islandpath,ginix -o predictions.gff`
**Explanation:** Uses specific prediction plugins for analysis.

### Batch mode (no GUI)
**Args:** `colombo -i genome.fasta -o predictions.gff --batch`
**Explanation:** Runs in batch mode without GUI for automated processing.

### Display help
**Args:** `colombo --help`
**Explanation:** Shows all available options and usage information.