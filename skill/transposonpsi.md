---
name: transposonpsi
category: analysis
description: TransposonPSI - Tool for identifying transposon-derived peptides.
tags: [transposonpsi, transposon, peptide-identification, proteomics, genome-analysis]
author: oxo-call-community
source_url: "https://github.com/compbio/transposonpsi"
---

## Concepts

- **Tool Overview**: TransposonPSI - A tool for identifying transposon-derived peptides from proteomics data.
- **Core Function**: Searches mass spectrometry data for peptides originating from transposon sequences.
- **Input**: Mass spectrometry data (mzML), transposon sequence database.
- **Output**: Identified transposon peptides, confidence scores, functional annotations.
- **Installation**: `pip install transposonpsi` or `conda install -c bioconda transposonpsi`
- **Use Case**: Proteomics, transposon biology, genome annotation.

## Pitfalls

- **Database**: Results depend on transposon database completeness.
- **False Positives**: May produce false positive peptide identifications.

## Examples

### Search transposon peptides
**Args:** `transposonpsi -i mass_spec.mzML -d transposon_db.fasta -o peptides/`
**Explanation:** Identify transposon-derived peptides from mass spectrometry data.

### With genome
**Args:** `transposonpsi -i spectra.mgf -g genome.fasta -o results/`
**Explanation:** Search for transposon peptides using genome as database.
