---
name: pbskera
category: qc
description: pbSkera splits concatenated read designs from PacBio sequencing.
tags: [pbskera, qc, pacbio, concatenated]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/skera"
---

## Concepts

- **Tool Overview**: pbSkera splits concatenated reads.
- **Core Function**: Separates concatenated read designs.
- **Algorithm**: Uses adapter detection and splitting.
- **Input Format**: Accepts PacBio BAM files.
- **Output**: Produces split read files.
- **Use Case**: Read processing, library design.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Adapter Detection**: Requires proper adapter sequences.
- **Read Quality**: Results depend on input quality.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `skera --help`
**Explanation:** Shows available options and usage instructions.

### Split reads
**Args:** `skera -i concatenated.bam -o split.bam`
**Explanation:** Splits concatenated reads.

### With adapters
**Args:** `skera -i concatenated.bam -a adapters.fasta -o split.bam`
**Explanation:** Uses custom adapter sequences.

### Verbose mode
**Args:** `skera -v -i concatenated.bam -o split.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `skera -t 4 -i concatenated.bam -o split.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `skera -i concatenated.bam -o split.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Generate report
**Args:** `skera -i concatenated.bam -o split.bam --report report.html`
**Explanation:** Generates HTML report.