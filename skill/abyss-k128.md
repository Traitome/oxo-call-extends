---
name: abyss-k128
category: assembly
description: ABySS assembler variant compiled with k-mer size up to 128 for de novo genome assembly
tags: [assembly, de-novo, k-mer, abyss, short-reads]
author: oxo-call-community
source_url: "http://www.bcgsc.ca/platform/bioinfo/software/abyss"
---

## Concepts

- **Tool Overview**: abyss-k128 is a variant of ABySS (Assembly By Short Sequences) compiled with maximum k-mer size of 128, for de novo parallel paired-end short read assembly.
- **Core Function**: Assembles short paired-end reads into contigs and scaffolds using de Bruijn graph approach with support for larger k-mer sizes.
- **Input/Output**: Input: FASTQ files (paired or single-end). Output: Assembled contigs (FASTA), scaffold files, and assembly statistics.
- **K-mer Size**: Supports k-mer sizes up to 128, useful for complex or repetitive genomes requiring longer k-mers.
- **Installation**: Install via bioconda: `conda install -c bioconda abyss-k128`

## Pitfalls

- **K-mer Selection**: Larger k-mers (up to 128) require more memory but provide better specificity for repetitive regions.
- **Memory Requirements**: Assembly of large genomes requires substantial RAM - allocate at least 1GB per million reads.
- **MPI Parallelism**: ABySS supports MPI for distributed assembly - requires proper MPI configuration.
- **Paired-End Data**: Best results require paired-end or mate-pair libraries for scaffolding.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and parameters for ABySS assembly.

### Basic assembly with abyss-pe
**Args:** `k=96 in='reads1.fastq reads2.fastq' name=asm`
**Explanation:** Runs ABySS with k=96 using paired-end reads, naming the assembly 'asm'.

### Assembly with maximum k-mer
**Args:** `k=128 in='R1.fq R2.fq' name=asm128`
**Explanation:** Uses k=128 for maximum specificity, useful for large complex genomes.

### Multi-library assembly
**Args:** `k=96 lib='pe1 pe2' pe1='R1_1.fq R1_2.fq' pe2='R2_1.fq R2_2.fq' name=asm`
**Explanation:** Assembles with multiple paired-end libraries for improved scaffolding.

### Assembly with mate-pair scaffolding
**Args:** `k=96 in='pe_R1.fq pe_R2.fq' mp='mp_R1.fq mp_R2.fq' name=asm_scaffold`
**Explanation:** Uses paired-end reads for contig assembly and mate-pair reads for scaffolding.

### Set memory and threads
**Args:** `k=96 in='R1.fq R2.fq' name=asm np=16 maxk=128`
**Explanation:** Uses 16 threads and allows k-mer sizes up to 128 for the assembly.

### Assembly with bloom filter
**Args:** `k=96 in='R1.fq R2.fq' name=asm_bloom nbloom=1`
**Explanation:** Uses bloom filter to reduce memory usage for large genome assembly.
