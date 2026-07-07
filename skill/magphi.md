---
name: magphi
category: formatting
description: A bioinformatics tool allowing for examination and extraction of genomic features using seed sequences.
tags: [magphi, formatting, genomic-features, extraction]
author: oxo-call-community
source_url: "https://github.com/milnus/Magphi"
---

## Concepts

- **Tool Overview**: magphi v2.0.2 - A bioinformatics tool for examining and extracting genomic features using seed sequences as anchors.
- **Core Function**: Identifies and extracts genomic regions of interest using seed sequences to locate specific features.
- **Input/Output**: Input: Genomic sequences (FASTA), seed sequences; Output: Extracted features, annotations, reports.
- **Installation**: `conda install -c bioconda magphi`
- **Seed-based Extraction**: Uses seed sequences to anchor and extract target genomic regions.
- **Feature Identification**: Supports identification of various genomic features like CRISPR arrays, repeats, and specific gene clusters.

## Pitfalls

- **Seed Sequence Quality**: Poor quality seed sequences lead to false positives.
- **Genome Complexity**: Repetitive regions may cause multiple hits.
- **Parameter Tuning**: Incorrect sensitivity thresholds affect results.
- **Memory Usage**: Large genomes require significant memory.
- **Output Format**: Multiple output formats require careful handling.
- **Annotation Dependencies**: Requires proper genome annotation for full functionality.

## Examples

### Extract features using seed
**Args:** `magphi extract -g genome.fasta -s seed.fasta -o output.gff`
**Explanation:** Extracts genomic features using seed sequences.

### Identify CRISPR arrays
**Args:** `magphi crispr -g genome.fasta -o crispr_results.txt`
**Explanation:** Identifies CRISPR arrays in the genome.

### With custom parameters
**Args:** `magphi extract -g genome.fasta -s seed.fasta -o output.gff -e 0.1`
**Explanation:** Sets e-value threshold to 0.1 for more sensitive search.

### Batch processing
**Args:** `magphi batch -i genomes/ -s seed.fasta -o results/`
**Explanation:** Processes multiple genomes in batch mode.

### Verbose mode
**Args:** `magphi extract -g genome.fasta -s seed.fasta -o output.gff -v`
**Explanation:** Provides detailed logging during extraction.

### Generate visualization
**Args:** `magphi plot -i output.gff -g genome.fasta -o plot.pdf`
**Explanation:** Creates visualization of extracted features.