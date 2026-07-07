---
name: bamcmp
category: alignment
description: bamcmp - Deconvolve host and graft reads using alignment scores
tags: [bamcmp, alignment, BAM, host-graft, deconvolution]
author: oxo-call-community
source_url: "https://github.com/CRUKMI-ComputationalBiology/bamcmp"
---

## Concepts

- **Tool Overview**: bamcmp deconvolves host and graft reads from mixed sequencing data using full-length alignments and their scores. Version 2.2.
- **Core Function**: Separates reads originating from host versus graft/tumor in transplantation or cancer sequencing experiments.
- **Alignment Scoring**: Uses alignment quality scores to distinguish between host and graft sequences.
- **Full-Length Analysis**: Analyzes complete read alignments for accurate classification.
- **Mixed Data Handling**: Designed for samples with mixed host and donor/graft DNA.
- **Input/Output**: Accepts BAM alignment files, outputs separated alignments or classification statistics.
- **Installation**: `conda install -c bioconda bamcmp`.

## Pitfalls

- **Reference Quality**: Requires high-quality reference sequences for both host and graft.
- **Alignment Quality**: Poor alignments lead to incorrect classification.
- **Mixing Proportions**: Very low proportions of graft DNA may be missed.
- **Contamination**: Contaminating sequences can affect classification accuracy.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Basic host-graft separation
**Args:** `bamcmp -i alignments.bam -H host_ref.fasta -G graft_ref.fasta -o separated/`
**Explanation:** Separates reads into host and graft based on alignment scores.

### Output statistics only
**Args:** `bamcmp -i alignments.bam -H host_ref.fasta -G graft_ref.fasta -s stats.txt`
**Explanation:** Generates classification statistics without separating BAM.

### Custom score threshold
**Args:** `bamcmp -i alignments.bam -H host_ref.fasta -G graft_ref.fasta -t 0.8 -o separated/`
**Explanation:** Uses custom similarity threshold of 0.8 for classification.

### Verbose mode
**Args:** `bamcmp -i alignments.bam -H host_ref.fasta -G graft_ref.fasta -v -o separated/`
**Explanation:** Shows detailed classification information.

### Single output BAM
**Args:** `bamcmp -i alignments.bam -H host_ref.fasta -G graft_ref.fasta --graft-only -o graft.bam`
**Explanation:** Outputs only graft reads to single BAM file.

### Paired-end processing
**Args:** `bamcmp -i alignments.bam -H host_ref.fasta -G graft_ref.fasta --paired -o separated/`
**Explanation:** Processes paired-end reads ensuring consistent classification.

### Display help
**Args:** `bamcmp --help`
**Explanation:** Shows all available command-line options and usage information.