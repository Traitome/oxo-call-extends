---
name: rnabloom
category: expression
description: RNA-Bloom is a Java-based reference-free de novo transcriptome assembler for short and long RNA-seq reads.
tags: [rnabloom, expression, rna-seq, assembly, de-novo, long-read]
author: oxo-call-community
source_url: "https://github.com/BirolLab/RNA-Bloom/blob/master/README.md"
---

## Concepts

- **Tool Overview**: RNA-Bloom is a fast de novo transcriptome assembler.
- **Core Function**: Assembles transcripts from RNA-seq reads without a reference genome.
- **Algorithm**: Uses Bloom-filter-based k-mer counting for memory-efficient assembly.
- **Input Format**: Accepts FASTQ/FASTA (gzipped OK) for short or long reads.
- **Output**: Produces FASTA files of assembled transcripts (full, short, non-redundant).
- **Use Case**: Reference-free transcriptome assembly for bulk, single-cell, or long-read RNA-seq.

## Pitfalls

- **Java Required**: Requires JDK 11+ (17 is faster); JAVA_HOME must be set.
- **External Deps**: Needs `minimap2` (≥2.22), `ntCard` (≥1.2.1); long-read mode also needs `Racon`.
- **PATH Setup**: All dependencies (minimap2, ntCard, Racon) must be in system PATH.
- **Strandedness**: Use `-revcomp-right` or `-revcomp-left` for dUTP/Illumina TruSeq stranded libraries.
- **Pooled Mode**: `-pool` mode is for single-cell data; long reads are NOT supported in pooled mode.
- **Output Threshold**: Default transcript length threshold is 200 bp; shorter transcripts go to `*.short.fa`.

## Examples

### Display help
**Args:** `java -jar RNA-Bloom.jar --help`
**Explanation:** Shows all flags including input, output, threads, and k-mer options.

### Paired-end short reads
**Args:** `java -jar RNA-Bloom.jar -left LEFT.fastq -right RIGHT.fastq -revcomp-right -t 8 -outdir out/`
**Explanation:** `-left`/`-right` are paired-end FASTQs; `-revcomp-right` reverse-complements right reads (Illumina TruSeq stranded); `-t 8` uses 8 threads.

### Single-end short reads
**Args:** `java -jar RNA-Bloom.jar -sef SE.fastq -t 8 -outdir out/`
**Explanation:** `-sef` is the single-end forward read file; output goes to `out/` directory.

### Long-read assembly (ONT/PacBio)
**Args:** `java -jar RNA-Bloom.jar -long long_reads.fastq -t 8 -outdir out/`
**Explanation:** `-long` enables long-read mode (requires Racon in PATH); works for ONT cDNA/direct RNA and PacBio cDNA.

### Strand-specific assembly
**Args:** `java -jar RNA-Bloom.jar -left R2.fastq -right R1.fastq -stranded -revcomp-right -t 8 -outdir out/`
**Explanation:** `-stranded` enables strand-specific mode; for F2R1 orientation, `-left` is R2 and `-right` is R1.

### Pooled single-cell assembly
**Args:** `java -jar RNA-Bloom.jar -pool reads_list.txt -revcomp-right -t 8 -outdir out/`
**Explanation:** `-pool` reads a tab-separated file listing single-cell FASTQ paths; not compatible with `-long`.

### Custom k-mer and FPR
**Args:** `java -jar RNA-Bloom.jar -left L.fq -right R.fq -revcomp-right -k 25 -fpr 0.01 -t 8 -outdir out/`
**Explanation:** `-k 25` sets k-mer size; `-fpr 0.01` sets Bloom filter false-positive rate (lower = more memory).