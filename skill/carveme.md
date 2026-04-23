---
name: carveme
category: utility
description: Automated genome-scale metabolic model reconstruction
tags: [carveme, metabolic, model, reconstruction, flux-balance]
author: oxo-call-community
source_url: "https://github.com/cdanielmachado/carveme"
---

## Concepts

- **Tool Overview**: CarveMe reconstructs genome-scale metabolic models from annotated genomes.
- **Core Function**: Builds metabolic models using a top-down carving approach from universal model.
- **Algorithm**: Carves organism-specific model from universal model based on gene annotations.
- **Input**: Annotated genome in GenBank or FASTA format.
- **Output**: SBML metabolic model ready for simulation.
- **Application**: Metabolic engineering, flux balance analysis, and phenotype prediction.
- **Installation**: Install via bioconda: `conda install -c bioconda carveme`

## Pitfalls

- **Annotation Required**: Requires properly annotated genome file.
- **Solver Dependency**: Needs CPLEX, Gurobi, or GLPK for model building.
- **Universal Model**: Downloads universal model on first run.
- **Gap Filling**: Models may need gap-filling for specific growth conditions.

## Examples

### Build metabolic model
**Args:** `carveme -i genome.gb -o model.xml`
**Explanation:** Reconstructs metabolic model from GenBank-annotated genome.

### Build from FASTA with diamond
**Args:** `carveme -i proteins.fa -o model.xml --dna False`
**Explanation:** Builds model from protein FASTA using diamond search.

### Gap-fill model
**Args:** `carveme -i genome.gb -o model_gapfilled.xml --gapfill M9`
**Explanation:** Builds and gap-fills model for M9 minimal medium growth.

### Build community model
**Args:** `carveme -i genome1.gb genome2.gb -o community.xml --community`
**Explanation:** Builds community metabolic model from multiple genomes.

### Set solver
**Args:** `carveme -i genome.gb -o model.xml --solver cplex`
**Explanation:** Uses CPLEX solver for model optimization.
