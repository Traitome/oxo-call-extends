---
name: arcsv
category: utility
description: ArcSV - Pipeline to detect structural variants in archaic human genomes
tags: [arcsv, utility, structural-variants, archaic-human, ancient-dna, genome-analysis]
author: oxo-call-community
source_url: "https://github.com/xuxif/ArcSV"
---

## Concepts

- **Tool Overview**: ArcSV is a specialized pipeline for detecting structural variants (SVs) in archaic human genomes, including Neanderthal and Denisovan samples. Version 1.0.2.
- **Core Function**: Identifies deletions, duplications, inversions, and other structural variants using ancient DNA sequencing data.
- **Ancient DNA Support**: Designed specifically for fragmented, low-coverage ancient DNA sequences typical of archaeological samples.
- ** archaic Human Analysis**: Optimized for detecting variants in archaic human genomes compared to modern human reference.
- **Input/Output**: Processes BAM/CRAM alignment files and outputs VCF format structural variant calls.
- **Integration**: Works with standard bioinformatics pipelines and variant calling formats.
- **Installation**: `conda install -c bioconda arcsv` or build from GitHub source.

## Pitfalls

- **Ancient DNA Damage**: Deaminated bases and fragmentation affect variant detection accuracy.
- **Low Coverage**: Ancient samples often have low coverage. Results may be limited by sequencing depth.
- **Reference Genome**: Requires appropriate reference genome (e.g., hs38 for human analysis).
- **Authentication**: Some detected variants may be modern human contamination rather than true archaic variants.
- **Computational Resources**: Large genomes require significant processing resources.

## Examples

### Display help
**Args:** `arcsv --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic structural variant detection
**Args:** `arcsv detect --bam archaic_sample.bam --ref hg38.fa --out variants.vcf`
**Explanation:** Performs structural variant detection on archaic human sample aligned to hg38 reference.

### Configure sensitivity
**Args:** `arcsv detect --bam sample.bam --ref hg38.fa --out variants.vcf --min_size 50 --max_size 100000`
**Explanation:** Sets minimum SV size to 50bp and maximum to 100kb for detection.

### Process multiple samples
**Args:** `arcsv batch --input_dir bam_files/ --ref hg38.fa --output_dir results/`
**Explanation:** Batch processes multiple BAM files in the specified directory.

### Generate detailed report
**Args:** `arcsv report --vcf variants.vcf --output report.html --format html`
**Explanation:** Creates interactive HTML report of detected structural variants with annotations.

### Filter variants by quality
**Args:** `arcsv filter --input variants.vcf --min_support 5 --out filtered_variants.vcf`
**Explanation:** Filters variants to those supported by at least 5 reads or spanning evidence.

### Comparative analysis
**Args:** `arcsv compare --vcf1 neanderthal.vcf --vcf2 denisovan.vcf --output comparison.csv`
**Explanation:** Compares structural variants between two archaic human samples.