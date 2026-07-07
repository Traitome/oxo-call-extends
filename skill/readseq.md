---
name: readseq
category: formatting
description: ReadSeq reads and reformats biosequences, supporting multiple sequence file formats for bioinformatics.
tags: [readseq, formatting, sequence-conversion, file-format]
author: oxo-call-community
source_url: "http://iubio.bio.indiana.edu/soft/molbio/readseq/java/"
---

## Concepts

- **Tool Overview**: readseq converts formats.
- **Core Function**: Sequence format conversion.
- **Algorithm**: Uses parsing methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces converted files.
- **Use Case**: Format conversion.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **File Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Conversion may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `readseq --help`
**Explanation:** Shows available options and usage instructions.

### Convert format
**Args:** `readseq convert -i input.fasta -o output.phylip`
**Explanation:** Converts sequence format.

### With parameters
**Args:** `readseq convert -i input.fasta -p params.yaml -o output.phylip`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `readseq -v convert -i input.fasta -o output.phylip`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `readseq -t 4 convert -i input.fasta -o output.phylip`
**Explanation:** Uses 4 threads for parallel processing.

### Reverse complement
**Args:** `readseq reverse -i input.fasta -o output.fasta`
**Explanation:** Generates reverse complement.

### Generate report
**Args:** `readseq convert -i input.fasta -o output.phylip --report report.html`
**Explanation:** Generates HTML report.