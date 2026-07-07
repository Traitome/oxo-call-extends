---
name: alpaqa-bio
category: qc
description: Quality control tool for bacterial ONT-only assemblies
tags: [alpaqa-bio, assembly, QC, nanopore, ONT, bacterial, quality-control]
author: oxo-call-community
source_url: "https://pypi.org/project/alpaqa-bio/"
---

## Concepts

- **Tool Overview**: alpaqa-bio is a specialized quality control tool designed specifically for bacterial genomes assembled using Oxford Nanopore Technologies (ONT) long-read sequencing data.
- **Core Function**: Evaluates assembly quality by analyzing metrics such as N50, contig count, GC content, coverage depth, and completeness estimates to assess the reliability of ONT-only assemblies.
- **Input/Output**: Accepts FASTA-formatted assembly files and produces comprehensive QC reports in multiple formats (JSON, TSV, HTML).
- **Installation**: Available via PyPI (`pip install alpaqa-bio`) or Bioconda (`conda install -c bioconda alpaqa-bio`).
- **Quality Metrics**: Computes key assembly statistics including total length, N50/N90, L50/L90, GC percentage, number of contigs, and estimated completeness based on conserved single-copy genes.

## Pitfalls

- **Version Differences**: Command-line options and output formats may vary between versions, especially between v0.1.x releases.
- **Input Format**: Requires uncompressed FASTA input; compressed files (FASTQ.gz) will cause errors.
- **Completeness Estimation**: The tool uses a built-in database of bacterial marker genes; results may not be accurate for non-bacterial genomes.
- **Memory Requirements**: Large assemblies (>100 Mb) may require significant memory; consider splitting large inputs or using the `--memory-efficient` flag.
- **Reference Dependencies**: Some advanced features require a reference genome for comparative analysis; ensure reference files are in the correct format.

## Examples

### Basic quality assessment
**Args:** `--input assembly.fasta --output qc_report`
**Explanation:** Runs comprehensive QC on the input assembly and generates reports in the specified output directory. The `--input` flag specifies the FASTA file to analyze, while `--output` defines where results will be saved.

### Generate JSON output only
**Args:** `--input contigs.fasta --json --output results.json`
**Explanation:** Produces a machine-readable JSON report containing all QC metrics. The `--json` flag bypasses HTML and TSV generation for faster processing.

### Include comparative analysis
**Args:** `--input assembly.fasta --reference ref_genome.fasta --output qc_with_ref`
**Explanation:** Performs comparative analysis against a reference genome, including alignment statistics and structural variation detection. Requires a reference FASTA file.

### Memory-efficient mode for large assemblies
**Args:** `--input large_assembly.fasta --memory-efficient --threads 8 --output qc_report`
**Explanation:** Optimizes memory usage for large bacterial assemblies by processing contigs in batches. The `--threads` flag specifies parallel processing for faster analysis.

### Generate HTML report with visualizations
**Args:** `--input assembly.fasta --html --plots --output qc_visualization`
**Explanation:** Creates an interactive HTML report with visualizations of assembly metrics including N50 distribution, GC content plots, and contig length histograms.