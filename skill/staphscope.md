---
name: staphscope
category: typing
description: Advanced Staphylococcus aureus Typing & Lineage Analysis Platform.
tags: [staphscope, staphylococcus, typing, lineage-analysis]
author: oxo-call-community
source_url: "https://github.com/bbeckley-hub/staphscope-typing-tool"
---

## Concepts

- **Tool Overview**: staphscope (v1.2.0) is an advanced typing and lineage analysis platform for Staphylococcus aureus.
- **Core Function**: Integrates multiple typing methods including MLST, SCCmec, spa typing, and virulence gene detection.
- **Analysis Modules**: MLST typing, SCCmec typing, spa typing, agr typing, and virulence factor identification.
- **Input/Output**: Input: FASTA genome assembly; Output: Comprehensive typing report with lineage information.
- **Database Integration**: Uses curated databases for accurate typing results.
- **Installation**: `conda install -c bioconda staphscope` or download from GitHub.

## Pitfalls

- **Assembly Quality**: Poor genome assembly affects typing accuracy.
- **Database Compatibility**: Requires matching database versions for staphscope-mlst-data and staphscope-sccmec-data.
- **Novel Variants**: May miss novel alleles not in the database.
- **False Positives**: Cross-reactivity between closely related alleles may occur.
- **Memory Requirements**: Large datasets may require significant memory.
- **Computational Time**: Comprehensive typing can be computationally intensive.

## Examples

### Display help
**Args:** `staphscope --help`
**Explanation:** Shows available options and usage information.

### Basic typing
**Args:** `staphscope -i genome.fasta -o results.txt`
**Explanation:** Run comprehensive typing analysis on genome assembly.

### MLST only
**Args:** `staphscope -i genome.fasta -o mlst.txt --mlst-only`
**Explanation:** Perform only MLST typing.

### SCCmec typing
**Args:** `staphscope -i genome.fasta -o sccmec.txt --sccmec-only`
**Explanation:** Perform only SCCmec typing.

### Spa typing
**Args:** `staphscope -i genome.fasta -o spa.txt --spa-only`
**Explanation:** Perform only spa typing.

### Virulence factors
**Args:** `staphscope -i genome.fasta -o virulence.txt --virulence`
**Explanation:** Detect virulence factors in genome.

### Verbose mode
**Args:** `staphscope -i genome.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### HTML report
**Args:** `staphscope -i genome.fasta -o report.html --html`
**Explanation:** Generate HTML report with visualizations.
