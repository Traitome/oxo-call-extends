---
name: snoscan
category: annotation
description: snoScan - Search for C/D box methylation guide snoRNA genes in genomic sequences
tags: [snoscan, annotation, snorna, methylation, non-coding-rna]
author: oxo-call-community
source_url: "http://cryptogenomicon.org/snoscan-and-squid-in-the-21st-century.html"
---

## Concepts

- **Tool Overview**: snoscan (v1.0) - A tool for discovering C/D box snoRNA genes
- **Core Function**: Searches genomic sequences for C/D box methylation guide snoRNAs
- **Input/Output**: Accepts genomic FASTA; outputs snoRNA predictions with annotations
- **Algorithm**: Uses sequence motifs and methylation target sites for detection
- **Installation**: `conda install -c bioconda snoscan`
- **Key Features**: C/D box detection, methylation guide identification, snoRNA annotation

## Pitfalls

- **Input Requirements**: Requires genomic sequence in FASTA format
- **Target Sites**: Requires known methylation target sites for accurate prediction
- **False Positives**: May produce false positives without proper filtering
- **Sequence Quality**: Low-quality sequences affect prediction accuracy
- **Annotation Files**: Requires proper annotation files for target sites
- **Computation Time**: Large genomes can be slow to process

## Examples

### Display help
**Args:** `snoscan --help`
**Explanation:** Shows available options and usage information.

### Basic snoRNA search
**Args:** `snoscan genome.fasta > snorna_predictions.txt`
**Explanation:** Search for C/D box snoRNAs in genome.

### With target sites
**Args:** `snoscan genome.fasta -t targets.txt > predictions.txt`
**Explanation:** Use methylation target sites for search.

### With output file
**Args:** `snoscan genome.fasta -o snorna_predictions.gff`
**Explanation:** Output predictions in GFF format.

### Set sensitivity
**Args:** `snoscan genome.fasta --sensitivity high > predictions.txt`
**Explanation:** Set search sensitivity level.

### Filter by score
**Args:** `snoscan genome.fasta --min-score 0.8 > predictions.txt`
**Explanation:** Filter predictions by minimum score.

### With annotation
**Args:** `snoscan genome.fasta -a annotations.gff > predictions.txt`
**Explanation:** Use existing annotations for validation.

### Output statistics
**Args:** `snoscan genome.fasta --stats > statistics.txt`
**Explanation:** Output search statistics.