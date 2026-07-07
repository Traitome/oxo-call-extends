---
name: pcne
category: annotation
description: PCNE estimates plasmid copy number from assembled genomes.
tags: [pcne, annotation, plasmid, copy-number]
author: oxo-call-community
source_url: "https://github.com/riccabolla/PCNE"
---

## Concepts

- **Tool Overview**: PCNE estimates plasmid copy numbers.
- **Core Function**: Calculates plasmid copy number from assembly.
- **Algorithm**: Uses read coverage analysis.
- **Input Format**: Accepts genome assemblies.
- **Output**: Produces copy number estimates.
- **Use Case**: Plasmid analysis, genome annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Depends on assembly size.
- **Coverage Quality**: Results depend on sequencing coverage.
- **Plasmid Detection**: Requires proper plasmid identification.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pcne --help`
**Explanation:** Shows available options and usage instructions.

### Estimate copy number
**Args:** `pcne -i assembly.fasta -o copy_numbers.txt`
**Explanation:** Estimates plasmid copy numbers.

### With reads
**Args:** `pcne -i assembly.fasta -r reads.bam -o copy_numbers.txt`
**Explanation:** Uses read coverage for estimation.

### Verbose mode
**Args:** `pcne -v -i assembly.fasta -o copy_numbers.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pcne -t 4 -i assembly.fasta -o copy_numbers.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pcne -i assembly.fasta -o copy_numbers.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pcne -i assembly.fasta -o copy_numbers.txt --report report.html`
**Explanation:** Generates HTML report.