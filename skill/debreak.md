---
name: debreak
category: annotation
description: DeBreak - deciphering exact breakpoints of structural variations using long sequencing reads.
tags: [debreak, annotation, structural-variation, long-reads, breakpoint-detection]
author: oxo-call-community
source_url: "https://github.com/ChongLab/DeBreak"
---

## Concepts

- **Tool Overview**: debreak (v1.3+) is a tool for precisely determining the breakpoints of structural variations using long sequencing reads. It identifies exact breakpoints at single-nucleotide resolution.
- **Core Function**: Analyzes long-read alignments to identify and precisely map structural variation breakpoints, including deletions, insertions, inversions, and translocations.
- **Input/Output**: Input: Aligned BAM file, reference genome. Output: Breakpoint coordinates, variant types, confidence scores, visualization data.
- **Algorithm**: Uses split-read alignment analysis, soft-clipped read detection, and local assembly to precisely determine breakpoint positions.
- **Key Features**: Single-nucleotide resolution, supports multiple variant types, confidence scoring, visualization output, compatible with PacBio and ONT reads.
- **Installation**: `conda install -c bioconda debreak`

## Pitfalls

- **Read Quality**: Requires high-quality long reads for accurate breakpoint detection.
- **Complex Variants**: Complex nested variants may be difficult to resolve.
- **Repeat Regions**: Breakpoints in repeat regions may be ambiguous.
- **Alignment Quality**: Depends on high-quality alignments from minimap2 or NGMLR.
- **Memory Usage**: Large genomes may require significant memory.

## Examples

### Detect breakpoints from BAM
**Args:** `debreak -i aligned.bam -r reference.fasta -o breakpoints.vcf`
**Explanation:** Detect structural variation breakpoints from aligned long reads.

### Specify minimum read support
**Args:** `debreak -i aligned.bam -r reference.fasta -o breakpoints.vcf -m 5`
**Explanation:** Require at least 5 reads supporting each breakpoint.

### Generate visualization
**Args:** `debreak -i aligned.bam -r reference.fasta -o breakpoints.vcf --visualize`
**Explanation:** Generate breakpoint visualization data.