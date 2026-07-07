---
name: syri
category: comparative-genomics
description: Synteny and rearrangement identifier between whole-genome assemblies.
tags: [syri, synteny, genome-rearrangement, comparative-genomics]
author: oxo-call-community
source_url: "https://schneebergerlab.github.io/syri"
---

## Concepts

- **Tool Overview**: syri (v1.7.1) identifies synteny and rearrangements between genomes.
- **Core Function**: Detects syntenic regions and structural rearrangements.
- **Algorithm**: Uses whole-genome alignment for rearrangement detection.
- **Input/Output**: Input: Genome assemblies; Output: Synteny blocks, rearrangements.
- **Applications**: Comparative genomics, evolutionary analysis, pan-genomics.
- **Installation**: `conda install -c bioconda syri` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Whole-genome alignment can be slow.
- **Parameter Tuning**: Incorrect parameters affect detection.
- **Assembly Quality**: Requires high-quality genome assemblies.
- **Alignment Quality**: Depends on accurate alignments.
- **Genome Complexity**: Complex genomes may be challenging.

## Examples

### Display help
**Args:** `syri --help`
**Explanation:** Shows available options and usage information.

### Basic synteny analysis
**Args:** `syri -c alignment.chain -d reference.fasta -q query.fasta -o syri.out`
**Explanation:** Analyze synteny between reference and query.

### With SAM input
**Args:** `syri -i alignment.sam -d reference.fasta -q query.fasta -o syri.out`
**Explanation:** Use SAM alignment file as input.

### Verbose mode
**Args:** `syri -c alignment.chain -d reference.fasta -q query.fasta -o syri.out -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `syri -c alignment.chain -d reference.fasta -q query.fasta -o syri.out --stats`
**Explanation:** Generate statistics about synteny analysis.

### Batch processing
**Args:** `for f in alignments/*.chain; do syri -c $f -d ref.fasta -q query.fasta -o results/${f%.chain}.out; done`
**Explanation:** Process multiple alignment files.

### Filter by size
**Args:** `syri -c alignment.chain -d reference.fasta -q query.fasta -o syri.out -s 1000`
**Explanation:** Filter by minimum synteny block size.

### Include all rearrangements
**Args:** `syri -c alignment.chain -d reference.fasta -q query.fasta -o syri.out --all-rearrangements`
**Explanation:** Detect all types of rearrangements.

### Generate report
**Args:** `syri -c alignment.chain -d reference.fasta -q query.fasta -o syri.out --report`
**Explanation:** Generate comprehensive synteny report.
