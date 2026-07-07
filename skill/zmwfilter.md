---
name: zmwfilter
category: sequencing
description: PacBio utility to filter reads based on ZMW (Zero-Mode Waveguide) IDs
tags: [zmwfilter, pacbio, sequencing, filtering, zmw]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbtk"
---

## Concepts

- **Tool Overview**: zmwfilter is part of the PacBio BAM Toolkit (pbtk) for filtering sequencing data
- **ZMW Filtering**: Filters reads based on Zero-Mode Waveguide (ZMW) hole numbers
- **Input/Output**: Accepts BAM, FASTA, FASTQ, and XML formats; outputs filtered files in the same format
- **Downsampling**: Supports proportional downsampling (--downsample) and count-based downsampling (--downsample-count)
- **Read Name Filtering**: Supports filtering by read names (--names) for BAM/XML only
- **Installation**: `conda install -c bioconda pbtk`

## Pitfalls

- **Format Compatibility**: Ensure input format matches expected format for filtering operations
- **ZMW Number Format**: ZMW numbers can be comma-separated list or a file with one number per line
- **Memory Usage**: Processing large BAM files may require significant memory
- **Downsample Seed**: Use --downsample-seed for reproducible random sampling
- **Read Name Filtering**: Only works with BAM/XML formats, not FASTA/FASTQ

## Examples

### Include specific ZMWs
**Args:** `zmwfilter --include 1,2,4,8,16 in.bam out.bam`
**Explanation:** Use --include with comma-separated ZMW hole numbers to keep only reads from specified ZMWs.

### Exclude specific ZMWs
**Args:** `zmwfilter --exclude hole_numbers.txt in.fasta out.fasta`
**Explanation:** Use --exclude with a file containing ZMW numbers to remove reads from those ZMWs.

### Random proportional downsampling
**Args:** `zmwfilter --downsample 0.333 in.bam out.bam`
**Explanation:** Use --downsample to randomly select 33.3% of reads from the input file.

### Count-based downsampling with seed
**Args:** `zmwfilter --downsample-count 1024 --downsample-seed 42 in.bam out.bam`
**Explanation:** Use --downsample-count to select exactly 1024 reads and --downsample-seed 42 for reproducible sampling.

### Show all ZMW numbers
**Args:** `zmwfilter --show-all in.bam > zmws.txt`
**Explanation:** Use --show-all to list all ZMW hole numbers in the input file without filtering.

### Filter by read names
**Args:** `zmwfilter --names read_names.txt in.bam out.bam`
**Explanation:** Use --names with a file containing read names to filter BAM/XML files by specific read identifiers.