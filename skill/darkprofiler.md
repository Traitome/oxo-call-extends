---
name: darkprofiler
category: alignment
description: DarkProfiler - Alignment and Classification of Peptides from De Novo Peptide Sequencing
tags: [darkprofiler, alignment, proteomics, peptide-sequencing, mass-spectrometry]
author: oxo-call-community
source_url: "https://pypi.org/project/darkprofiler/"
---

## Concepts

- **Tool Overview**: darkprofiler (v0.2.6+) aligns and classifies peptides from reference-independent de novo peptide sequencing experiments.
- **Core Function**: Matches de novo peptide sequences to databases for validation and annotation.
- **Input/Output**: Input: De novo peptide sequences. Output: Matched peptides, protein assignments.
- **Algorithm**: Uses peptide property matching and database searching for classification.
- **Key Features**: Reference-independent analysis, peptide classification, proteomics support.
- **Installation**: `conda install -c bioconda darkprofiler`

## Pitfalls

- **Database Quality**: Requires comprehensive protein databases for matching.
- **De Novo Quality**: Results depend on de novo sequencing accuracy.
- **Ambiguous Matches**: Multiple matches may complicate interpretation.
- **Parameter Tuning**: Matching thresholds require adjustment for specific data.
- **Validation**: Matched peptides should be validated experimentally.

## Examples

### Classify de novo peptides
**Args:** `darkprofiler -i denovo_peptides.txt -d protein_db.fasta -o classified.txt`
**Explanation:** Classify de novo peptide sequences using protein database.

### Adjust matching threshold
**Args:** `darkprofiler -i peptides.txt -d database.fasta -o results.txt --threshold 0.8`
**Explanation:** Use 80% peptide property matching threshold.

### Export to CSV
**Args:** `darkprofiler -i peptides.txt -d database.fasta -o results.csv --format csv`
**Explanation:** Export classification results in CSV format.
