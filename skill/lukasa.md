---
name: lukasa
category: alignment
description: Fast and accurate mapping of proteins against eukaryotic genomes
tags: [lukasa, alignment, protein-mapping, genome-annotation]
author: oxo-call-community
source_url: "https://github.com/pvanheus/lukasa"
---

## Concepts

- **Tool Overview**: lukasa v0.15.0 combines MetaEUK and spaln to rapidly identify matches between proteins and genomic contigs.
- **Core Function**: Maps proteins to eukaryotic genomes for annotation purposes.
- **Hybrid Approach**: First uses MetaEUK for rapid identification, then spaln for accurate mapping.
- **Input/Output**: Input: Protein sequences (FASTA), genome assembly (FASTA); Output: GFF3 annotation file.
- **Installation**: `conda install -c bioconda lukasa`
- **Key Features**: Fast and accurate, outputs standard GFF3 format, suitable for genome annotation pipelines.

## Pitfalls

- **Genome Quality**: Requires high-quality genome assembly for accurate mapping.
- **Memory Usage**: May require significant memory for large genomes.
- **Dependency**: Requires both MetaEUK and spaln to be installed.
- **Protein Database**: Performance depends on the quality of the input protein sequences.
- **Computation Time**: Processing large genomes can be time-consuming.
- **Parameter Tuning**: May require adjustment for different organism types.

## Examples

### Map proteins to genome
**Args:** `lukasa proteins.fasta genome.fasta -o annotations.gff3`
**Explanation:** Maps proteins to genome and outputs annotations.

### Threads
**Args:** `lukasa proteins.fasta genome.fasta -t 16 -o annotations.gff3`
**Explanation:** Uses 16 threads for parallel processing.

### Output directory
**Args:** `lukasa proteins.fasta genome.fasta -d results/ -o annotations.gff3`
**Explanation:** Saves intermediate files to results directory.

### Verbose mode
**Args:** `lukasa proteins.fasta genome.fasta -v -o annotations.gff3`
**Explanation:** Outputs detailed progress information.

### Minimum identity
**Args:** `lukasa proteins.fasta genome.fasta -i 0.8 -o annotations.gff3`
**Explanation:** Sets minimum sequence identity to 80%.

### Help documentation
**Args:** `lukasa --help`
**Explanation:** Displays all available options and parameters.