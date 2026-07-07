---
name: fastquast
category: qc
description: "Fast and simple Quality Assessment Tool for Large Genomes"
tags: [fastquast, qc, genome-assembly, quality-assessment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/aglabx/fastQuast"
---

## Concepts

- **Tool Overview**: fastQuast is a fast and simple quality assessment tool specifically designed for large genome assemblies.
- **Core Function**: Evaluates genome assembly quality using various metrics.
- **Input/Output**: Input: Genome assembly (FASTA). Output: Quality reports, statistics.
- **Algorithm**: Implements efficient quality assessment algorithms for large datasets.
- **Key Features**: Fast processing, large genome support, comprehensive metrics, HTML reports, visualizations.
- **Installation**: `conda install -c bioconda fastquast`

## Pitfalls

- **Memory Usage**: Large genomes may require significant memory.
- **Assembly Quality**: Results depend on input assembly quality.
- **Reference Genome**: May require reference genome for comparison.
- **Computation Time**: Very large genomes may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic quality assessment
**Args:** `fastquast -i assembly.fasta -o results/`
**Explanation:** Evaluates genome assembly quality.

### With reference
**Args:** `fastquast -i assembly.fasta -r reference.fasta -o results/`
**Explanation:** Compares assembly against reference genome.

### Generate HTML report
**Args:** `fastquast -i assembly.fasta -o results/ --html`
**Explanation:** Generates HTML quality report.

### Quality thresholds
**Args:** `fastquast -i assembly.fasta -o results/ -q 30`
**Explanation:** Sets minimum quality threshold.

### Verbose mode
**Args:** `fastquast -i assembly.fasta -o results/ -v`
**Explanation:** Shows detailed progress information.