---
name: targqc
category: qc
description: Target capture sequencing coverage QC.
tags: [targqc, qc, target-capture, coverage]
author: oxo-call-community
source_url: "https://github.com/vladsaveliev/TargQC"
---

## Concepts

- **Tool Overview**: targqc (v1.8.1) assesses target capture sequencing quality.
- **Core Function**: Evaluates coverage and quality of target regions.
- **Algorithm**: Calculates coverage statistics for targeted sequencing.
- **Input/Output**: Input: BAM alignments; Output: QC reports.
- **Applications**: Target capture QC, sequencing quality control.
- **Installation**: `conda install -c bioconda targqc` or download from GitHub.

## Pitfalls

- **BAM Index**: Requires indexed BAM files.
- **Target Regions**: Requires BED file for target regions.
- **Coverage Depth**: Insufficient coverage affects QC.
- **GC Bias**: High GC regions may have low coverage.
- **Performance**: Large BAM files process slowly.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `targqc --help`
**Explanation:** Shows available options and usage information.

### Basic QC analysis
**Args:** `targqc -i alignments.bam -b targets.bed -o qc_report/`
**Explanation:** Perform target coverage QC.

### With sample info
**Args:** `targqc -i alignments.bam -b targets.bed -s sample_info.txt -o qc_report/`
**Explanation:** Include sample information.

### Verbose mode
**Args:** `targqc -i alignments.bam -b targets.bed -o qc_report/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `targqc -i alignments.bam -b targets.bed -o qc_report/ --stats`
**Explanation:** Generate comprehensive statistics.

### Batch processing
**Args:** `for f in bams/*.bam; do targqc -i $f -b targets.bed -o qc/${f%.bam}_qc/; done`
**Explanation:** Process multiple BAM files.

### Filter by coverage
**Args:** `targqc -i alignments.bam -b targets.bed -o qc_report/ -c 20`
**Explanation:** Minimum coverage threshold of 20x.

### Generate HTML report
**Args:** `targqc -i alignments.bam -b targets.bed -o qc_report/ --html`
**Explanation:** Generate HTML report.

### Export to CSV
**Args:** `targqc -i alignments.bam -b targets.bed -o qc_report/ -f csv`
**Explanation:** Export results in CSV format.
