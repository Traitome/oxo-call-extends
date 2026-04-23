---
name: bitstring
category: programming
description: Simple construction, analysis and modification of binary data in Python
tags: [bitstring, python, binary, data-structures]
author: oxo-call-community
source_url: "https://github.com/scott-griffiths/bitstring"
---

## Concepts

- **Tool Overview**: bitstring is a Python library for manipulating binary data.
- **Core Function**: Creates, analyzes, and modifies binary data structures.
- **Features**: Bit-level manipulation, binary parsing, and data serialization.
- **Application**: General-purpose binary data handling, including bioinformatics file formats.
- **Installation**: Install via bioconda: `conda install -c bioconda bitstring`

## Pitfalls

- **Python Only**: Python library, not a command-line tool.
- **Memory Usage**: Large binary files may require significant memory.
- **Endianness**: Be aware of byte order when parsing binary data.

## Examples

### Parse binary data
**Args:** `python -c "from bitstring import BitArray; b = BitArray('0x1234'); print(b.bin)"`
**Explanation:** Creates BitArray from hex and prints binary representation.

### Read binary file
**Args:** `python -c "from bitstring import Bits; b = Bits(filename='data.bin'); print(b.read('uint:16'))"`
**Explanation:** Reads 16-bit unsigned integer from binary file.

### Create from binary string
**Args:** `python -c "from bitstring import BitArray; b = BitArray('0b11110000'); print(b.hex)"`
**Explanation:** Creates BitArray from binary string and prints hex.
