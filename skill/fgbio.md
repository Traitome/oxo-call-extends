---
name: fgbio
category: utility
description: "A set of tools for working with genomic and high throughput sequencing data, including UMIs"
tags: [fgbio, utility, genomics, UMI, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/fgbio"
---

## Concepts

- **Tool Overview**: fgbio is a toolkit for working with genomic and high-throughput sequencing data, with special support for Unique Molecular Identifiers (UMIs).
- **Core Function**: Provides tools for processing sequencing data including UMI handling, filtering, and analysis.
- **Input/Output**: Input: FASTQ/BAM files. Output: Processed BAM/FASTQ, reports.
- **Algorithm**: Implements various algorithms for sequencing data processing.
- **Key Features**: UMI processing, sequencing tools, BAM manipulation, error correction, molecular consensus, filtering.
- **Installation**: `conda install -c bioconda fgbio`

## Pitfalls

- **UMI Design**: Requires proper UMI barcode design.
- **Data Quality**: Results depend on input data quality.
- **Memory Usage**: Large datasets may require significant memory.
- **BAM Format**: Requires proper BAM format handling.
- **Version Compatibility**: Options may vary between versions.

## Examples

### UMI extraction
**Args:** `fgbio ExtractUmis -i reads.fastq -o extracted.fastq`
**Explanation:** Extracts UMI sequences from reads.

### UMI error correction
**Args:** `fgbio CorrectUmis -i extracted.fastq -o corrected.fastq`
**Explanation:** Corrects UMI errors.

### Consensus generation
**Args:** `fgbio GroupReadsByUmi -i aligned.bam -o grouped.bam`
**Explanation:** Groups reads by UMI for consensus.

### Filter reads
**Args:** `fgbio FilterBam -i aligned.bam -o filtered.bam --metric-file metrics.txt`
**Explanation:** Filters reads based on criteria.

### Bam statistics
**Args:** `fgbio BamMetrics -i aligned.bam -o metrics.txt`
**Explanation:** Generates BAM statistics.