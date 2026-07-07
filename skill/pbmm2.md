---
name: pbmm2
category: qc
description: pbmm2 provides minimap2 frontend for PacBio native data formats.
tags: [pbmm2, qc, pacbio, minimap2]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbmm2"
---

## Concepts

- **Tool Overview**: pbmm2 aligns PacBio data.
- **Core Function**: Wrapper for minimap2 alignment.
- **Algorithm**: Uses minimap2 for long-read alignment.
- **Input Format**: Accepts PacBio BAM/FASTQ formats.
- **Output**: Produces aligned BAM files.
- **Use Case**: Long-read alignment, PacBio data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Alignment Presets**: Different presets for different data types.
- **Computational Cost**: Alignment can be computationally intensive.
- **Runtime**: Depends on genome size and thread count.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbmm2 --help`
**Explanation:** Shows available options and usage instructions.

### Align reads
**Args:** `pbmm2 align reference.fasta reads.bam aligned.bam`
**Explanation:** Aligns reads to reference.

### With preset
**Args:** `pbmm2 align --preset SUBREAD reference.fasta reads.bam aligned.bam`
**Explanation:** Uses SUBREAD preset for alignment.

### Verbose mode
**Args:** `pbmm2 -v align reference.fasta reads.bam aligned.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbmm2 align -t 16 reference.fasta reads.bam aligned.bam`
**Explanation:** Uses 16 threads for parallel processing.

### Sort output
**Args:** `pbmm2 align --sort reference.fasta reads.bam aligned.bam`
**Explanation:** Sorts output BAM file.

### Output format
**Args:** `pbmm2 align --output-format sam reference.fasta reads.bam aligned.sam`
**Explanation:** Outputs in SAM format.