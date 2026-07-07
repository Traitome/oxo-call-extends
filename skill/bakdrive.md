---
name: bakdrive
category: metagenomics
description: Bakdrive - Identify driver species and simulate fecal microbial transplantation
tags: [bakdrive, metagenomics, fmt, microbial-transplantation, driver-species]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/bakdrive"
---

## Concepts

- **Tool Overview**: Bakdrive identifies a minimum set of driver species from metagenomic samples and simulates the fecal microbial transplantation (FMT) process. Version 1.0.4.
- **Core Function**: Finds key microbial species that drive community changes and simulates FMT outcomes.
- **Driver Species Identification**: Identifies minimal set of species responsible for community composition changes.
- **FMT Simulation**: Simulates fecal microbial transplantation process and predicts community outcomes.
- **Metagenomic Analysis**: Analyzes complex microbial communities from sequencing data.
- **Input/Output**: Accepts metagenomic abundance profiles, outputs driver species and simulation results.
- **Installation**: `conda install -c bioconda bakdrive`.

## Pitfalls

- **Data Quality**: Results depend on metagenomic data quality and sequencing depth.
- **Community Complexity**: Very diverse communities may be difficult to analyze.
- **Driver Assumptions**: Assumes linear relationships between species abundance and community changes.
- **FMT Simulation**: Simulation is a simplification of real biological processes.
- **Reference Databases**: Requires comprehensive reference databases for species identification.

## Examples

### Identify driver species
**Args:** `bakdrive drivers --input abundances.tsv --output drivers.txt`
**Explanation:** Identifies driver species from metagenomic abundance data.

### Simulate FMT
**Args:** `bakdrive simulate --input donors.tsv --recipients recipients.tsv --output fmt_results/`
**Explanation:** Simulates FMT process between donor and recipient communities.

### Complete analysis pipeline
**Args:** `bakdrive pipeline --input metagenomes/ --output results/`
**Explanation:** Runs complete analysis including driver identification and FMT simulation.

### Specify donor and recipient
**Args:** `bakdrive simulate --donor donor_profile.tsv --recipient recipient_profile.tsv --output result.tsv`
**Explanation:** Simulates FMT from specific donor to specific recipient.

### Set simulation parameters
**Args:** `bakdrive simulate --donor donor.tsv --recipient recipient.tsv --transfer-rate 0.5 --output result.tsv`
**Explanation:** Sets custom transfer rate for FMT simulation.

### Generate visualization
**Args:** `bakdrive plot --input results.tsv --output plot.pdf`
**Explanation:** Generates visualization of FMT simulation results.

### Display help
**Args:** `bakdrive --help`
**Explanation:** Shows all available command-line options and usage information.