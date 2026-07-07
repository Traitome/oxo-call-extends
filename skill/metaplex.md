---
name: metaplex
category: qc
description: Read Processing and Quality Control Toolkit for Dual-Indexed Metabarcoding
tags: [metaplex, qc, metabarcoding]
author: oxo-call-community
source_url: "https://github.com/NGabry/MetaPlex"
---

## Concepts

- **Tool Overview**: MetaPlex v1.1.0 is a read processing and quality control toolkit specifically designed for dual-indexed metabarcoding data.
- **Core Function**: Processes and quality controls dual-indexed sequencing data for metabarcoding applications.
- **Dual-Index Handling**: Specifically designed to handle dual-indexed sequencing libraries commonly used in metabarcoding.
- **Quality Control**: Includes quality filtering, primer trimming, and demultiplexing capabilities.
- **Input/Output**: Accepts raw FASTQ sequencing reads; outputs cleaned and demultiplexed reads.
- **Metabarcoding Optimization**: Optimized for metabarcoding workflows with support for various marker genes.

## Pitfalls

- **Index Misassignment**: May misassign reads to incorrect samples if indexes are not properly handled.
- **Quality Thresholds**: Requires appropriate quality thresholds for trimming and filtering.
- **Primer Design**: Analysis quality depends on primer design and specificity.
- **Sequence Quality**: Poor quality sequences may affect downstream analysis.
- **Demultiplexing Errors**: May produce errors during sample demultiplexing.
- **Memory Requirements**: Processing large datasets may require significant memory.

## Examples

### Process dual-indexed reads
**Args:** `metaplex -i reads.fastq -o processed/`
**Explanation:** Processes and quality controls dual-indexed sequencing reads.

### Demultiplex samples
**Args:** `metaplex -i reads.fastq -b barcodes.txt -o demultiplexed/`
**Explanation:** Demultiplexes reads based on provided barcode sequences.

### Trim primers
**Args:** `metaplex -i reads.fastq -p primers.fasta -o trimmed/`
**Explanation:** Trims primer sequences from reads.

### Quality filtering
**Args:** `metaplex -i reads.fastq -q 20 -o filtered/`
**Explanation:** Filters reads based on quality score threshold of 20.

### Batch processing
**Args:** `metaplex -i fastq/ -o results/`
**Explanation:** Processes multiple FASTQ files in batch mode.