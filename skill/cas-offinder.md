---
name: cas-offinder
category: genome-editing
description: Ultrafast CRISPR off-target site finder using OpenCL acceleration
tags: [cas-offinder, crispr, off-target, genome-editing, cas]
author: oxo-call-community
source_url: "https://github.com/snugel/cas-offinder"
---

## Concepts

- **Tool Overview**: Cas-OFFinder finds potential CRISPR/Cas off-target sites with ultrafast OpenCL-based search.
- **Core Function**: Searches genome for potential off-target sites of CRISPR guide RNAs.
- **Algorithm**: OpenCL-accelerated search allowing DNA/RNA bulges and mismatches.
- **Input**: Guide RNA sequences and reference genome.
- **Output**: Potential off-target sites with mismatch and bulge counts.
- **Cas Variants**: Supports Cas9, Cas12a (Cpf1), and other RGENs.
- **Installation**: Install via bioconda: `conda install -c bioconda cas-offinder`

## Pitfalls

- **OpenCL Optional**: OpenCL acceleration optional; falls back to CPU.
- **Genome Index**: Large genomes require significant memory.
- **Mismatch Limit**: Higher mismatch limits increase runtime exponentially.
- **PAM Specification**: Must specify correct PAM for the Cas variant.

## Examples

### Find Cas9 off-targets
**Args:** `cas-offinder input.txt G output.tsv`
**Explanation:** Searches for Cas9 off-target sites using GPU acceleration.

### CPU-only search
**Args:** `cas-offinder input.txt C output.tsv`
**Explanation:** Searches for off-target sites using CPU only.

### Allow RNA bulges
**Args:** `cas-offinder input.txt G output.tsv -b 1`
**Explanation:** Allows 1 RNA bulge in off-target search.

### Allow DNA bulges
**Args:** `cas-offinder input.txt G output.tsv -d 1`
**Explanation:** Allows 1 DNA bulge in off-target search.

### Set mismatch limit
**Args:** `cas-offinder input.txt C output.tsv -m 5`
**Explanation:** Allows up to 5 mismatches in off-target search.
