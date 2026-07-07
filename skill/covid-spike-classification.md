---
name: covid-spike-classification
category: variant-calling
description: Detect SARS-CoV-2 spike protein variants from Sanger sequencing data for COVID-19 surveillance
tags: [covid-spike-classification, sars-cov-2, spike-protein, variant-detection, sanger-sequencing, covid-19, mutation]
author: oxo-call-community
source_url: "https://github.com/kblin/covid-spike-classification/"
---

## Concepts

- **Tool Overview**: covid-spike-classification is a tool for detecting SARS-CoV-2 spike protein mutations from Sanger sequencing data, developed for COVID-19 surveillance efforts.
- **Core Function**: Calls spike protein mutations of interest from Sanger-sequenced RT-PCR products, aligning reads to a reference and identifying known variants.
- **Algorithm**: Uses bowtie2 for read mapping against spike protein reference, samtools for BAM processing, and detects mutations by analyzing aligned reads at specific genomic positions.
- **Input**: Sanger sequencing traces (AB1 format) or FASTQ/FASTA files, reference sequence (default: NC_045.512 Wuhan-Hu-1).
- **Output**: JSON file with detected mutations, summary of spike protein variants, alignment statistics.
- **Application**: COVID-19 variant surveillance, outbreak investigation, spike protein mutation monitoring, epidemiological tracking.
- **Installation**: Install via bioconda: `conda install -c bioconda covid-spike-classification`

## Pitfalls

- **Dependencies**: Requires tracy (for AB1 basecalling), bowtie2, samtools, and Biopython.
- **Reference Mismatch**: Using outdated reference sequences may miss newly emerging variants.
- **Sequence Quality**: Poor quality traces affect variant calling accuracy.
- **Mixed Infections**: May have difficulty detecting low-frequency variants in mixed samples.
- **Tracy Requirement**: AB1 format files require tracy tool for basecalling.

## Examples

### Classify spike variants from AB1 trace
**Args:** `covid-spike-classification -i sample.ab1 -o results.json`
**Explanation:** Analyzes Sanger trace file and identifies spike protein mutations.

### Using FASTQ input
**Args:** `covid-spike-classification -i sample.fastq -o results.json`
**Explanation:** Processes pre-basecalled FASTQ files instead of AB1 format.

### Batch process directory
**Args:** `covid-spike-classification -d /path/to/traces/ -o results/`
**Explanation:** Processes all trace files in the specified directory.

### With custom reference
**Args:** `covid-spike-classification -i sample.ab1 -r custom_ref.fasta -o results.json`
**Explanation:** Uses a custom spike protein reference sequence instead of default.

### Generate detailed report
**Args:** `covid-spike-classification -i sample.ab1 --json -o results.json`
**Explanation:** Outputs detailed mutation calls in JSON format.

### Quiet mode
**Args:** `covid-spike-classification -i sample.ab1 -o results.json -q`
**Explanation:** Suppresses verbose output during processing.

## Detected Mutations

The tool detects mutations at these spike protein positions (with genomic coordinates on NC_045.512):

| Mutation | Genomic Position | Mutation | Genomic Position |
|----------|-----------------|----------|-----------------|
| K417N/T | 22811-22813 | N679K | 23597-23599 |
| N439K | 22877-22879 | P681H/R | 23603-23605 |
| L452M/R | 22916-22918 | D614G | 23402-23404 |
| Y453F | 22919-22921 | N501Y | 23063-23065 |
| S477N | 22991-22993 | E484K/A/Q | 23012-23014 |
| T478K/R | 22994-22996 | Q677E/H | 23591-23593 |
