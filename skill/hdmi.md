---
name: hdmi
category: bioinformatics
description: HDMI detects horizontal gene transfer (HGT) from metagenome-assembled genomes (MAGs) in individuals.
tags: [hdmi, HGT, metagenomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/HaoranPeng21/HDMI"
---

## Concepts

- **Horizontal Gene Transfer**: HDMI detects HGT events.

- **MAG Analysis**: Analyzes metagenome-assembled genomes.

- **Microbial Genomics**: Focused on microbial genome analysis.

- **Gene Flow**: Identifies gene flow between organisms.

- **Metagenomics**: Works with metagenomic data.

- **Evolutionary Analysis**: Supports evolutionary studies.

## Pitfalls

- **Assembly Quality**: Results depend on MAG quality.

- **Data Complexity**: Complex metagenomes may be challenging.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Detect HGT
**Args:** `hdmi --input mags.fasta --output hgt_results.txt`
**Explanation:** Detects HGT events from MAGs.

### With annotation
**Args:** `hdmi --input mags.fasta --annotation annotations.gff --output hgt_results.txt`
**Explanation:** Uses gene annotations for improved detection.

### Batch processing
**Args:** `for f in *.fasta; do hdmi --input $f --output ${f%.fasta}_hgt.txt; done`
**Explanation:** Processes multiple MAG files.

### Generate report
**Args:** `hdmi --input mags.fasta --report --output report.html`
**Explanation:** Generates comprehensive HGT analysis report.

### Visualization
**Args:** `hdmi --input mags.fasta --plot --output hgt_plot.pdf`
**Explanation:** Generates visualization of HGT results.

### Help command
**Args:** `hdmi --help`
**Explanation:** Shows available options and usage information.