---
name: ericscript
category: utility
description: "EricScript is a computational framework for the discovery of gene fusions in paired end RNA-seq data."
tags: [ericscript, utility, gene-fusion, RNA-seq, fusion-detection]
author: oxo-call-community
source_url: "https://sites.google.com/site/bioericscript"
---

## Concepts

- **Tool Overview**: EricScript is a computational framework for discovering gene fusions from paired-end RNA-seq data, with additional tools for simulating synthetic fusions and evaluating detection methods.
- **Core Function**: Identifies gene fusion events by analyzing split reads and discordant read pairs in RNA-seq data.
- **Input/Output**: Input: Paired-end RNA-seq reads (FASTQ/BAM), reference genome. Output: Fusion candidates, supporting reads, statistical scores.
- **Algorithm**: Uses split-read mapping and discordant pair analysis to identify potential fusion events, with filtering based on quality scores and supporting evidence.
- **Key Features**: Gene fusion detection, synthetic fusion simulation, performance evaluation, visualization, batch processing.
- **Installation**: `conda install -c bioconda ericscript`

## Pitfalls

- **False Positives**: May produce false positive fusion calls requiring manual validation.
- **Read Quality**: Poor quality reads may affect detection accuracy.
- **Reference Genome**: Requires up-to-date reference genome annotation.
- **Computation Resources**: Large datasets require significant computational resources.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic fusion detection
**Args:** `ericscript --read1 reads_1.fastq --read2 reads_2.fastq --reference ref.fasta --output results/`
**Explanation:** Detects gene fusions from paired-end RNA-seq data.

### With annotation
**Args:** `ericscript --read1 reads_1.fastq --read2 reads_2.fastq --reference ref.fasta --annotation genes.gtf --output results/`
**Explanation:** Uses gene annotation for improved fusion calling.

### Simulate synthetic fusions
**Args:** `ericscript-simulate --reference ref.fasta --annotation genes.gtf --output synthetic_fusions.fastq`
**Explanation:** Generates synthetic gene fusion reads for testing.

### Performance evaluation
**Args:** `ericscript-calcstats --truth truth_set.txt --predictions predictions.txt --output stats.txt`
**Explanation:** Calculates performance metrics for fusion detection.

### Batch processing
**Args:** `ericscript --input samples.txt --reference ref.fasta --output results/`
**Explanation:** Processes multiple samples in batch mode.