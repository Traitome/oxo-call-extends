---
name: sketchy
category: variant-calling
description: Real-time lineage hashing and genotyping of bacterial pathogens
tags: [sketchy, variant-calling, bacterial-genomics, lineage-typing]
author: oxo-call-community
source_url: "https://github.com/esteinig/sketchy"
---

## Concepts

- **Tool Overview**: sketchy (v0.6.0) - A tool for real-time lineage hashing and genotyping of bacterial pathogens using MinHash-based methods
- **Core Function**: Uses MinHash sketching to rapidly compare bacterial genomes and determine genetic relatedness
- **Input/Output**: Accepts FASTA/FASTQ files; outputs lineage assignments and genotyping results
- **Algorithm**: Implements MinHash algorithm for efficient sequence comparison, similar to Mash and sourmash
- **Installation**: `conda install -c bioconda sketchy` or `pip install sketchy`
- **Key Feature**: Enables rapid identification of bacterial lineages from raw sequencing reads

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `sketchy --help`
- **Input Quality**: Requires high-quality sequencing data for accurate genotyping
- **Database Compatibility**: Must use compatible reference databases formatted for sketchy
- **Memory Usage**: Large datasets may require significant memory for sketch generation
- **k-mer Size Selection**: Default k-mer size (31) may need adjustment for specific applications
- **False Positives**: Low-coverage samples may produce incorrect lineage assignments

## Examples

### Display help
**Args:** `sketchy --help`
**Explanation:** Shows available options and usage information.

### Basic genotyping
**Args:** `sketchy -i input.fastq -r reference.fasta -o output.vcf`
**Explanation:** Perform genotyping with input reads and reference genome.

### Create sketch
**Args:** `sketchy sketch -i genome.fasta -o genome.sketch`
**Explanation:** Create a MinHash sketch from a genome sequence.

### Compare sketches
**Args:** `sketchy compare -a genome1.sketch -b genome2.sketch`
**Explanation:** Compare two genome sketches to estimate similarity.

### Batch processing
**Args:** `sketchy batch -d genomes/ -o results/`
**Explanation:** Process multiple genomes in batch mode.

### With custom k-mer size
**Args:** `sketchy -k 21 -i input.fastq -r reference.fasta -o output.vcf`
**Explanation:** Use k-mer size of 21 instead of default 31.

### Generate report
**Args:** `sketchy report -i input.fastq -r reference.fasta -o report.html`
**Explanation:** Generate an HTML report with genotyping results.