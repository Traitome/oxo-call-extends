---
name: coconet-binning
category: assembly
description: A contig binning tool from viral metagenomes
tags: [coconet-binning, contig-binning, viral-metagenomics, bioinformatics, metagenomics]
author: oxo-call-community
source_url: "https://coconet.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: CoCoNet is a contig binning tool specifically designed for viral metagenomics, grouping contigs into putative viral genomes.
- **Core Function**: Bins contigs from viral metagenomes into taxonomically related groups using sequence composition and coverage information.
- **Algorithm**: Uses graph-based clustering and machine learning to group contigs into viral bins.
- **Input**: Assembled contigs in FASTA format with coverage information.
- **Output**: Binned contigs grouped by predicted viral genome.
- **Application**: Viral metagenomics, virus discovery, and viral community analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda coconet-binning`

## Pitfalls

- **Contig Quality**: Requires high-quality assembled contigs.
- **Coverage Data**: Needs coverage information for accurate binning.
- **Memory Usage**: May require significant memory for large datasets.
- **Complex Communities**: May struggle with highly diverse viral communities.
- **Bin Quality**: Results depend on input data quality and sequencing depth.

## Examples

### Run binning on contigs
**Args:** `coconet -i contigs.fasta -c coverage.txt -o bins/`
**Explanation:** Bins contigs into viral genomes using coverage information.

### With abundance matrix
**Args:** `coconet -i contigs.fasta -a abundance.tsv -o bins/`
**Explanation:** Uses abundance matrix for binning.

### With custom k-mer size
**Args:** `coconet -i contigs.fasta -c coverage.txt -k 6 -o bins/`
**Explanation:** Uses 6-mers for sequence composition analysis.

### Display help
**Args:** `coconet --help`
**Explanation:** Shows all available options and usage information.