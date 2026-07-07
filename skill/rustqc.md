---
name: rustqc
category: quality_control
description: RNA-seq quality control suite combining dupRadar, featureCounts, RSeQC, preseq, samtools stats, and Qualimap.
tags: ["rustqc", "RNA-seq", "quality control", "QC", "bioinformatics"]
author: oxo-call-community
source_url: "https://seqeralabs.github.io/RustQC/"
---

## Concepts

- **Tool Overview**: rustqc (v0.2.1) is an integrated RNA-seq quality control suite that combines multiple QC tools into a single pipeline. It runs dupRadar, featureCounts, RSeQC, preseq, samtools stats, and Qualimap in one pass.
- **Core Function**: Performs comprehensive quality control analysis of RNA-seq data, including duplication analysis, gene expression quantification, read distribution, library complexity, and alignment statistics.
- **Architecture**: Wraps multiple QC tools and coordinates their execution, aggregating results into a unified report.
- **Input Format**: BAM files with aligned RNA-seq reads, GTF gene annotations.
- **Output Format**: Comprehensive HTML QC report, individual tool outputs, quality metrics in JSON/TSV format.
- **Use Case**: RNA-seq quality assessment, pipeline validation, quality control before downstream analysis.

## Pitfalls

- **Dependency requirements**: Requires all underlying tools (samtools, RSeQC, etc.) to be installed.
- **Resource intensive**: Running multiple QC tools simultaneously requires significant resources.
- **Annotation requirements**: Needs gene annotation GTF file for some analyses.
- **Memory usage**: Large BAM files require significant memory for processing.
- **Time consuming**: Full QC analysis can take time for large datasets.
- **Report complexity**: Comprehensive reports may be overwhelming for simple use cases.

## Examples

### Basic QC analysis
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report`
**Explanation:** `-i` input BAM; `-g` gene annotation GTF; `-o` output directory.

### Skip certain tools
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report --skip qualimap`
**Explanation:** `--skip` excludes specified tool from analysis.

### Include strandedness info
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report -s reverse`
**Explanation:** `-s` library strandedness (forward/reverse/unstranded).

### Threaded processing
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report -t 8`
**Explanation:** `-t` number of threads for parallel processing.

### Output JSON metrics
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report --json metrics.json`
**Explanation:** `--json` outputs metrics in JSON format.

### Quick mode
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report --quick`
**Explanation:** `--quick` runs only essential QC tools for faster results.

### Custom configuration
**Args:** `rustqc -i aligned.bam -g genes.gtf -o qc_report --config config.yaml`
**Explanation:** `--config` uses custom configuration file for tool parameters.
