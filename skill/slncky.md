---
name: slncky
category: rna-analysis
description: slncky is a tool for lncRNA discovery from RNA-Seq data that filters high-quality noncoding transcripts, discovers lncRNA orthologs, and characterizes conserved lncRNA evolution
tags: [slncky, rna-analysis, lncrna, rna-seq, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/slncky/slncky"
---

## Concepts

- **Tool Overview**: slncky (v1.0.4) - A computational pipeline for lncRNA discovery from RNA-Seq data
- **Core Function**: Identifies and characterizes long non-coding RNAs from transcriptome data
- **Input/Output**: Accepts assembled transcripts (FASTA/GFF); outputs lncRNA annotations and orthologs
- **Algorithm**: Combines coding potential prediction with evolutionary conservation analysis
- **Installation**: `conda install -c bioconda slncky`
- **Key Features**: Discovers lncRNA orthologs, characterizes conserved evolution, filters high-quality transcripts

## Pitfalls

- **Assembly Quality**: Requires high-quality transcript assemblies
- **Reference Genome**: Needs well-annotated reference genome
- **Memory Requirements**: Large datasets may require significant memory
- **Computation Time**: Ortholog detection can be computationally intensive
- **Annotation Dependencies**: Requires external annotation files
- **Species Limitations**: Best suited for well-studied species with reference genomes

## Examples

### Display help
**Args:** `slncky --help`
**Explanation:** Shows available options and usage information.

### Basic lncRNA discovery
**Args:** `slncky discover -i transcripts.fasta -g genome.fa -o lncrna_results/`
**Explanation:** Discover lncRNAs from assembled transcripts.

### With annotation file
**Args:** `slncky discover -i transcripts.fasta -g genome.fa -a annotations.gff -o results/`
**Explanation:** Use existing annotations to improve lncRNA identification.

### Find orthologs
**Args:** `slncky orthologs -i lncrnas.fasta -d reference_species/ -o orthologs.txt`
**Explanation:** Discover lncRNA orthologs across species.

### Characterize conservation
**Args:** `slncky conservation -i lncrnas.fasta -o conservation_stats.txt`
**Explanation:** Analyze evolutionary conservation of lncRNAs.

### Filter by length
**Args:** `slncky filter -i transcripts.fasta -m 200 -o filtered.fasta`
**Explanation:** Filter transcripts by minimum length (200bp).

### Batch processing
**Args:** `slncky batch -i samples/ -g genome.fa -o batch_results/`
**Explanation:** Process multiple samples in batch mode.