---
name: metator
category: metagenomics
description: Metagenomic binning based on Hi-C data.
tags: [metator, metagenomics, Hi-C, binning]
author: oxo-call-community
source_url: "https://github.com/koszullab/metator"
---

## Concepts

- **Tool Overview**: MetaTOR v1.3.10 is a metagenomic binning tool that utilizes Hi-C contact data to separate metagenomic sequences into individual genome bins.
- **Core Function**: Bins metagenomic sequences into genomes using Hi-C interaction information.
- **Hi-C Integration**: Leverages Hi-C data to determine which contigs belong to the same organism.
- **Proximity-based Binning**: Uses 3D genome organization to group contigs from the same genome.
- **Input/Output**: Accepts assembled contigs and Hi-C reads; outputs genome bins in FASTA format.
- **Multi-step Process**: Includes mapping, clustering, and bin refinement steps.

## Pitfalls

- **Hi-C Data Quality**: Binning accuracy depends on Hi-C data quality and coverage.
- **Contig Length**: Short contigs may be difficult to bin accurately.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal binning results.
- **Complex Communities**: May struggle with highly complex microbial communities.

## Examples

### Run Hi-C based binning
**Args:** `metator bin -i contigs.fasta -c hic_reads.fastq -o bins/`
**Explanation:** Performs metagenomic binning using Hi-C data.

### With existing alignment
**Args:** `metator bin -i contigs.fasta -b hic.bam -o bins/`
**Explanation:** Uses pre-computed Hi-C alignments for binning.

### Refine bins
**Args:** `metator refine -i bins/ -o refined_bins/`
**Explanation:** Refines existing genome bins.

### Visualize binning
**Args:** `metator plot -i bins/ -o visualization.png`
**Explanation:** Generates visualization of binning results.

### Batch processing
**Args:** `metator bin -i contigs/ -c hic/ -o bins/`
**Explanation:** Processes multiple samples in batch mode.