---
name: msaboot
category: alignment
description: Generate bootstrapping replicates for multiple sequence alignment data.
tags: [msaboot, alignment, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/phac-nml/msaboot"
---

## Concepts

- **Tool Overview**: MSAboot v0.1.2 generates bootstrap replicates for MSA validation.
- **Core Function**: Creates bootstrapped versions of sequence alignments.
- **Bootstrap Sampling**: Resamples columns from original alignment.
- **Statistical Support**: Provides confidence measures for phylogenetic trees.
- **Phylogenetic Analysis**: Supports downstream phylogenetic inference.
- **Input/Output**: Accepts alignments; outputs bootstrap replicates.

## Pitfalls

- **Alignment Required**: Requires pre-computed multiple sequence alignment.
- **Memory Requirements**: Memory usage depends on alignment size.
- **Parameter Tuning**: May require parameter adjustment for replicates.
- **Replicate Count**: More replicates provide better estimates.
- **Computational Resources**: Large alignments may require significant resources.
- **Data Quality**: Results depend on original alignment quality.

## Examples

### Generate bootstrap replicates
**Args:** `msaboot -i alignment.fasta -n 100 -o bootstrap/`
**Explanation:** Generates 100 bootstrap replicates.

### With custom output format
**Args:** `msaboot -i alignment.fasta -n 100 -f phylip -o bootstrap/`
**Explanation:** Outputs in PHYLIP format.

### Parallel processing
**Args:** `msaboot -i alignment.fasta -n 100 -t 4 -o bootstrap/`
**Explanation:** Uses 4 threads for generation.

### Generate consensus
**Args:** `msaboot -i bootstrap/ -c -o consensus.fasta`
**Explanation:** Creates consensus from replicates.

### Batch processing
**Args:** `msaboot -i fasta/ -n 100 -o results/`
**Explanation:** Processes multiple alignment files.