---
name: biocamlib
category: utility
description: OCaml foundation library for bioinformatics tools
tags: [ocaml, library, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/PaoloRibeca/BiOCamLib"
---

## Concepts
- **Tool Overview**: BiOCamLib is an OCaml foundation library upon which bioinformatics tools like KPop are built. It provides utilities for sequence manipulation and processing.
- **Included Tools**: RC (reverse complement), Octopus (transitive closure of strings), Parallel (chunk-wise file processing), FASTools (FASTA/FASTQ manipulation).
- **Applications**: High-performance sequence processing, bioinformatics tool development.

## Pitfalls
- **OCaml Dependency**: Requires OCaml runtime environment.
- **Developer Focus**: Primarily a library for tool developers, not end users.

## Examples
### Compute reverse complement
**Args:** `rc -i sequences.fa -o reverse_complement.fa`
**Explanation:** Computes reverse complement of sequences.

### Process FASTA file
**Args:** `fastools -i input.fa --operation clean -o cleaned.fa`
**Explanation:** Manipulates FASTA files using FASTools utility.
