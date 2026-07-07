---
name: dig2
category: utility
description: dig2 - In silico protein digester for MS/MS fragment simulation.
tags: [dig2, utility, proteomics, digestion, msms]
author: oxo-call-community
source_url: "https://github.com/mobiusklein/dig2"
---

## Concepts

- **Tool Overview**: dig2 (v1.0+) is an in silico protein sequence digester supporting various enzymes and MS/MS fragment generation.
- **Core Function**: Simulates enzymatic digestion of proteins and generates CID/ECD/ETD fragment ions for mass spectrometry analysis.
- **Input/Output**: Input: Protein FASTA files. Output: Digested peptides, fragment ions with m/z values.
- **Algorithm**: Uses enzyme specificity rules to cleave proteins and calculate fragment masses.
- **Key Features**: Multiple enzyme support, fragment ion generation, post-translational modification handling, batch processing.
- **Installation**: `conda install -c bioconda dig2`

## Pitfalls

- **Input Requirements**: Requires protein sequences in FASTA format.
- **Enzyme Specificity**: Results depend on correct enzyme selection.
- **Modifications**: May not handle all post-translational modifications.
- **Fragment Types**: Different fragmentation methods produce different ion types.
- **Mass Accuracy**: Fragment masses depend on mass calculation method.

## Examples

### Digest proteins with trypsin
**Args:** `dig2 --input proteins.fa --enzyme trypsin --output peptides.tsv`
**Explanation:** Simulates trypsin digestion of protein sequences.

### Generate fragment ions
**Args:** `dig2 --input proteins.fa --enzyme trypsin --output fragments.tsv --fragments`
**Explanation:** Generate MS/MS fragment ions for digested peptides.

### With missed cleavages
**Args:** `dig2 --input proteins.fa --enzyme trypsin --output peptides.tsv --missed-cleavages 2`
**Explanation:** Allow up to 2 missed cleavages per peptide.

### Include modifications
**Args:** `dig2 --input proteins.fa --enzyme trypsin --output peptides.tsv --modifications mods.txt`
**Explanation:** Apply post-translational modifications during digestion.

### Batch processing
**Args:** `dig2 --input-dir protein_files/ --output peptides.tsv`
**Explanation:** Process multiple protein files in batch.