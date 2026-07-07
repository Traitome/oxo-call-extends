---
name: salmon
category: alignment
description: Highly-accurate & wicked fast transcript-level quantification from RNA-seq reads using selective alignment.
tags: ["salmon", "alignment", "rna-seq", "quantification", "transcriptomics"]
author: oxo-call-community
source_url: "https://combine-lab.github.io/salmon"
---

## Concepts

- **Tool Overview**: Salmon (v1.11.4+) is a fast and accurate tool for transcript-level quantification from RNA-seq reads using selective alignment. It directly quantifies transcripts without full read alignment.
- **Core Function**: Performs lightweight alignment (quasi-mapping) of RNA-seq reads to transcript sequences for efficient quantification of gene/transcript expression levels.
- **Input/Output**: Input: FASTQ reads (single-end or paired-end), transcriptome FASTA. Output: Quantification files (quant.sf), auxiliary files for downstream analysis.
- **Algorithm**: Uses quasi-mapping to quickly map reads to transcripts, avoiding full alignment while maintaining accuracy. Employs expectation-maximization for abundance estimation.
- **Key Features**: Ultra-fast quantification, supports strand-specific libraries, performs bias correction, and outputs compatibility with downstream tools like DESeq2 and edgeR.
- **Installation**: `conda install -c bioconda salmon`

## Pitfalls

- **Index Compatibility**: Index must be built with the same Salmon version as used for quantification.
- **Transcriptome Reference**: Requires a transcriptome FASTA file, not a genome FASTA. Use tools like gffread to extract transcripts from genome and GTF.
- **Strand-Specific Data**: For strand-specific libraries, use `-l ISR` (dUTP) or `-l ISF` (forward) to ensure correct quantification.
- **Fragment Length Distribution**: Salmon auto-detects fragment lengths, but for paired-end data with large insert size variation, provide expected fragment length with `-fldMean` and `-fldSD`.
- **Bias Correction**: Enable bias correction with `--gcBias` and `--seqBias` for improved accuracy, especially for GC-content biased data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Build transcriptome index
**Args:** `index -t transcripts.fasta -i salmon_index -k 31`
**Explanation:** Builds a Salmon index from transcript sequences using k-mer size 31.

### Quantify paired-end RNA-seq reads
**Args:** `quant -i salmon_index -l A -1 R1.fastq.gz -2 R2.fastq.gz -o quant_output`
**Explanation:** Quantifies paired-end reads with automatic library type detection (-l A). Outputs to quant_output directory.

### Quantify with strand-specific library
**Args:** `quant -i salmon_index -l ISR -1 R1.fastq.gz -2 R2.fastq.gz -o quant_output`
**Explanation:** Quantifies strand-specific (dUTP/reverse-stranded) library. Use ISF for forward-stranded libraries.

### Quantify with bias correction
**Args:** `quant -i salmon_index -l A -1 R1.fastq.gz -2 R2.fastq.gz -o quant_output --gcBias --seqBias`
**Explanation:** Enables GC content and sequence bias correction for more accurate quantification.

### Quantify single-end reads
**Args:** `quant -i salmon_index -l A -r reads.fastq.gz -o quant_output`
**Explanation:** Quantifies single-end reads using automatic library type detection.

### Generate decoy-aware index
**Args:** `index -t transcripts.fasta -d decoys.txt -i salmon_decoy_index -k 31`
**Explanation:** Builds an index with decoy sequences to improve mapping accuracy. decoys.txt lists decoy sequence names.

### Quantify with validation mapping
**Args:** `quant -i salmon_index -l A -1 R1.fastq.gz -2 R2.fastq.gz -o quant_output --validateMappings`
**Explanation:** Validates mappings and provides additional diagnostic information about mapping quality.

### Quantify multiple samples at once
**Args:** `quant -i salmon_index -l A -1 sample1_R1.fastq.gz sample2_R1.fastq.gz -2 sample1_R2.fastq.gz sample2_R2.fastq.gz -o quant_output`
**Explanation:** Quantifies multiple paired-end samples in a single run. Each sample's reads must be specified in order.