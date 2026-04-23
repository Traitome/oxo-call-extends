---
name: canvas
category: variant-calling
description: Copy number variant (CNV) calling from DNA sequencing data
tags: [canvas, cnv, copy-number, structural-variant]
author: oxo-call-community
source_url: "https://github.com/Illumina/canvas"
---

## Concepts

- **Tool Overview**: Canvas calls copy number variants from DNA sequencing data.
- **Core Function**: Detects CNVs including deletions, duplications, and LOH events.
- **Input**: Aligned BAM/CRAM files and reference genome.
- **Output**: VCF file with CNV calls.
- **Algorithm**: Uses read-depth and B-allele frequency for CNV detection.
- **Installation**: Install via bioconda: `conda install -c bioconda canvas`

## Pitfalls

- **Reference Required**: Must use the same reference as alignment.
- **BAM Index**: Input BAM must be indexed with .bai file.
- **Memory Usage**: Large genomes require significant memory.
- **Windows**: CNV calls are made in variable-sized windows.

## Examples

### Run CNV calling
**Args:** `Canvas germline-wgs -b aligned.bam -g reference.fa -o cnv_output/`
**Explanation:** Calls germline CNVs from whole-genome sequencing data.

### Specify sample name
**Args:** `Canvas germline-wgs -b aligned.bam -g reference.fa -n sample1 -o output/`
**Explanation:** Sets sample name in output VCF.

### Use custom filter
**Args:** `Canvas germline-wgs -b aligned.bam -g reference.fa --filter-vcf filters.vcf -o output/`
**Explanation:** Applies custom filters to CNV calls.

### Display help
**Args:** `Canvas --help`
**Explanation:** Shows all available options and usage information.
