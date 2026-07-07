---
name: fusioncatcher
category: expression
description: Finder of Somatic Fusion Genes in RNA-seq data.
tags: [fusioncatcher, gene fusion, RNA-seq, cancer genomics]
author: oxo-call-community
source_url: "https://github.com/ndaniel/fusioncatcher"
---

## Concepts
- **Fusion Gene Detection**: Identifies somatic fusion genes from RNA-seq data.
- **Somatic Analysis**: Focuses on cancer-related gene fusions.
- **RNA-seq Integration**: Analyzes RNA-seq data for fusion transcripts.
- **Database Integration**: Uses known fusion gene databases for annotation.
- **False Positive Filtering**: Filters likely false-positive fusion calls.

## Pitfalls
- **Computational Requirements**: High computational requirements for large datasets.
- **Memory Usage**: Requires significant memory for analysis.
- **Reference Genome**: Needs appropriate reference genome.
- **Time Consuming**: Analysis can take hours to complete.
- **False Positives**: May report false positive fusion events.

## Examples
### Run fusion detection
**Args:** `fusioncatcher -d /path/to/databases -i reads.fastq -o results/`
**Explanation:** Runs fusion gene detection on RNA-seq data.

### Paired-end reads
**Args:** `fusioncatcher -d /databases -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** Analyzes paired-end RNA-seq reads.

### With custom genome
**Args:** `fusioncatcher -d /databases -g custom_genome.fa -i reads.fastq -o results/`
**Explanation:** Uses custom reference genome.

### Quick mode
**Args:** `fusioncatcher -d /databases -i reads.fastq -o results/ --quick`
**Explanation:** Runs in quick mode for faster analysis.

### Filter by confidence
**Args:** `fusioncatcher -d /databases -i reads.fastq -o results/ -c high`
**Explanation:** Only reports high-confidence fusion calls.