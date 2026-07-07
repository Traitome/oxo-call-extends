---
name: grafimo
category: bioinformatics
description: GRAFIMO (GRAph-based Finding of Individual Motif Occurrences) identifies transcription factor binding sites using a graph-based approach.
tags: [grafimo, motif-finding, transcription-factors, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pinellolab/GRAFIMO"
---

## Concepts

- **Motif Finding**: GRAFIMO identifies individual motif occurrences in genomic sequences using a graph-based approach.

- **Graph Representation**: Represents genomic sequences and motifs as graphs for efficient pattern matching.

- **Position Weight Matrix**: Uses position weight matrices (PWMs) to represent transcription factor binding motifs.

- **Multiple Testing Correction**: Implements various methods for correcting multiple testing in motif discovery.

- **Visualization**: Generates visualizations of motif occurrences and their genomic context.

- **Annotation Integration**: Integrates with genomic annotation databases for functional analysis.

## Pitfalls

- **Motif Database**: Results depend on the quality and completeness of the motif database used.

- **Threshold Selection**: Choosing appropriate significance thresholds is critical. Too strict may miss true sites.

- **Sequence Quality**: Low-quality sequence data can produce false positives.

- **Computational Resources**: Processing large genomes may require significant memory and time.

- **Motif Specificity**: Some motifs may be too generic, leading to many false positives.

## Examples

### Basic motif scanning
**Args:** `grafimo scan -m motifs.pwm -f genome.fasta -o results.txt`
**Explanation:** Scans genome sequence for motif occurrences using position weight matrices.

### Specify significance threshold
**Args:** `grafimo scan -m motifs.pwm -f genome.fasta -t 0.001 -o results.txt`
**Explanation:** Sets a strict significance threshold for motif detection.

### Include genomic annotations
**Args:** `grafimo scan -m motifs.pwm -f genome.fasta -a annotations.gtf -o results.txt`
**Explanation:** Integrates genomic annotations with motif results.

### Generate visualization
**Args:** `grafimo plot -i results.txt -o motif_plot.png`
**Explanation:** Creates a visualization of motif occurrences.

### Batch motif scanning
**Args:** `grafimo batch -m motifs/ -f genome.fasta -o results/`
**Explanation:** Processes multiple motif files in a directory.

### Filter by motif name
**Args:** `grafimo scan -m motifs.pwm -f genome.fasta -n "CTCF" -o results.txt`
**Explanation:** Only scans for specific named motifs.

### Output in BED format
**Args:** `grafimo scan -m motifs.pwm -f genome.fasta -f bed -o results.bed`
**Explanation:** Outputs results in BED format for genome browser visualization.