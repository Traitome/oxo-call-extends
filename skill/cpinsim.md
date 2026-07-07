---
name: cpinsim
category: utility
description: Constrained Protein Interaction Network Simulator - simulate protein complex assembly with interaction dependencies
tags: [cpinsim, protein-interactions, protein-complex, simulation, network, systems-biology]
author: oxo-call-community
source_url: "https://github.com/BiancaStoecker/cpinsim"
---

## Concepts

- **Tool Overview**: CPINSim (Constrained Protein Interaction Network Simulator) is a Python package for simulating protein complex assembly in constrained protein interaction networks.
- **Core Function**: Simulates protein complex formation considering interaction dependencies (constraints) encoded as propositional logic, such as allosteric effects and mutual exclusion due to steric hindrance.
- **Algorithm**: Uses efficient data structures and algorithms to simulate association and dissociation phases until convergence, handling complex interaction constraints.
- **Input**: Protein interaction network (edges with constraints), protein list/concentrations.
- **Output**: Simulated protein complex abundances, perturbation effect analyses, complex composition reports.
- **Application**: Systems biology, protein interaction network analysis, drug target validation, cell adhesion studies, perturbation effect simulation.
- **Installation**: Install via bioconda: `conda install -c bioconda cpinsim`

## Pitfalls

- **Python 3 Required**: Requires Python 3.x environment.
- **Dependencies**: Requires networkx, scipy, and bitarray packages.
- **Network Data**: Requires well-curated protein interaction network data with constraint annotations.
- **Computation Time**: Large networks may require significant simulation time.
- **Constraint Annotation**: Missing constraint information limits simulation accuracy.

## Examples

### Simulate complex formation
**Args:** `cpinsim simulate --network protein_network.tsv --proteins protein_list.txt`
**Explanation:** Runs complex formation simulation for the given protein network and protein list.

### Simulate knockout perturbation
**Args:** `cpinsim perturb --network network.tsv --proteins proteins.txt --knockout BRCA1`
**Explanation:** Simulates the effect of knocking out a specific protein in the network.

### Simulate overexpression
**Args:** `cpinsim perturb --network network.tsv --proteins proteins.txt --overexpress TP53`
**Explanation:** Simulates the effect of overexpressing a specific protein.

### Multi-protein perturbation
**Args:** `cpinsim perturb --network network.tsv --proteins proteins.txt --knockout protein1,protein2`
**Explanation:** Simulates simultaneous knockout of multiple proteins.

### Check version
**Args:** `cpinsim --version`
**Explanation:** Displays the installed CPINSim version.

### Display help
**Args:** `cpinsim --help`
**Explanation:** Shows all available commands and options.
