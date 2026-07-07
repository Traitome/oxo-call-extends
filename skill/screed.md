---
name: screed
category: sequence-analysis
description: screed - Biological sequence parsing and storage library
tags: ["screed", "sequence-analysis", "python", "bioinformatics"]
author: oxo-call-community
source_url: "http://github.com/dib-lab/screed/"
---

## Concepts

- **Tool Overview**: screed (v1.0.4) is a biological sequence parsing and storage/retrieval library for DNA and protein sequences.
- **Core Function**: Provides efficient parsing and storage of biological sequence data.
- **Algorithm**: Implements fast sequence parsing with memory-efficient storage.
- **Input/Output**: Accepts FASTA, FASTQ, and other sequence formats.
- **Performance**: Optimized for fast parsing of large sequence files.
- **Applications**: Sequence analysis, bioinformatics pipelines, and data processing.

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.
- **Error Handling**: Error messages may be unclear.
- **Performance**: May require optimization for extremely large datasets.
- **Format Support**: Limited support for some exotic sequence formats.

## Examples

### Read FASTA file
**Args:** `import screed; records = screed.open('sequences.fasta')`
**Explanation:** Opens FASTA file for reading.

### Iterate sequences
**Args:** `for record in screed.open('sequences.fasta'): print(record.name)`
**Explanation:** Iterates through sequences in file.

### Read FASTQ file
**Args:** `import screed; records = screed.open('reads.fastq')`
**Explanation:** Opens FASTQ file for reading.

### Get sequence length
**Args:** `len(record.sequence)`
**Explanation:** Gets length of sequence.

### Write sequences
**Args:** `screed.write(records, 'output.fasta')`
**Explanation:** Writes sequences to file.

### Filter sequences
**Args:** `filtered = [r for r in screed.open('seqs.fasta') if len(r.sequence) > 100]`
**Explanation:** Filters sequences longer than 100bp.

### Sequence statistics
**Args:** `gc_content = sum(1 for c in record.sequence if c in 'GC') / len(record.sequence)`
**Explanation:** Calculates GC content.