---
name: mview
category: formatting
description: MView extracts and reformats the results of a sequence database search or multiple alignment.
tags: [mview, formatting, alignment, blast, html, visualization]
author: oxo-call-community
source_url: "https://desmid.github.io/mview"
---

## Concepts

- **Tool Overview**: MView v1.68 - extracts and reformats sequence database search results or multiple alignments.
- **Core Function**: Converts BLAST/FASTA search results or multiple alignments into formatted HTML, FASTA, CLUSTAL, MSF, PIR, or RDB output.
- **Input/Output**: Takes BLAST, FASTA search results or CLUSTAL/HSSP/MSF/FASTA/PIR/MAF alignments; outputs HTML, FASTA, CLUSTAL, MSF, PIR, or RDB.
- **Installation**: `conda install -c bioconda mview`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports BLAST, FASTA suites, CLUSTAL, HSSP, MSF, FASTA, PIR, MAF input formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Convert BLAST to HTML
**Args:** `-in blast_results.xml -html on -out output.html`
**Explanation:** Converts BLAST XML results to formatted HTML.

### Convert alignment to FASTA
**Args:** `-in alignment.clustal -out output.fasta`
**Explanation:** Converts a CLUSTAL alignment to FASTA format.
