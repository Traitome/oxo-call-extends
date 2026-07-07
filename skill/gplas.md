---
name: gplas
category: bioinformatics
description: gplas bins plasmid-predicted contigs based on sequence composition, coverage, and assembly graph information for accurate plasmid component identification.
tags: [gplas, plasmid, binning, metagenomics, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/sirarredondo/gplas"
---

## Concepts

- **Plasmid Binning**: gplas bins predicted plasmid contigs into discrete plasmid components using multiple features.

- **Sequence Composition**: Uses k-mer composition to identify plasmid-specific patterns.

- **Coverage Analysis**: Analyzes coverage patterns to distinguish plasmids from chromosomal DNA.

- **Assembly Graph Integration**: Incorporates assembly graph information to improve binning accuracy.

- **Multi-Omics Support**: Integrates information from multiple sequencing technologies for improved predictions.

- **Quality Assessment**: Provides metrics for assessing binning quality and confidence.

## Pitfalls

- **Plasmid Prediction**: Relies on accurate plasmid prediction from other tools. Poor predictions will affect binning.

- **Coverage Variation**: Highly variable coverage can complicate binning. Normalize coverage when possible.

- **Contig Length**: Short contigs may not contain enough information for accurate binning.

- **Reference Bias**: May have bias towards well-characterized plasmids in reference databases.

- **Computational Requirements**: Processing large datasets may require significant resources.

## Examples

### Basic plasmid binning
**Args:** `gplas -i contigs.fasta -c coverage.txt -g graph.gfa -o bins/`
**Explanation:** Bins plasmid contigs using sequence composition, coverage, and assembly graph.

### Specify plasmid predictions
**Args:** `gplas -i contigs.fasta -p plasmid_predictions.txt -o bins/`
**Explanation:** Uses precomputed plasmid predictions as input for binning.

### Adjust k-mer size
**Args:** `gplas -i contigs.fasta -k 21 -o bins/`
**Explanation:** Uses k-mer size 21 for sequence composition analysis.

### Generate report
**Args:** `gplas -i contigs.fasta -c coverage.txt -r -o report.html`
**Explanation:** Generates a comprehensive HTML report with binning statistics.

### Batch processing
**Args:** `gplas -d samples/ -o results/`
**Explanation:** Processes multiple samples in a directory and saves individual results.

### Filter by confidence
**Args:** `gplas -i contigs.fasta -c coverage.txt -t 0.8 -o bins/`
**Explanation:** Only includes bins with confidence scores above 0.8.

### Visualize bins
**Args:** `gplas -i contigs.fasta -c coverage.txt -v -o visualization.html`
**Explanation:** Generates an interactive visualization of plasmid bins.