---
name: figaro
category: qc
description: "An efficient and objective tool for optimizing microbiome rRNA gene trimming parameters for DADA2 and Deblur pipelines."
tags: [figaro, qc, microbiome, rRNA, trimming, DADA2, Deblur, amplicon-sequencing, 16S, 18S, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Zymo-Research/figaro"
---

## Concepts

- **Tool Overview**: Figaro is a tool for optimizing microbiome rRNA gene trimming parameters. It analyzes error rates in FASTQ files to determine optimal trimming parameters for targeted microbiome sequencing pipelines.
- **Core Function**: Performs exponential regression on cumulative expected error values across read positions to find optimal forward/reverse trim positions that maximize read retention while maintaining quality.
- **Input/Output**: Input: Paired-end FASTQ files from the same sequencing run. Output: JSON file with ranked trimming parameter candidates and PNG plots of error models.
- **Algorithm**: Fits exponential regression curves to the percentile of cumulative expected errors at each position. The default percentile of 83 removes reads ~1 standard deviation worse than average.
- **Key Features**: Automatic parameter optimization, supports DADA2 and Deblur, produces publication-ready plots, subsampling for large datasets, Docker or command-line deployment.
- **Installation**: `pip install figaro` or `conda install -c bioconda figaro` or Docker deployment

## Pitfalls

- **Amplicon Length Excludes Primers**: The amplicon length should ONLY include the target sequence, NOT the primers. For 341F-806R primers (20bp each) with 465bp target, use amplicon length 425 (not 465).
- **Sequencing Run Consistency**: Reads from different sequencing runs or library preparations should have trimming parameters generated separately, as error profiles may differ significantly.
- **Naming Standard**: Currently supports Illumina and Zymo naming conventions. Other naming schemes require custom Python modifications.
- **R-squared Threshold**: If the exponential model has R-squared below 0.95, the data may not be suitable for Figaro analysis; check FASTQ quality and library preparation.
- **Overlap Requirements**: Longer overlap requirements (e.g., 20bp for DADA2) mean more 3' bases must be retained, which may decrease overall sequence quality.

## Examples

### Basic trimming optimization
**Args:** `figaro -i /path/to/fastqs -o results/ -a 425 -f 20 -r 20`
**Explanation:** Analyzes FASTQ files in the input directory for a 425bp amplicon (excluding primers) with 20bp forward and reverse primers. Outputs optimal trimming parameters to the results directory.

### Custom minimum overlap
**Args:** `figaro -i /path/to/fastqs -o results/ -a 425 -f 20 -r 20 -m 15`
**Explanation:** Sets minimum overlap to 15bp instead of the default 20bp. Use when amplicons have shorter expected overlap or when prioritizing quality over read length.

### Subsampling for large datasets
**Args:** `figaro -i /path/to/fastqs -o results/ -a 425 -f 20 -r 20 -s 10`
**Explanation:** Analyzes approximately 1/10 of reads (subsample=10) to speed up analysis for large datasets. Default subsampling is auto-calculated based on file size.

### Custom percentile threshold
**Args:** `figaro -i /path/to/fastqs -o results/ -a 425 -f 20 -r 20 -p 90`
**Explanation:** Uses 90th percentile instead of default 83rd. Higher percentile retains more reads but may include lower quality sequences.

### Using Zymo naming standard
**Args:** `figaro -i /path/to/fastqs -o results/ -a 425 -f 20 -r 20 -F zymo`
**Explanation:** Uses Zymo Services naming convention instead of the default Illumina standard for identifying forward/reverse reads.

### Docker deployment
**Args:** `docker container run --rm -e AMPLICONLENGTH=450 -e FORWARDPRIMERLENGTH=20 -e REVERSEPRIMERLENGTH=20 -v /path/to/fastqs:/data/input -v /path/to/output:/data/output figaro`
**Explanation:** Runs Figaro via Docker container. Environment variables specify amplicon and primer lengths, while volumes mount input/output directories.
