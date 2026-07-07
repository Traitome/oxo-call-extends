---
name: pymlst
category: programming
description: pyMLST is a Python tool for Multi-Locus Sequence Typing (MLST) analysis.
tags: [pymlst, programming, mlst, typing]
author: oxo-call-community
source_url: "https://github.com/bvalot/pyMLST.git"
---

## Concepts

- **Tool Overview**: pymlst performs MLST analysis.
- **Core Function**: Sequence typing.
- **Algorithm**: Uses allele matching.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces ST types.
- **Use Case**: Bacterial typing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Allele Database**: Must be current.
- **Sequence Quality**: Affects typing.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pymlst --help`
**Explanation:** Shows available options and usage instructions.

### Run MLST typing
**Args:** `pymlst type -i genome.fasta -d mlst_db/ -o result.txt`
**Explanation:** Determines MLST type.

### With parameters
**Args:** `pymlst type -i genome.fasta -p params.yaml -o result.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pymlst -v type -i genome.fasta -o result.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pymlst -t 4 type -i genome.fasta -o result.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Update database
**Args:** `pymlst update -d mlst_db/ -s species`
**Explanation:** Updates MLST database.

### Generate report
**Args:** `pymlst type -i genome.fasta -o result.txt --report report.html`
**Explanation:** Generates HTML report.