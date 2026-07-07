---
name: artemis
category: annotation
description: Artemis - Java genome visualization suite including genome browser, ACT, DNA Plotter, and BamView
tags: [artemis, annotation, visualization, genome-browser, bam-viewer, act]
author: oxo-call-community
source_url: "http://sanger-pathogens.github.io/Artemis/"
---

## Concepts

- **Tool Overview**: Artemis is a comprehensive Java-based genome visualization suite including the Artemis genome browser, ACT (Artemis Comparison Tool), DNA Plotter, and BamView. Version 18.2.0.
- **Artemis Browser**: Interactive genome browser for viewing and annotating genomic sequences with features, ORFs, and annotations.
- **ACT (Artemis Comparison Tool)**: Visualizes pairwise or multiple genome alignments for comparative genomics and synteny analysis.
- **DNA Plotter**: Generates publication-quality circular or linear genome plots with customizable features and annotations.
- **BamView**: Viewer for BAM/CRAM alignment files with read pileup visualization and variant inspection.
- **Java-Based**: Cross-platform Java application running on Windows, Mac, and Linux systems.
- **Input/Output**: Supports FASTA, GFF/GFF3, EMBL, GenBank, BAM, CRAM formats.
- **Installation**: `conda install -c bioconda artemis` or download from Sanger Pathogens website.

## Pitfalls

- **Java Version**: Requires Java 8 or higher. Incompatible with older Java versions.
- **Memory Requirements**: Large genomes require increased Java heap memory. Use -Xmx flag to allocate more memory.
- **File Formats**: Some annotation formats may require conversion. Check format compatibility.
- **Performance**: Visualizing large BAM files may be slow. Consider downsampling or using specialized viewers.
- **GUI Dependency**: Primarily GUI-based tools. Limited command-line automation options.

## Examples

### Launch Artemis genome browser
**Args:** `artemis genome.fasta`
**Explanation:** Opens Artemis genome browser with specified genome sequence. Interactive GUI for viewing and editing annotations.

### Load annotations
**Args:** `artemis genome.fasta annotations.gff`
**Explanation:** Opens Artemis with genome and GFF annotations. Displays features, genes, and other annotations on genome.

### Launch ACT for comparison
**Args:** `act genome1.fasta genome2.fasta comparison.txt`
**Explanation:** Opens ACT (Artemis Comparison Tool) for pairwise genome comparison. Visualizes alignments and synteny.

### Generate circular genome plot
**Args:** `dnaplotter -i genome.fasta -a annotations.gff -o genome_plot.png -format circular`
**Explanation:** Creates circular genome plot with annotations. Suitable for publication figures.

### View BAM file with BamView
**Args:** `bamview aligned.bam reference.fasta`
**Explanation:** Opens BamView to visualize read alignments. Shows pileup, coverage, and variants.

### Custom plot with multiple tracks
**Args:** `dnaplotter -i genome.fasta -a annotations.gff -f features.txt -o custom_plot.png`
**Explanation:** Generates custom plot with additional feature tracks specified in file.

### Export annotation as EMBL
**Args:** `artemis genome.fasta annotations.gff -o output.embl`
**Explanation:** Converts GFF annotations to EMBL format for submission or compatibility.