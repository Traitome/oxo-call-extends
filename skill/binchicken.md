---
name: binchicken
category: metagenomics
description: Targeted recovery of low abundance MAGs through intelligent coassembly
tags: [mag, metagenome-assembled-genome, coassembly, binning]
author: oxo-call-community
source_url: "https://github.com/aroneys/binchicken"
---

## Concepts
- **Tool Overview**: binchicken performs targeted recovery of low-abundance Metagenome-Assembled Genomes (MAGs) through intelligent coassembly strategies. It identifies samples for coassembly to maximize recovery of target genomes.
- **Coassembly**: Strategically selects samples for joint assembly to improve recovery of low-abundance genomes.
- **Target Recovery**: Focuses on recovering specific low-abundance MAGs that may be missed in individual assemblies.
- **Workflow**: Sample selection → coassembly → binning → MAG quality assessment.

## Pitfalls
- **Sample Selection**: Optimal sample selection depends on community composition and target genome abundance.
- **Computational Cost**: Coassembly of multiple samples is computationally intensive.
- **Strain Variation**: Coassembly may mix strain-level variants.

## Examples
### Identify samples for coassembly
**Args:** `binchicken select --samples samples.tsv --target target_genome.fna --output selection.tsv`
**Explanation:** Identifies optimal samples for coassembly to recover target genome.

### Run coassembly pipeline
**Args:** `binchicken run --samples selection.tsv --output results/`
**Explanation:** Executes coassembly and binning pipeline for selected samples.
