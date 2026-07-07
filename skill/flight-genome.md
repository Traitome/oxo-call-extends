---
name: flight-genome
category: programming
description: "Flight is the Python component of the Rosella and Lorikeet bioinformatics pipelines for genome assembly and analysis."
tags: [flight-genome, programming, genome-assembly, bioinformatics, python, pipeline, sequencing]
author: oxo-call-community
source_url: "https://github.com/rhysnewell/flight"
---

## Concepts
- **Tool Overview**: Flight is a Python library providing core utilities for genome assembly and analysis pipelines, used by Rosella and Lorikeet assemblers.
- **Core Function**: Provides shared components for sequence processing, assembly graph manipulation, and contig scaffolding in genome assembly pipelines.
- **Input/Output**: Input: FASTA sequences, assembly graphs, sequencing reads. Output: Processed sequences, assembly graphs, scaffolded contigs.
- **Sequence Processing**: Implements sequence cleaning, error correction, and quality filtering utilities.
- **Graph Manipulation**: Provides tools for working with assembly graphs (de Bruijn graphs, overlap graphs).
- **Scaffolding**: Includes utilities for ordering and orienting contigs into scaffolds using mate-pair information.
- **Installation**: `conda install -c bioconda flight-genome` or `pip install flight-genome`. Requires Python 3.x.

## Pitfalls
- **Memory Usage**: Processing large genomes requires significant memory. Use appropriate chunking for large datasets.
- **Graph Complexity**: Complex assembly graphs may require manual intervention. Simplify graphs before processing.
- **Read Quality**: Poor quality reads affect assembly accuracy. Quality filter before assembly.
- **Contig Size**: Very short contigs may not be suitable for scaffolding. Filter small contigs.
- **Mate-Pair Orientation**: Incorrect mate-pair orientation affects scaffolding. Verify library orientation.
- **Reference Dependence**: Some modules require reference genomes. Ensure references are available.

## Examples
### Clean sequencing reads
**Args:** `flight clean --input reads.fastq --output cleaned.fastq --quality 20`
**Explanation:** Filters reads by quality score (Q20) and removes low-quality sequences.

### Process assembly graph
**Args:** `flight graph --input assembly.gfa --output processed.gfa --simplify`
**Explanation:** Simplifies assembly graph by removing redundant edges and nodes.

### Scaffold contigs
**Args:** `flight scaffold --contigs contigs.fasta --mates mate_pairs.bam --output scaffolds.fasta`
**Explanation:** Scaffolds contigs using mate-pair information from BAM file.

### Error correction
**Args:** `flight correct --input reads.fastq --output corrected.fastq --kmer 31`
**Explanation:** Performs k-mer based error correction on sequencing reads.

### Generate assembly statistics
**Args:** `flight stats --assembly scaffolds.fasta --output stats.txt`
**Explanation:** Generates assembly statistics including N50, total length, and contig count.
