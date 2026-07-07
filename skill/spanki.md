---
name: spanki
category: transcriptomics
description: Spanki - Alternative splicing analysis from RNA-Seq data
tags: [spanki, transcriptomics, alternative-splicing, rna-seq, junction-analysis]
author: oxo-call-community
source_url: "http://www.cbcb.umd.edu/software/spanki/"
---

## Concepts

- **Tool Overview**: spanki (v0.5.1) - An alternative splicing analysis tool
- **Core Function**: Analyzes alternative splicing from RNA-Seq junction data
- **Input/Output**: Accepts BAM files; outputs splicing analysis results
- **Algorithm**: Junction-level splicing analysis
- **Installation**: `conda install -c bioconda spanki`
- **Key Features**: Alternative splicing, junction analysis, RNA-Seq processing

## Pitfalls

- **Input Requirements**: Requires properly aligned RNA-Seq BAM files
- **Junction Quality**: Junction quality affects splicing analysis
- **Splicing Events**: Different splicing events require different analysis
- **Memory Usage**: Large BAM files require significant memory
- **Output Format**: Output format depends on analysis type
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `spanki --help`
**Explanation:** Shows available options and usage information.

### Basic splicing analysis
**Args:** `spanki -i aligned.bam -o splicing_results.tsv`
**Explanation:** Analyze alternative splicing from BAM.

### Junction compilation
**Args:** `spanki -i aligned.bam -o junctions.tsv --compile`
**Explanation:** Compile junction information from BAM.

### Splicing event analysis
**Args:** `spanki -i aligned.bam -o events.tsv --events`
**Explanation:** Analyze splicing events.

### With annotation
**Args:** `spanki -i aligned.bam -g annotation.gtf -o splicing_results.tsv`
**Explanation:** Use annotation for splicing analysis.

### Filter by coverage
**Args:** `spanki -i aligned.bam -o splicing_results.tsv --min-coverage 10`
**Explanation:** Filter by minimum coverage.

### Output detailed results
**Args:** `spanki -i aligned.bam -o splicing_results.tsv --detailed`
**Explanation:** Output detailed splicing results.

### Output statistics
**Args:** `spanki -i aligned.bam -o splicing_results.tsv --stats`
**Explanation:** Output splicing statistics.

### Generate report
**Args:** `spanki -i aligned.bam -o splicing_results.tsv --report`
**Explanation:** Generate splicing analysis report.