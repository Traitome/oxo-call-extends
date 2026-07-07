---
name: modifi
category: variant-calling
description: DNA modification detection from PacBio SMRT metagenomic data
tags: [modifi, variant-calling, methylation]
author: oxo-call-community
source_url: "https://github.com/sachdevalab/MODIFI"
---

## Concepts

- **Tool Overview**: MODIFI v0.0.3 detects DNA modifications from PacBio metagenomic data.
- **Core Function**: Identifies DNA base modifications and host-MGE linkages.
- **PacBio Support**: Works with both subreads and HiFi reads.
- **Motif Discovery**: Discovers modification motifs in sequences.
- **Host-MGE Association**: Links modifications to mobile genetic elements.
- **Input/Output**: Accepts BAM files; outputs modification calls.

## Pitfalls

- **PacBio Specific**: Designed for PacBio SMRT sequencing data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on sequencing quality.
- **Motif Discovery**: Requires sufficient sequencing depth.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Detect modifications
**Args:** `modifi -i alignments.bam -o modifications.txt`
**Explanation:** Detects DNA modifications from PacBio data.

### With motif discovery
**Args:** `modifi -i alignments.bam -m -o modifications.txt`
**Explanation:** Enables motif discovery.

### For HiFi reads
**Args:** `modifi -i alignments.bam -t hifi -o modifications.txt`
**Explanation:** Optimized for HiFi sequencing data.

### With host-MGE analysis
**Args:** `modifi -i alignments.bam -a -o modifications.txt`
**Explanation:** Performs host-MGE association analysis.

### Batch processing
**Args:** `modifi -i bam/ -o results/`
**Explanation:** Processes multiple BAM files.