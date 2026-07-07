---
name: juicertools
category: utility
description: Visualization and analysis software for Hi-C data.
tags: [juicertools, utility, Hi-C, visualization, genomics]
author: oxo-call-community
source_url: "https://github.com/aidenlab/Juicebox"
---

## Concepts

- **Tool Overview**: juicertools (v2.20.00) - A comprehensive tool for Hi-C data visualization and analysis from Aiden Lab.
- **Hi-C Visualization**: Interactive visualization of Hi-C contact maps.
- **Matrix Operations**: Performs operations on Hi-C contact matrices.
- **Compartment Analysis**: Identifies A/B compartments from Hi-C data.
- **TAD Calling**: Detects topologically associating domains.
- **Visualization Modes**: Supports multiple visualization modes for Hi-C data.

## Pitfalls

- **Memory Usage**: Large Hi-C datasets require significant memory.
- **File Size**: Hi-C files can be very large (GBs).
- **Resolution**: Higher resolution requires more computational resources.
- **Normalization**: Different normalization methods affect visualization.
- **Java Version**: Requires specific Java version for optimal performance.
- **Display Requirements**: Interactive visualization requires modern graphics.

## Examples

### Convert fastq to Hi-C
**Args:** `juicertools pre -s MboI -o hic.hic reads.fastq`
**Explanation:** Processes FASTQ reads into Hi-C contact matrix.

### Extract observed/expected matrix
**Args:** `juicertools dump observed KR hic.hic chr1:1-1000000 chr1:1-1000000 BP 10000 output.txt`
**Explanation:** Extracts observed/expected matrix for specified region.

### Call TADs
**Args:** `juicertools arrowhead -c chr1 -m 10000 hic.hic tads/`
**Explanation:** Calls TADs using Arrowhead algorithm.

### Find compartments
**Args:** `juicertools eigenvector -p 10000 hic.hic compartments/`
**Explanation:** Computes eigenvectors to identify A/B compartments.

### Aggregate peak analysis
**Args:** `juicertools apa -o apa_results/ hic.hic peaks.bed`
**Explanation:** Performs aggregate peak analysis.

### Convert to cooler format
**Args:** `juicertools hic2cool hic.hic output.cool`
**Explanation:** Converts .hic file to cooler format.