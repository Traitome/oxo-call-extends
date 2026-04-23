---
name: atlas-gene-annotation-manipulation
category: annotation
description: Atlas Gene Annotation Manipulation - Scripts for manipulating gene annotation files
tags: [annotation-manipulation, gtf, gff, gene-models]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/atlas-gene-annotation-manipulation"
---

## Concepts

- **Tool Overview**: Collection of scripts for manipulating and processing gene annotation files in GTF/GFF formats for Expression Atlas pipelines.

- **Format Conversion**: Converts between different annotation formats and coordinate systems.

- **Annotation Filtering**: Filters annotations by gene type, biotype, or other attributes.

- **Coordinate Handling**: Manages coordinate systems, chromosome naming conventions, and genome assembly versions.

## Pitfalls

- **Format Variations**: GTF/GFF formats have variations between sources. Ensure input format matches expected format.

- **Chromosome Naming**: Different conventions (chr1 vs 1) can cause coordinate mismatches. Standardize before processing.

- **Gene ID Mapping**: Gene identifiers may change between annotation versions. Use appropriate mapping files.

- **Assembly Versions**: Ensure annotation matches genome assembly version used for alignment.

## Examples

### Filter protein-coding genes
**Args:** `filter_gtf.py --input annotation.gtf --biotype protein_coding --output filtered.gtf`
**Explanation:** Extracts only protein-coding genes from annotation file.

### Convert chromosome names
**Args:** `convert_chromosomes.py --input annotation.gtf --format ucsc --output converted.gtf`
**Explanation:** Converts chromosome names to UCSC format (adds 'chr' prefix).

### Merge annotation files
**Args:** `merge_gtf.py annotation1.gtf annotation2.gtf --output merged.gtf`
**Explanation:** Merges multiple GTF annotation files into single file.

### Extract gene features
**Args:** `extract_features.py --input annotation.gtf --features gene,exon --output features.gtf`
**Explanation:** Extracts only specified feature types from annotation.
