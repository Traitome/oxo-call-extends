---
name: rmetl
category: alignment
description: rMETL is a realignment-based Mobile Element insertion detection tool for long-read sequencing data.
tags: [rmetl, alignment, long-read, mobile-element, te-detection]
author: oxo-call-community
source_url: "https://github.com/tjiangHIT/rMETL"
---

## Concepts

- **Tool Overview**: rMETL detects mobile element insertions in long reads.
- **Core Function**: Identifies MEI (mobile element insertions) from long-read alignments.
- **Algorithm**: Uses realignment and clustering to identify non-reference TE insertions.
- **Input Format**: Accepts BAM/CRAM files and a reference genome.
- **Output**: Produces VCF of mobile element insertion sites.
- **Use Case**: Transposable element detection in PacBio/ONT genomes.

## Pitfalls

- **Read Length**: Designed for long reads (PacBio/ONT); not suitable for short-read data.
- **BAM Sort**: Input BAM must be coordinate-sorted and indexed (`samtools index`).
- **Reference Index**: FASTA reference must be indexed with `samtools faidx`.
- **MEI Sensitivity**: Tuned for germline MEIs; somatic MEIs may require parameter adjustment.
- **TE Annotation**: For highest accuracy, provide a known TE consensus library via `--mei` parameter.
- **Version**: rMETL 1.0.4 is the latest release; API has changed from earlier versions.

## Examples

### Display help
**Args:** `rMETL.py --help`
**Explanation:** Shows rMETL command-line options and required arguments.

### Basic MEI detection
**Args:** `rMETL.py -i sample.bam -r reference.fasta -o mei_results/`
**Explanation:** `-i` is input BAM; `-r` is reference FASTA; `-o` is output directory for VCF results.

### With threads
**Args:** `rMETL.py -i sample.bam -r reference.fasta -o mei_results/ -t 8`
**Explanation:** `-t 8` enables parallel processing across 8 CPU cores.

### With TE annotation
**Args:** `rMETL.py -i sample.bam -r reference.fasta -mei te_consensus.fa -o mei_results/`
**Explanation:** `-mei` provides TE consensus sequences to guide insertion classification.

### With read group
**Args:** `rMETL.py -i sample.bam -r reference.fasta -rg @RG\tID:s1\tSM:sample1 -o mei_results/`
**Explanation:** `-rg` adds a read group header to the output BAM for sample tracking.

### Specify insert size
**Args:** `rMETL.py -i sample.bam -r reference.fasta -o mei_results/ --min-ins 100 --max-ins 10000`
**Explanation:** `--min-ins`/`--max-ins` set the MEI size range; default is suitable for full-length L1/Alu/SVA.

### With min supporting reads
**Args:** `rMETL.py -i sample.bam -r reference.fasta -o mei_results/ -m 3`
**Explanation:** `-m 3` requires at least 3 supporting reads for an MEI call to be reported.