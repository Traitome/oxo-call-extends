---
name: crispector
category: utility
description: CRISPR off-target editing activity quantification from comparative NGS data using Bayesian classification
tags: [crispector, CRISPR, off-target, genome-editing, NGS, Bayesian, amplicon, translocation, multiplex-PCR]
author: oxo-call-community
source_url: "https://github.com/YakhiniGroup/crispector"
---

## Concepts

- **Tool Overview**: crispector (v1.0.7) / CRISPECTOR2.0 - A statistical tool for analyzing multiplex PCR/NGS data to evaluate CRISPR nuclease activity at on-target and off-target sites using a Bayesian classifier approach.
- **Core Function**: Compares CRISPR-edited samples to unedited (mock) samples to detect and quantify editing activity. Uses Bayesian classification to identify real editing events even at low, yet significant levels. Also detects chromosomal translocations from multiplex PCR data.
- **Algorithm**: (1) Maps NGS reads to PCR amplicons. (2) Aligns reads from edited and paired control samples to reference genome. (3) Compares sequence variations between edited and control samples. (4) Applies Bayesian classifier to distinguish genuine editing events from sequencing errors based on enrichment in edited sample. (5) Detects translocations by identifying reads with primer sequences from different PCR amplicons.
- **Input**: Multiplex rhAmpSeq PCR amplicons from CRISPR-edited and control samples (FASTQ/FASTA), candidate off-target sites nominated by GUIDE-seq, CIRCLE-seq, SITE-seq, or DISCOVER-seq.
- **Output**: Editing activity quantification at on/off-target sites, translocation detection results, statistical confidence values.
- **Application**: CRISPR gRNA validation, off-target activity profiling, genome editing efficiency assessment, multiplexed editing analysis.
- **Installation**: `pip install crispector` or `conda install -c bioconda crispector`

## Pitfalls

- **Paired Samples Required**: Requires both edited and mock/control samples for comparison - cannot analyze edited samples alone.
- **Multiplex PCR Design**: Results depend heavily on proper multiplex PCR primer design and amplification efficiency.
- **Low Signal Challenge**: In experiments with low editing rates, careful parameter tuning is needed to separate signal from noise.
- **Amplicon Length**: Designed for relatively short amplicons typical of rhAmpSeq - may not work well with long amplicon strategies.
- **Statistical Parameters**: Bayesian classification parameters may need adjustment based on expected editing frequencies.

## Examples

### Analyze editing at candidate sites
**Args:** `crispector analyze -i edited.fastq -c control.fastq -o results.csv`
**Explanation:** Compare edited and control samples to quantify editing activity at nominated off-target sites.

### Specify candidate off-target BED file
**Args:** `crispector analyze -i edited.fastq -c control.fastq -bed candidates.bed -o results.csv`
**Explanation:** Provide a BED file with candidate off-target sites for targeted analysis.

### Run in verbose mode
**Args:** `crispector analyze -i edited.fastq -c control.fastq -o results.csv -v`
**Explanation:** Enable verbose output to monitor analysis progress and see intermediate results.

### Adjust detection sensitivity
**Args:** `crispector analyze -i edited.fastq -c control.fastq -o results.csv --alpha 0.05`
**Explanation:** Adjust the Bayesian classification alpha parameter to tune sensitivity for low-frequency edits.

### Detect translocations
**Args:** `crispector translocation -i edited.fastq -c control.fastq -o translocation_results.csv`
**Explanation:** Screen for chromosomal translocation events resulting from CRISPR editing using primer combination patterns.

### Generate report
**Args:** `crispector report -i results.csv -o report.pdf`
**Explanation:** Generate a formatted PDF report from the analysis results.

### Validate with synthetic spike-in
**Args:** `crispector analyze -i edited.fastq -c control.fastq -spike spike_in.fa -o validated.csv`
**Explanation:** Include synthetic control sequences with known editing to validate detection sensitivity.

### Display version
**Args:** `crispector --version`
**Explanation:** Display the installed version of crispector.

### Show help
**Args:** `crispector --help`
**Explanation:** Display all available commands and options.
