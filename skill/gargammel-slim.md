---
name: gargammel-slim
category: programming
description: Tool for simulating ancient DNA datasets (slim version).
tags: [gargammel-slim, ancient DNA, simulation, aDNA]
author: oxo-call-community
source_url: "https://github.com/grenaud/gargammel"
---

## Concepts
- **Fragment Simulation**: Simulates aDNA fragment generation.
- **Deamination Simulation**: Simulates C-to-T deamination damage.
- **Adapter Simulation**: Simulates adapter contamination.
- **Lightweight Tool**: Simplified version of gargammel.
- **Fast Processing**: Fast simulation of DNA fragments.

## Pitfalls
- **Limited Features**: Fewer features than full gargammel.
- **Damage Model**: Simplified damage model.
- **No Contamination**: Does not simulate contamination.
- **Parameter Limitations**: Limited parameter options.
- **Output Format**: Specific output format requirements.

## Examples
### Simulate fragments
**Args:** `fragSim -ref reference.fasta -o fragments.fasta`
**Explanation:** Simulates DNA fragments.

### Deamination damage
**Args:** `deamSim -ref reference.fasta -o damaged.fasta`
**Explanation:** Simulates deamination damage.

### Adapter simulation
**Args:** `adptSim -ref reference.fasta -o adapters.fasta`
**Explanation:** Simulates adapter sequences.

### Set fragment size
**Args:** `fragSim -ref reference.fasta -s 50 -o fragments.fasta`
**Explanation:** Sets fragment size to 50bp.

### With damage rate
**Args:** `deamSim -ref reference.fasta -r 0.1 -o damaged.fasta`
**Explanation:** Sets damage rate to 0.1.