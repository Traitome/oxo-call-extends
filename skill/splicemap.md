---
name: splicemap
category: rna-seq
description: SpliceMap - Splice junction detection from RNA-seq data
tags: [splicemap, rna-seq, splice-junctions, alignment, novel-junctions]
author: oxo-call-community
source_url: "https://web.stanford.edu/group/wonglab/SpliceMap"
---

## Concepts

- **Tool Overview**: splicemap (v3.3.5.2) - A splice junction detection tool
- **Core Function**: Detects splice junctions from RNA-seq data without annotation
- **Input/Output**: Accepts RNA-seq reads; outputs splice junction predictions
- **Algorithm**: Novel splice junction detection with high sensitivity
- **Installation**: `conda install -c bioconda splicemap`
- **Key Features**: Splice detection, novel junctions, annotation-free

## Pitfalls

- **Input Requirements**: Requires properly formatted RNA-seq reads
- **Read Quality**: Read quality affects junction detection accuracy
- **Read Length**: Optimized for long reads (50-100 nt)
- **Memory Usage**: Large RNA-seq datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Detection Accuracy**: Accuracy depends on read quality and coverage

## Examples

### Display help
**Args:** `splicemap --help`
**Explanation:** Shows available options and usage information.

### Basic splice junction detection
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed`
**Explanation:** Detect splice junctions from RNA-seq reads.

### With paired-end reads
**Args:** `splicemap -i reads_1.fastq reads_2.fastq -r reference.fasta -o junctions.bed`
**Explanation:** Use paired-end reads for detection.

### With read length
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed --read-length 100`
**Explanation:** Set read length for detection.

### Output detailed results
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed --detailed`
**Explanation:** Output detailed junction information.

### Output novel junctions
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed --novel`
**Explanation:** Output novel splice junctions.

### Output statistics
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed --stats`
**Explanation:** Output detection statistics.

### Generate report
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed --report`
**Explanation:** Generate detection report.

### With threads
**Args:** `splicemap -i reads.fastq -r reference.fasta -o junctions.bed -p 8`
**Explanation:** Use multiple threads for detection.