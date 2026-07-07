---
name: parse_mito_blast
category: alignment
description: parse_mito_blast filters BLAST results from mitochondrial database queries.
tags: [parse_mito_blast, alignment, blast, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/VGP/vgp-assembly/tree/master/galaxy_tools/parse_mito_blast"
---

## Concepts

- **Tool Overview**: parse_mito_blast processes mitochondrial BLAST results.
- **Core Function**: Filters and analyzes BLAST alignments to mitochondria.
- **Algorithm**: Parses BLAST output and filters mitochondrial hits.
- **Input Format**: Accepts BLAST output files.
- **Output**: Produces filtered mitochondrial matches.
- **Use Case**: Mitochondrial genome analysis, assembly validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Quality**: Results depend on database quality.
- **E-value Threshold**: Results depend on E-value cutoff.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parse_mito_blast --help`
**Explanation:** Shows available options and usage instructions.

### Filter BLAST output
**Args:** `parse_mito_blast -i blast.out -o filtered.txt`
**Explanation:** Filters mitochondrial BLAST hits.

### With E-value cutoff
**Args:** `parse_mito_blast -i blast.out -e 1e-10 -o filtered.txt`
**Explanation:** Sets E-value threshold to 1e-10.

### Verbose mode
**Args:** `parse_mito_blast -v -i blast.out -o filtered.txt`
**Explanation:** Runs with verbose output.

### Identity threshold
**Args:** `parse_mito_blast -i blast.out -p 90 -o filtered.txt`
**Explanation:** Sets minimum identity to 90%.

### Output format
**Args:** `parse_mito_blast -i blast.out -o filtered.gff --gff`
**Explanation:** Outputs in GFF format.

### Include statistics
**Args:** `parse_mito_blast -i blast.out -o filtered.txt -s stats.txt`
**Explanation:** Generates statistics file.