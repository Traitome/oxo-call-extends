---
name: mapsembler2
category: assembly
description: Targeted assembly software
tags: [mapsembler2, assembly, targeted-assembly]
author: oxo-call-community
source_url: "https://colibread.inria.fr/software/mapsembler2/"
---

## Concepts

- **Tool Overview**: mapsembler2 v2.2.4 - Targeted assembly software for specific genomic regions of interest.
- **Core Function**: Performs targeted assembly of specific genomic regions from sequencing reads.
- **Input/Output**: Input: FASTQ reads, target regions; Output: Assembled contigs for target regions.
- **Installation**: `conda install -c bioconda mapsembler2`
- **Targeted Assembly**: Focuses assembly on specific regions of interest.
- **Multi-sample Support**: Supports analysis of multiple samples.

## Pitfalls

- **Target Definition**: Requires precise target region definition.
- **Read Quality**: Poor quality reads affect assembly accuracy.
- **Coverage**: Low coverage in target regions may fail assembly.
- **Repeat Regions**: Repetitive regions may cause misassembly.
- **Computational Resources**: Large target regions require significant memory.
- **Parameter Tuning**: Incorrect parameters affect assembly quality.

## Examples

### Run targeted assembly
**Args:** `mapsembler2 -i reads.fastq -t targets.bed -o contigs.fasta`
**Explanation:** Performs targeted assembly of specified regions.

### Paired-end reads
**Args:** `mapsembler2 -1 reads_1.fastq -2 reads_2.fastq -t targets.bed -o contigs.fasta`
**Explanation:** Processes paired-end reads.

### With reference guidance
**Args:** `mapsembler2 -i reads.fastq -t targets.bed -r ref.fa -o contigs.fasta`
**Explanation:** Uses reference genome for guided assembly.

### Verbose mode
**Args:** `mapsembler2 -i reads.fastq -t targets.bed -o contigs.fasta -v`
**Explanation:** Provides detailed logging during assembly.

### Quality filtering
**Args:** `mapsembler2 -i reads.fastq -t targets.bed -o contigs.fasta -q 30`
**Explanation:** Filters reads with quality < 30.

### Multiple targets
**Args:** `mapsembler2 -i reads.fastq -t targets.txt -o contigs.fasta`
**Explanation:** Processes multiple target regions from file.