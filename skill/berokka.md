---
name: berokka
category: assembly
description: Trim, circularise and orient long read bacterial genome assemblies
tags: [assembly, circularisation, bacterial-genome, long-reads]
author: oxo-call-community
source_url: "https://github.com/tseemann/berokka"
---

## Concepts
- **Tool Overview**: Berokka is a tool for processing bacterial genome assemblies from long-read data. It trims, circularizes, and orients contigs to produce polished circular genome sequences.
- **Circular Genomes**: Bacterial genomes are typically circular. Berokka identifies and processes assembly ends to create properly circularized sequences.
- **Long-Read Assembly**: Designed for assemblies from PacBio or Oxford Nanopore data, which can span entire bacterial genomes.
- **Orientation**: Ensures contigs are oriented in a standard direction (typically starting at a consistent gene like dnaA).

## Pitfalls
- **Bacterial Genomes Only**: Berokka is specifically designed for bacterial genomes and may not work for linear chromosomes or eukaryotic genomes.
- **Assembly Quality**: Requires reasonably complete assemblies. Highly fragmented assemblies may not circularize properly.
- **Duplicate Regions**: Circularization may create duplicate regions at the junction that need to be resolved.

## Examples
### Circularize bacterial assembly
**Args:** `berokka --input assembly.fasta --output circular.fasta`
**Explanation:** Trims and circularizes a bacterial genome assembly.

### Specify orientation gene
**Args:** `berokka --input assembly.fasta --output circular.fasta --start-gene dnaA`
**Explanation:** Orients the circular genome to start at the dnaA gene.

### Process multiple contigs
**Args:** `berokka --input assembly.fasta --output circular.fasta --min-length 10000`
**Explanation:** Only circularizes contigs longer than 10kb.
