---
name: sak
category: sequence_analysis
description: Sequence Analysis Toolkit for cutting and manipulating sequence files
tags: ["sak", "seqan", "sequence", "FASTA", "manipulation"]
author: oxo-call-community
source_url: "https://github.com/seqan/seqan/tree/master/apps/sak/README"
---

## Concepts

- **Tool Overview**: SAK (SeqAn Analysis Kit, v0.4.8) is a command-line toolkit for sequence manipulation, providing utilities for cutting, filtering, and transforming sequence files.
- **Core Function**: Manipulates FASTA/FASTQ sequences, including extraction, filtering, reverse complementing, and format conversion.
- **Algorithm**: Implements efficient sequence processing using the SeqAn library, supporting large files with minimal memory footprint.
- **Input Format**: FASTA, FASTQ, SAM/BAM (sequence data), BED/GFF (region definitions).
- **Output Format**: Processed sequences in FASTA/FASTQ format, statistics reports.
- **Use Case**: Sequence preprocessing, subsetting sequences, quality filtering, format conversion.

## Pitfalls

- **File size**: Very large files may require significant memory.
- **Format compatibility**: May not support all edge cases of sequence formats.
- **Quality scores**: FASTQ processing requires proper quality score handling.
- **Region specification**: BED coordinates must be 0-based or 1-based as specified.
- **Compression**: May require decompression for gzipped files.
- **Ambiguous bases**: Handling of ambiguous bases may vary by operation.

## Examples

### Extract subsequence
**Args:** `sak extract -i input.fasta -r chr1:1000-2000 -o output.fasta`
**Explanation:** Extracts sequence from position 1000-2000 on chr1.

### Filter by length
**Args:** `sak filter -i input.fasta -o filtered.fasta -m 1000 -M 5000`
**Explanation:** `-m` minimum length; `-M` maximum length filter.

### Reverse complement
**Args:** `sak revcomp -i input.fasta -o output.fasta`
**Explanation:** Generates reverse complement of sequences.

### Convert FASTQ to FASTA
**Args:** `sak convert -i reads.fastq -o reads.fasta --to fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Extract by ID
**Args:** `sak extract -i input.fasta --ids ids.txt -o selected.fasta`
**Explanation:** Extracts sequences matching IDs in ids.txt.

### Quality filter FASTQ
**Args:** `sak filter -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** `-q` minimum average quality score threshold.

### Shuffle sequences
**Args:** `sak shuffle -i input.fasta -o shuffled.fasta`
**Explanation:** Randomly shuffles sequence order.