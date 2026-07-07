---
name: arem
category: alignment
description: ARoEM - Aligning Reads by Expectation-Maximization for ChIP-Seq analysis
tags: [arem, alignment, chip-seq, em-algorithm, peak-calling]
author: oxo-call-community
source_url: "http://cbcl.ics.uci.edu/AREM"
---

## Concepts

- **Tool Overview**: ARoEM (Aligning Reads by Expectation-Maximization) is a read alignment tool that uses expectation-maximization algorithms for improved mapping, particularly optimized for ChIP-Seq data. Version 1.0.1.
- **Core Function**: Employs probabilistic alignment through EM optimization to handle ambiguous read mappings common in repetitive genomic regions.
- **ChIP-Seq Optimization**: Built on principles from MACS (Model-based Analysis for ChIP-Seq), specifically designed for chromatin immunoprecipitation experiments.
- **Ambiguous Mapping**: Uses statistical framework to assign reads that map to multiple locations based on likelihood scores.
- **Input/Output**: Accepts FASTQ input and outputs SAM/BAM alignments with probability-weighted mapping scores.
- **Installation**: `conda install -c bioconda arem` or download from project website.

## Pitfalls

- **EM Convergence**: EM algorithm may require multiple iterations for convergence. Runtime depends on dataset complexity.
- **Memory Requirements**: Large-scale ChIP-Seq experiments require significant memory for EM computations.
- **Parameter Tuning**: May require adjustment of convergence thresholds and iteration limits.
- **ChIP-Seq Specific**: Optimized for ChIP-Seq; may not be ideal for other sequencing applications.
- **Paired-end Handling**: Limited support for paired-end data compared to specialized aligners.

## Examples

### Basic alignment
**Args:** `arem -i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Performs basic read alignment using EM algorithm. Outputs SAM file with mapping probabilities.

### ChIP-Seq peak calling
**Args:** `arem -i chip_sample.fastq -r genome.fa -o alignments.sam --call_peaks`
**Explanation:** Aligns ChIP-Seq sample and performs peak calling based on enriched regions.

### Control sample alignment
**Args:** `arem -i control_input.fastq -r genome.fa -o control_alignments.sam`
**Explanation:** Aligns control/input sample for differential binding analysis.

### Adjust EM iterations
**Args:** `arem -i input.fastq -r reference.fa -o output.sam --max_iter 100 --convergence 0.0001`
**Explanation:** Sets maximum 100 iterations and convergence threshold of 0.0001 for EM algorithm.

### Multi-threaded alignment
**Args:** `arem -i sample.fastq -r genome.fa -o output.sam -t 8`
**Explanation:** Uses 8 threads for parallel processing to speed up alignment.

### Output with mapping probabilities
**Args:** `arem -i reads.fastq -r genome.fa -o output.sam --emit_probs`
**Explanation:** Outputs additional mapping probability scores for each aligned read.