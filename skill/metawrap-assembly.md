---
name: metawrap-assembly
category: assembly
description: MetaWRAP requirements for assembly step
tags: [metawrap-assembly, assembly, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Assembly v1.3.0 provides assembly functionality as part of the MetaWRAP metagenomic analysis pipeline.
- **Core Function**: Assembles metagenomic sequences from short-read sequencing data.
- **De Novo Assembly**: Performs de novo assembly without reference sequences.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts sequencing reads; outputs assembled contigs and scaffolds.
- **Multi-step Process**: Includes read preprocessing, assembly, and quality assessment.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Assembly of complex metagenomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assembly quality depends on input read quality.

## Examples

### Assemble metagenome
**Args:** `metawrap-assembly -i reads.fastq -o assembly/`
**Explanation:** Assembles metagenomic short reads into contigs.

### With custom k-mer size
**Args:** `metawrap-assembly -i reads.fastq -k 51 -o assembly/`
**Explanation:** Uses k-mer size of 51 for assembly.

### Paired-end assembly
**Args:** `metawrap-assembly -i reads_1.fastq -r reads_2.fastq -o assembly/`
**Explanation:** Processes paired-end sequencing data.

### Scaffold assembly
**Args:** `metawrap-assembly -i reads.fastq -o assembly/ --scaffold`
**Explanation:** Generates scaffolds from assembled contigs.

### Quality assessment
**Args:** `metawrap-assembly -i reads.fastq -o assembly/ --assess`
**Explanation:** Assesses assembly quality and generates statistics.