---
name: digest
category: utility
description: digest - In silico digestion of protein sequences.
tags: [digest, utility, proteomics, digestion]
author: oxo-call-community
source_url: "https://github.com/ProteomicsTools/Digest"
---

## Concepts

- **Tool Overview**: digest is an in silico protein digestion tool for mass spectrometry applications.
- **Core Function**: Simulates enzymatic digestion of protein sequences to generate theoretical peptide lists for proteomics analysis.
- **Input/Output**: Input: Protein FASTA files. Output: Digested peptide sequences with properties.
- **Algorithm**: Uses enzyme specificity rules to cleave proteins at specific amino acid residues.
- **Key Features**: Multiple enzyme support, missed cleavage handling, peptide length filtering, batch processing.
- **Installation**: `conda install -c bioconda digest`

## Pitfalls

- **Input Requirements**: Requires protein sequences in FASTA format.
- **Enzyme Selection**: Must select appropriate enzyme for digestion.
- **Missed Cleavages**: Can significantly increase number of peptides.
- **Peptide Length**: Short peptides may not be detected by mass spectrometry.
- **Modifications**: Does not handle post-translational modifications by default.

## Examples

### Digest proteins
**Args:** `digest --input proteins.fa --output peptides.fa`
**Explanation:** Performs in silico digestion of protein sequences.

### With specific enzyme
**Args:** `digest --input proteins.fa --output peptides.fa --enzyme chymotrypsin`
**Explanation:** Use chymotrypsin instead of default trypsin.

### Allow missed cleavages
**Args:** `digest --input proteins.fa --output peptides.fa --missed-cleavages 3`
**Explanation:** Allow up to 3 missed cleavages per peptide.

### Filter by peptide length
**Args:** `digest --input proteins.fa --output peptides.fa --min-length 6 --max-length 30`
**Explanation:** Filter peptides by length range.

### Batch processing
**Args:** `digest --input-dir protein_files/ --output peptides.fa`
**Explanation:** Process multiple protein files in batch.