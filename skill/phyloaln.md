---
name: phyloaln
category: population-genomics
description: phyloaln performs reference-based multiple sequence alignment.
tags: [phyloaln, population-genomics, alignment, phylogeny]
author: oxo-call-community
source_url: "https://github.com/huangyh45/PhyloAln"
---

## Concepts

- **Tool Overview**: phyloaln aligns sequences.
- **Core Function**: Reference-based alignment tool.
- **Algorithm**: Uses multiple sequence alignment methods.
- **Input Format**: Accepts FASTA/BAM/SAM files.
- **Output**: Produces aligned sequence results.
- **Use Case**: Sequence alignment, phylogeny.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Alignment Method**: Requires proper method selection.
- **Runtime**: Alignment may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyloaln --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `phyloaln -i sequences.fasta -r reference.fasta -o aligned_sequences.txt`
**Explanation:** Aligns sequences to reference.

### With parameters
**Args:** `phyloaln -i sequences.fasta -r reference.fasta -p params.yaml -o aligned_sequences.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyloaln -v -i sequences.fasta -r reference.fasta -o aligned_sequences.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyloaln -t 4 -i sequences.fasta -r reference.fasta -o aligned_sequences.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyloaln -i sequences.fasta -r reference.fasta -o aligned_sequences.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `phyloaln -i sequences.fasta -r reference.fasta -o aligned_sequences.txt --report report.html`
**Explanation:** Generates HTML report.