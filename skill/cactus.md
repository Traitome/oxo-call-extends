---
name: cactus
category: alignment
description: Reference-free whole-genome multiple alignment program based on Cactus graphs
tags: [cactus, whole-genome, alignment, pangenome, multiple-alignment]
author: oxo-call-community
source_url: "https://github.com/ComparativeGenomicsToolkit/cactus"
---

## Concepts

- **Tool Overview**: Cactus performs reference-free whole-genome multiple alignments using cactus graph structure.
- **Core Function**: Aligns multiple genomes simultaneously without a reference.
- **Algorithm**: Uses cactus graph data structure for progressive alignment.
- **Input**: Sequence file in HAL, FASTA, or cactus seqfile format.
- **Output**: Multiple alignment in HAL or MAF format.
- **Application**: Comparative genomics and pangenome analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cactus`

## Pitfalls

- **Memory Usage**: Very memory-intensive for large genomes; use --binMode mode.
- **Docker/Singularity**: Best run in container mode for dependency management.
- **Input Format**: Requires specific seqfile format listing genome paths.
- **Disk Space**: Intermediate files can be very large.
- **Runtime**: Full genome alignments can take days for large genomes.

## Examples

### Create seqfile for input
**Args:** `echo -e "human human.fa\nmouse mouse.fa\nrat rat.fa" > seqfile.txt`
**Explanation:** Creates input seqfile listing genome names and FASTA paths.

### Run whole-genome alignment
**Args:** `cactus seqfile.txt output.hal --binMode local`
**Explanation:** Runs Cactus whole-genome alignment outputting HAL format.

### Run with job store
**Args:** `cactus ./jobstore seqfile.txt output.hal`
**Explanation:** Uses local job store for intermediate files during alignment.

### Convert HAL to MAF
**Args:** `hal2maf output.hal alignment.maf`
**Explanation:** Converts HAL alignment to MAF format for visualization.

### Run with container
**Args:** `cactus --binMode docker seqfile.txt output.hal`
**Explanation:** Uses Docker containers for reproducible execution.

### Set reference genome
**Args:** `cactus seqfile.txt output.hal --reference human`
**Explanation:** Uses human as reference genome in the alignment.
