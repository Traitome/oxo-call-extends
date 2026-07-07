---
name: sadie-antibody
category: antibody_analysis
description: Comprehensive antibody sequence analysis toolkit for immunoinformatics
tags: ["sadie-antibody", "antibody", "immunoinformatics", "sequence analysis", "BCR"]
author: oxo-call-community
source_url: "https://sadie.jordanrwillis.com"
---

## Concepts

- **Tool Overview**: SADIE (v2.0.0) is a comprehensive antibody sequence analysis toolkit designed for immunoinformatics research, providing tools for B-cell receptor (BCR) sequence analysis, clonal assignment, and epitope prediction.
- **Core Function**: Analyzes antibody sequences to identify V(D)J rearrangements, compute clonal relationships, predict epitope binding, and generate comprehensive reports.
- **Algorithm**: Implements IMGT-based V(D)J annotation, clustering algorithms for clonal assignment, and machine learning models for epitope prediction.
- **Input Format**: Antibody sequences in FASTA or FASTQ format, AIRR-compliant JSON files, raw sequencing data.
- **Output Format**: Annotated sequences with V(D)J assignments, clonal clusters, epitope predictions, AIRR-formatted output, visualizations.
- **Use Case**: BCR repertoire analysis, vaccine development, antibody discovery, immunogenomics research, clinical immunology.

## Pitfalls

- **Germline database**: Requires up-to-date germline gene database for accurate V(D)J assignment.
- **Sequence quality**: Poor quality sequences may lead to incorrect annotations.
- **Ambiguous assignments**: Some sequences may have ambiguous V(D)J assignments.
- **Memory requirements**: Large repertoire datasets require significant memory.
- **Computational time**: Complex analyses can be time-consuming for large datasets.
- **Annotation errors**: Manual review recommended for critical applications.

## Examples

### Basic V(D)J annotation
**Args:** `sadie annotate -i sequences.fasta -o annotated.json`
**Explanation:** `-i` input FASTA with antibody sequences; `-o` output AIRR JSON file.

### Clonal assignment
**Args:** `sadie clone -i annotated.json -o clones.json`
**Explanation:** Identifies clonal relationships among annotated sequences.

### Epitope prediction
**Args:** `sadie epitope -i sequences.fasta -o predictions.csv`
**Explanation:** Predicts epitope binding sites from antibody sequences.

### Batch processing
**Args:** `sadie batch -d fastq_dir -o results.json`
**Explanation:** Processes all FASTQ files in a directory.

### Visualize clonal tree
**Args:** `sadie visualize -i clones.json -o tree.png`
**Explanation:** Generates visualization of clonal relationships.

### AIRR format conversion
**Args:** `sadie convert -i raw.fasta -o airr.json --format airr`
**Explanation:** Converts sequences to AIRR-compliant format.

### Filter by quality
**Args:** `sadie filter -i sequences.fasta -o filtered.fasta -q 30`
**Explanation:** `-q` minimum quality threshold for filtering sequences.