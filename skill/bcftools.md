---
name: bcftools
category: variant-calling
description: BCFtools - Utilities for manipulating variant calls in VCF/BCF format
tags: [vcf, bcf, variant-calling, variant-filtering, variant-annotation]
author: oxo-call-community
source_url: "https://github.com/samtools/bcftools"
---

## Concepts

- **Tool Overview**: BCFtools is a set of utilities for manipulating variant calls in VCF and BCF formats, including filtering, annotation, comparison, and conversion.

- **Format Support**: Works transparently with VCF, bgzipped VCF, and BCF formats with automatic detection.

- **Index Support**: Utilizes indexed files for efficient random access and region-based operations.

- **Streaming**: Most commands support streaming from pipes, enabling flexible workflow construction.

- **Plugin Architecture**: Extensible through plugins for specialized analyses.

## Pitfalls

- **Index Required**: Many operations require indexed VCF/BCF files. Use tabix to create indexes.

- **Memory Usage**: Large VCF files may require substantial memory. Use bgzip compression and indexing.

- **Reference Required**: Some operations (e.g., consensus calling) require reference genome.

- **Version Compatibility**: VCF format versions may differ. Ensure compatibility with tools.

## Examples

### Filter variants by quality
**Args:** `bcftools filter -i 'QUAL>30 && DP>10' -o filtered.vcf input.vcf`
**Explanation:** Filters variants with quality >30 and depth >10.

### Extract specific region
**Args:** `bcftools view -r chr1:1000-2000 -o region.vcf input.vcf`
**Explanation:** Extracts variants from specific genomic region.

### Merge multiple VCFs
**Args:** `bcftools merge -o merged.vcf sample1.vcf.gz sample2.vcf.gz`
**Explanation:** Merges multiple VCF files into single file.

### Call consensus sequence
**Args:** `bcftools consensus -f reference.fasta input.vcf > consensus.fasta`
**Explanation:** Generates consensus sequence from variants and reference.

### Annotate with database
**Args:** `bcftools annotate -a annotations.bed.gz -c CHROM,POS,REF,ALT,INFO/Annotation -o annotated.vcf input.vcf`
**Explanation:** Annotates variants with information from BED file.

### View statistics
**Args:** `bcftools stats input.vcf > stats.txt`
**Explanation:** Generates comprehensive statistics for VCF file.

### Convert to other formats
**Args:** `bcftools query -f '%CHROM\t%POS\t%REF\t%ALT\n' input.vcf > variants.tsv`
**Explanation:** Extracts specific fields from VCF in custom format.

### Normalize variants
**Args:** `bcftools norm -f reference.fasta -o normalized.vcf input.vcf`
**Explanation:** Normalizes variant representation (left-aligns, splits multiallelics).

### Compare VCFs
**Args:** `bcftools isec -p output_dir/ sample1.vcf.gz sample2.vcf.gz`
**Explanation:** Identifies common and unique variants between VCF files.

### Index VCF file
**Args:** `bcftools index input.vcf.gz`
**Explanation:** Creates index for VCF file for efficient access.
