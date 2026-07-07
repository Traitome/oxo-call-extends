---
name: solexaqa
category: qc
description: SolexaQA - Quality statistics and visualization for NGS data
tags: [solexaqa, qc, quality-control, visualization, sequencing]
author: oxo-call-community
source_url: "http://solexaqa.sourceforge.net/"
---

## Concepts

- **Tool Overview**: solexaqa (v3.1.7.1) - Quality assessment tool for NGS data
- **Core Function**: Generates quality statistics and visual representations
- **Input/Output**: Accepts FASTQ files; outputs quality reports and plots
- **Algorithm**: Analyzes base quality scores and sequence statistics
- **Installation**: `conda install -c bioconda solexaqa`
- **Key Features**: Quality statistics, visualization, NGS quality control

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **Quality Encoding**: Must correctly identify quality score encoding
- **Output Format**: Output format depends on analysis type
- **Large Files**: Large FASTQ files may require significant memory
- **Visualization**: Requires proper graphics environment for plots
- **Platform Support**: Originally designed for Solexa/Illumina data

## Examples

### Display help
**Args:** `SolexaQA.pl --help`
**Explanation:** Shows available options and usage information.

### Basic quality analysis
**Args:** `SolexaQA.pl reads.fastq`
**Explanation:** Analyze quality of FASTQ file.

### Generate plots
**Args:** `SolexaQA.pl reads.fastq --plot`
**Explanation:** Generate quality plots.

### Output statistics
**Args:** `SolexaQA.pl reads.fastq --stats`
**Explanation:** Output quality statistics.

### Dynamic trimming
**Args:** `SolexaQA.pl reads.fastq --dynamic_trim`
**Explanation:** Perform dynamic quality trimming.

### Cut-off trimming
**Args:** `SolexaQA.pl reads.fastq --cutoff 20`
**Explanation:** Trim with quality cutoff.

### Output directory
**Args:** `SolexaQA.pl reads.fastq --outdir results/`
**Explanation:** Output results to directory.

### Generate report
**Args:** `SolexaQA.pl reads.fastq --report`
**Explanation:** Generate quality report.