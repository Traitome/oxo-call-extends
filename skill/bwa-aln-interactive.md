---
name: bwa-aln-interactive
category: alignment
description: Fork of BWA supporting interactive/streaming alignment for real-time sequencing applications
tags: [bwa, alignment, interactive, streaming, real-time]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/bwa-aln-interactive"
---

## Concepts

- **Tool Overview**: bwa-aln-interactive is a fork of BWA (Burrows-Wheeler Aligner) by Fulcrum Genomics that supports interactive/streaming alignment. It is designed for real-time sequencing analysis where reads arrive continuously (e.g., from MinION or other streaming sequencers).
- **Core Function**: Maps DNA sequences against a large reference genome using BWA's algorithms (BWA-backtrack via `aln`/`samse`/`sampe`, BWA-MEM via `mem`, BWA-SW via `bwasw`). The key modification is the ability to process reads from stdin in a streaming fashion without batch file I/O overhead.
- **BWA Algorithms**: Includes all three BWA algorithms: BWA-backtrack (for Illumina reads <=100bp), BWA-SW (for long reads), and BWA-MEM (recommended for queries >=70bp, supports PacBio/ONT reads with `-x pacbio`/`-x ont2d`).
- **Streaming Support**: Reads can be piped via stdin (`-` as input file), enabling real-time alignment as reads are produced by sequencers or upstream basecallers. This eliminates the need to wait for complete FASTQ files.
- **Index Compatibility**: Uses standard BWA FM-index format built with `bwa index`. Indices built with standard BWA are compatible — no special index rebuild required.
- **Deprecation Notice**: The repository is no longer maintained. The maintainers recommend using [`pybwa`](https://github.com/fulcrumgenomics/pybwa) instead, which provides Python bindings to BWA with similar streaming capabilities.
- **Installation**: `conda install -c bioconda bwa-aln-interactive` (installs as `bwa` binary, replacing standard BWA in the environment).

## Pitfalls

- **Deprecated / Unmaintained**: The repository explicitly states "This repo is no longer being maintained!!!" Users should migrate to [`pybwa`](https://github.com/fulcrumgenomics/pybwa) for long-term support. Bug fixes and new features will not be backported.
- **Binary Name Collision**: The bioconda package installs the binary as `bwa`, which will shadow/replace any standard BWA installation in the same conda environment. Use separate conda environments to avoid conflicts.
- **Not for Long Reads**: The README notes that minimap2 has replaced BWA-MEM for PacBio and Nanopore read alignment — minimap2 is ~50x faster, more versatile, more accurate, and produces better base-level alignment. Use bwa-aln-interactive only when BWA compatibility is specifically required.
- **BWA-backtrack Limitations**: The `aln` algorithm is designed for Illumina reads up to ~100bp. For reads longer than 70bp, BWA-MEM (`mem` subcommand) is recommended as it is faster and more accurate, even for 70-100bp Illumina reads.
- **Streaming Latency**: In streaming mode, alignment latency per read depends on read length and index size. For real-time applications, ensure the alignment throughput matches or exceeds the sequencer's output rate to avoid backlog.
- **4GB Reference Limit**: While total reference can exceed 4GB, individual chromosomes must not exceed 2GB in length. BWA concatenates all sequences internally, so reads spanning chromosome junctions may produce artifacts in BWA-backtrack (flagged as unmapped but with position/CIGAR/tags).

## Examples

### Build standard BWA index
**Args:** `bwa index -a bwtsw ref.fa`
**Explanation:** Builds the FM-index for a large reference genome using the `bwtsw` algorithm (required for genomes >2GB; use `-a is` for small genomes <2GB). This index is fully compatible with standard BWA — no special format needed.

### Streaming alignment via stdin (BWA-MEM)
**Args:** `cat reads.fq.gz | zcat | bwa mem -t 8 ref.fa - | samtools sort -@ 4 -o aln.bam`
**Explanation:** Streams decompressed FASTQ to BWA-MEM via stdin (`-`), then pipes SAM directly to samtools sort. Eliminates intermediate files — useful for real-time pipelines where reads arrive incrementally from a basecaller or sequencer.

### BWA-backtrack for short Illumina reads (<70bp)
**Args:** `bwa aln -t 8 ref.fa read1.fq > read1.sai && bwa aln -t 8 ref.fa read2.fq > read2.sai && bwa sampe ref.fa read1.sai read2.sai read1.fq read2.fq > aln-pe.sam`
**Explanation:** Two-step BWA-backtrack for paired-end reads shorter than ~70bp: `aln` finds suffix array coordinates, `sampe` converts to chromosomal coordinates and pairs mates. For reads >=70bp, use `bwa mem` instead.

### BWA-MEM for PacBio/ONT long reads
**Args:** `bwa mem -x pacbio ref.fa pacbio_reads.fq > aln.sam`
**Explanation:** Uses BWA-MEM with the `pacbio` preset for PacBio subreads. For Oxford Nanopore reads, use `-x ont2d`. Note: minimap2 is now recommended over BWA-MEM for long-read alignment (~50x faster, more accurate).

### Streaming alignment from basecaller output
**Args:** `basecaller --stdout | bwa mem -p -t 8 ref.fa - | samtools view -bS - | samtools sort -@ 4 -o realtime.bam`
**Explanation:** Pipes interleaved paired-end FASTQ directly from a basecaller to BWA-MEM (`-p` for interleaved input, `-` for stdin). Enables real-time alignment during sequencing without waiting for the run to complete. Backpressure flows naturally through the Unix pipe.

### Single-end BWA-backtrack alignment
**Args:** `bwa aln -t 8 ref.fa reads.fq > reads.sai && bwa samse ref.fa reads.sai reads.fq > aln-se.sam`
**Explanation:** Two-step single-end alignment: `aln` generates suffix array indices (`.sai`), `samse` converts to SAM. Most compute time is in the `aln` step. For reads >=70bp, `bwa mem` is faster and preferred.
