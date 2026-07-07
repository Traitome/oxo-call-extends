---
name: structureharvester
category: analysis
description: structureHarvester.py extracts relevant data from STRUCTURE results files.
tags: [structureharvester, population-genetics, structure-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/"
---

## Concepts

- **Tool Overview**: structureharvester (v0.6.94) is a Python script for extracting and analyzing STRUCTURE population genetics results.
- **Core Function**: Parses STRUCTURE output files and generates summary statistics and visualizations.
- **Algorithm**: Reads STRUCTURE results files and computes statistics like delta K for optimal K selection.
- **Input/Output**: Input: STRUCTURE output files; Output: Summary statistics and visualization files.
- **Applications**: Population genetics, population structure analysis, admixture analysis.
- **Installation**: `conda install -c bioconda structureharvester` or download from website.

## Pitfalls

- **Input Format**: Requires specific STRUCTURE output format.
- **Version Compatibility**: May not work with all STRUCTURE versions.
- **Memory Requirements**: Large result files require significant memory.
- **Computational Time**: Processing large result sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect analysis results.
- **Delta K Calculation**: Delta K may not always identify optimal K correctly.

## Examples

### Display help
**Args:** `structureharvester --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `structureharvester -i structure_results/ -o analysis/`
**Explanation:** Analyze STRUCTURE results from directory.

### With PLINK format
**Args:** `structureharvester -i structure_results/ -o analysis/ --plink`
**Explanation:** Process PLINK-formatted STRUCTURE output.

### Verbose mode
**Args:** `structureharvester -i structure_results/ -o analysis/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output Evanno table
**Args:** `structureharvester -i structure_results/ -o analysis/ --evanno`
**Explanation:** Generate Evanno table for delta K analysis.

### Batch processing
**Args:** `structureharvester -i results_dir/ -o analyses/`
**Explanation:** Process multiple STRUCTURE result directories together.

### Filter by K range
**Args:** `structureharvester -i structure_results/ -o analysis/ -k 2-10`
**Explanation:** Analyze results for K values from 2 to 10.

### Include plots
**Args:** `structureharvester -i structure_results/ -o analysis/ --plot`
**Explanation:** Generate visualization plots.

### Generate report
**Args:** `structureharvester -i structure_results/ -o analysis/ --report`
**Explanation:** Generate comprehensive HTML report.
