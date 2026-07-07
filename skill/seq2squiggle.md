---
name: seq2squiggle
category: simulation
description: seq2squiggle - Simulation of nanopore sequencing signals with transformers
tags: ["seq2squiggle", "simulation", "nanopore", "transformers"]
author: oxo-call-community
source_url: "https://github.com/ZKI-PH-ImageAnalysis/seq2squiggle"
---

## Concepts

- **Tool Overview**: seq2squiggle (v0.3.4) simulates nanopore sequencing signals using transformers.
- **Core Function**: Generates simulated nanopore raw signal data from sequences.
- **Algorithm**: Uses feed-forward transformers for signal simulation.
- **Input/Output**: Accepts FASTA sequences and produces raw signal data.
- **Signal Simulation**: Focuses on simulating Oxford Nanopore sequencing signals.
- **Applications**: Algorithm development, testing, and benchmarking.

## Pitfalls

- **Computational Resources**: Requires significant compute resources (GPU recommended).
- **Memory Usage**: High memory requirements for large sequences.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Model Size**: Pre-trained models may be large.
- **Software Dependencies**: Requires PyTorch and other ML libraries.
- **Documentation**: Some features have limited documentation.

## Examples

### Simulate signals
**Args:** `seq2squiggle -i sequences.fasta -o signals/`
**Explanation:** `-i` input FASTA; `-o` output directory.

### With model
**Args:** `seq2squiggle -i sequences.fasta -m model.pt -o signals/`
**Explanation:** `-m` specifies custom model.

### Batch processing
**Args:** `seq2squiggle -i sequences.fasta -b 32 -o signals/`
**Explanation:** `-b 32` batch size for processing.

### Verbose logging
**Args:** `seq2squiggle -i sequences.fasta -v -o signals/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seq2squiggle --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seq2squiggle --version`
**Explanation:** Shows current version.

### Evaluate simulation
**Args:** `seq2squiggle evaluate -i signals/ -t truth/ -o metrics.txt`
**Explanation:** Evaluates simulation accuracy.