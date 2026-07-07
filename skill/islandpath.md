---
name: islandpath
category: comparative-genomics
description: IslandPath-DIMOB for predicting genomic islands in bacterial and archaeal genomes
tags: [islandpath, genomic-islands, horizontal-gene-transfer, prokaryotes]
author: oxo-call-community
source_url: "http://www.pathogenomics.sfu.ca/islandpath/"
---

## Concepts

- **Tool Overview**: IslandPath-DIMOB (v1.0.6) - Standalone software for predicting genomic islands (GIs) in prokaryotic genomes
- **Detection Methods**: Combines dinucleotide composition bias analysis with mobility gene identification
- **Genomic Islands**: Large genomic regions (>8kb) of probable horizontal origin, often encoding virulence or antibiotic resistance genes
- **DIMOB Algorithm**: Dinucleotide-based method using Pfam profiles for mobility gene detection
- **High Accuracy**: Among the most accurate GI prediction methods with high recall and precision
- **Output Formats**: Generates detailed reports including GI coordinates and characteristics

## Pitfalls

- **False Positives**: May identify regions with atypical composition that are not true GIs
- **GC Content Bias**: Less effective for genomes with extreme GC content
- **Short Islands**: May miss small genomic islands (<8kb)
- **Assembly Quality**: Requires complete or well-assembled genomes
- **Reference Dependence**: Performance varies based on database of mobility genes
- **Computational Time**: Analysis of large genomes can be time-consuming

## Examples

### Basic GI prediction
**Args:** `islandpath -i genome.fasta -o gi_results.txt`
**Explanation:** Predicts genomic islands in a bacterial or archaeal genome.

### With custom parameters
**Args:** `islandpath -i assembly.fasta -o results.txt -w 1000 -s 0.8`
**Explanation:** Uses window size of 1000bp and score threshold of 0.8 for GI detection.

### Output GFF format
**Args:** `islandpath -i genome.fasta -o gi_annotations.gff --gff`
**Explanation:** Generates GFF annotation file for visualization in IGV or other genome browsers.

### Detailed analysis
**Args:** `islandpath -i genome.fasta -o detailed_results.txt --verbose`
**Explanation:** Provides detailed analysis including dinucleotide bias scores and mobility gene hits.

### Batch processing
**Args:** `islandpath --batch genomes_list.txt --output-dir ./gi_results/`
**Explanation:** Processes multiple genomes listed in genomes_list.txt.

### Compare with IslandViewer
**Args:** `islandpath -i genome.fasta -o results.txt --compare islandviewer_output.gff`
**Explanation:** Compares predictions with IslandViewer results for validation.