---
name: cath-tools
category: protein-structure
description: Protein structure comparison tools including SSAP for CATH database curation
tags: [cath-tools, protein-structure, ssap, cath, structure-comparison]
author: oxo-call-community
source_url: "https://github.com/UCLOrengoGroup/cath-tools"
---

## Concepts

- **Tool Overview**: cath-tools provides protein structure comparison tools including SSAP, used by the Orengo Group for CATH database curation.
- **Core Function**: Compares protein structures and classifies them into the CATH hierarchy.
- **SSAP Algorithm**: Sequential Structure Alignment Program for protein structure comparison.
- **Input**: Protein structure files (PDB format).
- **Output**: Structure alignments, similarity scores, and CATH classifications.
- **Application**: Protein structure analysis, fold recognition, and evolutionary studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cath-tools`

## Pitfalls

- **PDB Format**: Requires properly formatted PDB files.
- **Structure Quality**: Poor quality structures affect alignment accuracy.
- **Computational Cost**: Structure comparison is computationally intensive.
- **Memory Usage**: Large structures require significant memory.

## Examples

### Compare two structures
**Args:** `ssap protein1.pdb protein2.pdb -o alignment.txt`
**Explanation:** Compares two protein structures using SSAP algorithm.

### Classify structure
**Args:** `cath-classify -i structure.pdb -o classification.txt`
**Explanation:** Classifies a protein structure into the CATH hierarchy.

### Build CATH superfamily alignment
**Args:** `cath-build-superfamily-align -i structures.list -o alignment.fa`
**Explanation:** Builds multiple structure alignment for a CATH superfamily.

### Display help
**Args:** `cath-tools --help`
**Explanation:** Shows all available tools and options.