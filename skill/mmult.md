---
name: mmult
category: alignment
description: Multiple sample analysis from large-scale WGBS data
tags: [mmult, alignment, methylation]
author: oxo-call-community
source_url: "https://github.com/lijinbio/MMULT"
---

## Concepts

- **Tool Overview**: mmult v0.0.0.2 performs multiple sample analysis from WGBS data.
- **Core Function**: Analyzes large-scale whole-genome bisulfite sequencing data.
- **WGBS Analysis**: Processes bisulfite sequencing for methylation analysis.
- **Multi-sample**: Supports analysis of multiple samples simultaneously.
- **Input/Output**: Accepts BAM files; outputs methylation calls.
- **Epigenomics**: Supports DNA methylation analysis workflows.

## Pitfalls

- **WGBS Specific**: Designed for bisulfite sequencing data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal analysis.
- **Data Quality**: Results depend on sequencing quality.
- **Computational Resources**: Large-scale analysis requires significant resources.
- **Reference Genome**: Requires appropriate reference genome.

## Examples

### Analyze WGBS data
**Args:** `mmult -i alignments.bam -g genome.fasta -o methylation.txt`
**Explanation:** Analyzes WGBS data for methylation.

### Multi-sample analysis
**Args:** `mmult -i sample1.bam,sample2.bam -g genome.fasta -o results/`
**Explanation:** Analyzes multiple samples simultaneously.

### With quality filtering
**Args:** `mmult -i alignments.bam -g genome.fasta -q -o methylation.txt`
**Explanation:** Applies quality filtering.

### Output in BED format
**Args:** `mmult -i alignments.bam -g genome.fasta -f bed -o methylation.bed`
**Explanation:** Outputs methylation calls in BED format.

### Batch processing
**Args:** `mmult -i bam/ -g genome.fasta -o results/`
**Explanation:** Processes multiple BAM files.