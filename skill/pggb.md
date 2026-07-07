---
name: pggb
category: hpc
description: pggb builds pan-genome graphs from genome sequences.
tags: [pggb, hpc, pan-genome, graph]
author: oxo-call-community
source_url: "https://github.com/pangenome/pggb"
---

## Concepts

- **Tool Overview**: pggb builds pan-genome graphs.
- **Core Function**: Constructs pangenome graph structures.
- **Algorithm**: Uses graph building pipeline.
- **Input Format**: Accepts genome sequence files.
- **Output**: Produces pan-genome graphs.
- **Use Case**: Pan-genome analysis, graph genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genome sets require memory.
- **Graph Quality**: Results depend on genome quality.
- **Pipeline Configuration**: Requires proper config setup.
- **Runtime**: Building may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pggb --help`
**Explanation:** Shows available options and usage instructions.

### Build graph
**Args:** `pggb -i genomes.fasta -o pan_graph.gfa`
**Explanation:** Builds pan-genome graph.

### With parameters
**Args:** `pggb -i genomes.fasta -p params.yaml -o pan_graph.gfa`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pggb -v -i genomes.fasta -o pan_graph.gfa`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pggb -t 8 -i genomes.fasta -o pan_graph.gfa`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pggb -i genomes.fasta -o pan_graph.vg --vg`
**Explanation:** Outputs in VG format.

### Generate report
**Args:** `pggb -i genomes.fasta -o pan_graph.gfa --report report.html`
**Explanation:** Generates HTML report.