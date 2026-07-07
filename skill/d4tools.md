---
name: d4tools
category: utility
description: The D4 command line utility program for quantitative genomics data storage and analysis.
tags: [d4tools, utility, genomics, d4-format, bam, cram, bigwig, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/38/d4-format/blob/v0.3.11/README.md"
---

## Concepts

- **Tool Overview**: d4tools (v0.3.11+) is a suite of command-line utilities for the D4 (Dense Depth Data Dump) format, an alternative to BigWig for fast analysis and compact storage of quantitative genomics data.
- **Core Function**: Converts BAM/CRAM/BigWig/BedGraph files to D4 format, and provides tools for querying, viewing, and analyzing D4 files with fast random access.
- **Input/Output**: Input: BAM, CRAM, BigWig, BedGraph files. Output: D4 files (.d4), BedGraph format text output.
- **Key Features**: Random access, multiple tracks support, HTTP range requests, statistics on arbitrary genome intervals.
- **Compression**: Adaptive encoding with deflate compression for optimal file size.
- **Installation**: `conda install -c bioconda d4tools` or `cargo install d4tools`

## Pitfalls

- **CRAM Reference**: When converting CRAM files, must provide reference genome with `-r` flag.
- **Genome File**: BedGraph input requires a genome description file with `-g` flag.
- **Dict Specification**: Use `-A` for automatic dictionary determination or `-R` for manual specification.
- **Thread Count**: Specify `-t` for multi-threaded processing to speed up large files.
- **Output Directory**: Ensure output directory exists when using `d4tools view` with file output.

## Examples

### Create D4 file from BAM
**Args:** `create -Az input.bam output.d4`
**Explanation:** Convert a BAM file to D4 format with automatic dictionary detection and deflate compression.

### Create D4 file from CRAM with reference
**Args:** `create -Azr hg19.fa.fai input.cram output.d4`
**Explanation:** Convert CRAM to D4 using reference genome index for decompression.

### Create D4 file from BigWig
**Args:** `create -z input.bw output.d4`
**Explanation:** Convert a BigWig file to D4 format with deflate compression.

### Create D4 file from BedGraph
**Args:** `create -z -g hg19.genome input.bedgraph output.d4`
**Explanation:** Convert BedGraph to D4 with genome description file for chromosome sizes.

### View D4 file content
**Args:** `view output.d4`
**Explanation:** Convert D4 file back to BedGraph format and print to stdout.

### Query specific genomic region
**Args:** `view output.d4 chr1:1000000-2000000`
**Explanation:** Extract depth values from a specific genomic interval.

### Show genome information
**Args:** `view -g output.d4`
**Explanation:** Display the genome/chromosome information stored in the D4 file.

### Multi-threaded conversion
**Args:** `create -Az -t 8 input.bam output.d4`
**Explanation:** Use 8 threads for faster conversion of large BAM files.
