---
name: genepender
category: variant-annotation
description: GenePender - Annotates overlapping BED-defined regions to variants in a VCF file, providing gene/exon context to variants.
tags: [genepender, variant-annotation, vcf, bed, gene-context]
author: oxo-call-community
source_url: "https://github.com/BioTools-Tek/genepender"
---

## Concepts
- **Variant Annotation**: Annotates variants with gene/exon context.
- **BED Integration**: Uses BED files to define genomic regions.
- **VCF Processing**: Processes VCF files for variant annotation.
- **Overlap Detection**: Identifies variants overlapping defined regions.
- **Context Annotation**: Provides functional context for variants.

## Pitfalls
- **BED Format**: Requires properly formatted BED files.
- **Coordinate Systems**: Must use consistent coordinate systems.
- **Overlap Sensitivity**: Overlap detection parameters matter.
- **Large Files**: Processing large VCF/BED files can be slow.
- **Memory Usage**: Requires sufficient memory for large datasets.

## Examples
### Annotate VCF with gene context
**Args:** `genepender -i variants.vcf -b genes.bed -o annotated.vcf`
**Explanation:** Annotates variants with gene/exon context from BED file.

### Annotate with multiple BED files
**Args:** `genepender -i variants.vcf -b genes.bed exons.bed -o annotated.vcf`
**Explanation:** Uses multiple BED files for annotation.

### Filter by overlap
**Args:** `genepender -i variants.vcf -b genes.bed -f -o filtered.vcf`
**Explanation:** Filters variants to include only those overlapping BED regions.

### Add custom annotations
**Args:** `genepender -i variants.vcf -b genes.bed -c annotation_key -o annotated.vcf`
**Explanation:** Adds custom annotation field to VCF.

### Batch processing
**Args:** `genepender -i ./vcf_files/ -b genes.bed -o ./annotated_output/`
**Explanation:** Processes multiple VCF files in batch.