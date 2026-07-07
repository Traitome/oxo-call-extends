---
name: mugsy
category: alignment
description: Mugsy is a multiple whole genome aligner.
tags: [mugsy, alignment, whole-genome, multiple-alignment, comparative-genomics]
author: oxo-call-community
source_url: "http://mugsy.sourceforge.net"
---

## Concepts

- **Tool Overview**: Mugsy v1.2.3 is a fast multiple whole genome aligner for closely related genomes.
- **Core Function**: Performs multiple genome alignment without requiring a reference sequence.
- **Algorithm**: Uses Nucmer for pairwise alignment, graph-based segmentation for collinear regions.
- **Input**: Accepts multi-FASTA files, one per genome; handles draft genomes with multiple contigs.
- **Output**: Produces multiple alignment in MAF (Multiple Alignment Format) format.
- **Performance**: Aligns 31 bacterial genomes in under 2 hours; handles rearrangements and duplications.

## Pitfalls

- **Evolutionary Distance**: Optimized for closely related genomes; performance degrades with distance.
- **Draft Quality**: Assumes reasonably complete assemblies; fragmented drafts affect alignment quality.
- **Memory Requirements**: Large genome sets require substantial memory.
- **Computational Time**: Full alignments of large eukaryotic genomes can be time-consuming.
- **No Reference**: Does not require reference but benefits from genome quality.
- **Parameter Tuning**: May require adjustment for optimal sensitivity on diverse datasets.

## Examples

### Basic multiple alignment
**Args:** `mugsy --directory genomes/ --output alignment.maf`
**Explanation:** Aligns all genomes in directory and outputs MAF format.

### Specify genomes individually
**Args:** `mugsy genome1.fna genome2.fna genome3.fna -o output.maf`
**Explanation:** Aligns specified genome files.

### Parallel execution
**Args:** `mugsy --directory genomes/ --output align.maf --cpu 8`
**Explanation:** Uses 8 CPU cores for faster alignment.

### Display help
**Args:** `mugsy --help`
**Explanation:** Shows usage and parameter options.

### Convert MAF to FASTA
**Args:** `maf2fasta alignment.maf -o aligned_sequences.fna`
**Explanation:** Converts MAF output to FASTA format for downstream analysis.
