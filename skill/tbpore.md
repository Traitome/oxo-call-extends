---
name: tbpore
category: analysis
description: TBpore - Nanopore sequencing analysis pipeline for Mycobacterium tuberculosis drug resistance detection and molecular clustering.
tags: [tbpore, tuberculosis, nanopore, mycobacterium, drug-resistance, clustering, ont-sequencing]
author: oxo-call-community
source_url: "https://github.com/raft-IRC/tbpore"
---

## Concepts

- **Tool Overview**: tbpore (v1.0+) - A Nanopore sequencing analysis pipeline for M. tuberculosis, designed for simultaneous drug resistance prediction and molecular clustering of transmission isolates.
- **Core Function**: Processes Nanopore FASTQ files to detect drug resistance mutations and perform molecular epidemiology clustering analysis. Companion tool to Mykrobe for integrated analysis.
- **Input**: Raw Nanopore reads (FASTQ) from M. tuberculosis sequencing, can accept multiplexed runs.
- **Output**: Drug resistance profile reports, clustering results, lineage information in JSON and text formats.
- **Installation**: `pip install tbpore` or `conda install -c bioconda tbpore`
- **Key Feature**: Combines drug susceptibility testing (DST) with molecular epidemiology for outbreak investigation.

## Pitfalls

- **Reference Bias**: Clustering relies on SNPs - may miss large structural variations.
- **Depth Requirement**: Adequate coverage (typically 100x+) needed for reliable resistance detection.
- **Database Updates**: Drug resistance mutations database requires regular updates for new drugs.
- **Species Specific**: Optimized for M. tuberculosis complex - not for other mycobacteria.

## Examples

### Basic analysis
**Args:** `tbpore -i reads.fastq.gz -o results/`
**Explanation:** Standard analysis of Nanopore reads for drug resistance and lineage.

### Specify reference
**Args:** `tbpore -i sample.fastq -o output/ -r NC_000962.3`
**Explanation:** Use specific reference genome version for alignment.

### Cluster samples
**Args:** `tbpore cluster -i sample1.fastq sample2.fastq -o clusters/`
**Explanation:** Perform molecular clustering between multiple samples for epidemiology.

### JSON output
**Args:** `tbpore -i reads.fastq -o results/ --json`
**Explanation:** Generate machine-readable JSON output for automated pipelines.

### With coverage threshold
**Args:** `tbpore -i sample.fastq -o results/ --min-depth 50`
**Explanation:** Set minimum depth threshold for reliable variant calling.
