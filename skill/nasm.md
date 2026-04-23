---
name: nasm
category: programming
description: NASM - The Netwide Assembler
tags: [nasm, programming, assembler, binary, compiler]
author: oxo-call-community
source_url: "https://www.nasm.us"
---

## Concepts

- **Tool Overview**: NASM v2.11.08 - the Netwide Assembler for x86 architecture.
- **Core Function**: Assembles x86 assembly language programs into object files.
- **Input/Output**: Takes assembly source files (.asm); outputs object files (.o).
- **Installation**: `conda install -c bioconda nasm`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Usage**: Build dependency for some bioinformatics tools.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-f elf64 source.asm -o output.o`
**Explanation:** Assembles source file into ELF64 object file.
