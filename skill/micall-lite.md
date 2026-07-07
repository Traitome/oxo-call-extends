---
name: micall-lite
category: alignment
description: A bioinformatic pipeline for mapping of FASTQ data to a set of reference sequences to generate consensus sequences, variant calls and coverage maps.
tags: [micall-lite, alignment, sequence]
author: oxo-call-community
source_url: "https://github.com/PoonLab/MiCall-Lite"
---

## Concepts

- **Tool Overview**: MiCall-Lite v0.1rc5 is a pipeline for mapping FASTQ data to reference sequences.
- **Core Function**: Maps sequencing reads to references and generates consensus sequences.
- **Read Mapping**: Aligns sequencing reads to reference sequences.
- **Consensus Generation**: Generates consensus sequences from mapped reads.
- **Variant Calling**: Identifies variants in mapped reads.
- **Coverage Analysis**: Generates coverage maps of reference sequences.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal mapping.
- **Data Quality**: Mapping accuracy depends on read quality.
- **Reference Genome**: Requires appropriate reference sequences.
- **Runtime**: Processing large FASTQ files can be time-consuming.

## Examples

### Map reads to reference
**Args:** `micall-lite -i reads.fastq -r reference.fasta -o output/`
**Explanation:** Maps reads to reference and generates results.

### Generate consensus
**Args:** `micall-lite -i reads.fastq -r reference.fasta -o output/ -c`
**Explanation:** Generates consensus sequence.

### Call variants
**Args:** `micall-lite -i reads.fastq -r reference.fasta -o output/ -v`
**Explanation:** Calls variants from mapped reads.

### Coverage map
**Args:** `micall-lite -i reads.fastq -r reference.fasta -o output/ -m`
**Explanation:** Generates coverage map.

### Paired-end analysis
**Args:** `micall-lite -i reads_1.fastq -R reads_2.fastq -r reference.fasta -o output/`
**Explanation:** Processes paired-end sequencing data.