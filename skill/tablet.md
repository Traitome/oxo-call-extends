---
name: tablet
category: visualization
description: Lightweight graphical viewer for next generation sequence assemblies and alignments.
tags: [tablet, visualization, sequence-viewer, alignment]
author: oxo-call-community
source_url: "https://ics.hutton.ac.uk/tablet"
---

## Concepts

- **Tool Overview**: tablet (v1.17.08.17) is a lightweight sequence assembly viewer.
- **Core Function**: Visualizes sequence assemblies and alignments.
- **Algorithm**: Efficiently renders large sequence data with zoom capabilities.
- **Input/Output**: Input: BAM, SAM, FASTA; Output: Visualization.
- **Applications**: Sequence assembly validation, alignment inspection.
- **Installation**: `conda install -c bioconda tablet` or download from website.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Performance**: Very large alignments may be slow to render.
- **Display Requirements**: Requires graphical environment.
- **File Format**: Supports limited set of input formats.
- **Zoom Level**: May be slow at very high zoom levels.
- **Export Options**: Limited export formats.

## Examples

### Display help
**Args:** `tablet --help`
**Explanation:** Shows available options and usage information.

### Basic visualization
**Args:** `tablet -i assembly.fasta -a alignments.sam`
**Explanation:** Open sequence assembly and alignments.

### Open BAM file
**Args:** `tablet -b reads.bam -r reference.fasta`
**Explanation:** View BAM alignments against reference.

### Verbose mode
**Args:** `tablet -i assembly.fasta -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tablet -i assembly.fasta --stats`
**Explanation:** Generate statistics about assembly.

### Batch processing
**Args:** `tablet -i assembly.fasta -a alignments.sam -o report.pdf`
**Explanation:** Generate PDF report of assembly.

### Filter by quality
**Args:** `tablet -b reads.bam -r reference.fasta -q 20`
**Explanation:** Filter reads by quality score.

### Include annotations
**Args:** `tablet -i assembly.fasta -g genes.gff`
**Explanation:** Display gene annotations.

### Generate report
**Args:** `tablet -i assembly.fasta -a alignments.sam --report`
**Explanation:** Generate comprehensive assembly report.
