---
name: salsa2
category: assembly
description: Hi-C based scaffolding tool for long read assemblies
tags: ["salsa2", "Hi-C", "scaffolding", "assembly", "genome"]
author: oxo-call-community
source_url: "https://github.com/marbl/SALSA"
---

## Concepts

- **Tool Overview**: SALSA2 (v2.3) is a Hi-C based scaffolding tool that uses chromosome conformation capture data to order and orient contigs into chromosome-scale scaffolds.
- **Core Function**: Uses Hi-C contact maps to determine the order and orientation of contigs, generating chromosome-scale scaffolds.
- **Algorithm**: Implements graph-based scaffolding using Hi-C interaction frequencies, resolving misassemblies and improving contiguity.
- **Input Format**: Assembled contigs (FASTA), Hi-C reads (FASTQ/BAM), restriction enzyme information.
- **Output Format**: Scaffolded sequences (FASTA), scaffolding statistics, visualization files.
- **Use Case**: Genome assembly improvement, chromosome-scale scaffolding, metagenomic assembly, comparative genomics.

## Pitfalls

- **Hi-C quality**: Requires high-quality Hi-C data with good coverage.
- **Contig quality**: Scaffolding quality depends on input contig quality.
- **Restriction enzyme**: Must specify correct restriction enzyme used in Hi-C library preparation.
- **Computational resources**: Large genomes require significant memory and CPU.
- **Parameter tuning**: May require adjustment for optimal scaffolding results.
- **Misassembly detection**: May miss complex misassemblies.

## Examples

### Basic scaffolding
**Args:** `salsa2 -a contigs.fasta -l hic_reads.fastq -o scaffolds -e MboI`
**Explanation:** `-a` input contigs; `-l` Hi-C reads; `-o` output directory; `-e` restriction enzyme.

### With aligned Hi-C reads
**Args:** `salsa2 -a contigs.fasta -b hic.bam -o scaffolds -e MboI`
**Explanation:** `-b` aligned Hi-C reads in BAM format.

### Multiple restriction enzymes
**Args:** `salsa2 -a contigs.fasta -l hic_reads.fastq -o scaffolds -e MboI -e HindIII`
**Explanation:** Specifies multiple restriction enzymes used.

### Resolution parameter
**Args:** `salsa2 -a contigs.fasta -l hic_reads.fastq -o scaffolds -e MboI -r 500000`
**Explanation:** `-r` resolution for Hi-C map (default: 100000).

### Gap filling
**Args:** `salsa2 -a contigs.fasta -l hic_reads.fastq -o scaffolds -e MboI --fill-gaps`
**Explanation:** `--fill-gaps` enables gap filling between contigs.

### Misassembly correction
**Args:** `salsa2 -a contigs.fasta -l hic_reads.fastq -o scaffolds -e MboI --correct-misassemblies`
**Explanation:** `--correct-misassemblies` detects and corrects misassemblies.

### Output statistics
**Args:** `salsa2 -a contigs.fasta -l hic_reads.fastq -o scaffolds -e MboI --stats`
**Explanation:** `--stats` generates detailed scaffolding statistics.