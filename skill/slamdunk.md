---
name: slamdunk
category: utility
description: SlamDunk is a software tool for SLAMseq data analysis, enabling quantification of experimentally induced nucleotide conversions in high-throughput sequencing datasets
tags: [slamdunk, utility, SLAMseq, RNA-seq, transcriptomics]
author: oxo-call-community
source_url: "http://t-neumann.github.io/slamdunk/docs.html"
---

## Concepts

- **Tool Overview**: slamdunk (v0.4.3) - A comprehensive tool for analyzing SLAMseq data to study RNA dynamics and transcription kinetics
- **Core Function**: Quantifies T>C conversions from 4-thiouridine labeling to distinguish nascent RNA from existing transcripts
- **Input/Output**: Accepts BAM/FASTQ files; outputs SLAMseq statistics, filtered BAM files, and count matrices
- **Algorithm**: Uses NextGenMap for alignment; performs statistical analysis of nucleotide conversions
- **Installation**: `conda install -c bioconda slamdunk` or `pip install slamdunk`
- **Key Features**: Complete SLAMseq analysis pipeline including mapping, filtering, and quantification

## Pitfalls

- **Reference Genome**: Requires appropriate reference genome and annotation files
- **BED File**: BED file with 3' UTR coordinates is required for certain analyses
- **Read Length**: Maximum read length parameter must match input data
- **Conversion Rate**: Low conversion rates may affect analysis accuracy
- **Java Dependency**: Requires Java for some components
- **Memory Usage**: Large datasets may require significant memory

## Examples

### Display help
**Args:** `slamdunk --help`
**Explanation:** Shows available options and usage information.

### Complete SLAMseq analysis
**Args:** `slamdunk all -r reference.fasta -b utrs.bed -o output_dir -5 12 -n 100 -t 4 reads.fastq`
**Explanation:** Run complete SLAMseq analysis pipeline with reference genome and UTR annotations.

### Map reads
**Args:** `slamdunk map -r reference.fasta -o output_dir reads.fastq`
**Explanation:** Map reads to reference genome using NextGenMap.

### Filter and count
**Args:** `slamdunk filter -i mapped.bam -o filtered.bam -5 12`
**Explanation:** Filter mapped reads and perform conversion-aware filtering.

### Generate statistics
**Args:** `slamdunk count -i filtered.bam -b utrs.bed -o counts.txt`
**Explanation:** Generate SLAMseq statistics per UTR.

### Quick sanity check
**Args:** `slamdunk alleyoop -i mapped.bam -o report.pdf`
**Explanation:** Generate quality control report for SLAMseq data.

### Multi-sample analysis
**Args:** `slamdunk all -r reference.fasta -b utrs.bed -o output_dir -t 8 sample1.fastq sample2.fastq`
**Explanation:** Analyze multiple samples simultaneously.