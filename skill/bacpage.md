---
name: bacpage
category: assembly
description: BacPage - Easy-to-use pipeline for assembly and analysis of bacterial genomes
tags: [bacterial-genomics, assembly, analysis, pipeline]
author: oxo-call-community
source_url: "https://github.com/CholGen/bacpage"
---

## Concepts

- **Tool Overview**: BacPage is an easy-to-use pipeline for assembling and analyzing bacterial genomes, designed for simplicity and accessibility.

- **Automated Workflow**: Handles the complete workflow from raw reads through assembly, quality assessment, and basic analysis.

- **User-Friendly**: Designed for users without extensive bioinformatics expertise, with sensible defaults.

- **Quality Reporting**: Provides comprehensive quality metrics and reports for assembled genomes.

## Pitfalls

- **Limited Customization**: Prioritizes ease-of-use over flexibility. Advanced users may need more configurable tools.

- **Assembly Quality**: Default parameters may not be optimal for all data types. Review results carefully.

- **Resource Requirements**: Requires adequate computational resources for assembly and analysis.

## Examples

### Basic assembly
**Args:** `bacpage assemble --reads R1.fastq.gz R2.fastq.gz --output results/`
**Explanation:** Assembles bacterial genome from paired-end Illumina reads.

### Full analysis pipeline
**Args:** `bacpage analyse --reads R1.fastq.gz R2.fastq.gz --output analysis/`
**Explanation:** Runs complete analysis pipeline including assembly and annotation.

### Specify genome size
**Args:** `bacpage assemble --reads R1.fastq.gz R2.fastq.gz --genome-size 5m --output results/`
**Explanation:** Provides expected genome size hint for improved assembly.

### Multiple samples
**Args:** `bacpage batch --samples samples.tsv --output batch_results/`
**Explanation:** Processes multiple samples defined in sample sheet.
