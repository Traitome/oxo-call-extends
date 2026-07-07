---
name: metawrap-blobology
category: qc
description: MetaWRAP requirements for read_qc step
tags: [metawrap-blobology, qc, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Blobology v1.3.0 provides quality control functionality as part of the MetaWRAP metagenomic analysis pipeline.
- **Core Function**: Performs quality control and visualization of metagenomic data.
- **Blob Plot Generation**: Creates blob plots to visualize sequence composition.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts sequencing reads or contigs; outputs quality reports and visualizations.
- **Quality Assessment**: Includes quality metrics and contamination detection.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Visualization Complexity**: Complex datasets may produce cluttered visualizations.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input data quality.

## Examples

### Run quality control
**Args:** `metawrap-blobology -i reads.fastq -o qc_report/`
**Explanation:** Performs quality control on metagenomic reads.

### Generate blob plot
**Args:** `metawrap-blobology -i contigs.fasta -o blob_plot.png --plot`
**Explanation:** Generates blob plot visualization.

### Contamination detection
**Args:** `metawrap-blobology -i reads.fastq -o qc_report/ --contamination`
**Explanation:** Detects potential contamination in sequencing data.

### Detailed report
**Args:** `metawrap-blobology -i reads.fastq -o qc_report/ -v`
**Explanation:** Generates detailed quality control report.

### Batch processing
**Args:** `metawrap-blobology -i fastq/ -o qc_reports/`
**Explanation:** Processes multiple samples in batch mode.