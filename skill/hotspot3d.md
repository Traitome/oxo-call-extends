---
name: hotspot3d
category: variant-analysis
description: HotSpot3D identifies mutation hotspots based on 3D protein structures, correlating mutations with protein domains, interacting partners, and drug targets.
tags: [hotspot3d, mutation, protein-structure, cancer]
author: oxo-call-community
source_url: "https://github.com/ding-lab/hotspot3d"
---

## Concepts

- **3D Proximity Analysis**: HotSpot3D maps somatic mutations onto protein 3D structures from the Protein Data Bank (PDB), identifying spatial clusters rather than just linear sequence hotspots.
- **Mutation-Drug Clusters**: The tool identifies mutations that co-cluster with known drug-binding sites, facilitating the discovery of potential drug targets and resistance mechanisms.
- **Graph-Based Clustering**: Uses graph-based hierarchical clustering algorithm considering closest atomic distances to construct mutation distance matrices and identify significant clusters.
- **TCGA Integration**: Provides a database of proximal mutations from 33 cancer types in The Cancer Genome Atlas, enabling cross-cancer comparison and analysis.
- **Multi-level Analysis**: Detects novel/rare mutations co-clustering with known hotspots, medium recurrent mutations showing collective enrichment, and cancer type-specific mutation patterns.
- **Structural Visualization**: Integrates with 3Dmol for interactive visualization of mutation clusters within protein structures in web browser.

## Pitfalls

- **Structure Availability**: Requires high-quality protein structures; proteins without PDB structures cannot be analyzed, potentially missing important hotspots.
- **Mapping Complexity**: Mutation mapping from genomic coordinates to PDB residue numbers involves complex transformations (genomic→transcript→protein→PDB), which may fail for splice variants.
- **Distance Threshold Selection**: The choice of distance threshold (typically 5-12 Å) significantly impacts cluster identification; defaults may not suit all proteins.
- **Multiple Testing**: Large-scale mutation analysis requires appropriate statistical correction to avoid false positive clusters.
- **Chain Limitations**: Currently limited to intra-chain (single polypeptide) analysis; does not support inter-chain or complex-level hotspot detection.
- **MAF Format Requirements**: Requires properly formatted MAF files with ENSP or SWISSPROT identifiers; missing or incorrect identifiers cause processing failures.

## Examples

### Basic hotspot detection
**Args:** `hotspot3d -i mutations.maf -o hotspot_results/ -p pdb_structures/`
**Explanation:** Identifies spatial mutation hotspots by mapping mutations from MAF file onto PDB structures and performing clustering analysis.

### With TCGA database comparison
**Args:** `hotspot3d -i mutations.maf -o results/ -t tcga`
**Explanation:** Compares identified hotspots against TCGA database of 33 cancer types to identify cancer-specific mutation patterns.

### Mutation-drug interaction analysis
**Args:** `hotspot3d -i mutations.maf -o drug_interaction_results/ -d drug_targets.txt`
**Explanation:** Identifies mutations that cluster near known drug-binding sites, revealing potential drug resistance mechanisms or novel therapeutic targets.

### Custom distance threshold
**Args:** `hotspot3d -i mutations.maf -o results/ -r 8`
**Explanation:** Sets custom distance threshold of 8 Å for clustering, suitable for analyzing larger protein domains or looser interaction interfaces.

### Generate visualization
**Args:** `hotspot3d -i mutations.maf -o results/ --visualize`
**Explanation:** Generates 3D visualization files for interactive exploration of mutation clusters within protein structures.

### Batch processing mode
**Args:** `hotspot3d -i batch_input/ -o batch_output/ -b`
**Explanation:** Processes multiple MAF files in batch mode, useful for large-scale cancer genomics studies.