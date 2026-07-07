---
name: tango
category: metagenomics
description: Assigns taxonomy to metagenomic contigs.
tags: [tango, metagenomics, taxonomy, contigs]
author: oxo-call-community
source_url: "https://github.com/johnne/tango"
---

## Concepts

- **Tool Overview**: tango (v0.5.7) assigns taxonomy to metagenomic contigs.
- **Core Function**: Taxonomic classification of metagenomic sequences.
- **Algorithm**: Uses k-mer based classification for taxonomy assignment.
- **Input/Output**: Input: FASTA contigs; Output: Taxonomic assignments.
- **Applications**: Metagenomics analysis, microbiome studies, taxonomic profiling.
- **Installation**: `conda install -c bioconda tango` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large databases require significant memory.
- **Database Quality**: Depends on reference database quality.
- **Contig Length**: Short contigs may be misclassified.
- **Computational Time**: Processing large datasets can be slow.
- **False Positives**: May assign incorrect taxonomy.
- **Database Updates**: Requires regular database updates.

## Examples

### Display help
**Args:** `tango --help`
**Explanation:** Shows available options and usage information.

### Basic taxonomy assignment
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.txt`
**Explanation:** Assign taxonomy to contigs.

### With confidence threshold
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.txt -c 0.8`
**Explanation:** Minimum confidence threshold of 0.8.

### Verbose mode
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.txt --stats`
**Explanation:** Generate statistics about classification.

### Batch processing
**Args:** `for f in contigs/*.fasta; do tango -i $f -d database/ -o results/${f%.fasta}_taxonomy.txt; done`
**Explanation:** Process multiple contig files.

### Include lineage
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.txt --lineage`
**Explanation:** Include full taxonomic lineage.

### Output in CSV format
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.csv -f csv`
**Explanation:** Output in CSV format.

### Generate report
**Args:** `tango -i contigs.fasta -d database/ -o taxonomy.txt --report`
**Explanation:** Generate comprehensive classification report.
