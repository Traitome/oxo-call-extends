---
name: mudskipper
category: alignment
description: mudskipper is a tool for converting genomic BAM/SAM files to transcriptomic BAM/RAD files.
tags: [mudskipper, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/OceanGenomics/mudskipper"
---

## Concepts

- **Tool Overview**: mudskipper v0.1.0 - mudskipper is a tool for converting genomic BAM/SAM files to transcriptomic BAM/RAD files..
- **Core Function**: mudskipper is a tool for converting genomic BAM/SAM files to transcriptomic BAM/RAD files.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mudskipper`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Align reads
**Args:** `mudskipper align -r reference.fa -i reads.fastq -o output.sam`
**Explanation:** Aligns long reads to reference genome.

