---
name: assembly-scan
category: assembly
description: Assembly-scan - Generate assembly summary statistics in JSON format
tags: [assembly-scan, assembly, statistics, json, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rpetit3/assembly-scan"
---

## Concepts

- **Tool Overview**: Assembly-scan is a tool for generating comprehensive assembly statistics from FASTA files and outputting results in JSON format. Version 1.0.0.
- **Core Function**: Computes assembly quality metrics and outputs them in machine-readable JSON format for easy integration into pipelines.
- **Statistics Calculation**: Computes N50, L50, total length, contig count, GC content, and other assembly metrics.
- **JSON Output**: Provides structured JSON output for programmatic access to assembly statistics.
- **Multi-File Support**: Can process multiple FASTA files simultaneously.
- **Quality Assessment**: Helps assess assembly completeness and quality through standardized metrics.
- **Input/Output**: Accepts FASTA assembly files, outputs JSON-formatted statistics.
- **Installation**: `conda install -c bioconda assembly-scan` or install from GitHub.

## Pitfalls

- **FASTA Format**: Requires properly formatted FASTA files. Invalid FASTA causes parsing errors.
- **Contig Names**: Contig names should not contain special characters that may affect JSON parsing.
- **Large Files**: Very large assemblies may require significant memory. Consider streaming for huge files.
- **Empty Files**: Empty FASTA files produce empty or incomplete statistics.
- **Ambiguity Codes**: May not handle non-standard IUPAC codes correctly.
- **JSON Parsing**: Output JSON should be validated before downstream processing.

## Examples

### Display help
**Args:** `assembly-scan --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic usage
**Args:** `assembly-scan -i assembly.fasta -o stats.json`
**Explanation:** Computes assembly statistics and saves to JSON file.

### Process multiple assemblies
**Args:** `assembly-scan -i asm1.fasta asm2.fasta asm3.fasta -o stats.json`
**Explanation:** Processes multiple FASTA files and combines statistics in single JSON output.

### Output to stdout
**Args:** `assembly-scan -i assembly.fasta`
**Explanation:** Outputs JSON statistics directly to standard output.

### Include GC content
**Args:** `assembly-scan -i assembly.fasta -o stats.json --gc`
**Explanation:** Computes and includes GC content percentage in statistics.

### Set minimum contig length
**Args:** `assembly-scan -i assembly.fasta -o stats.json --min-length 1000`
**Explanation:** Only includes contigs longer than 1000bp in statistics calculation.

### Pretty print JSON
**Args:** `assembly-scan -i assembly.fasta --pretty`
**Explanation:** Outputs formatted, human-readable JSON with indentation.

### Generate summary report
**Args:** `assembly-scan -i assembly.fasta -o stats.json --report report.txt`
**Explanation:** Generates both JSON output and human-readable text report.

### Calculate N75 and N90
**Args:** `assembly-scan -i assembly.fasta -o stats.json --n-values 50,75,90`
**Explanation:** Computes N50, N75, and N90 statistics instead of default N50 only.

### Filter by coverage
**Args:** `assembly-scan -i assembly.fasta -o stats.json --min-coverage 10`
**Explanation:** Filters contigs based on minimum coverage (requires coverage info in headers).