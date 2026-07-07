---
name: cfdna-biomarkersearch
category: variant-analysis
description: Pipeline to identify candidate cfDNA biomarker sequences from WGS data
tags: [cfdna-biomarkersearch, cfdna, biomarkers, wgs, liquid-biopsy]
author: oxo-call-community
source_url: "https://github.com/avo-hcemm/cfDNA-biomarkers-pipeline/blob/master/README.md"
---

## Concepts

- **Tool Overview**: cfDNA-BiomarkerSearch identifies candidate biomarker sequences from cell-free DNA (cfDNA) derived from blood samples.
- **Core Function**: Processes whole-genome sequencing (WGS) data to discover potential cfDNA biomarkers.
- **Pipeline Steps**: Quality control, alignment, variant calling, and biomarker candidate identification.
- **Input**: FASTQ files from cfDNA sequencing experiments.
- **Output**: Candidate biomarker sequences with associated statistics.
- **Application**: Liquid biopsy and non-invasive cancer diagnostics.
- **Installation**: Install via bioconda: `conda install -c bioconda cfdna-biomarkersearch`

## Pitfalls

- **Input Quality**: Requires high-quality cfDNA sequencing data.
- **Contamination**: May be affected by genomic DNA contamination.
- **Reference Genome**: Must use appropriate reference genome for alignment.
- **Computational Resources**: WGS analysis requires significant compute resources.

## Examples

### Run biomarker discovery pipeline
**Args:** `cfdna-biomarkersearch -i reads.fastq -r reference.fasta -o biomarkers/`
**Explanation:** Runs complete cfDNA biomarker discovery pipeline.

### With paired-end reads
**Args:** `cfdna-biomarkersearch -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o results/`
**Explanation:** Processes paired-end sequencing data.

### Quality control only
**Args:** `cfdna-biomarkersearch --qc-only -i reads.fastq -o qc_report/`
**Explanation:** Runs only quality control step.

### Display help
**Args:** `cfdna-biomarkersearch --help`
**Explanation:** Shows all available options and usage information.