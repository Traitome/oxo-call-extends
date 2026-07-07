---
name: sylph-tax
category: metagenomics
description: Integrating taxonomic information into the sylph metagenome profiler.
tags: [sylph-tax, metagenomics, taxonomy, classification]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/sylph-tax/blob/v1.8.0/README.md"
---

## Concepts

- **Tool Overview**: sylph-tax (v1.8.0) integrates taxonomic information into sylph.
- **Core Function**: Taxonomic classification of metagenome sequences.
- **Algorithm**: Combines k-mer analysis with taxonomic databases.
- **Input/Output**: Input: FASTQ reads, taxonomic database; Output: Taxonomic profiles.
- **Applications**: Metagenome classification, microbial community analysis.
- **Installation**: `conda install -c bioconda sylph-tax` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large databases require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect classification.
- **Database Quality**: Requires up-to-date taxonomic database.
- **Read Quality**: Poor quality reads affect classification.
- **Coverage Depth**: Very low coverage may affect accuracy.

## Examples

### Display help
**Args:** `sylph-tax --help`
**Explanation:** Shows available options and usage information.

### Basic taxonomic profiling
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -o results.txt`
**Explanation:** Perform taxonomic classification of reads.

### With reference
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -r reference.fasta -o results.txt`
**Explanation:** Use reference genome for comparison.

### Verbose mode
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -o results.txt --stats`
**Explanation:** Generate statistics about classification.

### Batch processing
**Args:** `for f in reads/*.fastq; do sylph-tax -i $f -d db/ -o results/${f%.fastq}.txt; done`
**Explanation:** Process multiple read files.

### Filter by confidence
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -o results.txt -c 0.9`
**Explanation:** Filter results by confidence threshold.

### Include all levels
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -o results.txt --all-levels`
**Explanation:** Output taxonomy at all levels.

### Generate report
**Args:** `sylph-tax -i reads.fastq -d taxonomy_db/ -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
