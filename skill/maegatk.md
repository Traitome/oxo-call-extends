---
name: maegatk
category: variant-calling
description: Mitochondrial Alteration Enrichment and Genome Analysis Toolkit.
tags: [maegatk, variant-calling, mitochondrial, genomics]
author: oxo-call-community
source_url: "https://github.com/caleblareau/maegatk"
---

## Concepts

- **Tool Overview**: maegatk v0.2.0 - A toolkit for processing and quality control of mitochondrial genome variants from single-cell data.
- **Core Function**: Enriches and analyzes mitochondrial alterations from scATAC-seq or scRNA-seq data.
- **Input/Output**: Input: BAM files, VCF files; Output: Processed variants, quality metrics, visualization files.
- **Installation**: `conda install -c bioconda maegatk` or from GitHub source
- **MAESTER Data**: Specifically designed for MAESTER (Mitochondrial Alteration Enrichment from Single-cEll scATAC-sequeR) data.
- **Variant Filtering**: Provides quality control filters for mitochondrial variants.

## Pitfalls

- **Contamination**: Nuclear mitochondrial sequences (NUMTs) can contaminate results.
- **Coverage**: Low coverage in mitochondrial reads affects variant calling accuracy.
- **Heteroplasmy**: High heteroplasmy levels require careful interpretation.
- **Alignment Issues**: Mitochondrial genome alignment has unique challenges due to circular nature.
- **Quality Thresholds**: Incorrect quality thresholds may filter true variants or retain false ones.
- **Reference Genome**: Using incorrect mitochondrial reference can cause mapping errors.

## Examples

### Process MAESTER data
**Args:** `maegatk process -i input.bam -o output_dir -r reference.fasta`
**Explanation:** Processes raw BAM file and extracts mitochondrial variants.

### Call variants
**Args:** `maegatk call -i processed_data -o variants.vcf`
**Explanation:** Calls mitochondrial variants from processed data.

### Filter variants
**Args:** `maegatk filter -i variants.vcf -o filtered.vcf --min-qual 30`
**Explanation:** Filters variants based on quality score.

### Generate QC report
**Args:** `maegatk qc -i variants.vcf -o qc_report.html`
**Explanation:** Generates quality control report for mitochondrial variants.

### Visualize variants
**Args:** `maegatk plot -i variants.vcf -o variant_plot.pdf`
**Explanation:** Creates visualization of mitochondrial variant distribution.

### Merge multiple samples
**Args:** `maegatk merge -i sample1.vcf sample2.vcf -o merged.vcf`
**Explanation:** Merges variant calls from multiple samples.