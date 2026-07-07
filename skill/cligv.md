---
name: cligv
category: alignment
description: Command line Interactive Genome Viewer for terminal-based genome visualization
tags: [cligv, genome-viewer, terminal, bam, vcf, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jonasfreudig/cligv"
---

## Concepts

- **Tool Overview**: clIGV (command line Interactive Genome Viewer) is a fast, interactive genome browser for the terminal, enabling visualization of genomic sequences, variants, and alignments.
- **Core Function**: Provides terminal-based interactive visualization of genomic data including sequence, variants, and read alignments.
- **Features**: Real-time navigation, zooming, and interactive exploration of genomic regions.
- **Input**: BAM/SAM alignment files, VCF variant files, and FASTA reference sequences.
- **Output**: Terminal-based visual display of genomic data.
- **Application**: Genome browsing, variant inspection, and alignment visualization without GUI.
- **Installation**: Install via bioconda: `conda install -c bioconda cligv`

## Pitfalls

- **Terminal Limitations**: Requires terminal with proper color support.
- **Screen Size**: Limited by terminal window size.
- **Performance**: May be slow with very large BAM files.
- **Memory Usage**: May require significant memory for large datasets.
- **Navigation**: Keyboard-based navigation may have learning curve.

## Examples

### View genome region
**Args:** `cligv -r reference.fasta -c chr1:1000000-1001000`
**Explanation:** Displays genomic region chr1:1000000-1001000.

### View with BAM alignments
**Args:** `cligv -r reference.fasta -b alignments.bam -c chr1:1000000-1001000`
**Explanation:** Shows alignments from BAM file in specified region.

### View with variants
**Args:** `cligv -r reference.fasta -v variants.vcf -c chr1:1000000-1001000`
**Explanation:** Displays variants from VCF file.

### Full command
**Args:** `cligv -r reference.fasta -b alignments.bam -v variants.vcf -c chr1:1000000-1001000`
**Explanation:** Shows reference, alignments, and variants together.