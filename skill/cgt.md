---
name: cgt
category: metagenomics
description: Calculate core genome threshold from metagenome sequencing data
tags: [cgt, metagenomics, core-genome, threshold, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bacpop/cgt"
---

## Concepts

- **Tool Overview**: CGT calculates core genome thresholds from metagenome sequencing data to determine species boundaries.
- **Core Function**: Identifies conserved genomic regions that define a species core genome from metagenomic reads.
- **Algorithm**: Uses coverage and presence/absence patterns across multiple samples to define core genome.
- **Input**: Metagenomic sequencing reads or assembled contigs from multiple samples.
- **Output**: Core genome threshold value and summary statistics.
- **Application**: Species boundary determination and population genomics from metagenomic data.
- **Installation**: Install via bioconda: `conda install -c bioconda cgt`

## Pitfalls

- **Sample Quality**: Requires high-quality sequencing data for accurate threshold calculation.
- **Coverage Depth**: Low coverage may affect core genome identification.
- **Assembly Quality**: Contig quality impacts core genome definition.
- **Reference Database**: May require reference genomes for validation.

## Examples

### Calculate core genome threshold
**Args:** `cgt -i reads_1.fastq -i reads_2.fastq -o cgt_result.txt`
**Explanation:** Calculates core genome threshold from paired-end reads.

### With multiple samples
**Args:** `cgt --samples samples.txt --output results/`
**Explanation:** Processes multiple samples listed in samples.txt.

### Use assembled contigs
**Args:** `cgt --contigs contigs.fasta --output cgt_result.txt`
**Explanation:** Uses assembled contigs instead of raw reads.

### Display help
**Args:** `cgt --help`
**Explanation:** Shows all available options and usage information.