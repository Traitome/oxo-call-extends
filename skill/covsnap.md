---
name: covsnap
category: qc
description: Coverage inspector for targeted sequencing QC - computes per-target and per-exon depth metrics with interactive HTML reports
tags: [covsnap, coverage, targeted-sequencing, qc, bam, cram, sequencing, quality-control, hg38]
author: oxo-call-community
source_url: "https://github.com/enes-ak/covsnap"
---

## Concepts

- **Tool Overview**: covsnap is a coverage inspector for targeted sequencing quality control, computing per-target and per-exon depth metrics from BAM/CRAM files and producing interactive HTML reports with PASS/FAIL classifications.
- **Core Function**: Analyzes sequencing coverage across targeted genomic regions, calculates depth statistics, and generates visual coverage summaries.
- **Algorithm**: Reads BAM/CRAM alignments, calculates per-position and per-interval coverage metrics, and compares against configurable thresholds.
- **Input**: BAM or CRAM alignment files (aligned to hg38).
- **Output**: Interactive HTML report with coverage visualizations, PASS/FAIL status for each target, and summary statistics.
- **Application**: Targeted sequencing QC, clinical sequencing validation, gene panel assessment, coverage uniformity analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda covsnap` or `pixi global install covsnap`

## Pitfalls

- **Reference Genome**: Requires hg38 reference. BAM/CRAM files must be aligned to GRCh38/hg38.
- **Index Files**: CRAM files require corresponding index (.crai) files.
- **Target Definition**: Must have proper interval lists or gene annotations for targeted regions.
- **Depth Thresholds**: Default thresholds may need adjustment based on specific assay requirements.
- **Bundle Data**: Requires bundled GENCODE v44 hg38 gene index for gene symbol lookups.

## Examples

### Basic coverage report
**Args:** `covsnap -i sample.bam`
**Explanation:** Generates a coverage report from a BAM file using default gene index and settings.

### Specify output directory
**Args:** `covsnap -i sample.bam -o output_report.html`
**Explanation:** Generates a coverage report and saves it to specified output file.

### Use CRAM input
**Args:** `covsnap -i sample.cram -o output_report.html`
**Explanation:** Generates coverage report from CRAM file (requires index file present).

### Query by gene symbol
**Args:** `covsnap -i sample.bam --gene BRCA1`
**Explanation:** Generates coverage report focused on a specific gene symbol.

### Query multiple genes (comma-separated)
**Args:** `covsnap -i sample.bam --gene "BRCA1,BRCA2,TP53"`
**Explanation:** Generates coverage report for multiple specified genes.

### Specify genomic region
**Args:** `covsnap -i sample.bam --region chr17:43000000-43100000`
**Explanation:** Generates coverage report for a specific genomic region.

### Use custom BED file
**Args:** `covsnap -i sample.bam --bed-file custom_targets.bed`
**Explanation:** Uses a custom BED file to define targeted regions instead of default gene index.
