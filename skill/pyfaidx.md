---
name: pyfaidx
category: formatting
description: pyfaidx provides efficient random access to FASTA subsequences.
tags: [pyfaidx, formatting, fasta, sequence-analysis]
author: oxo-call-community
source_url: "https://pypi.org/project/pyfaidx"
---

## Concepts

- **Tool Overview**: pyfaidx indexes FASTA files.
- **Core Function**: FASTA subsequence extraction.
- **Algorithm**: Uses index-based access.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces subsequences.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Index File**: Requires index generation.
- **Sequence Names**: Must match index.
- **Runtime**: Indexing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyfaidx --help`
**Explanation:** Shows available options and usage instructions.

### Extract subsequence
**Args:** `pyfaidx extract -i genome.fasta -r chr1:1-1000 -o region.fasta`
**Explanation:** Extracts subsequence from FASTA.

### With parameters
**Args:** `pyfaidx extract -i genome.fasta -p params.yaml -o region.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyfaidx -v extract -i genome.fasta -o region.fasta`
**Explanation:** Runs with verbose output.

### Build index
**Args:** `pyfaidx index -i genome.fasta`
**Explanation:** Creates FASTA index.

### List sequences
**Args:** `pyfaidx list -i genome.fasta`
**Explanation:** Lists sequence names.

### Generate report
**Args:** `pyfaidx extract -i genome.fasta -o region.fasta --report report.html`
**Explanation:** Generates HTML report.