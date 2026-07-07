---
name: assemblycomparator2
category: assembly
description: AssemblyComparator2 - Genome assembly comparison and reporting pipeline
tags: [assemblycomparator2, assembly, comparison, reporting, genomics]
author: oxo-call-community
source_url: "https://assemblycomparator2.readthedocs.io/"
---

## Concepts

- **Tool Overview**: AssemblyComparator2 is a comprehensive pipeline for comparing multiple genome assemblies and generating detailed comparison reports. Version 2.7.1.
- **Core Function**: Compares multiple genome assemblies against reference genomes, identifies structural variations, and generates comprehensive reports.
- **Multi-Assembly Comparison**: Supports comparison of multiple assemblies simultaneously for comparative analysis.
- **Reference Alignment**: Aligns assemblies to reference genomes to identify differences and similarities.
- **Variant Detection**: Identifies structural variants, SNPs, and indels between assemblies.
- **Report Generation**: Creates detailed HTML reports with visualizations of assembly comparisons.
- **Quality Assessment**: Evaluates assembly quality metrics and compares across assemblies.
- **Input/Output**: Accepts FASTA assemblies and reference genomes, outputs comparison reports and variant calls.
- **Installation**: `conda install -c bioconda assemblycomparator2` or install from GitHub.

## Pitfalls

- **Reference Genome**: Requires high-quality reference genome for meaningful comparison.
- **Assembly Quality**: Poor quality assemblies produce unreliable comparison results.
- **Memory Requirements**: Comparing large genomes requires significant memory resources.
- **Alignment Time**: Comparison of multiple large assemblies can be computationally intensive.
- **Contig Naming**: Assemblies should use consistent contig naming conventions for accurate comparison.
- **Report Interpretation**: Complex reports require careful interpretation of comparison metrics.

## Examples

### Display help
**Args:** `assemblycomparator2 --help`
**Explanation:** Shows all available command-line options and usage information.

### Compare two assemblies
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm1.fasta asm2.fasta --output report/`
**Explanation:** Compares two assemblies against reference genome and generates comparison report.

### Compare multiple assemblies
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm1.fasta asm2.fasta asm3.fasta --output report/`
**Explanation:** Compares three assemblies simultaneously against common reference.

### Generate variant calls
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm.fasta --output report/ --variants variants.vcf`
**Explanation:** Identifies variants between assembly and reference, outputs VCF file.

### Set minimum alignment length
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm.fasta --output report/ --min-length 1000`
**Explanation:** Ignores alignments shorter than 1000bp. Reduces noise from small contigs.

### Enable structural variant detection
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm.fasta --output report/ --sv-detection`
**Explanation:** Enables structural variant detection mode for comprehensive comparison.

### Generate visual report
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm.fasta --output report/ --visual-report`
**Explanation:** Generates HTML report with interactive visualizations of assembly comparisons.

### Specify output format
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm.fasta --output report/ --format html,pdf`
**Explanation:** Generates reports in both HTML and PDF formats.

### Run quality assessment
**Args:** `assemblycomparator2 --reference ref.fasta --assemblies asm.fasta --output report/ --quality-assessment`
**Explanation:** Includes comprehensive quality assessment metrics in the report.