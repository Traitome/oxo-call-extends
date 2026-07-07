---
name: samstats
category: alignment
description: SAM file alignment statistics at the read level
tags: ["samstats", "alignment", "sam", "bam", "quality-control", "statistics"]
author: oxo-call-community
source_url: "https://github.com/kundajelab/SAMstats"
---

## Concepts
- **Tool Overview**: SAMstats (v0.2.2) is a tool for comprehensive quality control metrics extraction from SAM/BAM alignment files at the read level.
- **Core Function**: Generates detailed statistics about mapping quality, base composition, and error profiles split by mapping quality bins.
- **Algorithm**: Uses htslib API for efficient BAM parsing, implements finite state automaton for parsing, supports multi-threaded processing.
- **Input Format**: SAM/BAM/CRAM alignment files, optionally with reference FASTA.
- **Output Format**: HTML quality control reports with interactive Plotly charts, CSV/TXT statistics files.
- **Use Case**: NGS data quality control, identifying mapping issues, adapter contamination detection, sequencing quality assessment.

## Pitfalls
- **Memory Requirements**: Large BAM files require sufficient memory for processing.
- **Index Requirement**: BAM files must be indexed for efficient region queries.
- **Reference Genome**: Some statistics require a reference FASTA file.
- **Paired-End Data**: Proper handling requires correctly paired reads in BAM.
- **Long Reads**: Performance may vary with long-read sequencing data.
- **Output Interpretation**: Understanding mapping quality distributions requires domain knowledge.

## Examples
### Generate basic QC report
**Args:** `samstats input.bam`
**Explanation:** Generates HTML QC report for the input BAM file.

### Specify output directory
**Args:** `samstats -o qc_report input.bam`
**Explanation:** `-o` specifies output directory for QC report.

### Multi-threaded processing
**Args:** `samstats -t 4 input.bam`
**Explanation:** `-t` specifies number of threads for parallel processing.

### Include reference genome
**Args:** `samstats -f reference.fasta input.bam`
**Explanation:** `-f` provides reference FASTA for additional statistics.

### Process multiple files
**Args:** `samstats sample1.bam sample2.bam sample3.bam`
**Explanation:** Processes multiple BAM files and generates combined reports.

### Filter by mapping quality
**Args:** `samstats -q 30 input.bam`
**Explanation:** `-q` filters to only consider reads with mapping quality >= 30.

### Generate CSV output
**Args:** `samstats --csv input.bam`
**Explanation:** Outputs statistics in CSV format for further analysis.