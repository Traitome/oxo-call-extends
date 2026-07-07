---
name: lastz
category: alignment
description: Pairwise DNA sequence aligner
tags: [lastz, alignment, DNA-alignment, pairwise-alignment, genomics]
author: oxo-call-community
source_url: "https://github.com/lastz/lastz"
---

## Concepts

- **Pairwise Alignment**: Aligns two DNA sequences
- **BLAST-like**: Similar to BLASTZ but improved
- **Dotplot Output**: Can generate dotplot visualizations
- **Gap Penalties**: Customizable gap open and extension penalties
- **Scoring Schemes**: Multiple scoring schemes available
- **Chain/Net Support**: Supports alignment chaining

## Pitfalls

- **Pairwise Only**: Cannot align multiple sequences at once
- **Memory Usage**: Large sequences require significant memory
- **Parameter Selection**: Default parameters may not suit all alignments
- **Seed Selection**: Seed step affects sensitivity/speed
- **Output Format**: Different from standard BLAST output
- **Identity Threshold**: Identity cutoff affects results

## Examples

### Align sequences
**Args:** `lastz target.fasta query.fasta --output=alignments.maf`
**Explanation:** Aligns query to target in MAF format.

### Dotplot output
**Args:** `lastz target.fasta query.fasta --dotplot`
**Explanation:** Creates dotplot visualization.

### Set identity threshold
**Args:** `lastz target.fasta query.fasta --identity=80 --output=results.maf`
**Explanation:** Only reports alignments with 80% identity.

### Custom gap penalties
**Args:** `lastz target.fasta query.fasta --gap=0,150 --output=results.maf`
**Explanation:** Sets gap open=0, extend=150.

### Convert to SAM
**Args:** `lastz target.fasta query.fasta --format=sam > alignments.sam`
**Explanation:** Outputs alignments in SAM format.

### Multiple query sequences
**Args:** `lastz target.fasta queries.fasta --output=results.maf`
**Explanation:** Aligns multiple query sequences.