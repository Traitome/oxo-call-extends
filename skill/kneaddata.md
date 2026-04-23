---
name: kneaddata
category: qc
description: KneadData is a tool designed to perform quality control on metagenomic sequencing data.
tags: [kneaddata, qc, alignment]
author: oxo-call-community
source_url: "https://huttenhower.sph.harvard.edu/kneaddata"
---

## Concepts

- **Tool Overview**: kneaddata v0.12.4 - KneadData is a tool designed to perform quality control on metagenomic sequencing data, especially data from microbiome experiments. In these experiments, samples are typically taken from a host in hopes of learning something about the microbial community on the host. However, metagenomic sequencing data from such experiments will often contain a high ratio of host to bacterial reads. This tool aims to perform principled in silico separation of bacterial reads from these "contaminant" reads, be they from the host, from bacterial 16S sequences, or other user-defined sources..
- **Core Function**: KneadData is a tool designed to perform quality control on metagenomic sequencing data.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kneaddata`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Remove host reads
**Args:** `--input reads.fastq --reference /path/to/host_db --output kneaddata_output`
**Explanation:** Removes host contamination from metagenomic reads.

