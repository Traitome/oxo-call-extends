---
name: haploclique
category: bioinformatics
description: HaploClique reconstructs viral haplotypes and detects large insertions/deletions from NGS data using maximal clique finding.
tags: [haploclique, viral-genomics, haplotype-assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/haploclique"
---

## Concepts

- **Viral Haplotype Assembly**: HaploClique reconstructs viral haplotypes.

- **Maximal Clique Finding**: Uses graph-based approach for assembly.

- **Indel Detection**: Detects large insertions and deletions.

- **Quasispecies Analysis**: Analyzes viral quasispecies populations.

- **NGS Data**: Works with next-generation sequencing data.

- **Error Correction**: Corrects sequencing errors during assembly.

## Pitfalls

- **Read Quality**: Low-quality reads may affect assembly.

- **Coverage Depth**: Requires sufficient sequencing coverage.

- **Viral Diversity**: High diversity may complicate assembly.

- **Computational Resources**: May require significant resources.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Assemble haplotypes
**Args:** `haploclique -i reads.fastq -r reference.fasta -o haplotypes.fasta`
**Explanation:** Reconstructs viral haplotypes from reads.

### Detect indels
**Args:** `haploclique -i reads.fastq -r reference.fasta -indel -o indels.txt`
**Explanation:** Detects large insertions and deletions.

### Paired-end reads
**Args:** `haploclique -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o haplotypes.fasta`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `for f in *.fastq; do haploclique -i $f -r reference.fasta -o ${f%.fastq}_haplotypes.fasta; done`
**Explanation:** Processes multiple FASTQ files.

### Generate statistics
**Args:** `haploclique -i reads.fastq -r reference.fasta -stats -o stats.txt`
**Explanation:** Generates assembly statistics.

### Quality filtering
**Args:** `haploclique -i reads.fastq -r reference.fasta -q 20 -o haplotypes.fasta`
**Explanation:** Filters reads by quality score.

### Help command
**Args:** `haploclique --help`
**Explanation:** Shows available options and usage information.