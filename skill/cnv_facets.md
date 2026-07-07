---
name: cnv_facets
category: variant-calling
description: Detect somatic copy number variants (CNV) in tumour-normal samples using next generation sequencing data
tags: [cnv_facets, cnv-calling, somatic-variants, cancer-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dariober/cnv_facets"
---

## Concepts

- **Tool Overview**: cnv_facets is a tool for detecting somatic copy number variants (CNVs) in tumor-normal paired sequencing samples using next-generation sequencing data.
- **Core Function**: Identifies copy number changes specific to tumor samples by comparing with matched normal samples.
- **Algorithm**: Uses read depth and allele frequency to detect CNVs and infer tumor purity and ploidy.
- **Input**: BAM files from tumor and normal samples, along with VCF file of germline variants.
- **Output**: CNV calls with copy number estimates, tumor purity, and ploidy.
- **Application**: Cancer genomics, somatic copy number analysis, and precision oncology.
- **Installation**: Install via bioconda: `conda install -c bioconda cnv_facets`

## Pitfalls

- **Matched Samples**: Requires matched tumor-normal pairs for accurate somatic calling.
- **Purity Estimation**: Tumor purity affects copy number estimation accuracy.
- **Segmentation**: May miss small CNVs depending on sequencing coverage.
- **GC Bias**: Requires proper normalization for GC content bias.
- **Complex Regions**: May have difficulty in repetitive or complex genomic regions.

## Examples

### Detect somatic CNVs
**Args:** `cnv_facets -t tumor.bam -n normal.bam -v germline.vcf -o results/`
**Explanation:** Detects somatic CNVs in tumor-normal pair.

### With purity constraint
**Args:** `cnv_facets -t tumor.bam -n normal.bam -v germline.vcf -p 0.7 -o results/`
**Explanation:** Constrains tumor purity to 0.7.

### Output VCF format
**Args:** `cnv_facets -t tumor.bam -n normal.bam -v germline.vcf -o cnv_calls.vcf -f vcf`
**Explanation:** Outputs CNV calls in VCF format.

### Display help
**Args:** `cnv_facets --help`
**Explanation:** Shows all available options and usage information.