---
name: bowtie
category: alignment
description: Ultrafast memory-efficient short read aligner for large-scale sequencing
tags: [bowtie, alignment, short-read, rna-seq]
author: oxo-call-community
source_url: "https://github.com/BenLangmead/bowtie"
---

## Concepts

- **Tool Overview**: Bowtie (version 1) is an ultrafast, memory-efficient short read aligner optimized for reads up to 50bp.
- **Core Function**: Aligns short DNA sequences (reads) to large genomes using the Burrows-Wheeler transform.
- **Index Building**: Use `bowtie-build` to create FM-index from reference FASTA files.
- **Colorspace Support**: Supports colorspace reads from SOLiD sequencing.
- **Memory Efficiency**: Uses minimal memory (~2GB for human genome) compared to hash-based aligners.
- **Installation**: Install via bioconda: `conda install -c bioconda bowtie`

## Pitfalls

- **Read Length**: Bowtie1 is optimized for reads up to 50bp; use Bowtie2 for longer reads.
- **No Gaps**: Original Bowtie does not support gaps; use Bowtie2 for gapped alignment.
- **Index Required**: Must build index with bowtie-build before alignment.
- **Quality Encoding**: Ensure correct quality encoding (--phred33-quals or --phred64-quals).
- **Strandedness**: Specify --fr/--rf/--ff for proper paired-end orientation.

## Examples

### Build genome index
**Args:** `bowtie-build genome.fa genome_index`
**Explanation:** Creates Bowtie index files from reference FASTA for alignment.

### Basic single-end alignment
**Args:** `bowtie genome_index reads.fq aligned.sam`
**Explanation:** Aligns single-end reads to the indexed reference genome.

### Paired-end alignment
**Args:** `bowtie genome_index -1 reads_R1.fq -2 reads_R2.fq aligned.sam`
**Explanation:** Aligns paired-end reads with proper pair handling.

### Alignment with threads
**Args:** `bowtie -p 8 genome_index reads.fq aligned.sam`
**Explanation:** Uses 8 threads for parallel alignment processing.

### Report all valid alignments
**Args:** `bowtie -a genome_index reads.fq aligned.sam`
**Explanation:** Reports all valid alignments per read instead of just the best.

### Best mode with strata
**Args:** `bowtie --best --strata genome_index reads.fq aligned.sam`
**Explanation:** Reports alignments in best stratum, ensuring highest quality matches.

### Limit mismatches
**Args:** `bowtie -v 2 genome_index reads.fq aligned.sam`
**Explanation:** Allows up to 2 mismatches in the seed region.

### Suppress unaligned reads
**Args:** `bowtie -m 1 genome_index reads.fq aligned.sam`
**Explanation:** Suppresses reads with more than 1 valid alignment (multi-mappers).
