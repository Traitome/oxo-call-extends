---
name: chexalign
category: chip-seq
description: Alignment and quantification of ChIP-exo crosslinking patterns
tags: [chexalign, chip-exo, alignment, transcription-factors, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/seqcode/chexalign"
---

## Concepts

- **Tool Overview**: ChExAlign aligns and quantifies ChIP-exo crosslinking patterns from multiple proteins across regulatory regions.
- **Core Function**: Detects and quantifies protein-DNA crosslinking events at high resolution.
- **Algorithm**: Uses positional crosslinking information to precisely map protein binding sites.
- **Input**: ChIP-exo sequencing data and genomic regions of interest.
- **Output**: Crosslinking profiles and binding site annotations.
- **Application**: Transcription factor binding analysis, chromatin structure studies.
- **Installation**: Install via bioconda: `conda install -c bioconda chexalign`

## Pitfalls

- **Data Quality**: Requires high-quality ChIP-exo sequencing data.
- **Crosslinking Bias**: May be affected by experimental crosslinking biases.
- **Peak Calling**: Depends on appropriate peak calling parameters.
- **Genome Assembly**: Results depend on reference genome quality.
- **Replicate Consistency**: Multiple replicates recommended for reliability.

## Examples

### Align ChIP-exo reads
**Args:** `chexalign -i reads.fastq -r reference.fasta -o alignment.bed`
**Explanation:** Aligns ChIP-exo reads and outputs crosslinking positions.

### Quantify crosslinking
**Args:** `chexalign --quantify -i alignment.bed -g genes.bed -o profiles.txt`
**Explanation:** Quantifies crosslinking patterns across gene regions.

### Compare replicates
**Args:** `chexalign --compare -i rep1.bed rep2.bed -o comparison.txt`
**Explanation:** Compares crosslinking patterns between replicates.

### Display help
**Args:** `chexalign --help`
**Explanation:** Shows all available options and usage information.