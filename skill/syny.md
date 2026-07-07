---
name: syny
category: comparative-genomics
description: Genome collinearity inference tool for comparative genomics analysis.
tags: [syny, collinearity, comparative-genomics, synteny]
author: oxo-call-community
source_url: "https://github.com/PombertLab/SYNY"
---

## Concepts

- **Tool Overview**: syny (v1.3.2) identifies collinearity between genomes.
- **Core Function**: Detects syntenic regions between genome sequences.
- **Algorithm**: Uses alignment-based approach for collinearity detection.
- **Input/Output**: Input: Genome sequences; Output: Collinearity blocks.
- **Applications**: Comparative genomics, evolutionary analysis, genome rearrangement.
- **Installation**: `conda install -c bioconda syny` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Processing large genomes can be slow.
- **Parameter Tuning**: Incorrect parameters affect collinearity detection.
- **Genome Quality**: Requires high-quality genome assemblies.
- **Assembly Completeness**: Incomplete assemblies affect results.
- **Evolutionary Distance**: Very divergent genomes may be challenging.

## Examples

### Display help
**Args:** `syny --help`
**Explanation:** Shows available options and usage information.

### Basic collinearity analysis
**Args:** `syny -i genome1.fasta -j genome2.fasta -o collinearity.txt`
**Explanation:** Detect collinearity between two genomes.

### With annotation
**Args:** `syny -i genome1.fasta -j genome2.fasta -a genes.gff -o collinearity.txt`
**Explanation:** Use gene annotation for analysis.

### Verbose mode
**Args:** `syny -i genome1.fasta -j genome2.fasta -o collinearity.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `syny -i genome1.fasta -j genome2.fasta -o collinearity.txt --stats`
**Explanation:** Generate statistics about collinearity.

### Batch processing
**Args:** `for f in genomes/*.fasta; do syny -i ref.fasta -j $f -o results/${f%.fasta}.txt; done`
**Explanation:** Compare multiple genomes against reference.

### Filter by length
**Args:** `syny -i genome1.fasta -j genome2.fasta -o collinearity.txt -l 10000`
**Explanation:** Filter by minimum block length.

### Include all blocks
**Args:** `syny -i genome1.fasta -j genome2.fasta -o collinearity.txt --all`
**Explanation:** Output all collinearity blocks.

### Generate report
**Args:** `syny -i genome1.fasta -j genome2.fasta -o collinearity.txt --report`
**Explanation:** Generate comprehensive collinearity report.
