---
name: ccsmeth
category: epigenomics
description: Detecting DNA methylation from PacBio CCS reads
tags: [ccsmeth, methylation, pacbio, ccs, epigenomics]
author: oxo-call-community
source_url: "https://github.com/PengNi/ccsmeth"
---

## Concepts

- **Tool Overview**: ccsmeth detects DNA methylation from PacBio Circular Consensus Sequencing (CCS) reads.
- **Core Function**: Calls 5mC and 6mA methylation from PacBio HiFi/CCS data.
- **Algorithm**: Uses deep learning model trained on PacBio kinetic signals.
- **Input**: PacBio CCS BAM file.
- **Output**: Methylation calls in bedGraph or allC format.
- **Application**: Epigenomics studies using PacBio long-read sequencing.
- **Installation**: Install via bioconda: `conda install -c bioconda ccsmeth`

## Pitfalls

- **CCS Required**: Requires PacBio CCS/HiFi reads, not subreads.
- **Model Files**: Downloads pre-trained models automatically.
- **Memory Usage**: Large BAM files require significant memory.
- **Strand Information**: Properly handles strand-specific methylation.

## Examples

### Call methylation from CCS BAM
**Args:** `ccsmeth call_mods --input ccs.bam --reference genome.fa --output methylation.tsv`
**Explanation:** Calls methylation from PacBio CCS reads aligned to reference.

### Output bedGraph format
**Args:** `ccsmeth call_mods --input ccs.bam --reference genome.fa --output methylation.bedGraph --out_format bedGraph`
**Explanation:** Outputs methylation calls in bedGraph format.

### Set minimum coverage
**Args:** `ccsmeth call_mods --input ccs.bam --reference genome.fa --output calls.tsv --min_cov 5`
**Explanation:** Requires minimum 5x coverage for methylation calling.

### Display help
**Args:** `ccsmeth --help`
**Explanation:** Shows all available options and usage information.
