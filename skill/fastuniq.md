---
name: fastuniq
category: assembly
description: "FastUniq, A Fast De Novo Duplicates Removal Tool for Paired Short Reads."
tags: [fastuniq, assembly, duplicate-removal, paired-end, bioinformatics]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/fastuniq"
---

## Concepts

- **Tool Overview**: FastUniq is a fast de novo duplicate removal tool for paired-end short reads, designed to identify and remove PCR duplicates without a reference genome.
- **Core Function**: Identifies and removes duplicate read pairs from paired-end sequencing data.
- **Input/Output**: Input: Paired-end FASTQ files. Output: Deduplicated FASTQ files.
- **Algorithm**: Uses hash-based approach to identify duplicate read pairs.
- **Key Features**: Fast de novo deduplication, paired-end support, memory efficient, no reference required, batch processing.
- **Installation**: `conda install -c bioconda fastuniq`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **Paired-End Only**: Designed specifically for paired-end reads.
- **Read Order**: Requires mate pairs to be in same order.
- **Disk Space**: Requires temporary disk space for sorting.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic duplicate removal
**Args:** `fastuniq -i reads_1.fastq -o reads_2.fastq -p deduplicated_`
**Explanation:** Removes duplicate read pairs from paired-end data.

### Input list
**Args:** `fastuniq -i input_list.txt -p output_`
**Explanation:** Uses input file list for batch processing.

### Quality filtering
**Args:** `fastuniq -i reads_1.fastq -o reads_2.fastq -p deduplicated_ -q 20`
**Explanation:** Filters by quality score during deduplication.

### Statistics
**Args:** `fastuniq -i reads_1.fastq -o reads_2.fastq -p deduplicated_ -s stats.txt`
**Explanation:** Generates deduplication statistics.

### Threaded processing
**Args:** `fastuniq -i reads_1.fastq -o reads_2.fastq -p deduplicated_ -t 8`
**Explanation:** Uses 8 threads for parallel processing.