---
name: scalop
category: annotation
description: SCALOP - Sequence-based antibody Canonical LOoP structure annotation
tags: ["scalop", "annotation", "antibody", "protein-structure"]
author: oxo-call-community
source_url: "https://github.com/oxpig/SCALOP"
---

## Concepts

- **Tool Overview**: SCALOP (v2021.01.27) is a sequence-based tool for annotating antibody Canonical Loop structures.
- **Core Function**: Identifies and annotates canonical loop conformations in antibody variable regions.
- **Algorithm**: Uses sequence patterns and machine learning to predict canonical loop structures.
- **Input/Output**: Accepts antibody sequence files and produces structural annotations.
- **Canonical Loops**: Focuses on CDR (Complementarity-Determining Region) loop conformations.
- **Applications**: Antibody structure prediction, antibody engineering, and immunoinformatics.

## Pitfalls

- **Antibody Specific**: Designed specifically for antibody sequences.
- **Sequence Quality**: Results depend on input sequence quality.
- **Limited Scope**: Focuses only on canonical loop structures.
- **Database Dependencies**: Requires reference databases for comparison.
- **Computational Resources**: May require significant compute resources for large datasets.
- **Parameter Tuning**: Requires careful adjustment of prediction parameters.

## Examples

### Basic annotation
**Args:** `scalop -i antibody.fasta -o annotations.txt`
**Explanation:** `-i` input antibody sequences; `-o` output annotations.

### With PDB comparison
**Args:** `scalop -i antibody.fasta -p pdb_structures/ -o annotations.txt`
**Explanation:** `-p` directory with PDB structures for comparison.

### Detailed output
**Args:** `scalop -i antibody.fasta -o annotations.txt -d`
**Explanation:** `-d` generates detailed annotation report.

### Multiple sequences
**Args:** `scalop -i antibodies.fasta -o annotations.txt`
**Explanation:** Processes multiple antibody sequences from single file.

### Verbose logging
**Args:** `scalop -i antibody.fasta -o annotations.txt -v`
**Explanation:** `-v` enables verbose output for debugging.

### Output JSON
**Args:** `scalop -i antibody.fasta -o annotations.json -f json`
**Explanation:** `-f json` outputs in JSON format.

### Custom database
**Args:** `scalop -i antibody.fasta -d custom_db/ -o annotations.txt`
**Explanation:** `-d` specifies custom reference database.