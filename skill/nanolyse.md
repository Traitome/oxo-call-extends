---
name: nanolyse
category: qc
description: NanoLyse - Remove lambda DNA control reads from Oxford Nanopore datasets
tags: [nanolyse, qc, nanopore, lambda-dna, filtering, spike-in]
author: oxo-call-community
source_url: "https://github.com/wdecoster/NanoLyse"
---

## Concepts

- **Tool Overview**: NanoLyse v1.2.1 removes lambda phage DNA control reads from Oxford Nanopore sequencing datasets. Lambda DNA is commonly used as a spike-in control for sequencing quality assessment.
- **Core Function**: Identifies and filters out reads originating from lambda phage control DNA, leaving only biological sample reads for downstream analysis.
- **Algorithm**: Aligns reads against the lambda phage reference genome and removes matching reads. Uses minimap2 for rapid alignment.
- **Input Format**: Accepts FASTQ format reads from stdin (can be gzipped). Works seamlessly in Unix pipelines.
- **Output**: Produces filtered FASTQ reads to stdout, excluding lambda phage sequences.
- **Use Case**: Quality control for Nanopore sequencing, removing control spike-in reads, and preparing clean datasets for downstream analysis.

## Pitfalls

- **Streaming Requirement**: Designed for stdin/stdout streaming. May require shell redirection for file-based operations.
- **Lambda Reference**: Default lambda reference may not match all control DNA sequences. Use appropriate reference for your control.
- **Alignment Sensitivity**: Highly divergent lambda sequences may not be filtered. Adjust alignment parameters if needed.
- **Biological Contamination**: If sample contains lambda-like sequences, they may be incorrectly filtered.
- **Compression**: Ensure consistent compression when piping between tools. Mixed compression states may cause issues.
- **Performance**: For very large datasets, consider parallel processing to improve speed.

## Examples

### Basic lambda removal
**Args:** `nanolyse < input.fastq > filtered.fastq`
**Explanation:** Removes lambda DNA control reads using default reference.

### Specify lambda reference
**Args:** `nanolyse -r lambda_reference.fasta < input.fastq > filtered.fastq`
**Explanation:** Uses custom lambda reference sequence for filtering.

### Process gzipped input
**Args:** `gunzip -c input.fastq.gz | nanolyse | gzip > filtered.fastq.gz`
**Explanation:** Processes gzipped FASTQ and re-compresses output.

### Combine with NanoFilt
**Args:** `gunzip -c input.fastq.gz | nanolyse | nanofilt -q 10 | gzip > filtered.fastq.gz`
**Explanation:** Pipeline combining lambda removal and quality filtering.

### Display help
**Args:** `nanolyse --help`
**Explanation:** Shows all available options for lambda filtering.
