---
name: mauve
category: alignment
description: System for constructing multiple genome alignments in the presence of large-scale evolutionary events.
tags: [mauve, genome-alignment, comparative-genomics]
author: oxo-call-community
source_url: "http://darlinglab.org/mauve/"
---

## Concepts

- **Tool Overview**: Mauve is a comprehensive system for multiple genome alignment.
- **Core Function**: Constructs alignments accounting for rearrangements, inversions, and translocations.
- **Visualization**: Provides interactive visualization of genome alignments.
- **Synteny Detection**: Identifies conserved syntenic blocks between genomes.
- **Input/Output**: Accepts FASTA files, produces alignment and visualization outputs.
- **Installation**: `conda install -c bioconda mauve`

## Pitfalls

- **Memory Requirements**: High memory usage for large genome sets.
- **Computation Time**: Slow for large datasets or many genomes.
- **Java Dependencies**: Requires Java Runtime Environment.
- **GUI Limitations**: GUI may not handle very large datasets.
- **Reference Selection**: Reference genome choice affects alignment quality.
- **Output Interpretation**: Requires understanding of syntenic blocks.

## Examples

### Launch GUI
**Args:** `mauve`
**Explanation:** Starts the Mauve graphical interface.

### Align genomes via command line
**Args:** `mauve --align genomes.txt --output alignment.xmfa`
**Explanation:** Aligns genomes listed in genomes.txt file.

### Progressive alignment
**Args:** `mauve --progressive --output alignment.xmfa *.fasta`
**Explanation:** Performs progressive multiple alignment.

### Export visualization
**Args:** `mauve --align genomes.txt --image alignment.png`
**Explanation:** Generates alignment visualization image.

### Create backbone
**Args:** `mauve --backbone ref.fasta --output backbone.txt`
**Explanation:** Creates backbone from reference genome.

### Help documentation
**Args:** `mauve --help`
**Explanation:** Displays available commands and options.
