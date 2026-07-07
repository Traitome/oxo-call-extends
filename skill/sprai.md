---
name: sprai
category: assembly
description: Sprai - Single-pass read accuracy improver for de novo assembly
tags: [sprai, assembly, error-correction, pacbio, long-reads]
author: oxo-call-community
source_url: "http://zombie.cb.k.u-tokyo.ac.jp/sprai/"
---

## Concepts

- **Tool Overview**: sprai (v0.9.9.23) - A read error correction tool for assembly
- **Core Function**: Corrects sequencing errors in single-pass reads for de novo assembly
- **Input/Output**: Accepts PacBio CLRs; outputs error-corrected reads
- **Algorithm**: Error correction optimized for assembly continuity
- **Installation**: `conda install -c bioconda sprai`
- **Key Features**: Error correction, PacBio reads, assembly optimization

## Pitfalls

- **Input Requirements**: Requires properly formatted PacBio CLR reads
- **Read Quality**: Read quality affects correction accuracy
- **Assembly Continuity**: Optimized for N50 contig length, not read accuracy
- **Memory Usage**: Large read sets require significant memory
- **Output Format**: Output format depends on configuration
- **Correction Accuracy**: Accuracy depends on read quality and coverage

## Examples

### Display help
**Args:** `sprai --help`
**Explanation:** Shows available options and usage information.

### Basic error correction
**Args:** `sprai -i reads.fastq -o corrected_reads/`
**Explanation:** Correct errors in PacBio reads.

### With coverage
**Args:** `sprai -i reads.fastq -o corrected_reads/ --coverage 30`
**Explanation:** Set expected coverage for correction.

### With k-mer size
**Args:** `sprai -i reads.fastq -o corrected_reads/ --kmer 15`
**Explanation:** Set k-mer size for error correction.

### Multiple read files
**Args:** `sprai -i reads1.fastq reads2.fastq -o corrected_reads/`
**Explanation:** Correct multiple read files.

### Output detailed results
**Args:** `sprai -i reads.fastq -o corrected_reads/ --detailed`
**Explanation:** Output detailed correction information.

### Output statistics
**Args:** `sprai -i reads.fastq -o corrected_reads/ --stats`
**Explanation:** Output correction statistics.

### Generate report
**Args:** `sprai -i reads.fastq -o corrected_reads/ --report`
**Explanation:** Generate correction report.

### With threads
**Args:** `sprai -i reads.fastq -o corrected_reads/ -p 8`
**Explanation:** Use multiple threads for correction.