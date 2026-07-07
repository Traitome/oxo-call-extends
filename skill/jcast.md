---
name: jcast
category: formatting
description: Jcast retrieves splice junction information and translates into amino acids.
tags: [jcast, formatting, splice-junction, translation, RNA-seq]
author: oxo-call-community
source_url: "https://github.com/ed-lau/jcast"
---

## Concepts

- **Tool Overview**: jcast (v0.3.5) - A tool for analyzing splice junctions and translating them into amino acid sequences.
- **Splice Junction Analysis**: Extracts splice junction information from RNA-Seq data.
- **Amino Acid Translation**: Translates spliced sequences into amino acids.
- **ORF Prediction**: Identifies open reading frames in spliced transcripts.
- **Alternative Splicing**: Analyzes alternative splicing events.
- **Integration**: Works with existing RNA-Seq analysis workflows.

## Pitfalls

- **Ambiguous Junctions**: Some splice junctions may be ambiguous.
- **Frame Shifts**: Incorrect splicing can cause frame shifts.
- **Reference Genome**: Requires accurate reference genome annotation.
- **Low Coverage**: Low coverage regions may miss splice junctions.
- **Novel Junctions**: Novel splice junctions may not be annotated.
- **Multiple Isoforms**: Multiple transcript isoforms complicate analysis.

## Examples

### Analyze splice junctions
**Args:** `jcast -i junctions.bed -g ref.gtf -o results/`
**Explanation:** Analyzes splice junctions and translates to amino acids.

### Include novel junctions
**Args:** `jcast -i junctions.bed -g ref.gtf -o results/ --include-novel`
**Explanation:** Includes novel splice junctions in analysis.

### Specify output format
**Args:** `jcast -i junctions.bed -g ref.gtf -o results/ --format fasta`
**Explanation:** Outputs translated sequences in FASTA format.

### Filter by coverage
**Args:** `jcast -i junctions.bed -g ref.gtf -o results/ --min-cov 5`
**Explanation:** Filters junctions with minimum coverage of 5.

### Predict ORFs
**Args:** `jcast -i junctions.bed -g ref.gtf -o results/ --predict-orfs`
**Explanation:** Predicts open reading frames from spliced sequences.

### Generate report
**Args:** `jcast -i junctions.bed -g ref.gtf -o results/ --report`
**Explanation:** Generates detailed analysis report.