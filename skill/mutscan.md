---
name: mutscan
category: variant-calling
description: Detect and visualize target mutations by scanning FastQ files directly
tags: [mutscan, variant-calling, mutation, fastq, visualization, targeted-mutation]
author: oxo-call-community
source_url: "https://github.com/OpenGene/MutScan"
---

## Concepts

- **Tool Overview**: MutScan v1.14.1 is a high-performance tool for detecting target mutations directly from FASTQ files without requiring prior alignment. It rapidly scans raw sequencing data to identify presence of specific mutations, generating visual reports for each detected variant.
- **Core Function**: Takes FASTQ files and a list of target mutations, scans reads to find supporting evidence, and produces an HTML report with read-level visualization of each mutation.
- **Algorithm**: Uses efficient pattern matching against known mutation sequences. Reads containing the mutation are extracted and visualized, enabling rapid assessment of mutation presence and read-level context.
- **Input Format**: Accepts gzipped or uncompressed FASTQ files (single-end or paired-end). Requires a mutation definition file containing target mutations in a simple text format.
- **Output**: Generates an HTML report showing mutation detection results, including read counts supporting each mutation, example read alignments, and quality metrics.
- **Speed**: Designed for rapid screening - can scan billions of reads quickly without alignment, making it ideal for targeted mutation validation.

## Pitfalls

- **Mutation Definition Format**: The mutation file format must be correct. Typically one mutation per line in format like `chr1:12345:A>G`. Check documentation for exact format.
- **Paired-End Handling**: For paired-end reads, both files should be provided. MutScan will use read pairs to improve confidence.
- **Compression Support**: Supports gzipped FASTQ (.gz) but not bzip2 or other formats. Ensure correct file extension.
- **Quality Filtering**: Default quality thresholds may filter some reads. Adjust if too many reads are being discarded.
- **Read Length Requirements**: Mutations near read ends may have insufficient context. Longer reads provide more reliable detection.
- **Memory Usage**: Large FASTQ files require substantial memory. Consider streaming or chunked processing for very large files.

## Examples

### Basic mutation scanning
**Args:** `-i input.fastq.gz -m mutations.txt -o output_dir`
**Explanation:** Standard MutScan workflow. Scans FASTQ for mutations defined in mutations.txt and outputs HTML report to output_dir.

### Paired-end reads
**Args:** `-1 R1.fastq.gz -2 R2.fastq.gz -m targets.txt -o results/`
**Explanation:** For paired-end data, provide both read files with `-1` and `-2`. MutScan will use both for improved detection.

### Specify output format
**Args:** `-i sample.fq -m mutations.txt -o results/ --html-only`
**Explanation:** Use `--html-only` to generate only HTML report without JSON results. Faster for quick visual inspection.

### Set minimum quality threshold
**Args:** `-i reads.fq -m targets.txt -o results/ -q 20`
**Explanation:** Sets minimum base quality of 20 for reads to be considered. Filters out low-quality reads that may cause false positives.

### Enable tumor-normal mode
**Args:** `-1 tumor_R1.fq -2 tumor_R2.fq -1n normal_R1.fq -2n normal_R2.fq -m mutations.txt -o results/`
**Explanation:** Tumor-normal mode compares mutations between tumor and normal samples to identify somatic variants.
