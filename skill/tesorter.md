---
name: tesorter
category: annotation
description: TESorter - Transposable Element (TE) classifier based on protein domain analysis.
tags: [tesorter, transposable-element, classification, protein-domain, te-annotation, repeat]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/TESorter"
---

## Concepts

- **Tool Overview**: TESorter - A tool that classifies transposable elements by analyzing protein domains of TE-encoded proteins.
- **Core Function**: Identifies and classifies TEs into known families by screening TE protein sequences against protein domain databases (Pfam, REX).
- **Input**: TE sequences (DNA or protein) or genome assembly with TE candidates.
- **Output**: TE classification with family assignment, protein domain annotations, and visualization.
- **Installation**: `pip install tesorter` or `conda install -c bioconda tesorter`
- **Use Case**: TE annotation, studying TE diversity, evolutionary analysis of TE families.

## Pitfalls

- **Protein-coding TEs**: Only works for TEs with protein-coding capacity (Class I retrotransposons).
- **Database Coverage**: Classification depends on completeness of protein domain databases.

## Examples

### Classify TEs
**Args:** `tesorter -i te_sequences.fasta -o classification_results/`
**Explanation:** Classify transposable elements by protein domain analysis.

### From genome
**Args:** `tesorter -g genome.fasta -o te_analysis/`
**Explanation:** Identify and classify TEs directly from genome assembly.

### Generate report
**Args:** `tesorter -i te.fasta --report -o results/`
**Explanation:** Generate detailed classification report with statistics.
