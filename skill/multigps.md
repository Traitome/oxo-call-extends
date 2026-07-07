---
name: multigps
category: expression
description: MultiGPS is a framework for analyzing collections of multi-condition ChIP-seq datasets and characterizing differential binding events between conditions.
tags: [multigps, chip-seq, differential-binding, expression, peak-calling]
author: oxo-call-community
source_url: "http://mahonylab.org/software/multigps/"
---

## Concepts

- **Tool Overview**: MultiGPS v0.74 is a framework for analyzing collections of multi-condition ChIP-seq datasets and characterizing differential binding events between conditions. It uses an integrated model to encourage consistency in reported binding event locations across conditions.
- **Core Function**: Performs multi-condition ChIP-seq analysis with accurate estimation of ChIP enrichment levels at each binding event, integrating data across experimental conditions for robust differential binding detection.
- **Algorithm**: Uses EM optimization for binding event detection along the genome and across experimental conditions, with optional motif-finding integration via MEME for motif prior incorporation.
- **Input Format**: Accepts ChIP-seq read files in common formats (BED, SAM, BAM) and requires genome information file listing chromosome names and lengths.
- **Output**: Generates binding event reports with Q-values, fold-change estimates, and condition-specific enrichment levels in tab-delimited text format.
- **Dependencies**: Requires Java 8+, MEME for motif analysis, and R/Bioconductor/edgeR for differential binding statistical analysis.

## Pitfalls

- **Java Memory**: MultiGPS loads all data into memory. Large datasets require substantial RAM (recommended 20GB via `-Xmx20G`). Insufficient memory causes crashes during EM optimization.
- **Long Runtime**: EM optimization and motif-finding make MultiGPS very time-intensive. Expect extended run times for large genomes or many conditions.
- **Chromosome Naming**: Chromosome names in input files must exactly match those in the genome info file. UCSC-style (chr1) vs NCBI-style (1) mismatches cause silent failures.
- **Control Sample Requirements**: Each experimental condition requires a matched control sample. Using mismatched controls leads to false differential binding calls.
- **Version Compatibility**: JAR-based distribution requires exact Java version match. Java 11+ may cause compatibility issues with older MultiGPS versions.
- **Motif Discovery Memory**: Running motif-finding with MEME requires additional memory and can significantly increase total runtime for large datasets.

## Examples

### Run MultiGPS with config file
**Args:** `--config config.txt`
**Explanation:** Uses a configuration file to specify all options. The config file uses name-value pairs without the `--` prefix, one per line. Command-line arguments override config file settings.

### Specify genome and output prefix
**Args:** `--geninfo genome.info --out experiment1_results`
**Explanation:** Defines the genome info file (chrName<tab>chrLength format) and sets the output prefix. All results go into a directory named experiment1_results/.

### Define experimental conditions
**Args:** `--expt Cond1_Rep1 reads1.bed --ctrl Cond1_Rep1 control1.bed`
**Explanation:** Defines an experimental condition (Cond1_Rep1) and its control (control1.bed). Repeat for each condition and replicate. MultiGPS analyzes all conditions together.

### Set differential binding thresholds
**Args:** `--q 0.001 --minfold 2.0 --nodifftests`
**Explanation:** Sets minimum Q-value (corrected p-value) to 0.001 and minimum fold-change to 2.0. `--nodifftests` disables differential testing, useful for initial exploration.

### Run with multiple threads
**Args:** `--threads 8`
**Explanation:** Uses 8 threads for binding event detection. Improves performance on multi-core systems but increases memory consumption proportionally.

### Specify sequence directory for motif analysis
**Args:** `--seq fasta_directory/`
**Explanation:** Provides a directory containing FASTA files for each chromosome. Required when running motif-finding or using a motif prior. Must match chromosome names in genome info file.
