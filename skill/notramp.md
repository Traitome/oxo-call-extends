---
name: notramp
category: alignment
description: Super-fast Normalization and Trimming for Amplicon Sequencing Data (Long- and Short-read)
tags: [notramp, alignment]
author: oxo-call-community
source_url: "https://github.com/simakro/NoTrAmp.git"
---

## Concepts
- **Tool Overview**: NoTrAmp is a Tool for super fast trimming and read-depth normalization of amplicon reads. It is designed to be used in amplicon-tiling panels (or similar multiplexed amplicon sequencing approaches) to cap coverage of each amplicon (if desired) and to trim amplicons to their appropriate length removing barcodes, adpaters and primers (if desired) in a single clipping step.  NoTrAmp is suitable for use with both long (e.g. ONT/PacBio) and short reads (e.g Illumina). When using reads that are significantly shorter than amplicon sizes, you should adjust the minimum required alignment length using the --set_min_len argument.  See the projects [home](https://github.com/simakro/NoTrAmp) for usage and additional documentation.
- **Core Function**: Processes bioinformatics data for alignment tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda notramp`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
