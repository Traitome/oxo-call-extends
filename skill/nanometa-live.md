---
name: nanometa-live
category: metagenomics
description: NanoMeta-Live - Real-time species classification and pathogen characterization for Nanopore data
tags: [nanometa-live, metagenomics, nanopore, real-time, pathogen, gui]
author: oxo-call-community
source_url: "https://github.com/FOI-Bioinformatics/nanometa_live"
---

## Concepts

- **Tool Overview**: NanoMeta-Live v0.4.3 is a real-time metagenomic analysis tool with a GUI for Oxford Nanopore sequencing data. It provides immediate species classification and pathogen detection during sequencing runs.
- **Core Function**: Processes streaming Nanopore reads in real-time, performing taxonomic classification and generating pathogen reports as data is being sequenced.
- **Algorithm**: Uses minimap2 for rapid alignment and Centrifuge/Kraken2 for taxonomic classification. Supports both reference-based and k-mer based approaches.
- **Input Format**: Accepts streaming FASTQ reads from Nanopore sequencers or pre-recorded FASTQ files. Works with live sequencing data.
- **Output**: Produces real-time species abundance charts, pathogen detection alerts, and comprehensive taxonomic reports.
- **Use Case**: Real-time pathogen detection in clinical settings, environmental monitoring, and rapid metagenomic analysis during sequencing runs.

## Pitfalls

- **Real-time Requirements**: Requires stable network connection and proper sequencing setup for live analysis.
- **Reference Database**: Classification accuracy depends on reference database quality and completeness.
- **Internet Access**: Some features may require internet access for database updates.
- **Computational Resources**: Real-time analysis requires sufficient computational resources. Consider GPU acceleration.
- **False Positives**: Low-abundance species may produce false positive calls. Use appropriate thresholds.
- **Database Updates**: Outdated databases may miss novel pathogens. Regular updates recommended.

## Examples

### Basic real-time analysis
**Args:** `-i reads_directory -o output_dir`
**Explanation:** Runs real-time species classification on incoming Nanopore reads.

### Use specific classifier
**Args:** `-i fastq_dir -o results/ -c kraken2`
**Explanation:** Specifies Kraken2 as the classification tool instead of default.

### Set confidence threshold
**Args:** `-i reads/ -o output/ -t 0.95`
**Explanation:** Sets minimum confidence threshold of 95% for species calls.

### Run in GUI mode
**Args:** `nanometa-live --gui`
**Explanation:** Launches the graphical user interface for interactive analysis.

### Display help
**Args:** `nanometa-live --help`
**Explanation:** Shows all available options for real-time analysis.
