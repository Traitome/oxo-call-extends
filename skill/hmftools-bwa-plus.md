---
name: hmftools-bwa-plus
category: alignment
description: BWA-MEM with Hartwig-specific extensions for the WiGiTS cancer genomics analysis pipeline.
tags: [hmftools-bwa-plus, alignment, BWA, WiGiTS, cancer genomics]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/bwa-plus"
---

## Concepts

- **Tool Overview**: hmftools-bwa-plus (v1.0.0) is an extended version of BWA-MEM (Burrows-Wheeler Aligner) with Hartwig Medical Foundation-specific modifications optimized for the WiGiTS (Whole Genome Toolkit Suite) cancer genomics pipeline.
- **BWA-MEM Foundation**: Built on BWA-MEM algorithm for fast and accurate short-read alignment to reference genomes, supporting reads from 70bp to 1Mbp.
- **WiGiTS Integration**: Part of the WiGiTS suite used by Hartwig Medical Foundation for comprehensive cancer DNA/RNA analysis, supporting both whole genome sequencing (WGS) and targeted sequencing.
- **Input/Output**: Accepts FASTQ input (single or paired-end) and outputs SAM/BAM format alignments compatible with the Hartwig analysis pipeline.
- **Multi-threaded Execution**: Supports parallel processing with -t flag for faster alignment of large datasets.

## Pitfalls

- **Reference Genome Requirements**: Must use reference genomes compatible with the Hartwig pipeline (typically GRCh37 or GRCh38 with specific contig naming conventions).
- **Pair-end Ordering**: For paired-end data, read files must be properly ordered with mate information correctly embedded.
- **Memory Consumption**: Index files for large genomes require significant memory (2-4GB for human genome); ensure adequate RAM when processing multiple samples.
- **Coordinate Sort Requirement**: Output BAM must be coordinate-sorted for compatibility with downstream tools like PURPLE and AMBER in the WiGiTS pipeline.
- **Version-specific Parameters**: Hartwig-specific extensions may use different default parameters than standard BWA-MEM; refer to WiGiTS documentation for optimal settings.

## Examples

### Single-end alignment with BWA-MEM
**Args:** `bwa-plus mem -t 8 reference.fasta reads.fastq.gz | samtools sort -@ 8 -o aligned.bam`
**Explanation:** Aligns single-end reads using 8 threads and pipes directly to samtools for coordinate sorting. The -t parameter controls thread count for parallel alignment.

### Paired-end alignment for tumor-normal analysis
**Args:** `bwa-plus mem -t 16 -R "@RG\tID:tumor\tSM:tumor\tPL:ILLUMINA" reference.fasta tumor_R1.fq.gz tumor_R2.fq.gz | samtools sort -@ 16 -o tumor.bam`
**Explanation:** Performs paired-end alignment with read group header for tumor sample identification. The -R flag adds read group metadata essential for downstream variant calling.

### Alignment with mark duplicates workflow
**Args:** `bwa-plus mem -K 10000000 -t 24 reference.fasta R1.fq.gz R2.fq.gz 2> align.log | samtools sort -@ 24 | picard MarkDuplicates REMOVE_DUPLICATES=false METRICS_FILE=dups.txt OUTPUT=marked.bam`
**Explanation:** Uses -K for batch size optimization in streaming mode and processes through Picard MarkDuplicates for duplicate marking. The -K 10000000 sets 10M reads per batch for optimal memory usage.

### Generate alignment with MD tags
**Args:** `bwa-plus mem reference.fasta reads.fastq.gz | samtools calmd -@ 8 - reference.fasta > aligned.bam`
**Explanation:** Produces alignment with MD tags for SNP/indel calling compatibility. The calmd command adds MD/NM tags required by many variant callers.

### Build reference genome index
**Args:** `bwa-plus index -a bwtsw reference.fasta`
**Explanation:** Constructs BWA index using the bwtsw algorithm (required for genomes >2GB like human). This is a prerequisite for alignment operations.
