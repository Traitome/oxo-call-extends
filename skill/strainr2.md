---
name: strainr2
category: metagenomics
description: StrainR2 accurately deconvolutes strain-level abundances in synthetic microbial communities.
tags: [strainr2, metagenomics, strain-deconvolution, synthetic-communities]
author: oxo-call-community
source_url: "https://github.com/BisanzLab/StrainR2"
---

## Concepts

- **Tool Overview**: strainr2 (v2.3.0) is a tool for deconvoluting strain-level abundances in synthetic microbial communities.
- **Core Function**: Accurately estimates relative abundances of individual strains in mixed populations.
- **Algorithm**: Uses k-mer based profiling and statistical modeling for strain deconvolution.
- **Input/Output**: Input: Metagenomic reads (FASTQ), reference genomes; Output: Strain abundance estimates.
- **Applications**: Synthetic community analysis, strain validation, metagenomic benchmarking.
- **Installation**: `conda install -c bioconda strainr2` or download from GitHub.

## Pitfalls

- **Community Complexity**: Very complex communities may be hard to deconvolve.
- **Reference Completeness**: Missing reference genomes affect accuracy.
- **Strain Similarity**: Highly similar strains are hard to distinguish.
- **Read Quality**: Low-quality reads affect estimation accuracy.
- **Abundance Range**: Extreme abundance differences may affect detection.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `strainr2 --help`
**Explanation:** Shows available options and usage information.

### Basic deconvolution
**Args:** `strainr2 -i reads.fastq -d database/ -o results.txt`
**Explanation:** Deconvolve strain abundances from metagenomic reads.

### With custom references
**Args:** `strainr2 -i reads.fastq -r references/ -o results.txt`
**Explanation:** Use custom reference genomes for deconvolution.

### Verbose mode
**Args:** `strainr2 -i reads.fastq -d database/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strainr2 -i reads.fastq -d database/ -o results.txt --plot`
**Explanation:** Generate visualization of strain abundances.

### Custom k-mer size
**Args:** `strainr2 -i reads.fastq -d database/ -o results.txt -k 31`
**Explanation:** Use k-mer size of 31 for profiling.

### Batch processing
**Args:** `strainr2 -i batch/ -d database/ -o results/`
**Explanation:** Process multiple metagenomic samples together.

### Build database
**Args:** `strainr2 build -i references/ -o database/`
**Explanation:** Build k-mer database from reference genomes.

### Generate report
**Args:** `strainr2 -i reads.fastq -d database/ -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
