---
name: gargammel
category: formatting
description: Tool for simulating ancient DNA datasets.
tags: [gargammel, ancient DNA, simulation, aDNA]
author: oxo-call-community
source_url: "https://github.com/grenaud/gargammel"
---

## Concepts
- **Ancient DNA Simulation**: Simulates ancient DNA fragments.
- **Damage Patterns**: Simulates characteristic aDNA damage.
- **Contamination Modeling**: Models present-day human contamination.
- **Microbial Contamination**: Simulates microbial contamination.
- **Fragment Simulation**: Generates realistic aDNA fragments.

## Pitfalls
- **Damage Model**: Damage patterns may not match real aDNA.
- **Complex Parameters**: Many parameters require careful selection.
- **Reference Quality**: Simulated data depends on reference quality.
- **Computational Time**: Large simulations can be slow.
- **Database Requirements**: Requires appropriate reference databases.

## Examples
### Simulate aDNA fragments
**Args:** `gargammel -ref reference.fasta -o simulated/`
**Explanation:** Simulates ancient DNA fragments.

### With contamination
**Args:** `gargammel -ref reference.fasta -contam 0.05 -o simulated/`
**Explanation:** Simulates with 5% contamination.

### Damage simulation
**Args:** `gargammel -ref reference.fasta -dmg -o simulated/`
**Explanation:** Includes aDNA damage patterns.

### Paired-end simulation
**Args:** `gargammel -ref reference.fasta -pe -o simulated/`
**Explanation:** Simulates paired-end reads.

### Specify fragment length
**Args:** `gargammel -ref reference.fasta -l 50-100 -o simulated/`
**Explanation:** Sets fragment length range 50-100bp.