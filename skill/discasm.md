---
name: discasm
category: assembly
description: DISCASM - Discordant read extraction and de novo transcriptome assembly.
tags: [discasm, assembly, transcriptome, discordant-reads, fusion]
author: oxo-call-community
source_url: "https://github.com/DISCASM/DISCASM"
---

## Concepts

- **Tool Overview**: DISCASM (v0.1.3+) extracts discordant reads and performs de novo transcriptome assembly.
- **Core Function**: Extracts discordantly mapped and unmapped reads from STAR output, then assembles them.
- **Input/Output**: Input: STAR alignment output (Chimeric.out.junction files). Output: De novo assembled transcripts.
- **Algorithm**: Uses Trinity or Oases for de novo assembly of discordant reads.
- **Key Features**: Discordant read extraction, fusion transcript detection, de novo assembly, supports multiple assemblers, chimeric transcript identification.
- **Installation**: `conda install -c bioconda discasm`

## Pitfalls

- **Input Requirements**: Requires STAR alignment output with chimeric junction files.
- **Assembly Quality**: Depends on read coverage and quality.
- **Computational Resources**: Assembly step requires significant resources.
- **False Positives**: May generate false fusion transcripts.
- **Memory Usage**: High memory requirements for large datasets.

## Examples

### Extract discordant reads and assemble
**Args:** `discasm --star_dir star_output/ --output discasm_results/`
**Explanation:** Extracts discordant reads and assembles transcripts.

### With specific assembler
**Args:** `discasm --star_dir star_output/ --output discasm_results/ --assembler trinity`
**Explanation:** Use Trinity assembler for de novo assembly.

### Filter by coverage
**Args:** `discasm --star_dir star_output/ --output discasm_results/ --min-coverage 5`
**Explanation:** Filter assemblies by minimum coverage.

### Generate fusion report
**Args:** `discasm --star_dir star_output/ --output discasm_results/ --fusion-report fusion.tsv`
**Explanation:** Generate report of potential fusion transcripts.

### Large dataset mode
**Args:** `discasm --star_dir star_output/ --output discasm_results/ --large`
**Explanation:** Use optimized mode for large datasets.