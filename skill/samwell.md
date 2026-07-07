---
name: samwell
category: formatting
description: Useful utilities for biological data formats and analyses
tags: ["samwell", "formatting", "sam", "bam", "python", "utilities"]
author: oxo-call-community
source_url: "https://pypi.org/project/samwell/"
---

## Concepts
- **Tool Overview**: samwell (v0.0.4) is a Python package providing elegant utilities for managing biological data formats and analyses.
- **Core Function**: Offers utilities for SAM/BAM file manipulation, DNA sequence handling, genomic region queries, and BWA alignment integration.
- **Algorithm**: Built on pysam with additional abstraction layers for easier manipulation of genomic data.
- **Input Format**: SAM/BAM files, FASTA sequences, genomic intervals.
- **Output Format**: Processed SAM/BAM files, sequence data, analysis results.
- **Use Case**: Bioinformatics pipeline development, SAM/BAM file processing, sequence analysis, testing utilities.

## Pitfalls
- **Python Dependencies**: Requires specific Python version and dependencies.
- **BWA Integration**: BWA must be installed for alignment functions.
- **File Compatibility**: May not support all SAM/BAM features or edge cases.
- **Memory Management**: Large files require careful memory handling.
- **API Changes**: As a young package, API may change between versions.
- **Documentation**: Limited documentation for some advanced features.

## Examples
### Read BAM file
**Args:** `from samwell import sam; with sam.reader("input.bam") as bam: ...`
**Explanation:** Python API for reading BAM files with automatic format detection.

### Write filtered BAM
**Args:** `with sam.writer("output.bam", header=bam.header) as out: [out.write(r) for r in bam if r.is_paired]`
**Explanation:** Filters and writes only paired reads to output BAM.

### Realign reads with BWA
**Args:** `from samwell.sam import bwa_mem; for read in bwa_mem.align(fastq_gen, "genome.fasta"): ...`
**Explanation:** Realigns FASTQ records using BWA-MEM.

### Soft-clip reads
**Args:** `from samwell.sam import clipping; clipped = clipping.soft_clip(read, 5)`
**Explanation:** Soft-clips 5 bases from both ends of a read.

### Query genomic overlaps
**Args:** `from samwell import intervals; overlaps = intervals.query(regions, query_region)`
**Explanation:** Finds intervals overlapping with a query region.

### Generate test data
**Args:** `from samwell.testing import make_bam; bam = make_bam(reads=1000)`
**Explanation:** Generates synthetic BAM files for testing purposes.

### DNA sequence utilities
**Args:** `from samwell import dna; rc = dna.reverse_complement("ACGT")`
**Explanation:** Computes reverse complement of DNA sequence.