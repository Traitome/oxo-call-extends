---
name: deepacvir
category: qc
description: DeePaC-Vir - detecting novel human viruses from DNA reads using reverse-complement neural networks.
tags: [deepacvir, qc, virus-detection, deep-learning, metagenomics]
author: oxo-call-community
source_url: "https://rki_bioinformatics.gitlab.io/DeePaC/"
---

## Concepts

- **Tool Overview**: deepacvir (v0.2.2+) is a deep learning-based tool for detecting novel human viruses from DNA sequencing reads. It uses reverse-complement neural networks to improve detection accuracy.
- **Core Function**: Identifies viral sequences in metagenomic or clinical sequencing data, enabling detection of known and novel viruses.
- **Input/Output**: Input: Sequencing reads (FASTQ), assembled contigs (FASTA). Output: Viral sequence predictions, taxonomy classification, abundance estimates.
- **Algorithm**: Uses CNNs with reverse-complement awareness to capture both strands of DNA, improving detection of viral sequences.
- **Key Features**: Reverse-complement processing, novel virus detection, taxonomy classification, supports metagenomics, high sensitivity.
- **Installation**: `conda install -c bioconda deepacvir`

## Pitfalls

- **Host DNA Contamination**: High host DNA content reduces sensitivity.
- **Virus Abundance**: Low-abundance viruses may be missed.
- **Novel Viruses**: Detection of completely novel viruses may be limited.
- **Assembly Quality**: Contig-based detection depends on assembly quality.
- **Computational Resources**: Requires significant computational resources for large datasets.

## Examples

### Detect viruses from reads
**Args:** `deepacvir -i reads.fastq -o virus_detection.txt`
**Explanation:** Detect viral sequences from raw sequencing reads.

### From assembled contigs
**Args:** `deepacvir -i contigs.fasta -o virus_detection.txt`
**Explanation:** Analyze assembled contigs for viral sequences.

### With taxonomy output
**Args:** `deepacvir -i reads.fastq -o virus_detection.txt --taxonomy`
**Explanation:** Include taxonomy classification in output.