---
name: coot-headless
category: programming
description: Headless API for macromolecular model building
tags: [coot-headless, protein-structure, model-building, crystallography, api]
author: oxo-call-community
source_url: "https://www.mrc-lmb.cam.ac.uk/software/coot"
---

## Concepts

- **Tool Overview**: Coot-headless provides the API bindings for Coot, a macromolecular model building and validation application, without GUI dependencies for automated processing.
- **Core Function**: Enables programmatic access to Coot's model building, refinement, and validation capabilities through Python (Chapi) and C++ (libcootapi) interfaces.
- **Algorithm**: Implements crystallographic model building algorithms including real-space refinement, density fitting, and Ramachandran validation.
- **Input**: PDB files, electron density maps (CCP4/MRC format), MTZ reflection files.
- **Output**: Refined PDB files, validation reports, and model statistics.
- **Application**: Automated structure refinement pipelines, high-throughput model validation, and crystallographic data processing.
- **Installation**: Install via bioconda: `conda install -c bioconda coot-headless`

## Pitfalls

- **Memory Requirements**: Large density maps require significant memory.
- **Model Quality**: Results depend on input model and density map quality.
- **API Learning Curve**: Requires understanding of crystallographic concepts.
- **Version Compatibility**: API may change between versions.
- **Map Resolution**: Low-resolution maps limit model building accuracy.

## Examples

### Python API usage
**Args:** `from chapi import coot; coot.read_pdb("model.pdb"); coot.read_map("density.ccp4")`
**Explanation:** Loads PDB model and density map using Python API.

### Real-space refinement
**Args:** `coot.real_space_refine(1, 10)`
**Explanation:** Performs 10 cycles of real-space refinement on chain 1.

### Validate model
**Args:** `coot.ramachandran_plot("validation.png")`
**Explanation:** Generates Ramachandran plot for model validation.

### Save refined model
**Args:** `coot.write_pdb("refined_model.pdb")`
**Explanation:** Saves refined model to PDB file.

### Display help
**Args:** `coot --help`
**Explanation:** Shows available command-line options.