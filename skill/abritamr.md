---
name: abritamr
category: annotation
description: Identify bacterial AMR genes and SNPs in genome assemblies.
tags: [abritamr, annotation, amr, antimicrobial-resistance, bacteria, snp]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/abritamr"
---

## Concepts

- **Tool Overview**: AMR gene detection pipeline that runs AMRFinderPlus on bacterial genome assemblies and collates results into organized tables. Version 1.2.0.
- **Core Function**: Identifies antimicrobial resistance genes and point mutations in bacterial genomes using the NCBI AMRFinderPlus database.
- **Input/Output**: Input is genome assemblies (FASTA) or a list of assemblies; output is tabular reports with AMR genes categorized by function.
- **Installation**: Install via bioconda: `conda install -c bioconda abritamr`
- **Platform Support**: Platform-independent (noarch)
- **AMRFinderPlus Backend**: Uses NCBI's AMRFinderPlus, which is NATA-accredited for clinical AMR reporting.
- **Functional Grouping**: Separates identified genes into functionally relevant groups (e.g., beta-lactamases, fluoroquinolones).
- **Point Mutation Detection**: Detects both acquired AMR genes and point mutations conferring resistance.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **AMRFinderPlus Database**: Requires AMRFinderPlus database to be downloaded. Run database update before first use.
- **Assembly Quality**: Results depend on assembly quality. Poor assemblies may miss genes or have false positives.
- **Species-Specific**: Some point mutation rules are species-specific. Ensure correct species identification.
- **Database Updates**: AMRFinderPlus database is regularly updated. Keep database current for best results.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and parameters.

### Run AMR detection on a single assembly
**Args:** `run --assembly genome.fasta --output results/`
**Explanation:** Runs AMRFinderPlus on a single genome assembly and outputs a tabular report of detected AMR genes.

### Run on multiple assemblies
**Args:** `run --assembly-list isolates.txt --output amr_results/`
**Explanation:** Processes multiple assemblies listed in a text file (one path per line) and generates a combined summary table.

### Run with custom AMRFinderPlus parameters
**Args:** `run --assembly genome.fasta --organism "Escherichia coli" --output results/`
**Explanation:** Specifies the organism for species-specific point mutation detection. Improves accuracy for known organisms.

### Generate detailed report
**Args:** `run --assembly genome.fasta --output results/ --plus`
**Explanation:** Runs with AMRFinderPlus `--plus` mode for additional gene families and expanded detection.
