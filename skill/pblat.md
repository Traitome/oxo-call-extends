---
name: pblat
category: utility
description: pblat provides BLAT alignment with multi-threading support.
tags: [pblat, utility, alignment, blat]
author: oxo-call-community
source_url: "https://icebert.github.io/pblat"
---

## Concepts

- **Tool Overview**: pblat aligns sequences using BLAT.
- **Core Function**: Performs fast sequence alignment.
- **Algorithm**: Uses BLAT algorithm with parallel processing.
- **Input Format**: Accepts FASTA/FASTQ sequences.
- **Output**: Produces alignment files (PSL format).
- **Use Case**: Sequence alignment, genome mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Alignment Sensitivity**: May miss some alignments.
- **Computational Cost**: Parallel processing improves speed.
- **Runtime**: Depends on genome size and thread count.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pblat --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `pblat database.fasta query.fasta output.psl`
**Explanation:** Aligns query to database.

### With threads
**Args:** `pblat -threads=8 database.fasta query.fasta output.psl`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `pblat -verbose database.fasta query.fasta output.psl`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `pblat -out=blast8 database.fasta query.fasta output.blast8`
**Explanation:** Outputs in BLAST-8 format.

### Fine alignment
**Args:** `pblat -fine database.fasta query.fasta output.psl`
**Explanation:** Uses fine alignment mode.

### Min identity
**Args:** `pblat -minIdentity=90 database.fasta query.fasta output.psl`
**Explanation:** Sets minimum identity threshold.