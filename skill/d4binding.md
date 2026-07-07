---
name: d4binding
category: formatting
description: C/C++ binding for the D4 file format
tags: [d4binding, formatting, D4, C++, genomics]
author: oxo-call-community
source_url: "https://github.com/38/d4-format/blob/v0.3.11/README.md"
---

## Concepts

- **Tool Overview**: d4binding (v0.3.11+) provides C/C++ bindings for the D4 file format, a compressed binary format for genomic data.
- **Core Function**: Enables reading and writing D4 files from C/C++ applications.
- **Input/Output**: Input: D4 format files. Output: D4 format files, in-memory data structures.
- **Key Features**: High-performance I/O, compression support, random access.
- **Installation**: `conda install -c bioconda d4binding`

## Pitfalls

- **C/C++ Knowledge**: Requires C/C++ programming knowledge to use bindings.
- **Memory Management**: Manual memory management required in C/C++.
- **Version Compatibility**: Ensure compatibility with D4 format version.
- **Build Requirements**: Requires appropriate build tools and dependencies.
- **Documentation**: Limited documentation for C/C++ API.

## Examples

### Read D4 file in C++
**Args:**
```cpp
#include <d4/d4.h>

int main() {
    D4File file("data.d4");
    auto reader = file.OpenReader();
    auto data = reader->Read("chr1", 1000, 2000);
    return 0;
}
```
**Explanation:** Read genomic data from D4 file using C++ binding.

### Write D4 file in C++
**Args:**
```cpp
#include <d4/d4.h>

int main() {
    D4File file("output.d4", D4File::WRITE);
    auto writer = file.OpenWriter();
    writer->Write("chr1", 1000, data, size);
    return 0;
}
```
**Explanation:** Write genomic data to D4 file using C++ binding.

### Create D4 index
**Args:**
```cpp
#include <d4/d4.h>

int main() {
    D4File::CreateIndex("data.d4", "data.d4.idx");
    return 0;
}
```
**Explanation:** Create index for D4 file to enable fast random access.
