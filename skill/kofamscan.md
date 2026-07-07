---
name: kofamscan
category: annotation
description: KofamKOALA - K number assignment using HMMER against KOfam
tags: [kofamscan, annotation, KEGG, KOfam, HMM, functional-annotation]
author: oxo-call-community
source_url: "https://www.genome.jp/tools/kofamkoala/"
---

## Concepts

- **K Number Assignment**: Assigns KEGG Orthology (KO) numbers to sequences
- **HMM-based Detection**: Uses HMMER/HMMSEARCH against KOfam database
- **Functional Annotation**: Provides functional annotation of protein sequences
- **Pathway Mapping**: Links annotations to KEGG pathways
- **EC Number Prediction**: Predicts Enzyme Commission numbers
- **Threshold-based Scoring**: Uses score thresholds for reliable assignments

## Pitfalls

- **Database Size**: Large KOfam database requires significant resources
- **Score Thresholds**: Improper thresholds lead to false positives/negatives
- **Novel Functions**: Novel proteins may not find significant matches
- **Sequence Quality**: Poor quality sequences affect annotation accuracy
- **E-value Selection**: E-value cutoff affects detection sensitivity
- **Annotation Transfer**: Annotations are transferred from database entries

## Examples

### Annotate protein sequences
**Args:** `exec_annotation -f mapper -p profiles -k ko_list -i proteins.faa -o annotation.tsv`
**Explanation:** Annotates proteins with K numbers using HMM profiles.

### Koala mode
**Args:** `koala -i proteins.faa -o annotation.txt`
**Explanation:** Uses Koala web server mode for annotation.

### Batch annotation
**Args:** `exec_annotation -i proteins_dir/ -p profiles -k ko_list -o annotations/`
**Explanation:** Batch annotates multiple protein files.

### Detailed output
**Args:** `exec_annotation -i proteins.faa -o detailed.tsv --details`
**Explanation:** Provides detailed output with all matches.

### Filter by score
**Args:** `exec_annotation -i proteins.faa -o filtered.tsv --score 50`
**Explanation:** Only reports annotations above score threshold.

### Export pathway results
**Args:** `exec_annotation -i proteins.faa -o results.tsv --pathway`
**Explanation:** Exports KEGG pathway mapping results.