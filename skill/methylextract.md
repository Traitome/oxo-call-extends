---
name: methylextract
category: variant-calling
description: High-Quality methylation maps and SNV calling from whole genome bisulfite sequencing data
tags: [methylextract, variant-calling, methylation]
author: oxo-call-community
source_url: "http://bioinfo2.ugr.es/MethylExtract/"
---

## Concepts

- **Tool Overview**: MethylExtract v1.9.1 is a tool for generating high-quality methylation maps and calling SNVs from whole genome bisulfite sequencing data.
- **Core Function**: Generates methylation maps and calls SNVs from bisulfite sequencing data.
- **Methylation Mapping**: Creates high-resolution methylation maps.
- **SNV Calling**: Calls single nucleotide variants from bisulfite data.
- **Input/Output**: Accepts bisulfite sequencing reads; outputs methylation maps and SNV calls.
- **Integrated Analysis**: Combines methylation analysis with variant calling.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Analysis of whole-genome bisulfite data can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis accuracy depends on input data quality.
- **Reference Genome**: Requires reference genome for mapping.

## Examples

### Generate methylation map
**Args:** `methylextract -i reads.fastq -o methylation_map.txt`
**Explanation:** Generates high-quality methylation map from bisulfite reads.

### Call SNVs
**Args:** `methylextract snv -i reads.fastq -o snvs.vcf`
**Explanation:** Calls SNVs from bisulfite sequencing data.

### With reference genome
**Args:** `methylextract -i reads.fastq -r reference.fasta -o methylation_map.txt`
**Explanation:** Uses reference genome for mapping.

### Combined analysis
**Args:** `methylextract -i reads.fastq -o methylation_map.txt -s snvs.vcf`
**Explanation:** Performs both methylation mapping and SNV calling.

### Batch processing
**Args:** `methylextract -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.