---
name: pyfasta
category: formatting
description: pyfasta provides fast, memory-efficient access to FASTA sequence files.
tags: [pyfasta, formatting, fasta, sequence-analysis]
author: oxo-call-community
source_url: "http://github.com/brentp/pyfasta/"
---

## Concepts

- **Tool Overview**: pyfasta accesses FASTA files.
- **Core Function**: FASTA sequence retrieval.
- **Algorithm**: Uses indexed access.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces sequences.
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
**Args:** `pyfasta --help`
**Explanation:** Shows available options and usage instructions.

### Extract sequence
**Args:** `pyfasta extract -i genome.fasta -c chr1 -s 1 -e 1000 -o region.fasta`
**Explanation:** Extracts subsequence from FASTA.

### With parameters
**Args:** `pyfasta extract -i genome.fasta -p params.yaml -o region.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyfasta -v extract -i genome.fasta -o region.fasta`
**Explanation:** Runs with verbose output.

### Build index
**Args:** `pyfasta index -i genome.fasta`
**Explanation:** Creates FASTA index.

### List sequences
**Args:** `pyfasta list -i genome.fasta`
**Explanation:** Lists sequence names.

### Generate report
**Args:** `pyfasta extract -i genome.fasta -o region.fasta --report report.html`
**Explanation:** Generates HTML report.