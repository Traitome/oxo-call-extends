---
name: taseq
category: amplicon-sequencing
description: Downstream analysis for targeted amplicon sequencing.
tags: [taseq, amplicon-sequencing, microbiome, metabarcoding]
author: oxo-call-community
source_url: "https://github.com/KChigira/taseq/"
---

## Concepts

- **Tool Overview**: taseq (v1.1.1) performs downstream analysis for amplicon sequencing.
- **Core Function**: Analyzes amplicon sequencing data for microbial profiling.
- **Algorithm**: Uses sequence clustering and taxonomic assignment.
- **Input/Output**: Input: FASTQ reads; Output: Taxonomic profiles.
- **Applications**: Microbiome analysis, metabarcoding, environmental studies.
- **Installation**: `conda install -c bioconda taseq` or download from GitHub.

## Pitfalls

- **Primer Handling**: Requires proper primer removal.
- **Sequence Quality**: Poor quality affects analysis.
- **Chimera Detection**: May produce chimeric sequences.
- **Clustering Threshold**: Incorrect thresholds affect OTU/ASV calling.
- **Database Coverage**: Limited by reference database.
- **Contamination**: Environmental contamination affects results.

## Examples

### Display help
**Args:** `taseq --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `taseq -i reads.fastq -o results/`
**Explanation:** Analyze amplicon sequencing data.

### With reference database
**Args:** `taseq -i reads.fastq -d silva_db/ -o results/`
**Explanation:** Use reference database for classification.

### Verbose mode
**Args:** `taseq -i reads.fastq -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `taseq -i reads.fastq -o results/ --stats`
**Explanation:** Generate statistics about analysis.

### Batch processing
**Args:** `for f in fastq/*.fastq; do taseq -i $f -o results/${f%.fastq}_out/; done`
**Explanation:** Process multiple FASTQ files.

### Filter by abundance
**Args:** `taseq -i reads.fastq -o results/ -a 0.001`
**Explanation:** Filter by minimum abundance threshold.

### Generate report
**Args:** `taseq -i reads.fastq -o results/ --report`
**Explanation:** Generate comprehensive analysis report.

### Export to BIOM
**Args:** `taseq -i reads.fastq -o results/ -f biom`
**Explanation:** Export results in BIOM format.
