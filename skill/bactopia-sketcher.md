---
name: bactopia-sketcher
category: utility
description: Bactopia Sketcher - Minmer sketching component for Bactopia pipeline
tags: [bactopia-sketcher, utility, minmer, sketching, sequence-comparison]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: Bactopia Sketcher is the minmer sketching component of the Bactopia pipeline, used for fast sequence comparison and clustering. Version 1.0.3.
- **Core Function**: Generates minmer sketches from sequence data for efficient similarity comparison.
- **Minmer Sketching**: Uses minimizer-based sketching to represent sequences in compact form.
- **Sequence Comparison**: Enables fast comparison of large sequence datasets.
- **Mash Integration**: Leverages Mash algorithm for approximate sequence matching.
- **Sketch Size**: Controls sketch size to balance between speed and accuracy.
- **Input/Output**: Accepts FASTA/FASTQ sequences, outputs sketch files for comparison.
- **Installation**: `conda install -c bioconda bactopia-sketcher`.

## Pitfalls

- **Version Compatibility**: Must match Bactopia pipeline version for proper integration.
- **Sketch Size**: Smaller sketches are faster but less accurate. Choose appropriate size.
- **Sequence Quality**: Poor quality sequences can produce unreliable sketches.
- **Memory Usage**: Large sketch databases require sufficient memory.

## Examples

### Generate sketch from assembly
**Args:** `bactopia-sketcher --input assembly.fasta --output sketch.msh`
**Explanation:** Creates minmer sketch from genome assembly.

### Compare two sketches
**Args:** `bactopia-sketcher --compare sketch1.msh sketch2.msh --output comparison.tsv`
**Explanation:** Compares two sketches and outputs similarity metrics.

### Custom sketch size
**Args:** `bactopia-sketcher --input reads.fastq --output sketch.msh --sketch-size 1000`
**Explanation:** Creates sketch with specified number of minmers.

### Sketch multiple sequences
**Args:** `bactopia-sketcher --input-dir assemblies/ --output sketches/`
**Explanation:** Generates sketches for all sequences in directory.

### Compute distance matrix
**Args:** `bactopia-sketcher --distance-matrix sketches/ --output distance_matrix.tsv`
**Explanation:** Computes pairwise distances between all sketches.

### Specify k-mer size
**Args:** `bactopia-sketcher --input sequence.fasta --output sketch.msh --kmer-size 21`
**Explanation:** Uses custom k-mer size for sketch generation.

### Display help
**Args:** `bactopia-sketcher --help`
**Explanation:** Shows all available command-line options and usage information.