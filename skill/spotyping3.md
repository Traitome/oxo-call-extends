---
name: spotyping3
category: microbiology
description: SpoTyping3 - Mycobacterium spoligotyping from sequence reads (Python3)
tags: [spotyping3, microbiology, spoligotyping, mycobacterium, tuberculosis]
author: oxo-call-community
source_url: "https://github.com/matnguyen/SpoTyping"
---

## Concepts

- **Tool Overview**: spotyping3 (v3.0) - A Mycobacterium spoligotyping tool
- **Core Function**: Performs in silico spoligotyping from sequence reads
- **Input/Output**: Accepts sequence reads; outputs spoligotype patterns
- **Algorithm**: Spoligotype pattern detection and classification
- **Installation**: `conda install -c bioconda spotyping3`
- **Key Features**: Spoligotyping, Mycobacterium, Python3 compatible

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence reads
- **Read Quality**: Read quality affects spoligotype accuracy
- **Database Coverage**: Database coverage affects spoligotype identification
- **Memory Usage**: Large read sets require significant memory
- **Output Format**: Output format depends on configuration
- **Spoligotype Accuracy**: Accuracy depends on read quality and database

## Examples

### Display help
**Args:** `spotyping3 --help`
**Explanation:** Shows available options and usage information.

### Basic spoligotyping
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt`
**Explanation:** Perform spoligotyping from reads.

### With database
**Args:** `spotyping3 -i reads.fastq -d spoligotype_db/ -o spoligotype.txt`
**Explanation:** Use specific spoligotype database.

### Multiple read files
**Args:** `spotyping3 -i reads_1.fastq reads_2.fastq -o spoligotype.txt`
**Explanation:** Spoligotype from multiple read files.

### With quality filter
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt --quality-filter`
**Explanation:** Enable quality filtering.

### Output detailed results
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt --detailed`
**Explanation:** Output detailed spoligotype information.

### Output patterns
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt --patterns`
**Explanation:** Output spoligotype patterns.

### Output statistics
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt --stats`
**Explanation:** Output spoligotyping statistics.

### Generate report
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt --report`
**Explanation:** Generate spoligotyping report.

### With threads
**Args:** `spotyping3 -i reads.fastq -o spoligotype.txt -p 8`
**Explanation:** Use multiple threads for spoligotyping.