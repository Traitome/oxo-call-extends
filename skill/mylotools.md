---
name: mylotools
category: utility
description: Mylotools - Utilities for myloasm long-read assembler QC and manipulation
tags: [mylotools, utility, assembly, qc, long-reads, myloasm]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/mylotools"
---

## Concepts

- **Tool Overview**: Mylotools v2.0.0 is a utility suite for quality control and manipulation of myloasm long-read metagenome assembly outputs. Provides tools for assessing assembly quality and processing assembly results.
- **Core Function**: Offers QC reporting for myloasm assemblies, including completeness assessment, contamination screening, and assembly statistics. Also provides utilities for filtering and manipulating assembly outputs.
- **QC Features**: Evaluates assembly quality metrics including N50, total contig length, genome completeness estimates, and contamination detection using reference databases.
- **Input Format**: Works with FASTA output from myloasm assemblies. Can also process other metagenome assemblers' outputs for comparative QC.
- **Output**: Produces quality reports in tabular format (TSV), summary statistics, and filtered FASTA files based on quality thresholds.
- **Use Case**: Validating myloasm assembly quality, comparing assembly methods, filtering low-quality contigs, and preparing assemblies for downstream analysis.

## Pitfalls

- **Myloasm Dependency**: Primary purpose is working with myloasm outputs. Using with other assemblers may give inconsistent or meaningless metrics.
- **Quality Thresholds**: Default QC thresholds may not be appropriate for all sample types. Adjust based on expected community complexity and sequencing depth.
- **Reference Database**: Some QC features require reference databases (e.g., CheckM for completeness). Ensure databases are installed for full functionality.
- **Contig Filtering**: Aggressive filtering may remove legitimate low-coverage genomes. Balance between quality and completeness.
- **Version Compatibility**: Database formats may change between versions. Match mylotools and reference database versions.
- **Large Assemblies**: Processing very large assemblies (many GB of sequence) may require substantial memory and time.

## Examples

### Generate QC report for assembly
**Args:** `-i assembly.fasta -o qc_report.tsv`
**Explanation:** Standard QC workflow. Analyzes assembly and outputs comprehensive quality metrics.

### Filter contigs by length
**Args:** `-i assembly.fasta -o filtered.fasta -min_length 1000`
**Explanation:** Removes contigs shorter than 1000bp to focus on more complete genome assemblies.

### Estimate genome completeness
**Args:** `-i assembly.fasta -o completeness.tsv --completeness`
**Explanation:** Runs completeness estimation using lineage-specific marker genes to assess assembly quality.

### Summary statistics
**Args:** `-i assembly.fasta --stats`
**Explanation:** Shows basic assembly statistics: total length, contig count, N50, longest contig, etc.

### Display help
**Args:** `--help`
**Explanation:** Shows all available commands and options for mylotools utility suite.
