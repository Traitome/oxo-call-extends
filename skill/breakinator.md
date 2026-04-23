---
name: breakinator
category: qc
description: Detection of foldback and chimeric read artifacts in SAM/BAM/CRAM and PAF files
tags: [breakinator, artifact, qc, chimeric, foldback]
author: oxo-call-community
source_url: "https://github.com/jheinz27/breakinator"
---

## Concepts

- **Tool Overview**: Breakinator detects foldback and chimeric read artifacts in alignment files.
- **Core Function**: Identifies sequencing artifacts that can affect downstream analysis.
- **Input**: SAM/BAM/CRAM alignment files or PAF files.
- **Output**: Artifact report and flagged reads.
- **Application**: Quality control for long-read and linked-read sequencing.
- **Installation**: Install via bioconda: `conda install -c bioconda breakinator`

## Pitfalls

- **File Format**: Supports SAM/BAM/CRAM and PAF formats.
- **Artifact Types**: Specifically detects foldback and chimeric artifacts.
- **Output Interpretation**: High artifact rates indicate library preparation issues.

## Examples

### Detect artifacts in BAM
**Args:** `breakinator -i aligned.bam -o artifacts.tsv`
**Explanation:** Identifies foldback and chimeric read artifacts in BAM file.

### Process PAF file
**Args:** `breakinator -i alignments.paf -o artifacts.tsv`
**Explanation:** Detects artifacts in PAF alignment file.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
