---
name: kmer2stats
category: utility
description: A tool for creating data files for statistic based on kmers
tags: [kmer2stats, utility, k-mer, statistics, genomics]
author: oxo-call-community
source_url: "https://github.com/SantaMcCloud/kmer2stats"
---

## Concepts

- **K-mer Statistics**: Generates statistical data from k-mer analysis
- **Data Export**: Creates files for downstream statistical analysis
- **Genomic Analysis**: Provides statistics for genomic sequence analysis
- **Quality Assessment**: Assesses sequencing data quality using k-mers
- **Distribution Analysis**: Analyzes k-mer frequency distributions
- **Report Generation**: Generates comprehensive statistical reports

## Pitfalls

- **K-mer Size**: Different k-mer sizes provide different insights
- **Data Quality**: Low-quality reads affect statistics
- **Memory Usage**: Large genomes require significant memory
- **Input Format**: Requires proper input format for analysis
- **Statistical Interpretation**: Statistical results require careful interpretation
- **Database Dependency**: Some analyses depend on reference databases

## Examples

### Generate k-mer statistics
**Args:** `kmer2stats -i input.fastq -o statistics.csv`
**Explanation:** Generates k-mer statistics from sequencing data.

### Specify k-mer size
**Args:** `kmer2stats -i input.fastq -k 21 -o stats.csv`
**Explanation:** Uses k-mer size of 21 for statistics generation.

### Quality assessment
**Args:** `kmer2stats -i reads.fastq --quality -o quality_report.txt`
**Explanation:** Assesses sequencing quality using k-mer analysis.

### Export distribution data
**Args:** `kmer2stats -i input.fastq --distribution -o distribution.csv`
**Explanation:** Exports k-mer frequency distribution data.

### Batch processing
**Args:** `kmer2stats --batch -d samples/ -o results/`
**Explanation:** Processes multiple samples and generates batch statistics.

### Compare samples
**Args:** `kmer2stats -i sample1.fastq -i sample2.fastq --compare -o comparison.csv`
**Explanation:** Compares k-mer statistics between two samples.