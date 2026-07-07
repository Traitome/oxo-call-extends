---
name: infernal
category: rna-analysis
description: Search DNA sequence databases for RNA structure and sequence similarities using covariance models
tags: [infernal, RNA-structure, covariance-models, sequence-analysis]
author: oxo-call-community
source_url: "http://eddylab.org/infernal/"
---

## Concepts

- **Tool Overview**: Infernal (v1.1.5) is a software package for searching DNA sequence databases for RNA structure and sequence similarities using covariance models (CMs).
- **Core Function**: Uses stochastic context-free grammars to model RNA secondary structure, enabling sensitive detection of homologous RNAs in sequence databases.
- **Key Programs**: Includes cmbuild (build CMs), cmcalibrate (calibrate E-values), cmsearch (search CM vs sequences), cmscan (search sequences vs CM database), and cmalign (align sequences to CM).
- **Input/Output**: Accepts FASTA, Stockholm, and other sequence formats. Outputs alignments, hit tables, and structural annotations.
- **Rfam Integration**: Widely used with Rfam database for genome annotation of non-coding RNAs.

## Pitfalls

- **CM Database Preparation**: CM databases must be calibrated with cmcalibrate and compressed with cmpress before use with cmscan.
- **Computational Complexity**: RNA structure alignment is computationally intensive; large datasets may require parallel processing.
- **E-value Calculation**: Accurate E-values require proper database size specification using -Z option.
- **Truncated Hits**: By default, truncated hits must include sequence endpoints; use --anytrunc for more permissive detection.
- **Memory Requirements**: Large CM databases can require significant memory resources.

## Examples

### Build covariance model from alignment
**Args:** `cmbuild -F model.cm alignment.sto`
**Explanation:** Constructs a covariance model from a Stockholm-format alignment file.

### Calibrate model for E-values
**Args:** `cmcalibrate --mpi model.cm`
**Explanation:** Calibrates the CM for accurate E-value calculation; use --mpi for parallel processing.

### Search sequence database with CM
**Args:** `cmsearch -o results.txt --tblout hits.tsv model.cm sequences.fa`
**Explanation:** Searches a sequence database against a single covariance model.

### Scan sequences against CM database
**Args:** `cmscan -Z 6 --cut_ga --rfam --tblout output.tsv Rfam.cm genome.fa`
**Explanation:** Scans genome sequences against Rfam CM database with GA threshold cutoff.

### Align sequences to CM
**Args:** `cmalign -o aligned.sto model.cm unaligned.fa`
**Explanation:** Aligns unaligned sequences to a covariance model.

### Compress CM database
**Args:** `cmpress Rfam.cm`
**Explanation:** Compresses and indexes CM database for efficient cmscan searches.