---
name: gc-meox-tms
category: qc
description: Python package for in-silico methoximation (MeOX) and trimethylsilylation (TMS) derivatization of chemical compounds from SMILES strings
tags: [gc-meox-tms, metabolomics, derivatization, SMILES, RDKit, MeOX, TMS, GC-MS, chemistry]
author: oxo-call-community
source_url: "https://github.com/RECETOX/gc-meox-tms"
---

## Concepts

- **Tool Overview**: gc-meox-tms performs in-silico methoximation (MeOX) and trimethylsilylation (TMS) derivatization of chemical compounds, commonly used in GC-MS (Gas Chromatography-Mass Spectrometry) sample preparation for metabolomics.
- **Core Function**: Converts SMILES strings or RDKit molecule objects into their derivatized forms by adding MeOX groups (replacing carbonyl oxygens with =O-N-OCH3) and/or TMS groups (replacing active hydrogens with -Si(CH3)3).
- **Input Formats**: Accepts SMILES strings directly or RDKit Mol objects for processing. Supports batch processing of multiple compounds.
- **Output**: Returns derivatized SMILES strings or RDKit Mol objects with calculated derivatization patterns showing which functional groups were modified.
- **Derivatization Purpose**: Chemical derivatization increases compound volatility and thermal stability for GC-MS analysis. Carbonyl compounds (ketones, aldehydes) are methoximated to prevent keto-enol tautomerization. Active hydrogen groups (OH, NH, SH) are TMS-silylated to improve peak shape and detection.
- **Detection**: Can identify whether a compound is already derivatized by MeOX or TMS methods, preventing over-derivatization.
- **Installation**: `pip install gc-meox-tms` or `conda install -c bioconda gc-meox-tms`. Requires Python >=3.8 and RDKit.
- **Dependencies**: RDKit for molecular structure handling and SMILES parsing; Python standard library for I/O operations.

## Pitfalls

- **RDKit installation**: RDKit is a complex C++ extension. Install via conda (`conda install -c conda-forge rdkit`) rather than pip for reliable installation on most platforms.
- **Over-derivatization**: Running derivatization on already-derivatized compounds can produce incorrect products. Always check the `is_derivatized()` status before processing.
- **SMILES validity**: Invalid SMILES strings will cause processing errors. Validate SMILES format before batch processing using RDKit's MolFromSmiles function.
- **Functional group limitations**: Not all functional groups are equally reactive. Carboxylic acids, alcohols, amines, and thiols are silylatable; aromatic nitro groups and some heterocyclic nitrogens are not.
- **MeOX reaction conditions**: Methoximation specifically targets carbonyl groups (aldehydes and ketones). Other functional groups are not affected by MeOX derivatization.
- **Stereosochemistry**: Derivatization can alter or destroy stereochemical information in molecules. Handle chiral compounds with care.
- **Batch processing memory**: Processing large compound lists (10,000+) may require memory management. Consider processing in chunks for very large datasets.

## Examples

### Basic MeOX derivatization
**Args:** `gc-meox-tms --smiles "CC(=O)CC" --meox --output json`
**Explanation:** Derivatizes acetone (CC(=O)CC) with a single carbonyl group using methoximation. The carbonyl oxygen is replaced with =N-O-CH3, producing a more stable compound suitable for GC-MS analysis. Output in JSON format shows the derivatized SMILES and reaction details.

### Basic TMS silylation
**Args:** `gc-meox-tms --smiles "CCO" --tms --output json`
**Explanation:** Silylates ethanol (CCO) containing an hydroxyl group. The active hydrogen on the oxygen is replaced with TMS (-Si(CH3)3), dramatically increasing volatility. Multiple OH groups each receive a TMS substitution.

### Combined MeOX and TMS derivatization
**Args:** `gc-meox-tms --smiles "CC(=O)CCO" --meox --tms --output json`
**Explanation:** For compounds with both carbonyl and hydroxyl groups (like 3-hydroxy-2-butanone), both derivatization steps are applied sequentially. MeOX first targets the ketone, then TMS silylates the hydroxyl group. Order of operations ensures complete derivatization.

### Check if compound is already derivatized
**Args:** `gc-meox-tms --smiles "CC(=NOCH3)CC" --check`
**Explanation:** Checks whether the input SMILES contains MeOX (=NOCH3) or TMS (-Si(CH3)3) groups. Returns a boolean flag indicating derivatization status. Prevents over-derivatization of samples already processed.

### Process from SMILES file
**Args:** `gc-meox-tms --input compounds.smi --meox --tms --output results.csv`
**Explanation:** Batch processing mode reads multiple SMILES from an input file (one per line). Applies both derivatizations to each compound and writes results to CSV with columns: original_smiles, derivatized_smiles, num_meox_groups, num_tms_groups.

### Python API usage
**Args:** `from gc_meox_tms import derivatize, is_derivatized; mol = derivatize("CCO", method="tms")`
**Explanation:** The gc-meox-tms package exposes a Python API for integration into analysis pipelines. The derivatize() function accepts SMILES strings or Mol objects and returns derivatized molecules. is_derivatized() checks compound status programmatically.

### RDKit Mol object processing
**Args:** `from rdkit import Chem; from gc_meox_tms import derivatize; mol = Chem.MolFromSmiles("CCO"); derivatized = derivatize(mol, method="tms")`
**Explanation:** For molecules already parsed by RDKit, pass the Mol object directly to avoid re-parsing. Useful when gc-meox-tms is integrated into RDKit-based workflows for metabolomics data processing.

### Generate derivatization report
**Args:** `gc-meox-tms --input metabolites.smi --meox --tms --report --output report.json`
**Explanation:** The report option generates detailed information including: which functional groups were modified, number of MeOX/TMS additions, molecular weight change, and any groups that could not be derivatized. Useful for quality control in metabolomics studies.
