---
name: density-fitness
category: utility
description: density-fitness - calculate density statistics for X-ray crystallography structures.
tags: [density-fitness, utility, crystallography, x-ray, structure-validation]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/density-fitness"
---

## Concepts

- **Tool Overview**: density-fitness (v1.2.0+) calculates electron density statistics for X-ray crystallography structures. It provides metrics for structure validation and refinement assessment.
- **Core Function**: Computes RSR, SRSR, RSCC, EDIAm and OPIA density statistics for main-chain and side-chain atoms in protein structures.
- **Input/Output**: Input: PDB/mmCIF structure files, MTZ/density maps. Output: Per-residue density metrics, quality scores, validation reports.
- **Algorithm**: Uses electron density map correlation and statistical analysis to assess model fit to experimental data.
- **Key Features**: Multiple density metrics, per-residue analysis, supports PDB/mmCIF formats, visualization support, batch processing.
- **Installation**: `conda install -c bioconda density-fitness`

## Pitfalls

- **Input Requirements**: Requires both structure model and electron density maps.
- **Map Quality**: Poor quality density maps affect metric accuracy.
- **Resolution**: Metrics may vary with different resolution ranges.
- **Model Completeness**: Incomplete models may produce unreliable results.
- **File Formats**: Requires specific format versions (MTZ, mmCIF).

## Examples

### Calculate density fitness metrics
**Args:** `density-fitness --model structure.cif --mtz data.mtz --output metrics.tsv`
**Explanation:** Calculates density fitness metrics for X-ray structure.

### With PDB input
**Args:** `density-fitness --model structure.pdb --mtz data.mtz --output metrics.tsv`
**Explanation:** Use PDB format structure file.

### Generate visual report
**Args:** `density-fitness --model structure.cif --mtz data.mtz --output metrics.tsv --plot plot.pdf`
**Explanation:** Generate PDF report with visualizations.