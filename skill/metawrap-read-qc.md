---
name: metawrap-read-qc
category: qc
description: MetaWRAP requirements for read_qc step
tags: [metawrap-read-qc, qc, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Read QC v1.3.0 provides quality control functionality for sequencing reads as part of the MetaWRAP pipeline.
- **Core Function**: Performs quality control on metagenomic sequencing reads.
- **Quality Assessment**: Evaluates sequencing read quality and identifies issues.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts raw sequencing reads; outputs cleaned reads and quality reports.
- **Adapter Trimming**: Removes sequencing adapters and low-quality bases.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Data Quality**: Analysis quality depends on input data quality.
- **Adapter Contamination**: Persistent adapter sequences can affect downstream analysis.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Memory Requirements**: Processing large datasets may require significant memory.
- **Runtime**: Quality control of large datasets can be time-consuming.

## Examples

### Run read quality control
**Args:** `metawrap-read-qc -i reads.fastq -o cleaned/`
**Explanation:** Performs quality control on sequencing reads.

### With custom quality threshold
**Args:** `metawrap-read-qc -i reads.fastq -o cleaned/ -q 20`
**Explanation:** Uses minimum quality score of 20 for filtering.

### Paired-end analysis
**Args:** `metawrap-read-qc -i reads_1.fastq -r reads_2.fastq -o cleaned/`
**Explanation:** Processes paired-end sequencing data.

### Generate report
**Args:** `metawrap-read-qc -i reads.fastq -o cleaned/ -r report.html`
**Explanation:** Generates comprehensive quality control report.

### Batch processing
**Args:** `metawrap-read-qc -i fastq/ -o cleaned/`
**Explanation:** Processes multiple samples in batch mode.