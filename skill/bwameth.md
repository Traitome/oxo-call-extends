---
name: bwameth
category: epigenomics
description: Fast and accurate aligner for bisulfite sequencing reads using BWA-MEM
tags: [bwameth, bisulfite, methylation, alignment, bwa]
author: oxo-call-community
source_url: "https://github.com/brentp/bwa-meth"
---

## Concepts

- **Tool Overview**: bwa-meth aligns bisulfite-converted reads using BWA-MEM with three-letter encoding.
- **Core Function**: Maps bisulfite-treated reads to reference genome for methylation analysis.
- **Algorithm**: Converts C to T in reads and reference, aligns with BWA-MEM, then back-converts.
- **Input**: Bisulfite FASTQ files and reference genome.
- **Output**: SAM/BAM alignment file for methylation calling.
- **Installation**: Install via bioconda: `conda install -c bioconda bwameth`

## Pitfalls

- **BWA Required**: Requires BWA to be installed in PATH.
- **Index Required**: Must run bwa-meth index before alignment.
- **Reference Preparation**: Reference needs special indexing for bisulfite alignment.
- **Output Processing**: Use MethylDackel or similar for methylation calling from alignments.

## Examples

### Index reference genome
**Args:** `bwa-meth.py index reference.fa`
**Explanation:** Builds bisulfite-aware index from reference genome.

### Align bisulfite reads
**Args:** `bwa-meth.py mem reference.fa reads.fq | samtools sort -o aligned.bam`
**Explanation:** Aligns bisulfite reads and converts to sorted BAM.

### Paired-end alignment
**Args:** `bwa-meth.py mem reference.fa R1.fq R2.fq | samtools sort -o paired.bam`
**Explanation:** Aligns paired-end bisulfite reads.

### Multi-threaded alignment
**Args:** `bwa-meth.py mem -t 8 reference.fa reads.fq | samtools sort -o aligned.bam`
**Explanation:** Uses 8 threads for faster bisulfite alignment.

### Call methylation with MethylDackel
**Args:** `MethylDackel extract reference.fa aligned.bam -o methylation.bedGraph`
**Explanation:** Extracts methylation levels from bwa-meth alignments.

### Display help
**Args:** `bwa-meth.py --help`
**Explanation:** Shows all available options and usage information.
