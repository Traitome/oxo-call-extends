---
name: staramr
category: annotation
description: Scan genome contigs against the ResFinder and PointFinder databases.
tags: [staramr, antibiotic-resistance, resfinder, pointfinder]
author: oxo-call-community
source_url: "https://github.com/phac-nml/staramr"
---

## Concepts

- **Tool Overview**: staramr (v0.12.1) is a tool for detecting antimicrobial resistance genes from bacterial genome sequences.
- **Core Function**: Scans genome contigs against ResFinder and PointFinder databases to identify resistance genes and mutations.
- **Algorithm**: Uses BLAST-based approach for gene detection with percent identity and coverage thresholds.
- **Input/Output**: Input: FASTA genome assembly or contigs; Output: Resistance gene report with gene names and phenotypes.
- **Databases**: Integrates ResFinder (acquired resistance genes) and PointFinder (point mutations).
- **Installation**: `conda install -c bioconda staramr` or download from GitHub.

## Pitfalls

- **Assembly Quality**: Poor assembly affects resistance gene detection.
- **Database Updates**: Outdated databases may miss newly discovered resistance genes.
- **False Positives**: Highly conserved genes may produce false positive matches.
- **Coverage Threshold**: Incorrect threshold settings affect sensitivity/specificity.
- **Memory Requirements**: Large databases require significant memory for scanning.
- **Mixed Results**: Multiple resistance determinants may complicate interpretation.

## Examples

### Display help
**Args:** `staramr --help`
**Explanation:** Shows available options and usage information.

### Basic resistance scanning
**Args:** `staramr search -i genome.fasta -o results/`
**Explanation:** Scan genome for antimicrobial resistance genes.

### With PointFinder
**Args:** `staramr search -i genome.fasta -o results/ --pointfinder`
**Explanation:** Include point mutation detection from PointFinder.

### Custom database
**Args:** `staramr search -i genome.fasta -o results/ -d custom_db/`
**Explanation:** Use custom resistance gene database.

### Threshold settings
**Args:** `staramr search -i genome.fasta -o results/ --identity 90 --coverage 80`
**Explanation:** Set minimum identity (90%) and coverage (80%) thresholds.

### Output format
**Args:** `staramr search -i genome.fasta -o results/ --format csv`
**Explanation:** Output results in CSV format.

### Verbose mode
**Args:** `staramr search -i genome.fasta -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Batch processing
**Args:** `staramr search -i batch/ -o results/`
**Explanation:** Process multiple genomes in batch mode.

### Update databases
**Args:** `staramr update`
**Explanation:** Update ResFinder and PointFinder databases.
