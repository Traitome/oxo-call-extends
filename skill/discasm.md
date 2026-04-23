---
name: discasm
category: assembly
description: DISCASM - extract discordant reads and perform de novo transcriptome assembly.
tags: [discasm, assembly, transcriptome, discordant-reads, fusion]
author: oxo-call-community
source_url: "https://github.com/DISCASM/DISCASM"
---

## Concepts

- **Tool Overview**: DISCASM v0.1.3 - Tool for extracting discordant reads and performing de novo transcriptome assembly.
- **Core Function**: Extracts discordantly mapped and unmapped reads from STAR output, then assembles them using Trinity or Oases.
- **Input/Output**: Expects STAR/STAR-Fusion output; outputs de novo assembled transcripts from discordant reads.
- **Installation**: `conda install -c bioconda discasm`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires STAR alignment output (Chimeric.out.junction files).

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `discasm --star_dir star_output/ --output discasm_results/`
**Explanation:** Extracts discordant reads and assembles transcripts.
