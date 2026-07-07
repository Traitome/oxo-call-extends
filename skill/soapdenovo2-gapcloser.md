---
name: soapdenovo2-gapcloser
category: assembly
description: GapCloser - Gap filling tool for SOAPdenovo2 assemblies
tags: [soapdenovo2-gapcloser, assembly, gap-filling, soapdenovo]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/soapdenovo2/files/GapCloser"
---

## Concepts

- **Tool Overview**: soapdenovo2-gapcloser (v1.12) - A tool for filling gaps in assemblies
- **Core Function**: Closes gaps in draft assemblies using read information
- **Input/Output**: Accepts assembly and reads; outputs gap-filled assembly
- **Algorithm**: Uses read alignments to fill assembly gaps
- **Installation**: `conda install -c bioconda soapdenovo2-gapcloser`
- **Key Features**: Gap filling, assembly improvement, read-based closure

## Pitfalls

- **Input Requirements**: Requires assembly contigs/scaffolds and reads
- **Assembly Quality**: Quality of input assembly affects gap filling
- **Read Coverage**: Sufficient read coverage needed for gap closure
- **Memory Usage**: Large assemblies require significant memory
- **Gap Size**: Large gaps may not be fully closed
- **Output Format**: Output format must match assembly format

## Examples

### Display help
**Args:** `GapCloser --help`
**Explanation:** Shows available options and usage information.

### Basic gap closing
**Args:** `GapCloser -a assembly.fasta -b reads.fastq -o closed.fasta`
**Explanation:** Fill gaps in assembly.

### With config file
**Args:** `GapCloser -a assembly.fasta -c config.txt -o closed.fasta`
**Explanation:** Use configuration file for gap closing.

### Paired-end reads
**Args:** `GapCloser -a assembly.fasta -p reads_1.fastq reads_2.fastq -o closed.fasta`
**Explanation:** Use paired-end reads for gap filling.

### Set overlap length
**Args:** `GapCloser -a assembly.fasta -b reads.fastq -o closed.fasta -l 31`
**Explanation:** Set minimum overlap length.

### With threads
**Args:** `GapCloser -a assembly.fasta -b reads.fastq -o closed.fasta -p 8`
**Explanation:** Use multiple threads for gap closing.

### Output statistics
**Args:** `GapCloser -a assembly.fasta -b reads.fastq -o closed.fasta --stats`
**Explanation:** Output gap closing statistics.

### Generate report
**Args:** `GapCloser -a assembly.fasta -b reads.fastq -o closed.fasta --report`
**Explanation:** Generate gap closing report.