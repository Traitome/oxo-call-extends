---
name: tn3_ta_finder
category: analysis
description: TN3-TA-Finder - Tool for finding Tn3 transposon insertion sites.
tags: [tn3_ta_finder, transposon, insertion-site, tn3, genetic-analysis]
author: oxo-call-community
source_url: "https://github.com/compbio/tn3_ta_finder"
---

## Concepts

- **Tool Overview**: TN3-TA-Finder - A tool for identifying Tn3 transposon insertion sites in sequencing data.
- **Core Function**: Detects transposon insertion sites by analyzing target site duplications (TSD).
- **Input**: Sequencing reads (FASTQ), transposon sequence, reference genome (optional).
- **Output**: Insertion site coordinates, TSD sequences, flanking sequences.
- **Installation**: `pip install tn3-ta-finder` or `conda install -c bioconda tn3-ta-finder`
- **Use Case**: Transposon mutagenesis analysis, genetic screening, insertion mapping.

## Pitfalls

- **TSD Size**: Tn3 typically creates 5-bp TSD, but variations may occur.
- **Reads Quality**: Requires good quality sequencing reads for accurate detection.

## Examples

### Find insertion sites
**Args:** `tn3-ta-finder -i reads.fastq -t transposon.fasta -o insertions/`
**Explanation:** Identify Tn3 transposon insertion sites from sequencing data.

### With reference
**Args:** `tn3-ta-finder -i reads.fastq -t tn3.fasta -r genome.fasta -o mapped_insertions/`
**Explanation:** Map insertion sites to reference genome.
