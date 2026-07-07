---
name: fastqsplitter
category: formatting
description: "Splits FASTQ files evenly."
tags: [fastqsplitter, formatting, FASTQ, splitting, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/LUMC/fastqsplitter"
---

## Concepts

- **Tool Overview**: fastqsplitter is a tool for splitting large FASTQ files into smaller, evenly sized files.
- **Core Function**: Divides FASTQ files into multiple smaller files for parallel processing.
- **Input/Output**: Input: FASTQ file. Output: Multiple smaller FASTQ files.
- **Algorithm**: Splits files based on read count or file size.
- **Key Features**: Even splitting, configurable chunk size, paired-end support, progress tracking, efficient processing.
- **Installation**: `conda install -c bioconda fastqsplitter`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Read Distribution**: May not perfectly balance reads across output files.
- **File Size**: Very small chunk sizes may create many files.
- **Format Compatibility**: Requires standard FASTQ format.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Split by number of files
**Args:** `fastqsplitter -i input.fastq -o split_ -n 10`
**Explanation:** Splits into 10 equal parts.

### Split by reads per file
**Args:** `fastqsplitter -i input.fastq -o split_ -r 1000000`
**Explanation:** Splits into files with 1 million reads each.

### Paired-end splitting
**Args:** `fastqsplitter -i reads_1.fastq -I reads_2.fastq -o split_ -n 10`
**Explanation:** Splits paired-end files maintaining synchronization.

### Output directory
**Args:** `fastqsplitter -i input.fastq -d output_dir/ -n 10`
**Explanation:** Outputs split files to directory.

### Verbose mode
**Args:** `fastqsplitter -i input.fastq -o split_ -n 10 -v`
**Explanation:** Shows detailed progress information.