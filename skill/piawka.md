---
name: piawka
category: population-genomics
description: The powerful AWK script to calculate population statistics in VCF files with support for varying ploidy and missing data
tags: [piawka, population-genomics]
author: oxo-call-community
source_url: "https://github.com/novikovalab/piawka"
---

## Concepts
- **Tool Overview**: The powerful awk script to calculate π, Dxy (or πxy, or Nei's D) and some more simple stats (Fst, Tajima's D, Ronfort's rho) in VCF files in the command line. Developed to analyze arbitrary-ploidy groups with substantial amounts of missing data. Largely inspired by https://github.com/ksamuk/pixy
- **Core Function**: The powerful AWK script to calculate population statistics in VCF files with support for varying ploidy and missing data
- **Input/Output**: BAM/SAM/VCF
- **Installation**: `conda install -c bioconda piawka`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
