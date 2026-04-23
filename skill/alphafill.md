---
name: alphafill
category: annotation
description: Algorithm to transplant missing ligands, cofactors and ions to AlphaFold protein structure models
tags: [alphafold, ligand, cofactor, structure, protein, transplantation]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/alphafill"
---

## Concepts

- **Tool Overview**: AlphaFill enriches AlphaFold protein structure models by transplanting missing ligands, cofactors, and metal ions from experimentally determined structures.
- **Core Function**: Uses sequence and structure similarity to identify and transplant relevant molecular context to AlphaFold models, improving functional interpretation.
- **Input/Output**: Input: AlphaFold PDB/mmCIF model. Output: Enriched model with transplanted ligands and cofactors.
- **Database**: Uses PDB structure database to find homologous structures with bound ligands for transplantation.
- **Installation**: Install via bioconda: `conda install -c bioconda alphafill`

## Pitfalls

- **Sequence Similarity**: Transplantation quality depends on sequence similarity to structures with known ligands.
- **Conformer Selection**: Multiple conformers may be transplanted - review for biological relevance.
- **Clash Detection**: Transplanted ligands may clash with the model - check for steric conflicts.
- **Binding Site Accuracy**: AlphaFold may not accurately predict binding site conformation - transplanted ligands are approximate.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for AlphaFill.

### Fill a single AlphaFold model
**Args:** `fill -i AF-P12345-F1.pdb -o filled_model.cif`
**Explanation:** Transplants ligands and cofactors to an AlphaFold model from UniProt P12345.

### Fill with custom database
**Args:** `fill -i model.pdb -o filled.cif -d /path/to/alphafill/db`
**Explanation:** Uses custom AlphaFill database directory for ligand transplantation.

### Batch process multiple models
**Args:** `fill -i models/ -o filled_models/`
**Explanation:** Processes all AlphaFold models in a directory, outputting filled models.

### Set BLAST e-value threshold
**Args:** `fill -i model.pdb -o filled.cif --blast-expect 1e-10`
**Explanation:** Uses stricter e-value threshold for more reliable homolog identification.

### Disable gap filtering in BLAST
**Args:** `fill -i model.pdb -o filled.cif --blast-no-gapped`
**Explanation:** Disables gapped alignment in BLAST search for more sensitive homology detection.

### Custom BLAST matrix
**Args:** `fill -i model.pdb -o filled.cif --blast-matrix BLOSUM80`
**Explanation:** Uses BLOSUM80 substitution matrix for more stringent sequence comparison.

### Verbose output for debugging
**Args:** `fill -i model.pdb -o filled.cif -v`
**Explanation:** Enables verbose output to track transplantation decisions and matches.
