---
name: crux-toolkit
category: utility
description: A cross-platform suite of analysis tools for interpreting protein mass spectrometry data
tags: [crux-toolkit, utility, mass-spectrometry, proteomics, peptide-identification]
author: oxo-call-community
source_url: "http://crux.ms"
---

## Concepts

- **Tool Overview**: crux-toolkit (v4.2+) is a cross-platform suite of analysis tools for interpreting protein mass spectrometry data, including database search engines and post-processing tools.
- **Core Function**: Provides tools for peptide identification, protein inference, label-free quantification, and statistical confidence estimation from MS/MS data.
- **Input/Output**: Input: Mass spectrometry data files (MS2, mzML), protein FASTA databases. Output: Peptide-spectrum matches (PSMs), protein identifications, quantification results.
- **Key Commands**: tide-index, tide-search, comet, percolator, lfq, pipeline, bullseye, kojak (cross-linking).
- **Installation**: `conda install -c bioconda crux-toolkit` or download from crux.ms

## Pitfalls

- **FASTA Index**: Must build a peptide index with `tide-index` before running `tide-search`.
- **Decoy Database**: Decoy sequences are automatically generated; use `--decoy-format` to specify strategy.
- **Modifications**: Static and variable modifications must be specified during index creation.
- **Memory Usage**: Large protein databases require significant memory for indexing.
- **Thread Count**: Multi-threading support varies by command; check individual tool help.

## Examples

### Build peptide index
**Args:** `tide-index --missed-cleavages 2 uniprot_human.fasta human_index`
**Explanation:** Create a peptide index from a protein FASTA file with up to 2 missed cleavages.

### Search spectra against index
**Args:** `tide-search --precursor-window 20 --fragment-window 0.5 spectra.ms2 human_index results.txt`
**Explanation:** Search MS/MS spectra against a pre-built peptide index with specified tolerance windows.

### Run complete pipeline
**Args:** `pipeline --peptide-spectrum-match-output T spectra.mzML uniprot_human.fasta output_dir`
**Explanation:** Run the complete analysis pipeline including indexing, searching, and confidence estimation.

### Label-free quantification
**Args:** `lfq --min-peptides 2 --output-dir lfq_results/ spectra.mzML`
**Explanation:** Perform label-free quantification on MS/MS data, requiring at least 2 peptides per protein.

### Percolator for confidence estimation
**Args:** `percolator --protein-level-fdr 0.01 psms.txt`
**Explanation:** Re-rank PSMs and estimate protein-level FDR at 1% threshold.

### Comet search
**Args:** `comet --database uniprot.fasta --output-dir comet_results/ spectra.ms2`
**Explanation:** Use the Comet search engine for peptide identification directly from FASTA.

### Cross-link search with Kojak
**Args:** `kojak --database proteins.fasta --output kojak_results/ crosslink_spectra.ms2`
**Explanation:** Search for cross-linked peptides in MS/MS data using the Kojak algorithm.

### Set static modifications
**Args:** `tide-index --mods-spec K+229.162932 --nterm-peptide-mods-spec X+229.162932 proteins.fasta indexed_db`
**Explanation:** Create index with TMT11 modification on lysines and N-termini.
