---
name: rmats
category: expression
description: rMATS detects differential alternative splicing events from replicate RNA-Seq data.
tags: [rmats, expression, rna-seq, alternative-splicing, mats]
author: oxo-call-community
source_url: "http://rnaseq-mats.sourceforge.net"
---

## Concepts

- **Tool Overview**: rMATS quantifies differential alternative splicing across conditions.
- **Core Function**: Detects SE, A5SS, A3SS, MXE, and RI splicing events.
- **Algorithm**: Uses a hierarchical model to calculate PSI/IncLevel differences and FDR.
- **Input Format**: Accepts BAM files (preferred) or FASTQ + GTF annotation.
- **Output**: Produces per-event JC, JCEC, and novel splice site counts with statistics.
- **Use Case**: Differential alternative splicing analysis in RNA-seq studies.

## Pitfalls

- **GTF Naming**: GTF chromosome/contig names must match the BAM reference sequence names exactly.
- **Read Length**: Required `-len` parameter; use uniform read length or trim beforehand.
- **BAM Sort**: Input BAMs must be coordinate-sorted; rMATS does not sort automatically.
- **Read Type**: `-t` parameter (paired/single) must match the library prep protocol.
- **Strandedness**: `-libType` affects counting; specify fr-unstranded, fr-firststrand, or fr-secondstrand.
- **JC vs JCEC**: JC uses only reads on splice junctions; JCEC adds reads on exons — report both for completeness.

## Examples

### Display help
**Args:** `rmats.py --help`
**Explanation:** Shows all required and optional flags for rMATS-turbo v4.x.

### Run rMATS with BAM files
**Args:** `python rmats.py --b1 s1_rep1.bam,s1_rep2.bam --b2 s2_rep1.bam,s2_rep2.bam --gtf genes.gtf --od output/ --tmp tmp/ -t paired --readLength 101 --nthread 4`
**Explanation:** `--b1`/`--b2` are comma-separated replicate BAMs per condition; `--gtf` annotation; `-t paired`; `--readLength 101` for paired-end 101bp reads.

### From FASTQ (alignment step)
**Args:** `python rmats.py --s1 rep1_1.fq:rep1_2.fq,rep2_1.fq:rep2_2.fq --s2 ctrl1_1.fq:ctrl1_2.fq,ctrl2_1.fq:ctrl2_2.fq --gtf genes.gtf --bi bowtieIndex -o output/ -t paired --readLength 50`
**Explanation:** `--s1`/`--s2` use colon-separated paired FASTQ and comma-separated replicates; `--bi` provides the bowtie index base.

### Specify library type
**Args:** `python rmats.py --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp/ -t paired --libType fr-firststrand --readLength 100`
**Explanation:** `--libType fr-firststrand` matches dUTP/Illumina TruSeq stranded library protocol.

### Detect novel splice sites
**Args:** `python rmats.py --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp/ -t paired --readLength 100 --novelSS`
**Explanation:** `--novelSS` enables detection of previously unannotated splice junctions.

### Adjust statistical cutoff
**Args:** `python rmats.py --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp/ -t paired --readLength 100 --cstat 0.05`
**Explanation:** `--cstat 0.05` sets the minimum splicing difference (delta PSI) threshold for significance.

### Use STAR-aligned BAMs
**Args:** `python rmats.py --b1 star_s1.bam --b2 star_s2.bam --gtf genes.gtf --od output/ --tmp tmp/ -t paired --readLength 100 --variable-read-length`
**Explanation:** `--variable-read-length` accommodates read length variation typical of STAR alignments with soft clipping.