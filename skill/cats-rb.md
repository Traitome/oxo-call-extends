---
name: cats-rb
category: transcriptomics
description: Reference-based transcriptome assembly quality assessment tool
tags: [cats-rb, transcriptome, assembly, quality-control, rna-seq]
author: oxo-call-community
source_url: "https://github.com/bodulic/CATS-rb/blob/main/README.md"
---

## Concepts

- **Tool Overview**: CATS-rb evaluates transcriptome assembly quality using a reference genome.
- **Core Function**: Assesses completeness and accuracy of transcriptome assemblies.
- **Algorithm**: Compares assembled transcripts against reference genome annotations.
- **Input**: Assembled transcriptome FASTA and reference genome/GFF.
- **Output**: Quality metrics including sensitivity, precision, and completeness.
- **Application**: Evaluating de novo transcriptome assemblies from RNA-seq data.
- **Installation**: Install via bioconda: `conda install -c bioconda cats-rb`

## Pitfalls

- **Reference Required**: Needs corresponding species reference genome.
- **Annotation Quality**: Results depend on reference annotation quality.
- **Assembly Format**: Requires properly formatted FASTA assembly.
- **Memory Usage**: Large genomes may require significant memory.

## Examples

### Assess assembly quality
**Args:** `cats-rb -a assembly.fasta -r reference.fa -g annotation.gff -o results/`
**Explanation:** Evaluates transcriptome assembly quality using reference genome.

### Generate report
**Args:** `cats-rb -a assembly.fasta -r reference.fa -o report.txt --report`
**Explanation:** Generates detailed quality assessment report.

### Display help
**Args:** `cats-rb --help`
**Explanation:** Shows all available options and usage information.