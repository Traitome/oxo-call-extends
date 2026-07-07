---
name: tbox-scan
category: annotation
description: Tool for scanning and annotating transcription factor binding boxes in genomic sequences.
tags: [tbox-scan, transcription-factor, binding-site, annotation, motif-discovery, regulatory-elements]
author: oxo-call-community
source_url: "https://github.com/compbio/tbox-scan"
---

## Concepts

- **Tool Overview**: tbox-scan - A tool for scanning genomic sequences to identify and annotate transcription factor binding boxes (T-boxes) and related regulatory elements.
- **Core Function**: Searches DNA sequences for T-box binding motifs and provides positional information and annotation.
- **Input**: DNA sequences in FASTA format, with optional reference genome for context.
- **Output**: List of identified binding sites with coordinates, scores, and sequence context.
- **Installation**: `pip install tbox-scan` or `conda install -c bioconda tbox-scan`
- **Use Case**: Identifying T-box regulated genes in bacterial genomes, particularly useful for Gram-positive bacteria like Bacillus and Streptococcus.

## Pitfalls

- **Motif Specificity**: T-boxes have specific sequence requirements - scan sensitivity depends on motif database completeness.
- **Genome Version**: Results may vary depending on reference genome version used.
- **Multiple Hits**: Genes may have multiple T-boxes - interpret results in regulatory context.

## Examples

### Scan sequence for T-boxes
**Args:** `tbox-scan -i genome.fasta -o results.gff`
**Explanation:** Scan FASTA sequences and output results in GFF3 format.

### With scoring threshold
**Args:** `tbox-scan -i sequences.fasta -o hits.txt -t 0.8`
**Explanation:** Use threshold of 0.8 for binding site scoring to filter low-confidence hits.

### Verbose output
**Args:** `tbox-scan -i genome.fasta --verbose -o results.txt`
**Explanation:** Enable verbose logging showing scanning progress and detailed hit information.
