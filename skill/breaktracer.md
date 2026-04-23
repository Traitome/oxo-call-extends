---
name: breaktracer
category: variant-calling
description: Tracing inserted sequence fragments at structural variant breakpoints using long-reads
tags: [breaktracer, sv, structural-variant, breakpoint, long-read]
author: oxo-call-community
source_url: "https://github.com/tobiasrausch/breaktracer"
---

## Concepts

- **Tool Overview**: Breaktracer traces inserted sequence fragments at structural variant breakpoints.
- **Core Function**: Identifies and characterizes inserted sequences at SV breakpoints using long reads.
- **Input**: Long-read alignment BAM file and SV calls.
- **Output**: Annotated SV breakpoints with inserted sequence information.
- **Application**: Characterization of complex structural variants.
- **Installation**: Install via bioconda: `conda install -c bioconda breaktracer`

## Pitfalls

- **Long Reads Required**: Designed for PacBio or ONT long-read data.
- **SV Calls Needed**: Requires pre-called structural variants as input.
- **Reference Genome**: Must provide same reference used for alignment.

## Examples

### Trace inserted sequences
**Args:** `breaktracer -b long_reads.bam -v svs.vcf -r reference.fa -o traced_svs.vcf`
**Explanation:** Traces inserted sequences at SV breakpoints from long-read data.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
