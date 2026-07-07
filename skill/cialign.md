---
name: cialign
category: alignment
description: Toolkit for cleaning and interpreting multiple sequence alignments
tags: [cialign, alignment, msa, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/KatyBrown/CIAlign"
---

## Concepts

- **Tool Overview**: CIAlign is a toolkit for cleaning and interpreting multiple sequence alignments (MSAs).
- **Core Function**: Cleans alignments by removing poor quality regions and provides tools for MSA interpretation.
- **Features**: Alignment cleaning, gap handling, quality assessment, and visualization.
- **Input**: Multiple sequence alignment in FASTA, Clustal, or PHYLIP format.
- **Output**: Cleaned alignment and various statistics/visualizations.
- **Application**: Phylogenetics, sequence analysis, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cialign`

## Pitfalls

- **Alignment Quality**: Requires good quality input alignments.
- **Gap Handling**: Poorly handled gaps can affect downstream analysis.
- **Sequence Divergence**: May struggle with highly divergent sequences.
- **Memory Usage**: May require significant memory for large alignments.
- **Parameter Tuning**: Requires careful parameter selection for optimal results.

## Examples

### Clean alignment
**Args:** `cialign -i alignment.fasta -o cleaned.fasta`
**Explanation:** Cleans multiple sequence alignment.

### Assess alignment quality
**Args:** `cialign -i alignment.fasta --assess -o quality_report.txt`
**Explanation:** Generates quality assessment report.

### Remove columns
**Args:** `cialign -i alignment.fasta --remove-columns 1-100 -o trimmed.fasta`
**Explanation:** Removes specified columns from alignment.

### Display help
**Args:** `cialign --help`
**Explanation:** Shows all available options and usage information.