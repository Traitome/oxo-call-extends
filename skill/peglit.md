---
name: peglit
category: utility
description: peglit identifies non-interfering linkers for pegRNA design.
tags: [peglit, utility, pegrna, linker]
author: oxo-call-community
source_url: "https://github.com/sshen8/peglit/"
---

## Concepts

- **Tool Overview**: peglit designs pegRNA linkers.
- **Core Function**: Identifies non-interfering nucleotide linkers.
- **Algorithm**: Uses linker optimization algorithms.
- **Input Format**: Accepts pegRNA sequences.
- **Output**: Produces linker designs.
- **Use Case**: Prime editing, pegRNA design.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large pegRNA sets require memory.
- **Linker Quality**: Results depend on pegRNA quality.
- **Interference Detection**: May miss some interference.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peglit --help`
**Explanation:** Shows available options and usage instructions.

### Identify linkers
**Args:** `peglit -i pegRNA.fasta -o linkers.txt`
**Explanation:** Identifies non-interfering linkers.

### With motif
**Args:** `peglit -i pegRNA.fasta -m motif.txt -o linkers.txt`
**Explanation:** Uses 3' motif for linker design.

### Verbose mode
**Args:** `peglit -v -i pegRNA.fasta -o linkers.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peglit -t 4 -i pegRNA.fasta -o linkers.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peglit -i pegRNA.fasta -o linkers.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peglit -i pegRNA.fasta -o linkers.txt --report report.html`
**Explanation:** Generates HTML report.