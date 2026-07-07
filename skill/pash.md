---
name: pash
category: alignment
description: Pash performs read mapping and analysis of genomic and epigenomic variation.
tags: [pash, alignment, read-mapping, epigenomics]
author: oxo-call-community
source_url: "http://www.bioinformatics.bbsrc.ac.uk/projects/bismark/"
---

## Concepts

- **Tool Overview**: Pash maps reads and analyzes genomic variation.
- **Core Function**: Performs read mapping and variant analysis.
- **Algorithm**: Uses efficient mapping strategies.
- **Input Format**: Accepts sequencing reads in FASTQ format.
- **Output**: Produces alignment files and variant calls.
- **Use Case**: Genomic and epigenomic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Index**: Requires indexed reference genome.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pash --help`
**Explanation:** Shows available options and usage instructions.

### Map reads
**Args:** `pash -r reference.fasta -i reads.fastq -o output.bam`
**Explanation:** Maps reads to reference genome.

### Paired-end mapping
**Args:** `pash -r reference.fasta -1 read1.fastq -2 read2.fastq -o output.bam`
**Explanation:** Maps paired-end reads.

### Verbose mode
**Args:** `pash -v -r reference.fasta -i reads.fastq -o output.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pash -t 8 -r reference.fasta -i reads.fastq -o output.bam`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pash -r reference.fasta -i reads.fastq -o output.sam --sam`
**Explanation:** Outputs in SAM format.

### Quality filtering
**Args:** `pash -q 20 -r reference.fasta -i reads.fastq -o output.bam`
**Explanation:** Filters reads by quality.