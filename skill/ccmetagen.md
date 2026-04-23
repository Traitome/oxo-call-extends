---
name: ccmetagen
category: metagenomics
description: Comprehensive and accurate identification of eukaryotes and prokaryotes in metagenomic data
tags: [ccmetagen, taxonomy, metagenomics, classification]
author: oxo-call-community
source_url: "https://github.com/vrmarcelino/CCMetagen"
---

## Concepts

- **Tool Overview**: CCMetagen identifies eukaryotes and prokaryotes in metagenomic data.
- **Core Function**: Taxonomic classification of metagenomic reads or contigs.
- **Algorithm**: Uses k-mer matching with KMA or other aligners.
- **Input**: FASTQ reads or FASTA contigs and reference database.
- **Output**: Taxonomic profile with abundance estimates.
- **Features**: Supports both eukaryotic and prokaryotic classification.
- **Installation**: Install via bioconda: `conda install -c bioconda ccmetagen`

## Pitfalls

- **Database Required**: Requires KMA-indexed reference database.
- **Memory Usage**: Large databases require significant memory.
- **Eukaryotic Complexity**: Eukaryotic classification more challenging than prokaryotic.
- **Read Length**: Works best with reads >50bp.

## Examples

### Classify metagenomic reads
**Args:** `CCMetagen.py -i reads.fq -db kma_db -o classification.tsv`
**Explanation:** Classifies metagenomic reads using KMA database.

### Classify contigs
**Args:** `CCMetagen.py -i contigs.fa -db kma_db -o contig_classification.tsv`
**Explanation:** Classifies assembled contigs taxonomically.

### Display help
**Args:** `CCMetagen.py --help`
**Explanation:** Shows all available options and usage information.
