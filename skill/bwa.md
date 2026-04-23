---
name: bwa
category: alignment
description: Burrows-Wheeler Aligner for short-read mapping to reference genomes
tags: [bwa, alignment, short-read, mapping, dna-seq]
author: oxo-call-community
source_url: "https://github.com/lh3/bwa"
---

## Concepts

- **Tool Overview**: BWA is a widely-used short-read aligner based on the Burrows-Wheeler transform.
- **Core Algorithms**: BWA-MEM (default, best for 70bp-1Mbp reads), BWA-ALN (legacy, for <70bp), BWA-SW (for long reads).
- **Index Building**: Must build FM-index from reference before alignment.
- **Output**: SAM format by default; pipe to samtools for BAM conversion.
- **Paired-End**: Supports paired-end alignment with proper insert size handling.
- **Installation**: Install via bioconda: `conda install -c bioconda bwa`

## Pitfalls

- **Index Required**: Always run `bwa index` before alignment.
- **Read Groups**: Add read groups with -R for GATK compatibility.
- **Thread Count**: Use -t for multi-threading; default is 1 thread.
- **Output Sorting**: BWA outputs unsorted SAM; sort with samtools for downstream use.
- **Alt Contigs**: Use -a for alternative contig mapping in GRCh38+.

## Examples

### Build genome index
**Args:** `index reference.fa`
**Explanation:** Creates BWA FM-index files from reference genome FASTA.

### Align single-end reads with BWA-MEM
**Args:** `mem -t 8 reference.fa reads.fq > aligned.sam`
**Explanation:** Aligns single-end reads using BWA-MEM algorithm with 8 threads.

### Align paired-end reads
**Args:** `mem -t 8 -R '@RG\tID:sample1\tSM:sample1' reference.fa R1.fq R2.fq > aligned.sam`
**Explanation:** Aligns paired-end reads with read group information for GATK.

### Convert to sorted BAM
**Args:** `mem -t 8 reference.fa R1.fq R2.fq | samtools sort -o aligned.bam`
**Explanation:** Aligns and directly converts to sorted BAM format.

### Align with BWA-ALN (legacy, short reads)
**Args:** `aln -t 8 reference.fa reads.fq > reads.sai && sampe reference.fa reads.sai reads.fq > aligned.sam`
**Explanation:** Two-step alignment for very short reads (<70bp) using legacy algorithm.

### Map to alternate loci
**Args:** `mem -t 8 -a reference.fa reads.fq > aligned.sam`
**Explanation:** Outputs all alignments including those to alternative contigs.

### Check index information
**Args:** `samtools faidx reference.fa && bwa index reference.fa`
**Explanation:** Creates both samtools and BWA indexes for the reference genome.
