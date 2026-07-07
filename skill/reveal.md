---
name: reveal
category: alignment
description: Reveal is a graph-based multi-genome aligner for comparative genomics.
tags: [reveal, alignment, graph-based, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/jasperlinthorst/reveal"
---

## Concepts

- **Tool Overview**: reveal aligns genomes.
- **Core Function**: Multi-genome alignment.
- **Algorithm**: Uses graph-based methods.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces alignments.
- **Use Case**: Comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Graph Complexity**: Affects alignment.
- **Parameters**: Must be configured.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reveal --help`
**Explanation:** Shows available options and usage instructions.

### Align genomes
**Args:** `reveal align -i genomes.txt -o alignment.maf`
**Explanation:** Aligns multiple genomes.

### With parameters
**Args:** `reveal align -i genomes.txt -p params.yaml -o alignment.maf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reveal -v align -i genomes.txt -o alignment.maf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reveal -t 4 align -i genomes.txt -o alignment.maf`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `reveal align -i genomes.txt -r reference.fasta -o alignment.maf`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `reveal align -i genomes.txt -o alignment.maf --report report.html`
**Explanation:** Generates HTML report.