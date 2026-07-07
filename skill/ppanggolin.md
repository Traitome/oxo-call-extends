---
name: ppanggolin
category: utility
description: ppanggolin constructs partitioned pangenome graphs for microbial species.
tags: [ppanggolin, utility, pangenome, graph]
author: oxo-call-community
source_url: "https://ppanggolin.readthedocs.io"
---

## Concepts

- **Tool Overview**: ppanggolin builds pangenome graphs.
- **Core Function**: Pangenome analysis.
- **Algorithm**: Uses graph-based methods.
- **Input Format**: Accepts FASTA/GBFF files.
- **Output**: Produces pangenome graph.
- **Use Case**: Microbial genomics, comparative analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large pangenomes require memory.
- **Data Quality**: Results depend on sequence quality.
- **Graph Complexity**: May have visualization issues.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ppanggolin --help`
**Explanation:** Shows available options and usage instructions.

### Build pangenome
**Args:** `ppanggolin pan -i genomes/ -o pangenome/`
**Explanation:** Constructs partitioned pangenome graph.

### With parameters
**Args:** `ppanggolin pan -i genomes/ -p params.yaml -o pangenome/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ppanggolin -v pan -i genomes/ -o pangenome/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ppanggolin -t 4 pan -i genomes/ -o pangenome/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `ppanggolin pan -i genomes/ -o pangenome.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `ppanggolin pan -i genomes/ -o pangenome/ --report report.html`
**Explanation:** Generates HTML report.