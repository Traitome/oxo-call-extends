---
name: hylight
category: assembly
description: HyLight - Strain aware assembly of low coverage metagenomes
tags: [hylight, metagenomics, strain assembly]
author: oxo-call-community
source_url: "https://github.com/LuoGroup2023/HyLight"
---

## Concepts

- **Tool Overview**: HyLight is a hybrid assembly tool for strain-aware assembly of low coverage metagenomes, combining NGS and TGS data advantages.
- **Strain Resolution**: Uses strain-aware overlap graph (OG) to accurately reconstruct individual strains from microbial communities.
- **Cross-hybrid Approach**: Treats both short and long reads as primary assembly data rather than using one as auxiliary.
- **Low Coverage Optimization**: Designed to work effectively with low coverage long-read data, reducing sequencing costs.
- **Error Correction**: Integrates multiple polishing steps including FMLRC2 for long-read correction and Racon for error removal.
- **Installation**: `conda install -c bioconda hylight`

## Pitfalls

- **Input Requirements**: Requires both long reads (Nanopore/PacBio) and short reads (Illumina) for optimal results.
- **Memory Considerations**: Processing complex metagenomic datasets may require significant memory resources.
- **Strain Complexity**: Highly complex communities with many strains may affect assembly accuracy.
- **Read Quality**: Low-quality reads should be filtered before assembly to improve results.
- **Dependency Requirements**: Requires minimap2, FMLRC2, Racon, and other bioinformatics tools.
- **Computational Resources**: Assembly can be computationally intensive for large datasets.

## Examples

### Hybrid assembly with short and long reads
**Args:** `hylight -l long_reads.fastq.gz -s short_reads_R1.fastq.gz -s2 short_reads_R2.fastq.gz -o assembly/`
**Explanation:** Runs strain-aware hybrid assembly using both long and short reads.

### Long-read only assembly
**Args:** `hylight -l long_reads.fastq.gz -o assembly/ --no_short`
**Explanation:** Runs assembly using only long reads without short read correction.

### Specify k-mer size
**Args:** `hylight -l long_reads.fastq.gz -s short_reads.fastq.gz -k 31 -o assembly/`
**Explanation:** Uses k-mer size of 31 for assembly graph construction.

### Set thread count
**Args:** `hylight -l long_reads.fastq.gz -s short_reads.fastq.gz -t 16 -o assembly/`
**Explanation:** Runs assembly with 16 threads for parallel processing.

### Output intermediate files
**Args:** `hylight -l long_reads.fastq.gz -s short_reads.fastq.gz -o assembly/ --keep_intermediate`
**Explanation:** Retains intermediate files for debugging and analysis.