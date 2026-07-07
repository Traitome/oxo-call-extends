---
name: telomore
category: analysis
description: Telomere More - Telomere elongation simulation tool for evolutionary genomics.
tags: [telomere, telomere-elongation, simulation, genomics, evolution, telomere-maintenance]
author: oxo-call-community
source_url: "https://github.com/genome-tools/telomere_more"
---

## Concepts

- **Tool Overview**: Telomere More - A tool for simulating and analyzing telomere elongation scenarios in evolutionary genomics.
- **Core Function**: Simulates telomere elongation mechanisms and predicts sequence composition changes over evolutionary time.
- **Input**: Current telomere sequences, species tree, or evolutionary parameters.
- **Output**: Simulated telomere sequences, evolutionary trajectories, composition statistics.
- **Installation**: `pip install telomere-more` or `conda install -c bioconda telomere-more`
- **Use Case**: Studying telomere evolution across species, understanding telomere maintenance mechanisms.

## Pitfalls

- **Parameter Selection**: Evolutionary parameters significantly affect simulation results.
- **Model Limitations**: Current models may not capture all telomere maintenance mechanisms.

## Examples

### Simulate telomere elongation
**Args:** `telomere-more simulate -i telomere_seq.fasta -o simulated_output/ --generations 1000`
**Explanation:** Simulate telomere evolution over 1000 generations.

### Compare species
**Args:** `telomere-more compare -s species1_telomere.fasta species2_telomere.fasta -o comparison/`
**Explanation:** Compare telomere evolution trajectories between two species.
