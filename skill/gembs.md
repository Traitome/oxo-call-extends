---
name: gembs
category: epigenomics
description: gemBS is a bioinformatics pipeline for high-throughput analysis of DNA methylation from Whole Genome Bisulfite Sequencing (WGBS) data.
tags: [gembs, dna-methylation, WGBS, epigenomics, bioinformatics-pipeline]
author: oxo-call-community
source_url: "https://github.com/heathsc/gemBS"
---

## Concepts
- **WGBS Analysis**: Comprehensive pipeline for Whole Genome Bisulfite Sequencing data.
- **DNA Methylation**: Analyzes DNA methylation patterns at single-base resolution.
- **Quality Control**: Includes QC steps for raw sequencing data.
- **Alignment**: Maps bisulfite-converted reads to reference genome.
- **Methylation Calling**: Calls methylation status at each CpG site.

## Pitfalls
- **Data Quality**: Requires high-quality bisulfite sequencing data.
- **Bisulfite Conversion**: Incomplete conversion affects methylation estimates.
- **Computational Resources**: WGBS analysis requires significant computational resources.
- **Reference Genome**: Requires bisulfite-converted reference genome.
- **Memory Usage**: Large datasets require substantial memory.

## Examples
### Initialize pipeline
**Args:** `gemBS init -r genome.fasta -o project/`
**Explanation:** Initializes a gemBS project with reference genome.

### Run full pipeline
**Args:** `gemBS run -i project/ -1 reads_1.fastq -2 reads_2.fastq`
**Explanation:** Runs the complete WGBS analysis pipeline.

### Only quality control
**Args:** `gemBS qc -i project/ -1 reads_1.fastq -2 reads_2.fastq`
**Explanation:** Performs only QC steps on raw reads.

### Call methylation
**Args:** `gemBS call -i project/ -o methylation_calls.txt`
**Explanation:** Calls methylation from aligned reads.

### Generate report
**Args:** `gemBS report -i project/ -o report.html`
**Explanation:** Generates HTML report of analysis results.