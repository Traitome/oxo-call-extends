---
name: thapbi-pict
category: analysis
description: THapBI - fungal metabarcoding analysis pipeline for Phytophthora detection.
tags: [thapbi-pict, metabarcoding, fungi, phytophthora, its, pathogen-detection, ngs]
author: oxo-call-community
source_url: "https://github.com/peterjc/thapbi-pict"
---

## Concepts

- **Tool Overview**: THapBI (Tools for Haplotype Analysis of Phytophthora barcode markers) - A pipeline for metabarcoding analysis of fungal and Phytophthora species from environmental samples.
- **Core Function**: Processes ITS barcode amplicon sequencing data for identification and quantification of Phytophthora and other oomycete species.
- **Input**: ITS1 or ITS2 amplicon sequencing reads (FASTQ), barcode/marker database.
- **Output**: Species identification reports, abundance tables, phylogenetic placements.
- **Installation**: `pip install thapbi-pict` or `conda install -c bioconda thapbi-pict`
- **Use Case**: Phytophthora detection in environmental samples, plant disease surveillance, biodiversity surveys.

## Pitfalls

- **ITS Marker**: Relies on ITS barcode markers - may not resolve closely related species.
- **Database Quality**: Species identification accuracy depends on reference database completeness.

## Examples

### Basic ITS analysis
**Args:** `thapbi_pict import -i reads.fastq.gz -o analysis/`
**Explanation:** Import and analyze ITS amplicon reads for Phytophthora detection.

### Sample comparison
**Args:** `thapbi_pict compare -s sample1.tsv -s sample2.tsv -o comparison/`
**Explanation:** Compare Phytophthora communities between samples.

### Report generation
**Args:** `thapbi_pict summary -i results/ -o report.pdf`
**Explanation:** Generate summary report of metabarcoding analysis.
