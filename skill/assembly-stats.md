---
name: assembly-stats
category: assembly
description: Assembly-stats - Get assembly statistics from FASTA and FASTQ files
tags: [assembly-stats, assembly, statistics, fasta, fastq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/assembly-stats"
---

## Concepts

- **Tool Overview**: Assembly-stats is a command-line tool for calculating assembly statistics from FASTA and FASTQ files. Version 1.0.1.
- **Core Function**: Computes various assembly quality metrics including N50, L50, total bases, contig counts, and read statistics.
- **Multi-format Support**: Works with both FASTA (assemblies) and FASTQ (raw reads) files.
- **Statistics Calculation**: Computes N50, L50, N90, total length, GC content, number of sequences, and average sequence length.
- **Read Statistics**: For FASTQ files, calculates read count, total bases, average read length, and quality metrics.
- **Simple Output**: Provides clear, human-readable output with summary statistics.
- **Input/Output**: Accepts FASTA/FASTQ files, outputs statistics to stdout or file.
- **Installation**: `conda install -c bioconda assembly-stats` or compile from source.

## Pitfalls

- **File Format**: Requires properly formatted FASTA/FASTQ files. Invalid formats cause parsing errors.
- **Compressed Files**: Does not handle gzipped files directly. Must uncompress first or use zcat.
- **Memory Usage**: Large files may require significant memory. Consider processing in chunks.
- **Ambiguity Codes**: May not correctly handle non-standard IUPAC nucleotide codes.
- **Quality Scores**: FASTQ quality scores must be in valid format (Phred 33 or 64).
- **Empty Files**: Empty input files produce no output or errors.

## Examples

### Display help
**Args:** `assembly-stats --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic usage with FASTA
**Args:** `assembly-stats assembly.fasta`
**Explanation:** Outputs assembly statistics for FASTA file including N50, L50, and total length.

### Basic usage with FASTQ
**Args:** `assembly-stats reads.fastq`
**Explanation:** Outputs read statistics for FASTQ file including read count and total bases.

### Output to file
**Args:** `assembly-stats assembly.fasta > stats.txt`
**Explanation:** Redirects statistics output to text file for later analysis.

### Multiple files
**Args:** `assembly-stats assembly1.fasta assembly2.fasta`
**Explanation:** Processes multiple FASTA files and outputs statistics for each.

### Detailed output
**Args:** `assembly-stats -d assembly.fasta`
**Explanation:** Provides detailed statistics including N90, N75, and GC content.

### Summary only
**Args:** `assembly-stats -s assembly.fasta`
**Explanation:** Outputs only summary statistics without detailed breakdown.

### From stdin
**Args:** `cat assembly.fasta | assembly-stats`
**Explanation:** Reads FASTA data from standard input and outputs statistics.

### Process compressed file
**Args:** `zcat assembly.fasta.gz | assembly-stats`
**Explanation:** Processes gzipped FASTA file by piping through zcat.

### Compare assemblies
**Args:** `assembly-stats -d assembly1.fasta assembly2.fasta | diff -u`
**Explanation:** Compares statistics between two assemblies using diff.