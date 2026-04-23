---
name: carnac-lr
category: expression
description: Clustering coefficient-based Acquisition of RNA Communities in Long Read data
tags: [carnac, long-read, rna, clustering, transcript]
author: oxo-call-community
source_url: "https://github.com/kamimrcht/CARNAC-LR"
---

## Concepts

- **Tool Overview**: CARNAC-LR clusters long reads from RNA sequencing into transcript communities.
- **Core Function**: Groups long reads originating from the same transcript or gene.
- **Algorithm**: Uses clustering coefficient on read overlap graphs.
- **Input**: Long reads in FASTA/FASTQ format.
- **Output**: Clustered read groups representing transcripts.
- **Application**: Transcript discovery from long-read RNA-seq.
- **Installation**: Install via bioconda: `conda install -c bioconda carnac-lr`

## Pitfalls

- **Long Reads**: Designed for PacBio/ONT long reads only.
- **Overlap Step**: Requires computing read overlaps first.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Cluster long RNA reads
**Args:** `CARNAC-LR -i reads.fa -o clusters.tsv`
**Explanation:** Clusters long RNA reads into transcript communities.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
