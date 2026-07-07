---
name: py2bit
category: containerization
description: py2bit provides Python bindings for accessing 2bit compressed genome files using lib2bit.
tags: [py2bit, containerization, file-format, genome-data]
author: oxo-call-community
source_url: "https://github.com/deeptools/py2bit"
---

## Concepts

- **Tool Overview**: py2bit reads 2bit files.
- **Core Function**: 2bit file access.
- **Algorithm**: Uses lib2bit library.
- **Input Format**: Accepts 2bit files.
- **Output**: Produces sequence data.
- **Use Case**: Genome data access.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on file integrity.
- **File Compatibility**: May have version issues.
- **Runtime**: Access may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `py2bit --help`
**Explanation:** Shows available options and usage instructions.

### Extract sequence
**Args:** `py2bit extract -i genome.2bit -c chr1:1-1000 -o sequence.fasta`
**Explanation:** Extracts sequence region from 2bit file.

### List chromosomes
**Args:** `py2bit list -i genome.2bit`
**Explanation:** Lists available chromosomes.

### With parameters
**Args:** `py2bit extract -i genome.2bit -c chr1:1-1000 -p params.yaml -o sequence.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `py2bit -v extract -i genome.2bit -c chr1:1-1000 -o sequence.fasta`
**Explanation:** Runs with verbose output.

### Convert to FASTA
**Args:** `py2bit convert -i genome.2bit -o genome.fasta`
**Explanation:** Converts entire 2bit file to FASTA.

### Generate report
**Args:** `py2bit extract -i genome.2bit -c chr1:1-1000 -o sequence.fasta --report report.html`
**Explanation:** Generates HTML report.