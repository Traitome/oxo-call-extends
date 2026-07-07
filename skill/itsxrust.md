---
name: itsxrust
category: utility
description: HMMER-based ITS subregion extraction for long-read fungal metabarcoding.
tags: [itsxrust, utility, ITS, fungal, metabarcoding]
author: oxo-call-community
source_url: "https://github.com/ayobi/ITSxRust"
---

## Concepts

- **Tool Overview**: itsxrust (v0.2.2) - A Rust implementation of ITSx for extracting ITS subregions (ITS1, 5.8S, ITS2) from long-read sequencing data, optimized for fungal metabarcoding.
- **ITS Subregions**: The Internal Transcribed Spacer (ITS) region consists of ITS1, 5.8S rRNA gene, and ITS2. itsxrust identifies and extracts these regions using HMMER profiles.
- **Long-read Support**: Specifically designed for Oxford Nanopore and PacBio long-read data, handling reads spanning several kilobases.
- **HMMER Integration**: Uses hidden Markov models (HMMs) to accurately identify conserved rRNA gene boundaries.
- **Multi-threading**: Leverages Rust's concurrency model for fast processing of large datasets.
- **Output Formats**: Generates FASTA sequences for each ITS subregion separately or concatenated.

## Pitfalls

- **Read Length Variation**: Very short reads may fail to contain complete ITS regions, leading to partial extractions.
- **Quality Thresholds**: Low-quality base calls at region boundaries can affect accurate identification.
- **Non-fungal Sequences**: May misclassify non-target sequences if input contains mixed organism types.
- **HMM Model Selection**: Using inappropriate HMM profiles can reduce extraction accuracy.
- **Memory Usage**: Processing extremely large datasets may require significant RAM.
- **Overlapping Regions**: Ambiguous boundaries between ITS1/5.8S/ITS2 can cause inconsistent results.

## Examples

### Basic ITS extraction
**Args:** `itsxrust -i input.fastq -o output/`
**Explanation:** Extracts ITS regions from long-read FASTQ file and writes results to output directory.

### Extract specific subregions
**Args:** `itsxrust -i reads.fasta --regions ITS1,ITS2 -o results/`
**Explanation:** Only extracts ITS1 and ITS2 regions, excluding the 5.8S rRNA gene.

### Adjust quality threshold
**Args:** `itsxrust -i input.fastq -o output/ --min-quality 15`
**Explanation:** Sets minimum Phred quality score to 15 for base calling at boundaries.

### Multi-threaded processing
**Args:** `itsxrust -i input.fastq -o output/ --threads 8`
**Explanation:** Uses 8 threads for parallel processing to speed up analysis.

### Output concatenated sequences
**Args:** `itsxrust -i input.fastq -o output/ --concatenate`
**Explanation:** Concatenates ITS1+5.8S+ITS2 into single sequences instead of separate files.

### Filter by length
**Args:** `itsxrust -i input.fastq -o output/ --min-length 200 --max-length 1500`
**Explanation:** Filters output sequences to be between 200-1500 bp in length.