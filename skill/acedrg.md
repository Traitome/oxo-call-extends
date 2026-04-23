---
name: acedrg
category: utility
description: Ligand and monosaccharide coordinate and restraint dictionary generator for macromolecular crystallography (CCP4)
tags: [crystallography, ligand, restraint, ccp4, monosaccharide, structure]
author: oxo-call-community
source_url: "https://www2.mrc-lmb.cam.ac.uk/groups/murshudov/content/acedrg/acedrg.html"
---

## Concepts

- **Tool Overview**: ACEDRG is a tool from CCP4 suite for generating ligand and monosaccharide coordinates and restraint dictionaries for macromolecular crystallography refinement.
- **Core Function**: Creates stereochemically accurate 3D coordinates and restraint files from chemical descriptions (SMILES, Mol files, or chemical drawings).
- **Input/Output**: Input: SMILES strings, MOL/SDF files, or chemical descriptions. Output: PDB coordinates and CIF restraint dictionaries compatible with refinement programs.
- **Integration**: Works with CCP4 suite, REFMAC5, and other crystallographic refinement programs that require proper ligand geometry restraints.
- **Installation**: Install via bioconda: `conda install -c bioconda acedrg`

## Pitfalls

- **Minimum Requirements**: ACEDRG requires element types and basic bonding pattern information - incomplete chemical descriptions will fail.
- **SMILES Format**: SMILES strings must be chemically valid; stereochemistry must be properly specified for correct 3D generation.
- **Output Files**: Generates multiple output files including coordinates (PDB) and restraints (CIF) - both are needed for refinement.
- **Conformer Generation**: For ligands with rotatable bonds, multiple conformers may be generated - select appropriate one for fitting.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available command line options and usage information for ACEDRG.

### Generate ligand from SMILES string
**Args:** `-s "CC(=O)OC1=CC=CC=C1C(=O)O" -o aspirin`
**Explanation:** Generates coordinates and restraints for aspirin from its SMILES string, output files named aspirin.pdb and aspirin.cif.

### Generate from MOL file
**Args:** `-i ligand.mol -o output_ligand`
**Explanation:** Reads chemical structure from MOL file and generates PDB coordinates and CIF restraint dictionary.

### Generate monosaccharide restraints
**Args:** `-m GLC -o glucose`
**Explanation:** Generates coordinates and restraints for glucose monosaccharide using standard three-letter code.

### Generate with specific protonation state
**Args:** `-s "C(C(=O)[O-])[NH3+]" -p 7.4 -o amino_acid`
**Explanation:** Generates ligand with protonation state appropriate for pH 7.4, important for biological conditions.

### Generate multiple conformers
**Args:** `-s "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O" -c 10 -o ibuprofen`
**Explanation:** Generates 10 conformers for ibuprofen to sample different rotameric states during ligand fitting.
