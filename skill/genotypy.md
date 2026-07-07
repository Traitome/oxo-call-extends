---
name: genotypy
category: barcode-analysis
description: genotypy - Automatically detect genomic barcodes integrated into loci of interest from sequencing data.
tags: [genotypy, barcode-analysis, genomic-barcodes, sequencing]
author: oxo-call-community
source_url: "https://gitbio.ens-lyon.fr/LBMC/yvertlab/vortex/plasticity_mutation/colony_rnaseq_bioinformatics/genotypy"
---

## Concepts
- **Barcode Detection**: Detects genomic barcodes in sequencing data.
- **Locus Identification**: Identifies barcodes integrated into specific loci.
- **Sequencing Analysis**: Analyzes sequencing data for barcodes.
- **Genetic Screening**: Supports genetic screening experiments.
- **Data Processing**: Processes sequencing data efficiently.

## Pitfalls
- **Barcode Design**: Depends on barcode design quality.
- **Sequencing Quality**: Requires high-quality sequencing data.
- **False Positives**: May detect false barcode signals.
- **Computational Resources**: Large datasets require resources.
- **Result Validation**: Results should be validated.

## Examples
### Detect barcodes
**Args:** `genotypy -i reads.fastq -l loci.bed -o barcodes.txt`
**Explanation:** Detects barcodes in sequencing reads.

### With reference genome
**Args:** `genotypy -i reads.fastq -l loci.bed -r genome.fasta -o barcodes.txt`
**Explanation:** Uses reference genome for barcode detection.

### Batch processing
**Args:** `genotypy -i ./fastq_files/ -l loci.bed -o ./results/`
**Explanation:** Processes multiple sequencing files.

### Filter by quality
**Args:** `genotypy -i reads.fastq -l loci.bed -q 0.95 -o barcodes.txt`
**Explanation:** Filters barcodes by quality score.

### Generate report
**Args:** `genotypy -i reads.fastq -l loci.bed -r -o report.html`
**Explanation:** Generates barcode detection report.