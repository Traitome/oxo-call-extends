---
name: py_nucflag
category: alignment
description: py_nucflag detects misassemblies in genome assemblies from long-read alignments.
tags: [py_nucflag, alignment, assembly, misassembly]
author: oxo-call-community
source_url: "https://github.com/logsdon-lab/rs-nucflag"
---

## Concepts

- **Tool Overview**: py_nucflag detects misassemblies.
- **Core Function**: Misassembly calling.
- **Algorithm**: Uses alignment analysis.
- **Input Format**: Accepts BAM files.
- **Output**: Produces misassembly calls.
- **Use Case**: Assembly validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Affects detection.
- **Read Length**: Longer reads improve accuracy.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `py_nucflag --help`
**Explanation:** Shows available options and usage instructions.

### Detect misassemblies
**Args:** `py_nucflag detect -i alignments.bam -r reference.fasta -o misassemblies.txt`
**Explanation:** Identifies misassembled regions.

### With parameters
**Args:** `py_nucflag detect -i alignments.bam -p params.yaml -o misassemblies.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `py_nucflag -v detect -i alignments.bam -o misassemblies.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `py_nucflag -t 4 detect -i alignments.bam -o misassemblies.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Filter results
**Args:** `py_nucflag filter -i misassemblies.txt -q high -o filtered.txt`
**Explanation:** Filters by confidence.

### Generate report
**Args:** `py_nucflag detect -i alignments.bam -o misassemblies.txt --report report.html`
**Explanation:** Generates HTML report.