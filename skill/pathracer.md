---
name: pathracer
category: assembly
description: PathRacer aligns profile HMMs against assembly graphs.
tags: [pathracer, assembly, hmm, assembly-graph]
author: oxo-call-community
source_url: "http://cab.spbu.ru/software/pathracer/"
---

## Concepts

- **Tool Overview**: PathRacer aligns profile HMMs to assembly graphs.
- **Core Function**: Finds paths in assembly graphs using HMMs.
- **Algorithm**: Uses profile HMM alignment on graphs.
- **Input Format**: Accepts assembly graphs and HMM profiles.
- **Output**: Produces most probable paths through graph.
- **Use Case**: Metagenomics, gene finding in fragmented assemblies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large graphs require memory.
- **Graph Complexity**: Complex assemblies may affect results.
- **HMM Quality**: Results depend on HMM profile quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathracer --help`
**Explanation:** Shows available options and usage instructions.

### Align HMM to graph
**Args:** `pathracer -g assembly.gfa -h profile.hmm -o results/`
**Explanation:** Aligns HMM to assembly graph.

### Amino acid HMM
**Args:** `pathracer -g assembly.gfa -h protein.hmm --translate -o results/`
**Explanation:** Translates DNA on-the-fly for amino acid HMM.

### Verbose mode
**Args:** `pathracer -v -g assembly.gfa -h profile.hmm -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathracer -t 8 -g assembly.gfa -h profile.hmm -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pathracer -g assembly.gfa -h profile.hmm -o results.fasta --fasta`
**Explanation:** Outputs sequences in FASTA format.

### Top paths
**Args:** `pathracer -g assembly.gfa -h profile.hmm -n 5 -o results/`
**Explanation:** Returns top 5 most probable paths.