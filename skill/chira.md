---
name: chira
category: rna-seq
description: Integrated framework for annotation and visualization of chimeric reads
tags: [chira, chimeric-reads, rna-fusion, annotation, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pavanvidem/chira/"
---

## Concepts

- **Tool Overview**: Chira provides an integrated framework for annotating and visualizing chimeric reads from RNA-seq data.
- **Core Function**: Identifies, annotates, and visualizes chimeric RNA reads that span across different genomic locations.
- **Features**: Chimeric read detection, fusion transcript identification, annotation with gene information, and visualization.
- **Input**: RNA-seq alignment files (BAM/SAM) with chimeric reads.
- **Output**: Annotated fusion events and visualization plots.
- **Application**: RNA fusion detection, cancer transcriptomics, and gene rearrangement analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda chira`

## Pitfalls

- **Alignment Quality**: Requires properly aligned reads with chimeric alignments marked.
- **False Positives**: May detect spurious fusions from sequencing errors.
- **Annotation Dependencies**: Requires gene annotation files for proper annotation.
- **Visualization Resources**: May require significant resources for large datasets.
- **Filtering**: Appropriate filtering is needed to remove low-confidence fusions.

## Examples

### Annotate chimeric reads
**Args:** `chira annotate -i alignments.bam -g genes.gtf -o fusions.txt`
**Explanation:** Annotates chimeric reads with gene information.

### Visualize fusions
**Args:** `chira visualize -i fusions.txt -o plots/`
**Explanation:** Generates visualization plots for fusion events.

### Filter fusions
**Args:** `chira filter -i fusions.txt -q 30 -o filtered.txt`
**Explanation:** Filters fusions by quality score.

### Display help
**Args:** `chira --help`
**Explanation:** Shows all available options and usage information.