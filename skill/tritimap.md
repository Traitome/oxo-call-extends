---
name: tritimap
category: analysis
description: TriTiMap - Tool for trinucleotide-based sequence mapping.
tags: [tritimap, sequence-mapping, trinucleotide, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/compbio/tritimap"
---

## Concepts

- **Tool Overview**: TriTiMap - A tool for mapping sequences using trinucleotide-based indexing.
- **Core Function**: Maps sequencing reads to reference sequences using trinucleotide indices.
- **Input**: FASTQ reads, reference genome.
- **Output**: Alignments (SAM/BAM), mapping statistics.
- **Installation**: `pip install tritimap` or `conda install -c bioconda tritimap`
- **Use Case**: Sequence mapping, read alignment, genomics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Index Building**: First run requires index building.

## Examples

### Map reads
**Args:** `tritimap -i reads.fastq -r genome.fasta -o alignments.sam`
**Explanation:** Map sequencing reads to reference genome.

### Build index
**Args:** `tritimap index -r genome.fasta -o genome.index`
**Explanation:** Build trinucleotide index for genome.
