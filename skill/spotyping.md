---
name: spotyping
category: microbiology
description: SpoTyping - Mycobacterium spoligotyping from sequence reads
tags: [spotyping, microbiology, spoligotyping, mycobacterium, tuberculosis]
author: oxo-call-community
source_url: "https://github.com/xiaeryu/SpoTyping"
---

## Concepts

- **Tool Overview**: spotyping (v2.1) - A Mycobacterium spoligotyping tool
- **Core Function**: Performs in silico spoligotyping from sequence reads
- **Input/Output**: Accepts sequence reads; outputs spoligotype patterns
- **Algorithm**: Spoligotype pattern detection and classification
- **Installation**: `conda install -c bioconda spotyping`
- **Key Features**: Spoligotyping, Mycobacterium, fast and accurate

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence reads
- **Read Quality**: Read quality affects spoligotype accuracy
- **Database Coverage**: Database coverage affects spoligotype identification
- **Memory Usage**: Large read sets require significant memory
- **Output Format**: Output format depends on configuration
- **Spoligotype Accuracy**: Accuracy depends on read quality and database

## Examples

### Display help
**Args:** `spotyping --help`
**Explanation:** Shows available options and usage information.

### Basic spoligotyping
**Args:** `spotyping -i reads.fastq -o spoligotype.txt`
**Explanation:** Perform spoligotyping from reads.

### With database
**Args:** `spotyping -i reads.fastq -d spoligotype_db/ -o spoligotype.txt`
**Explanation:** Use specific spoligotype database.

### Multiple read files
**Args:** `spotyping -i reads_1.fastq reads_2.fastq -o spoligotype.txt`
**Explanation:** Spoligotype from multiple read files.

### With quality filter
**Args:** `spotyping -i reads.fastq -o spoligotype.txt --quality-filter`
**Explanation:** Enable quality filtering.

### Output detailed results
**Args:** `spotyping -i reads.fastq -o spoligotype.txt --detailed`
**Explanation:** Output detailed spoligotype information.

### Output patterns
**Args:** `spotyping -i reads.fastq -o spoligotype.txt --patterns`
**Explanation:** Output spoligotype patterns.

### Output statistics
**Args:** `spotyping -i reads.fastq -o spoligotype.txt --stats`
**Explanation:** Output spoligotyping statistics.

### Generate report
**Args:** `spotyping -i reads.fastq -o spoligotype.txt --report`
**Explanation:** Generate spoligotyping report.

### With threads
**Args:** `spotyping -i reads.fastq -o spoligotype.txt -p 8`
**Explanation:** Use multiple threads for spoligotyping.