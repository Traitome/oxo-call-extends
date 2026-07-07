---
name: contigtax
category: assembly
description: Assign taxonomy to metagenomic contigs
tags: [contigtax, taxonomy, metagenomics, contigs, classification]
author: oxo-call-community
source_url: "https://github.com/NBISweden/contigtax"
---

## Concepts

- **Tool Overview**: ContigTax is a tool for assigning taxonomy to metagenomic contigs, previously known as Tango. It uses sequence composition and alignment information for taxonomic classification.
- **Core Function**: Classifies metagenomic contigs into taxonomic groups using k-mer frequencies and optional alignment data.
- **Algorithm**: Combines k-mer based classification with alignment-based methods for improved accuracy.
- **Input**: Metagenomic contigs in FASTA format, optionally aligned reads.
- **Output**: Taxonomic assignments for each contig with confidence scores.
- **Application**: Metagenome binning, taxonomic profiling, and genome-resolved metagenomics.
- **Installation**: Install via bioconda: `conda install -c bioconda contigtax`

## Pitfalls

- **Reference Database**: Classification accuracy depends on database completeness.
- **Contig Length**: Short contigs may produce unreliable classifications.
- **Compositional Bias**: GC content bias may affect classification.
- **Horizontal Gene Transfer**: HGT regions may be misclassified.
- **Novel Taxa**: Novel organisms may be classified at higher taxonomic levels.

## Examples

### Assign taxonomy to contigs
**Args:** `contigtax -i contigs.fasta -o taxonomy.txt`
**Explanation:** Assigns taxonomy to metagenomic contigs.

### With alignment information
**Args:** `contigtax -i contigs.fasta -a alignments.bam -o taxonomy.txt`
**Explanation:** Uses alignment information to improve classification.

### With custom database
**Args:** `contigtax -i contigs.fasta -d custom_db/ -o taxonomy.txt`
**Explanation:** Uses custom reference database for classification.

### Display help
**Args:** `contigtax --help`
**Explanation:** Shows all available options and usage information.