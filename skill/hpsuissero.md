---
name: hpsuissero
category: classification
description: Rapid Haemophilus parasuis serotyping pipeline for Nanopore Data
tags: [hpsuissero, haemophilus, serotyping, nanopore, bacteria]
author: oxo-call-community
source_url: "https://github.com/jimmyliu1326/HpsuisSero"
---

## Concepts

- **Haemophilus parasuis Serotyping**: Specialized pipeline for rapid serotype prediction of Haemophilus parasuis from Nanopore sequencing data
- **Nanopore Data Support**: Optimized for Oxford Nanopore long-read sequencing data
- **Glässer's Disease**: Targets the causative agent of Glässer's disease in swine
- **15 Serotypes**: Capable of identifying all 15 known H. parasuis serotypes plus non-typable strains
- **Assembly-Based**: Works with complete or draft genome assemblies
- **Rapid Analysis**: Designed for fast turnaround in diagnostic settings

## Pitfalls

- **Sequence Quality**: Nanopore basecalling accuracy affects serotyping results
- **Assembly Completeness**: Draft assemblies may miss key serotype-determining regions
- **Contamination**: Mixed cultures or environmental DNA can confound results
- **Reference Database**: Results depend on the quality and completeness of reference serotype sequences
- **Non-typable Strains**: A significant proportion of isolates remain non-typable
- **Low Coverage**: Insufficient sequencing depth may lead to incorrect calls

## Examples

### Basic serotyping
**Args:** `hpsuissero -i assembly.fasta -o serotype_result.txt`
**Explanation:** Determines the serotype of Haemophilus parasuis from a genome assembly.

### With quality filtering
**Args:** `hpsuissero -i assembly.fasta -o result.txt --quality-filter`
**Explanation:** Applies quality filtering to improve serotype prediction accuracy.

### Batch processing
**Args:** `hpsuissero --batch assemblies/ -o batch_results/`
**Explanation:** Processes multiple genome assemblies in batch mode.

### Generate detailed report
**Args:** `hpsuissero -i assembly.fasta -o result.txt --detailed`
**Explanation:** Generates a detailed report with confidence scores for each serotype prediction.

### Specify custom reference
**Args:** `hpsuissero -i assembly.fasta -o result.txt -r custom_ref.fasta`
**Explanation:** Uses a custom reference database for serotyping.