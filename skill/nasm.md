---
name: nasm
category: programming
description: NASM (The Netwide Assembler) is an x86 assembly language compiler for creating binary executables.
tags: [nasm, programming, assembler, binary, compiler]
author: oxo-call-community
source_url: "https://www.nasm.us"
---

## Concepts

- **Tool Overview**: NASM v2.11.08 is the Netwide Assembler, a portable x86 assembly language compiler.
- **Core Function**: Assembles x86/x86-64 assembly language source code into machine-readable object files.
- **Algorithm**: Parses assembly language syntax and generates corresponding machine code instructions.
- **Input Format**: Accepts assembly source files with .asm extension.
- **Output**: Produces object files (.o), executable files, or binary flat files.
- **Use Case**: Low-level programming, system programming, reverse engineering, and compiler development.

## Pitfalls

- **Syntax Differences**: NASM syntax differs from other assemblers like GNU as.
- **Version Compatibility**: Newer features may not be backward compatible.
- **Architecture Specific**: Output is architecture-specific (x86/x86-64 only).
- **Debug Information**: Requires specific flags for debug symbol generation.
- **Linking Required**: Object files need linking to create executables.
- **Cross-compilation**: Cross-compiling for different targets requires special configuration.

## Examples

### Display help
**Args:** `nasm --help`
**Explanation:** Shows available options and usage instructions.

### Assemble to ELF64
**Args:** `nasm -f elf64 source.asm -o output.o`
**Explanation:** Assembles source file into ELF64 object file.

### Assemble to 32-bit ELF
**Args:** `nasm -f elf32 source.asm -o output.o`
**Explanation:** Assembles source file into 32-bit ELF object file.

### Assemble to Windows PE
**Args:** `nasm -f win32 source.asm -o output.obj`
**Explanation:** Assembles source file into Windows 32-bit object file.

### Generate listing file
**Args:** `nasm -f elf64 source.asm -o output.o -l listing.lst`
**Explanation:** Generates assembly listing file with addresses.

### Assemble and link
**Args:** `nasm -f elf64 source.asm -o output.o && ld output.o -o executable`
**Explanation:** Assembles and links to create executable.