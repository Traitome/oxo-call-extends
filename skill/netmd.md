---
name: netmd
category: alignment
description: NetMD identifies consensus behavior across multiple molecular dynamics simulations using graph-based embeddings.
tags: [netmd, alignment, molecular-dynamics, graph-embedding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/mazzalab/NetMD"
---

## Concepts

- **Tool Overview**: NetMD aligns molecular dynamics trajectories and identifies consensus behavior.
- **Core Function**: Uses graph-based embeddings and dynamic time warping for trajectory alignment.
- **Algorithm**: Applies graph neural networks and dynamic time warping to align trajectories.
- **Input Format**: Accepts molecular dynamics trajectory files (DCD, XTC, TRR).
- **Output**: Produces aligned trajectories and consensus analysis reports.
- **Use Case**: Molecular dynamics analysis, protein structure prediction, and simulation comparison.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Trajectory Quality**: Results depend on input trajectory quality.
- **Computational Cost**: Processing large trajectories is computationally intensive.
- **Memory Usage**: Large simulations require significant memory.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Alignment Complexity**: May struggle with highly dissimilar trajectories.

## Examples

### Display help
**Args:** `netmd --help`
**Explanation:** Shows available options and usage instructions.

### Basic alignment
**Args:** `netmd -i trajectories/ -o aligned/`
**Explanation:** Aligns multiple MD trajectories.

### Single trajectory
**Args:** `netmd -i trajectory.dcd -o aligned.dcd`
**Explanation:** Processes single trajectory file.

### Dynamic time warping
**Args:** `netmd -i trajectories/ --dtw -o aligned/`
**Explanation:** Uses dynamic time warping for alignment.

### Graph embedding
**Args:** `netmd -i trajectories/ --graph -o aligned/`
**Explanation:** Uses graph-based embedding approach.

### Consensus analysis
**Args:** `netmd -i trajectories/ --consensus -o consensus/`
**Explanation:** Identifies consensus behavior across trajectories.

### Threads
**Args:** `netmd -i trajectories/ -t 8 -o aligned/`
**Explanation:** Uses 8 threads for parallel processing.