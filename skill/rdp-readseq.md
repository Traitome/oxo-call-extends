---
name: rdp-readseq
category: formatting
description: RDP-ReadSeq is a Java-based common sequence file format reader and sequence file manipulation tool.
tags: [rdp-readseq, formatting, sequence-conversion, file-format]
author: oxo-call-community
source_url: "https://github.com/rdpstaff/ReadSeq"
---

## Concepts

- **Tool Overview**: rdp-readseq converts formats.
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
**Args:** `rdp-readseq --help`
**Explanation:** Shows available options and usage instructions.

### Convert format
**Args:** `rdp-readseq convert -i input.fasta -o output.phylip`
**Explanation:** Converts sequence format.

### With parameters
**Args:** `rdp-readseq convert -i input.fasta -p params.yaml -o output.phylip`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rdp-readseq -v convert -i input.fasta -o output.phylip`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rdp-readseq -t 4 convert -i input.fasta -o output.phylip`
**Explanation:** Uses 4 threads for parallel processing.

### Reverse complement
**Args:** `rdp-readseq reverse -i input.fasta -o output.fasta`
**Explanation:** Generates reverse complement.

### Generate report
**Args:** `rdp-readseq convert -i input.fasta -o output.phylip --report report.html`
**Explanation:** Generates HTML report.