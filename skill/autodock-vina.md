---
name: autodock-vina
category: utility
description: AutoDock Vina - Open-source molecular docking program for protein-ligand binding prediction
tags: [molecular-docking, drug-discovery, protein-ligand, binding-prediction, virtual-screening]
author: oxo-call-community
source_url: "https://github.com/ccsb-scripps/AutoDock-Vina"
---

## Concepts

- **Tool Overview**: AutoDock Vina is one of the fastest and most widely used open-source molecular docking programs. It predicts how small molecules (ligands) bind to receptor proteins using a simple scoring function and efficient optimization algorithm.

- **Speed and Accuracy**: Significantly faster than AutoDock 4 while maintaining or improving binding mode prediction accuracy. Utilizes multi-core parallelization for even greater speed.

- **Input Requirements**: Requires receptor and ligand structures in PDBQT format, and definition of search space (binding site) via grid box coordinates. No need to pre-calculate grid maps when using Vina or Vinardo force field.

- **Scoring Function**: Uses a simple empirical scoring function combining steric, hydrophobic, and hydrogen bonding terms. Provides binding affinity estimates in kcal/mol.

- **Flexible Docking**: Supports receptor flexibility by allowing specified side chains to move during docking, improving accuracy for proteins with flexible binding sites.

- **Multiple Modes**: Outputs multiple binding poses (conformations) ranked by predicted binding affinity, allowing analysis of alternative binding modes.

- **Batch Processing**: Can dock multiple ligands in a single run, making it suitable for virtual screening of compound libraries.

## Pitfalls

- **PDBQT Preparation**: Receptor and ligand must be properly prepared in PDBQT format, including addition of hydrogens, assignment of atom types, and removal of water molecules (unless specifically needed).

- **Search Space Definition**: Grid box size and center significantly affect results. Too small box misses correct poses; too large box increases computation time and may find irrelevant binding sites.

- **Exhaustiveness Parameter**: Default exhaustiveness (8) may be insufficient for complex binding sites. Increase for more thorough search at cost of longer computation time.

- **Force Field Selection**: Vina and Vinardo force fields have different strengths. Test both for your specific system to determine optimal choice.

- **Metal Ions**: Standard Vina has limited support for metal-containing proteins. Special handling required for zinc metalloproteins and other metal-dependent receptors.

- **Water Molecules**: Deciding whether to include or exclude structural water molecules in binding site requires careful consideration of their role in ligand binding.

- **Protonation States**: Correct protonation states of ionizable groups (especially histidine) are critical for accurate docking. Use appropriate pKa predictions.

## Examples

### Basic receptor-ligand docking
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --out output.pdbqt`
**Explanation:** Docks ligand into receptor binding site defined by center coordinates and box dimensions (20Å in each dimension). Outputs top poses to PDBQT file.

### Docking with increased exhaustiveness
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 15.5 --center_y 12.3 --center_z -8.7 --size_x 25 --size_y 25 --size_z 25 --exhaustiveness 32 --out output.pdbqt`
**Explanation:** Uses higher exhaustiveness (32) for more thorough conformational search, recommended for complex binding sites or when default fails to find good poses.

### Flexible receptor docking
**Args:** `vina --receptor receptor_rigid.pdbqt --flex receptor_flex.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --out output.pdbqt`
**Explanation:** Docks with flexible receptor side chains specified in receptor_flex.pdbqt, allowing induced-fit binding mode prediction.

### Batch docking multiple ligands
**Args:** `vina --receptor receptor.pdbqt --ligand_dir ligands/ --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --out_dir results/`
**Explanation:** Docks all ligands in specified directory against the receptor, saving results to output directory. Useful for virtual screening.

### Using Vinardo force field
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --scoring vinardo --out output.pdbqt`
**Explanation:** Uses Vinardo scoring function instead of default Vina, which may perform better for certain protein-ligand systems.

### Multi-threaded docking
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --cpu 8 --out output.pdbqt`
**Explanation:** Utilizes 8 CPU cores for parallel docking, significantly reducing computation time for large-scale screening.

### Specify output pose count
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --num_modes 20 --energy_range 5 --out output.pdbqt`
**Explanation:** Outputs up to 20 binding modes within 5 kcal/mol of best pose, useful for analyzing alternative binding conformations.

### Random seed for reproducibility
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --seed 42 --out output.pdbqt`
**Explanation:** Sets random seed for reproducible results, important for debugging or when exact reproducibility is required.

### Docking with log file
**Args:** `vina --receptor receptor.pdbqt --ligand ligand.pdbqt --center_x 10.0 --center_y 20.0 --center_z 30.0 --size_x 20 --size_y 20 --size_z 20 --out output.pdbqt --log docking.log`
**Explanation:** Saves detailed docking output including binding affinities, RMSD values, and computation time to log file for record keeping.

### Python API basic usage
**Args:** `python -c "from vina import Vina; v = Vina(sf_name='vina'); v.set_receptor('receptor.pdbqt'); v.set_ligand_from_file('ligand.pdbqt'); v.compute_vina_maps(center=[10.0, 20.0, 30.0], box_size=[20, 20, 20]); v.dock(exhaustiveness=8); v.write_poses('output.pdbqt')"`
**Explanation:** Uses Python API for programmatic docking, allowing integration into custom workflows and automation scripts.
