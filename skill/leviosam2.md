---
name: leviosam2
category: alignment
description: Fast and accurate coordinate conversion between genome assemblies
tags: [leviosam2, alignment, lift-over, coordinate-conversion, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/milkschen/leviosam2"
---

## Concepts

- **Coordinate Conversion**: Converts alignments between genome assemblies
- **Chain File**: Uses chain files for liftover operations
- **Fast Conversion**: High-performance alignment liftover
- **Accurate Mapping**: Preserves alignment quality during conversion
- **BAM Support**: Works directly with BAM alignment files
- **Assembly Comparison**: Enables comparison between assemblies

## Pitfalls

- **Chain File Quality**: Poor chain files lead to incorrect mappings
- **Assembly Divergence**: Highly divergent assemblies may fail
- **Ambiguous Regions**: Repeat regions cause mapping ambiguity
- **File Size**: Large BAM files require memory management
- **Version Compatibility**: Chain files need matching assembly versions
- **Unmapped Reads**: Some reads may not map to target assembly

## Examples

### Lift over alignments
**Args:** `leviosam2 lift -a aln.bam -c chain.txt -o lifted.bam`
**Explanation:** Lifts over BAM alignments using a chain file.

### Generate chain file
**Args:** `leviosam2 chain -s source.fasta -t target.fasta -o chain.txt`
**Explanation:** Creates chain file between assemblies.

### Validate mappings
**Args:** `leviosam2 validate -a lifted.bam -c chain.txt`
**Explanation:** Validates liftover accuracy.

### Chain statistics
**Args:** `leviosam2 stats -c chain.txt`
**Explanation:** Shows chain file statistics.

### Batch lift over
**Args:** `leviosam2 batch -d bams/ -c chain.txt -o results/`
**Explanation:** Processes multiple BAM files.

### SAM input
**Args:** `leviosam2 lift -a aln.sam -c chain.txt -o lifted.sam`
**Explanation:** Works with SAM format.