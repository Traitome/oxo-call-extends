---
name: deblur
category: qc
description: Deblur is a greedy deconvolution algorithm for resolving biological sequences from sequencing reads.
tags: [deblur, qc, sequence-error-correction, amplicon-sequencing, microbiome]
author: oxo-call-community
source_url: "https://github.com/biocore/deblur"
---

## Concepts

- **Tool Overview**: deblur (v1.1.1+) is a greedy deconvolution algorithm designed to resolve biological sequences from Illumina amplicon sequencing reads. It uses known read error profiles to reconstruct true sequences.
- **Core Function**: Deconvolves sequencing reads into their original biological sequences by iteratively removing errors based on quality scores and error profiles.
- **Input/Output**: Input: FASTQ reads (typically 16S rRNA amplicon data). Output: Deblurred sequences, error-corrected reads, abundance tables.
- **Algorithm**: Uses a greedy approach to iteratively deconvolve reads, starting from the most abundant sequences and progressively resolving less abundant ones.
- **Key Features**: Amplicon-focused, error profile modeling, chimera detection, produces exact sequences, integration with QIIME.
- **Installation**: `conda install -c bioconda deblur`

## Pitfalls

- **Amplicon Specific**: Designed for amplicon sequencing, may not work well with metagenomic data.
- **Read Length**: Works best with specific read lengths; may struggle with very short or very long reads.
- **Abundance Bias**: May miss low-abundance sequences.
- **Chimera Detection**: Chimera detection may have false positives/negatives.
- **Computational Time**: Can be slow for large datasets.

## Examples

### Deblur amplicon reads
**Args:** `deblur workflow --seqs-fp reads.fastq --output-dir output/`
**Explanation:** Run deblur workflow on amplicon sequencing reads.

### Specify trim length
**Args:** `deblur workflow --seqs-fp reads.fastq --trim-length 150 --output-dir output/`
**Explanation:** Trim reads to 150 bp before deblurring.

### Denoise with error profile
**Args:** `deblur denoise --seqs-fp reads.fastq --error-profile error_profile.txt --output-dir output/`
**Explanation:** Use custom error profile for denoising.