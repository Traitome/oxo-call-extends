---
name: sylph
category: metagenomics
description: Quickly query genomes against low-coverage shotgun metagenomes to find nearest neighbour ANI.
tags: [sylph, metagenomics, ANI, genome-comparison]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/sylph/blob/v0.9.0/README.md"
---

## Concepts

- **Tool Overview**: sylph (v0.9.0) is a fast metagenome profiler for ANI estimation.
- **Core Function**: Query genomes against low-coverage shotgun metagenomes.
- **Algorithm**: Uses k-mer based approach for fast ANI estimation.
- **Input/Output**: Input: FASTQ reads, genome database; Output: ANI scores.
- **Applications**: Metagenome analysis, microbial identification, strain typing.
- **Installation**: `conda install -c bioconda sylph` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large databases require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect ANI estimation.
- **Read Quality**: Poor quality reads affect results.
- **Database Quality**: Requires well-curated genome database.
- **Coverage Depth**: Very low coverage may affect accuracy.

## Examples

### Display help
**Args:** `sylph --help`
**Explanation:** Shows available options and usage information.

### Basic metagenome profiling
**Args:** `sylph -i reads.fastq -d genome_db/ -o results.txt`
**Explanation:** Profile metagenome reads against genome database.

### With reference
**Args:** `sylph -i reads.fastq -d genome_db/ -r reference.fasta -o results.txt`
**Explanation:** Use reference genome for comparison.

### Verbose mode
**Args:** `sylph -i reads.fastq -d genome_db/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sylph -i reads.fastq -d genome_db/ -o results.txt --stats`
**Explanation:** Generate statistics about profiling.

### Batch processing
**Args:** `for f in reads/*.fastq; do sylph -i $f -d db/ -o results/${f%.fastq}.txt; done`
**Explanation:** Process multiple read files.

### Filter by ANI
**Args:** `sylph -i reads.fastq -d genome_db/ -o results.txt -a 95`
**Explanation:** Filter results by minimum ANI score.

### Include all hits
**Args:** `sylph -i reads.fastq -d genome_db/ -o results.txt --all`
**Explanation:** Output all matches.

### Generate report
**Args:** `sylph -i reads.fastq -d genome_db/ -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
