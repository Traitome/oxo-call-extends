---
name: align_it
category: chemistry
description: Align-it is a tool to align molecules according to their pharmacophores for drug discovery and virtual screening
tags: [align_it, pharmacophore, molecular-alignment, drug-discovery, virtual-screening, ligand-based]
author: oxo-call-community
source_url: "http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/align-it/1.0.4/align-it.html"
---

## Concepts

- **Tool Overview**: Align-it is a computational chemistry tool for aligning molecules based on their pharmacophore features, enabling ligand-based virtual screening in drug discovery.
- **Core Function**: Aligns molecules by matching pharmacophore features including hydrogen bond donors/acceptors, hydrophobic regions, aromatic rings, positive/negative centers, and charge transfer interactions.
- **Pharmacophore Definition**: An abstract concept representing the essential molecular features required for optimal interaction with a biological target.
- **Input/Output**: Input: Molecular structures in SDF, SMILES, or MOL2 format. Output: Aligned molecules with pharmacophore matching scores.
- **Scoring**: Computes similarity scores based on pharmacophore feature alignment and geometric matching.
- **Applications**: Ligand-based virtual screening, scaffold hopping, drug repurposing, polypharmacology studies.
- **Installation**: Install via bioconda: `conda install -c bioconda align_it`

## Pitfalls

- **Pharmacophore Model Quality**: Results depend on the quality of the pharmacophore model used for alignment.
- **Conformer Generation**: Multiple conformations may be needed to find optimal alignment.
- **Feature Detection**: Automatic feature detection may miss biologically relevant features.
- **Score Interpretation**: Lower scores indicate better alignment - check documentation for scoring details.
- **Molecular Format**: Ensure input files are in supported formats (SDF, SMILES, MOL2).

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and usage instructions.

### Basic pharmacophore alignment
**Args:** `align-it -i query.sdf -r reference.sdf -o aligned.sdf`
**Explanation:** Aligns molecules in query.sdf to reference molecule using pharmacophore matching.

### Align with pharmacophore file
**Args:** `align-it -i query.sdf -p reference.phar -o results.sdf`
**Explanation:** Aligns query molecules against a pre-defined pharmacophore model file.

### Set alignment score cutoff
**Args:** `align-it -i query.sdf -r reference.sdf -c 0.7 -o filtered.sdf`
**Explanation:** Only outputs molecules with alignment score >= 0.7 (higher is better).

### Generate pharmacophore from molecule
**Args:** `align-it -g input.sdf -o pharmacophore.phar`
**Explanation:** Generates a pharmacophore model from input molecule(s).

### Multiple reference molecules
**Args:** `align-it -i query.sdf -r ref1.sdf ref2.sdf ref3.sdf -o aligned.sdf`
**Explanation:** Aligns query against multiple reference molecules.

### Output alignment scores
**Args:** `align-it -i query.sdf -r reference.sdf -s scores.txt -o aligned.sdf`
**Explanation:** Outputs alignment scores to separate file along with aligned molecules.

### Set maximum number of results
**Args:** `align-it -i query.sdf -r reference.sdf -n 10 -o top10.sdf`
**Explanation:** Outputs only top 10 best-scoring alignments.

### Include pharmacophore visualization
**Args:** `align-it -i query.sdf -r reference.sdf -v -o aligned.sdf`
**Explanation:** Generates visualization files for pharmacophore alignment.

### Hybrid pharmacophore mode
**Args:** `align-it -i query.sdf -r reference.sdf --hybrid -o results.sdf`
**Explanation:** Enables hybrid pharmacophore point matching for more flexible alignment.

### Exclude normal information
**Args:** `align-it -i query.sdf -r reference.sdf --no-normal -o results.sdf`
**Explanation:** Disables use of normal vector information during alignment.

### Batch processing
**Args:** `align-it -b batch_list.txt -r reference.sdf -o batch_results/`
**Explanation:** Processes multiple query files listed in batch_list.txt.
