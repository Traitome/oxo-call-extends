---
name: strucvis
category: visualization
description: strucVis displays small RNA depth of coverage on a predicted RNA secondary structure.
tags: [strucvis, rna-structure, visualization, small-rna]
author: oxo-call-community
source_url: "https://github.com/MikeAxtell/strucVis"
---

## Concepts

- **Tool Overview**: strucvis (v0.9) is a tool for visualizing small RNA coverage on predicted RNA secondary structures.
- **Core Function**: Maps small RNA sequencing reads onto predicted RNA secondary structures.
- **Algorithm**: Uses RNA structure prediction and read mapping to visualize coverage.
- **Input/Output**: Input: Small RNA reads, RNA sequence; Output: Visualized structure with coverage.
- **Applications**: RNA structure analysis, small RNA targeting, regulatory RNA research.
- **Installation**: `conda install -c bioconda strucvis` or download from GitHub.

## Pitfalls

- **Structure Quality**: Poor quality structure predictions affect visualization.
- **Read Quality**: Low-quality reads affect mapping accuracy.
- **Coverage Bias**: Uneven coverage affects visualization.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Structure Format**: Requires specific structure format.

## Examples

### Display help
**Args:** `strucvis --help`
**Explanation:** Shows available options and usage information.

### Basic visualization
**Args:** `strucvis -i reads.bam -r rna.fasta -o structure.svg`
**Explanation:** Visualize small RNA coverage on RNA structure.

### With structure file
**Args:** `strucvis -i reads.bam -r rna.fasta -s structure.dot -o structure.svg`
**Explanation:** Use precomputed RNA structure.

### Verbose mode
**Args:** `strucvis -i reads.bam -r rna.fasta -o structure.svg -v`
**Explanation:** Run with detailed logging for debugging.

### Output multiple formats
**Args:** `strucvis -i reads.bam -r rna.fasta -o structure --formats svg pdf png`
**Explanation:** Output visualization in multiple formats.

### Batch processing
**Args:** `strucvis -i bam_files/ -r rna.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `strucvis -i reads.bam -r rna.fasta -o structure.svg -q 20`
**Explanation:** Filter reads by mapping quality.

### Include statistics
**Args:** `strucvis -i reads.bam -r rna.fasta -o structure.svg --stats`
**Explanation:** Generate statistics about coverage.

### Generate report
**Args:** `strucvis -i reads.bam -r rna.fasta -o structure.svg --report`
**Explanation:** Generate comprehensive HTML report.
