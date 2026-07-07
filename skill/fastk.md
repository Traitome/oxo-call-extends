---
name: fastk
category: expression
description: "FastK is a k‑mer counter that is optimized for processing high quality DNA assembly data sets such as those produced with an Illumina instrument or a PacBio run in HiFi mode."
tags: [fastk, expression, k-mer, sequencing-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/FASTK"
---

## Concepts

- **Tool Overview**: FastK is a highly optimized k-mer counter designed for processing high-quality DNA assembly data from Illumina and PacBio HiFi sequencing.
- **Core Function**: Counts k-mer frequencies in sequencing data efficiently.
- **Input/Output**: Input: Sequencing reads (FASTQ/FASTA). Output: k-mer counts, frequency tables.
- **Algorithm**: Uses advanced data structures for efficient k-mer counting.
- **Key Features**: High-speed k-mer counting, memory efficient, supports large datasets, multiple k-mer sizes, batch processing.
- **Installation**: `conda install -c bioconda fastk`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Data Quality**: Poor quality sequences may affect counting accuracy.
- **Format Compatibility**: Requires standard input formats.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic k-mer counting
**Args:** `fastk -i reads.fastq -o kmer_counts.txt -k 21`
**Explanation:** Counts 21-mers in FASTQ file.

### Multiple k-mer sizes
**Args:** `fastk -i reads.fastq -o kmer_counts.txt -k 15,21,31`
**Explanation:** Counts multiple k-mer sizes.

### Output frequency histogram
**Args:** `fastk -i reads.fastq -o histogram.txt -k 21 --histogram`
**Explanation:** Generates k-mer frequency histogram.

### Filter by count
**Args:** `fastk -i reads.fastq -o kmer_counts.txt -k 21 -m 5`
**Explanation:** Only reports k-mers with count >= 5.

### Batch processing
**Args:** `fastk -i fastq_files/ -o results/ -k 21 --batch`
**Explanation:** Processes multiple files in batch mode.