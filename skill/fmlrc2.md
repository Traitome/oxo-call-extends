---
name: fmlrc2
category: utility
description: A Rust implementation of fmlrc with faster run times for long-read error correction.
tags: [fmlrc2, error correction, long reads, Rust, sequencing]
author: oxo-call-community
source_url: "https://github.com/HudsonAlpha/fmlrc2"
---

## Concepts
- **Long-read Error Correction**: fmlrc2 corrects errors in long sequencing reads (PacBio/ONT) using a multi-string Burrows-Wheeler Transform (msBWT) approach.
- **Rust Implementation**: Rewritten in Rust for improved performance and memory efficiency compared to the original C++ fmlrc.
- **msBWT Index**: Constructs an index from short reads (Illumina) to serve as a reference for error correction of long reads.
- **Streaming Correction**: Processes long reads in a streaming fashion, minimizing memory footprint during correction.
- **Quality-aware Correction**: Takes base quality scores into account when determining correct bases during alignment.

## Pitfalls
- **Short Read Requirement**: Requires high-quality short reads (Illumina) as input for building the correction index.
- **Memory Requirements**: Building the msBWT index can be memory-intensive for large datasets.
- **K-mer Size Selection**: Default k-mer size may not be optimal for all datasets; needs tuning based on read length and error rate.
- **Output Format**: Default output is in FASTA format; users needing FASTQ with quality scores must use appropriate flags.
- **Reference Bias**: Correction is biased towards the short read index, potentially introducing systematic errors.

## Examples
### Build index and correct long reads
**Args:** `fmlrc2 build -r short_reads.fastq -o index.msbwt && fmlrc2 correct -i index.msbwt -l long_reads.fastq -o corrected.fastq`
**Explanation:** Builds an msBWT index from short reads and uses it to correct errors in long reads, producing corrected output.

### Correct with quality trimming
**Args:** `fmlrc2 correct -i index.msbwt -l long_reads.fastq -o corrected.fastq -q 10`
**Explanation:** Corrects long reads with a minimum quality threshold of 10, trimming low-quality regions before correction.

### Build index with specific k-mer size
**Args:** `fmlrc2 build -r short_reads.fastq -o index.msbwt -k 31`
**Explanation:** Builds an msBWT index using k-mer size 31, suitable for longer reads or higher error rates.

### Stream correction from stdin
**Args:** `cat long_reads.fastq | fmlrc2 correct -i index.msbwt -l /dev/stdin -o -`
**Explanation:** Reads long reads from stdin and writes corrected reads to stdout, useful for pipeline integration.

### Generate stats during correction
**Args:** `fmlrc2 correct -i index.msbwt -l long_reads.fastq -o corrected.fastq --stats`
**Explanation:** Outputs correction statistics including number of corrections made and error rate reduction.