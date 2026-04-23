---
name: camlhmp
category: annotation
description: Classification through YAML Heuristic Mapping Protocol for pathogen typing
tags: [camlhmp, typing, classification, yaml, pathogen]
author: oxo-call-community
source_url: "https://github.com/rpetit3/camlhmp"
---

## Concepts

- **Tool Overview**: camlhmp classifies pathogens using YAML-based heuristic mapping protocols.
- **Core Function**: Assigns isolates to types based on user-defined YAML rules.
- **Input**: Assembly FASTA and YAML typing scheme.
- **Output**: Type assignments with matching evidence.
- **Application**: Flexible pathogen typing and classification.
- **Installation**: Install via bioconda: `conda install -c bioconda camlhmp`

## Pitfalls

- **YAML Scheme**: Requires properly formatted YAML typing scheme.
- **Database**: Needs BLAST database or similar for gene detection.
- **Customization**: Schemes must be created for each target organism.

## Examples

### Classify isolate
**Args:** `camlhmp classify -i assembly.fa -s typing_scheme.yaml -o classification.tsv`
**Explanation:** Classifies isolate using YAML heuristic mapping protocol.

### Create typing scheme
**Args:** `camlhmp create -o new_scheme.yaml`
**Explanation:** Creates template YAML typing scheme for customization.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
