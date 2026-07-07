---
name: arborator
category: utility
description: Arborator - Simplifying operationalized pathogen surveillance and outbreak detection
tags: [arborator, utility, pathogen-surveillance, outbreak-detection, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/phac-nml/arborator"
---

## Concepts

- **Tool Overview**: Arborator is a bioinformatics tool designed to simplify operationalized pathogen surveillance and outbreak detection workflows. Version 1.2.2.
- **Core Function**: Provides automated pipeline for analyzing pathogen genomic data to support public health surveillance and outbreak response.
- **Surveillance Pipeline**: Streamlines the process of detecting and tracking pathogens through genomic sequencing data analysis.
- **Outbreak Detection**: Identifies potential outbreaks by comparing genomic sequences and detecting clusters of related isolates.
- **Data Integration**: Combines genomic, epidemiological, and geographic data for comprehensive analysis.
- **Report Generation**: Produces standardized reports for public health officials and researchers.
- **Installation**: `conda install -c bioconda arborator` or download source code from GitHub repository.

## Pitfalls

- **Version Differences**: Command-line options and configuration parameters may vary between versions.
- **Input Format**: Requires specific input formats for genomic sequences and metadata.
- **Database Requirements**: May require access to reference databases for pathogen identification.
- **Network Access**: Some features may require internet access for database queries.
- **Resource Requirements**: Large datasets may require significant computational resources.
- **Configuration Complexity**: May require detailed configuration for specific surveillance scenarios.

## Examples

### Display help
**Args:** `arborator --help`
**Explanation:** Shows all available command-line options, subcommands, and usage examples.

### Basic surveillance analysis
**Args:** `arborator analyze --input sequences.fasta --metadata metadata.csv --output results/`
**Explanation:** Performs comprehensive pathogen surveillance analysis on input sequences with associated metadata.

### Outbreak detection
**Args:** `arborator detect --input isolates.fasta --threshold 0.95 --out clusters.json`
**Explanation:** Detects potential outbreak clusters by identifying closely related genomic sequences.

### Generate surveillance report
**Args:** `arborator report --input analysis_results/ --format pdf --output surveillance_report.pdf`
**Explanation:** Generates a comprehensive PDF report summarizing surveillance findings and analysis results.

### Database update
**Args:** `arborator update --database pathogen_db --source genbank`
**Explanation:** Updates reference database with latest pathogen sequences from GenBank.

### Batch processing
**Args:** `arborator batch --input_dir fastq_files/ --output_dir results/ --config config.yaml`
**Explanation:** Processes multiple sequence files in batch mode using specified configuration.

### Phylogenetic analysis
**Args:** `arborator phylogeny --input sequences.fasta --out tree.newick --method fasttree`
**Explanation:** Constructs phylogenetic tree from input sequences using FastTree algorithm.