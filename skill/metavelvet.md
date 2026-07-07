---
name: metavelvet
category: assembly
description: "MetaVelvet : An extension of Velvet assembler to de novo metagenome assembly from short sequence reads"
tags: [metavelvet, assembly, metagenomics]
author: oxo-call-community
source_url: "http://metavelvet.dna.bio.keio.ac.jp"
---
## Concepts

- **Tool Overview**: MetaVelvet v1.2.02 is an extension of the Velvet assembler specifically designed for de novo metagenome assembly from short sequencing reads.
- **Core Function**: Assembles metagenomic sequences from short-read sequencing data.
- **De Novo Assembly**: Performs de novo assembly without reference sequences.
- **Meta-specific Optimization**: Optimized for metagenomic datasets with complex microbial communities.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs assembled contigs and scaffolds.
- **Multi-step Process**: Includes read preprocessing, k-mer counting, assembly, and scaffolding.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Assembly of complex metagenomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assembly quality depends on input read quality.
- **Storage Requirements**: Intermediate files can require substantial storage space.

## Examples

### Assemble metagenome
**Args:** `metavelvet -f reads.fastq -o assembly/`
**Explanation:** Assembles metagenomic short reads into contigs.

### With custom k-mer size
**Args:** `metavelvet -f reads.fastq -k 51 -o assembly/`
**Explanation:** Uses k-mer size of 51 for assembly.

### Paired-end assembly
**Args:** `metavelvet -f reads_1.fastq -r reads_2.fastq -o assembly/`
**Explanation:** Processes paired-end sequencing data.

### Scaffold assembly
**Args:** `metavelvet -f reads.fastq -o assembly/ --scaffold`
**Explanation:** Generates scaffolds from assembled contigs.

### Quality assessment
**Args:** `metavelvet -f reads.fastq -o assembly/ --assess`
**Explanation:** Assesses assembly quality and generates statistics.