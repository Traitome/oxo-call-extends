---
name: mob_suite
category: utility
description: MOB-suite is a set of tools for finding, typing and reconstruction of plasmids from draft and complete genome assemblies.
tags: [mob_suite, utility, plasmids]
author: oxo-call-community
source_url: "https://pypi.org/project/mob-suite/"
---

## Concepts

- **Tool Overview**: MOB-suite v3.1.9 analyzes and reconstructs plasmids from genome assemblies.
- **Core Function**: Identifies, types, and reconstructs plasmids.
- **Plasmid Detection**: Finds plasmid sequences in assemblies.
- **Plasmid Typing**: Classifies plasmids by incompatibility groups.
- **Reconstruction**: Assembles complete plasmid sequences.
- **Input/Output**: Accepts FASTA assemblies; outputs plasmid sequences and annotations.

## Pitfalls

- **Assembly Required**: Requires assembled genomes as input.
- **Memory Requirements**: Memory usage depends on assembly size.
- **Parameter Tuning**: May require parameter adjustment for optimal plasmid detection.
- **Data Quality**: Results depend on assembly quality.
- **Contamination Risk**: Requires careful handling of contaminated assemblies.
- **Computational Resources**: Large assemblies may require significant resources.

## Examples

### Find plasmids
**Args:** `mob_recon -i assembly.fasta -o plasmids/`
**Explanation:** Identifies and reconstructs plasmids from assembly.

### With plasmid database
**Args:** `mob_recon -i assembly.fasta -d plasmid_db.fasta -o plasmids/`
**Explanation:** Uses custom plasmid reference database.

### Plasmid typing
**Args:** `mob_typer -i plasmid.fasta -o typing_result.txt`
**Explanation:** Determines plasmid incompatibility group.

### Batch processing
**Args:** `mob_recon -i fasta/ -o results/`
**Explanation:** Processes multiple genome assemblies.

### Generate report
**Args:** `mob_recon -i assembly.fasta -o plasmids/ -r report.html`
**Explanation:** Generates analysis report.