---
name: rmats-long
category: expression
description: rMATS-long performs differential isoform analysis on long-read RNA-seq data.
tags: [rmats-long, expression, long-read, isoform, alternative-splicing]
author: oxo-call-community
source_url: "https://github.com/Xinglab/rMATS-long"
---

## Concepts

- **Tool Overview**: rMATS-long is the long-read extension of rMATS.
- **Core Function**: Detects differential alternative splicing from long-read RNA-seq.
- **Algorithm**: Uses full-length isoform reads for accurate splicing quantification.
- **Input Format**: Accepts BAM files from PacBio/ONT long-read RNA-seq; GTF annotation.
- **Output**: Produces splicing event counts and statistics.
- **Use Case**: Full-length isoform quantification and differential splicing.

## Pitfalls

- **Read Type**: Designed for long reads (PacBio Iso-Seq, ONT); not suitable for short-read data — use rMATS-turbo instead.
- **GTF Compatibility**: GTF chromosome names must match BAM reference contig names.
- **Memory Usage**: Long-read alignments are large; allocate sufficient RAM.
- **Statistics**: Long-read counts have higher variance; replicate numbers should be higher than for short reads.
- **Version**: rMATS-long is a separate tool from rMATS-turbo; install with `rmats-long` not `rmats`.
- **Coordinate Sort**: BAM files must be sorted and indexed; long-read alignments often have supplementary records.

## Examples

### Display help
**Args:** `rmats-long --help`
**Explanation:** Shows version-specific options for long-read splicing analysis.

### Run with long-read BAMs
**Args:** `rmats-long --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp_dir/ -t paired`
**Explanation:** `--b1`/`--b2` are sample BAMs; `--gtf` provides gene annotation; `--od` is output directory; `-t paired` for paired-end convention.

### Single-sample analysis
**Args:** `rmats-long --b1 sample.bam --gtf genes.gtf --od output/ --tmp tmp_dir/ -t single`
**Explanation:** `-t single` runs in single-sample mode; useful for exploratory analysis.

### With read length filter
**Args:** `rmats-long --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp_dir/ -t paired --readLength 50`
**Explanation:** `--readLength 50` filters reads shorter than 50bp to improve full-length isoform quantification.

### Set thread count
**Args:** `rmats-long --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp_dir/ -t paired --nthread 8`
**Explanation:** `--nthread 8` enables parallel processing across 8 CPU cores.

### Specify statistical model
**Args:** `rmats-long --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp_dir/ -t paired --cstat 0.0001`
**Explanation:** `--cstat 0.0001` sets the splicing difference cutoff for significance testing.

### With variable read lengths
**Args:** `rmats-long --b1 s1.bam --b2 s2.bam --gtf genes.gtf --od output/ --tmp tmp_dir/ -t paired --variable-read-length`
**Explanation:** `--variable-read-length` accommodates variable read lengths typical of ONT data.