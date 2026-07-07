---
name: microhapulator
category: variant-calling
description: Tools for empirical microhaplotype calling, forensic interpretation, and simulation.
tags: [microhapulator, variant-calling, forensics]
author: oxo-call-community
source_url: "https://github.com/bioforensics/MicroHapulator/"
---

## Concepts

- **Tool Overview**: MicroHapulator v0.8.4 provides tools for microhaplotype calling and forensic interpretation.
- **Core Function**: Calls microhaplotypes from sequencing data for forensic analysis.
- **Microhaplotype Calling**: Identifies microhaplotype alleles from sequence reads.
- **Forensic Interpretation**: Supports forensic DNA analysis workflows.
- **Input/Output**: Accepts sequencing data; outputs microhaplotype calls.
- **Simulation**: Enables simulation of microhaplotype data.

## Pitfalls

- **Forensic Specific**: Designed for forensic applications.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Calling accuracy depends on input data quality.
- **Population Data**: Requires population allele frequency data.

## Examples

### Call microhaplotypes
**Args:** `microhapulator call -i reads.bam -o calls.txt`
**Explanation:** Calls microhaplotypes from sequencing data.

### Forensic interpretation
**Args:** `microhapulator interpret -i calls.txt -o report.txt`
**Explanation:** Generates forensic interpretation report.

### Simulate microhaplotypes
**Args:** `microhapulator simulate -n 100 -o simulated.txt`
**Explanation:** Simulates microhaplotype data.

### Batch processing
**Args:** `microhapulator batch -i bam/ -o results/`
**Explanation:** Processes multiple samples in batch mode.

### Generate visualization
**Args:** `microhapulator visualize -i calls.txt -o plot.png`
**Explanation:** Generates visualization of microhaplotype calls.