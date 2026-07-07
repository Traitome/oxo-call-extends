---
name: squigulator
category: simulation
description: Squigulator - Tool for simulating Oxford Nanopore raw signal data
tags: [squigulator, simulation, ont, nanopore, raw-signals]
author: oxo-call-community
source_url: "https://github.com/hasindu2008/squigulator"
---

## Concepts

- **Tool Overview**: squigulator (v0.5.0) - A signal simulation tool
- **Core Function**: Simulates Oxford Nanopore raw signal data from reference sequences
- **Input/Output**: Accepts reference sequences; outputs simulated signal files
- **Algorithm**: Signal simulation based on pore models and sequence context
- **Installation**: `conda install -c bioconda squigulator`
- **Key Features**: Signal simulation, ONT data, basecalling testing

## Pitfalls

- **Input Requirements**: Requires properly formatted reference sequences
- **Pore Model**: Pore model affects signal accuracy
- **Noise Parameters**: Noise parameters affect simulation realism
- **Memory Usage**: Large sequences require significant memory
- **Output Format**: Output format depends on configuration
- **Simulation Accuracy**: Accuracy depends on pore model and parameters

## Examples

### Display help
**Args:** `squigulator --help`
**Explanation:** Shows available options and usage information.

### Basic signal simulation
**Args:** `squigulator -i reference.fasta -o simulated_signals.fast5`
**Explanation:** Simulate ONT raw signals from reference.

### With pore model
**Args:** `squigulator -i reference.fasta -p pore_model.txt -o simulated_signals.fast5`
**Explanation:** Use specific pore model for simulation.

### With noise parameters
**Args:** `squigulator -i reference.fasta -o simulated_signals.fast5 --noise 0.1`
**Explanation:** Set noise level for simulation.

### Multiple references
**Args:** `squigulator -i ref1.fasta ref2.fasta -o simulated_signals.fast5`
**Explanation:** Simulate signals from multiple references.

### Output detailed results
**Args:** `squigulator -i reference.fasta -o simulated_signals.fast5 --detailed`
**Explanation:** Output detailed simulation information.

### Output statistics
**Args:** `squigulator -i reference.fasta -o simulated_signals.fast5 --stats`
**Explanation:** Output simulation statistics.

### Generate report
**Args:** `squigulator -i reference.fasta -o simulated_signals.fast5 --report`
**Explanation:** Generate simulation report.

### With threads
**Args:** `squigulator -i reference.fasta -o simulated_signals.fast5 -p 8`
**Explanation:** Use multiple threads for simulation.