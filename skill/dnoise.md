---
name: dnoise
category: utility
description: DNOISE - Denoising tool for removing sequencing errors from amplicon data.
tags: [dnoise, utility, denoising, sequencing, amplicon, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ibisbailey/dnoise"
---

## Concepts

- **Tool Overview**: DNOISE is a denoising algorithm specifically designed for amplicon sequencing data.
- **Core Function**: Removes sequencing errors and noise by clustering similar sequences and generating consensus sequences.
- **Input/Output**: Input: FASTQ reads from amplicon sequencing. Output: Denoised sequences in FASTA format.
- **Algorithm**: Uses alignment-free sequence comparison to identify and correct sequencing errors.
- **Key Features**: Error correction, chimera detection, consensus generation, batch processing, quality filtering.
- **Installation**: `conda install -c bioconda dnoise`

## Pitfalls

- **Input Requirements**: Optimized for amplicon data; may not work well with whole-genome sequencing reads.
- **Sequence Length**: Works best with reads of consistent length typical of amplicons.
- **Error Rate**: Very high error rates may overwhelm the denoising algorithm.
- **Chimeras**: Chimeric sequences may not be properly handled and could produce false consensus sequences.
- **Computational Resources**: Large datasets may require significant memory and processing time.
- **Parameter Tuning**: Default parameters may need adjustment for different sequencing platforms.

## Examples

### Basic denoising
**Args:** `dnoise --input reads.fq --output denoised.fa`
**Explanation:** Denoises amplicon sequencing reads to remove errors and generate clean sequences.

### With quality filtering
**Args:** `dnoise --input reads.fq --output denoised.fa --min-quality 20`
**Explanation:** Filters low-quality reads before denoising to improve results.

### Batch processing
**Args:** `dnoise --input-dir fastq_files/ --output-dir denoised/`
**Explanation:** Processes multiple FASTQ files in batch mode.

### Custom clustering threshold
**Args:** `dnoise --input reads.fq --output denoised.fa --threshold 0.95`
**Explanation:** Sets a 95% similarity threshold for sequence clustering.

### With chimera removal
**Args:** `dnoise --input reads.fq --output denoised.fa --remove-chimeras`
**Explanation:** Detects and removes chimeric sequences during denoising.

### Output as FASTQ
**Args:** `dnoise --input reads.fq --output denoised.fq --format fastq`
**Explanation:** Outputs denoised sequences in FASTQ format preserving quality scores.