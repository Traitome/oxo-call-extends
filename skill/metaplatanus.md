---
name: metaplatanus
category: assembly
description: "MetaPlatanus: A hybrid metagenome assembler"
tags: [metaplatanus, assembly, metagenomics, hybrid]
author: oxo-call-community
source_url: "https://github.com/rkajitani/metaplatanus"
---
## Concepts

- **Tool Overview**: MetaPlatanus v1.3.1 is a hybrid metagenome assembler that combines short and long read sequencing data.
- **Core Function**: Assembles metagenomic sequences using both short reads (Illumina) and long reads (PacBio/ONT).
- **Hybrid Assembly**: Integrates short-read accuracy with long-read contiguity for improved assembly quality.
- **Meta-specific Optimization**: Optimized for metagenomic datasets with complex microbial communities.
- **Input/Output**: Accepts FASTQ reads (both short and long); outputs assembled contigs and scaffolds.
- **Multi-step Process**: Includes read preprocessing, assembly, and scaffolding steps.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Assembly of complex metagenomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assembly quality depends on input read quality.
- **Storage Requirements**: Intermediate files can require substantial storage space.

## Examples

### Assemble metagenome with short reads
**Args:** `metaplatanus assemble -i short_reads.fastq -o assembly/`
**Explanation:** Assembles metagenomic short reads into contigs.

### Hybrid assembly with long reads
**Args:** `metaplatanus assemble -i short_reads.fastq -l long_reads.fastq -o assembly/`
**Explanation:** Performs hybrid assembly using both short and long reads.

### With custom k-mer size
**Args:** `metaplatanus assemble -i reads.fastq -k 55 -o assembly/`
**Explanation:** Uses custom k-mer size for assembly.

### Scaffold assembly
**Args:** `metaplatanus scaffold -i contigs.fasta -l long_reads.fastq -o scaffolds.fasta`
**Explanation:** Scaffolds contigs using long reads.

### Quality assessment
**Args:** `metaplatanus assess -i assembly.fasta -o stats.txt`
**Explanation:** Assesses assembly quality and generates statistics.