---
name: afpdb
category: utility
description: High-performance NumPy-based Python package for protein structure manipulation using AlphaFold architecture
tags: [protein-structure, pdb, alphafold, numpy, structure-manipulation]
author: oxo-call-community
source_url: "https://github.com/data2code/afpdb"
---

## Concepts

- **Tool Overview**: Afpdb is a high-performance Python module built on AlphaFold's NumPy architecture for efficient protein structure manipulation and analysis.
- **Core Function**: Provides fast structure operations including residue/atom selection, coordinate manipulation, format conversion, and structure analysis.
- **Input/Output**: Input: PDB, mmCIF, or AlphaFold prediction files. Output: Modified structures in various formats.
- **RFDiffusion Syntax**: Uses RFDiffusion's contig syntax for streamlined residue and atom selection, enabling flexible structure manipulation.
- **Installation**: Install via bioconda: `conda install -c bioconda afpdb`

## Pitfalls

- **NumPy Dependency**: Requires NumPy and may need specific versions compatible with AlphaFold architecture.
- **Large Structures**: Very large protein complexes may require significant memory for coordinate arrays.
- **Format Compatibility**: Some PDB files with non-standard formatting may require preprocessing.
- **Chain Handling**: Multi-chain structures require explicit chain specification in selections.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and modules in the afpdb package.

### Load and inspect structure
**Args:** `load structure.pdb --info`
**Explanation:** Loads a PDB file and displays basic information about chains, residues, and atoms.

### Extract specific chain
**Args:** `select structure.pdb -c A -o chainA.pdb`
**Explanation:** Extracts chain A from the structure and saves to new PDB file.

### Select residue range
**Args:** `select structure.pdb -r "50-150" -o domain.pdb`
**Explanation:** Extracts residues 50-150 from the structure using contig syntax.

### Convert PDB to mmCIF
**Args:** `convert structure.pdb -o structure.cif --format mmcif`
**Explanation:** Converts PDB format to mmCIF format for compatibility with modern tools.

### Calculate RMSD between structures
**Args:** `rmsd structure1.pdb structure2.pdb -o rmsd.txt`
**Explanation:** Calculates root-mean-square deviation between two aligned structures.

### Merge multiple structures
**Args:** `merge chainA.pdb chainB.pdb -o complex.pdb`
**Explanation:** Combines multiple PDB files into a single structure file.

### Apply transformation
**Args:** `transform structure.pdb --rotate "x:90" --translate "10,0,5" -o transformed.pdb`
**Explanation:** Applies rotation and translation to the structure coordinates.
