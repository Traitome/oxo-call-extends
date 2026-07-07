---
name: tcfinder
category: annotation
description: TC-Finder - Tool for identifying transcription factor binding sites and regulatory elements.
tags: [tcfinder, transcription-factor, binding-site, regulatory-elements, motif-discovery, annotation]
author: oxo-call-community
source_url: "https://github.com/compbio/tcfinder"
---

## Concepts

- **Tool Overview**: TC-Finder - A tool for identifying transcription factor binding sites and regulatory elements in genomic sequences.
- **Core Function**: Scans DNA sequences for transcription factor binding motifs and provides positional and scoring information.
- **Input**: Genomic DNA sequences in FASTA format.
- **Output**: List of identified binding sites with coordinates, motif names, and confidence scores.
- **Installation**: `pip install tcfinder` or `conda install -c bioconda tcfinder`
- **Use Case**: Identifying TF binding sites in bacterial genomes for regulatory network analysis.

## Pitfalls

- **Motif Database**: Detection accuracy depends on the quality and completeness of the transcription factor motif database.
- **Sequence Complexity**: Highly complex regions may produce false positives.
- **Score Threshold**: Adjustable threshold affects sensitivity vs specificity trade-off.

## Examples

### Scan genome for TF binding sites
**Args:** `tcfinder -i genome.fasta -o binding_sites.gff`
**Explanation:** Identify transcription factor binding sites and output in GFF format.

### Adjust detection threshold
**Args:** `tcfinder -i sequence.fasta -o results.txt -s 0.85`
**Explanation:** Use higher score threshold (0.85) to filter low-confidence predictions.

### Verbose output
**Args:** `tcfinder -i genome.fasta --verbose -o detailed.txt`
**Explanation:** Enable detailed logging of scanning process and motif matching statistics.
