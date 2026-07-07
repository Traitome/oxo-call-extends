---
name: metawatt
category: alignment
description: MetaWatt is a metagenomic binning tool
tags: [metawatt, alignment, sequence, binning]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/metawatt/"
---

## Concepts

- **Tool Overview**: MetaWatt v3.5.3 is a graphical metagenomic binning tool that uses multivariate statistics of tetranucleotide frequencies and differential coverage for binning.
- **Core Function**: Bins metagenomic sequences into genome bins using multiple approaches.
- **Tetranucleotide Frequency**: Uses tetranucleotide frequency analysis for binning.
- **Differential Coverage**: Incorporates coverage information for improved binning.
- **Taxonomic Assessment**: Provides taxonomic assessment of binning quality via Diamond BLASTx.
- **Visual Interface**: Features a Java SWING graphical interface for interactive binning.

## Pitfalls

- **Java Dependency**: Requires Java environment for the graphical interface.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Visualization Complexity**: Complex datasets may produce cluttered visualizations.
- **Parameter Tuning**: May require parameter adjustment for optimal binning.
- **Taxonomic Database**: Classification depends on reference database completeness.

## Examples

### Run MetaWatt GUI
**Args:** `metawatt`
**Explanation:** Launches the MetaWatt graphical interface.

### Batch binning mode
**Args:** `metawatt -i contigs.fasta -o bins/`
**Explanation:** Runs batch binning without GUI.

### With coverage information
**Args:** `metawatt -i contigs.fasta -c coverage.txt -o bins/`
**Explanation:** Uses coverage information for binning.

### Taxonomic assessment
**Args:** `metawatt -i contigs.fasta -o bins/ -t`
**Explanation:** Performs taxonomic assessment of bins.

### Export bins as FASTA
**Args:** `metawatt -i contigs.fasta -o bins/ -f fasta`
**Explanation:** Exports bins in FASTA format.