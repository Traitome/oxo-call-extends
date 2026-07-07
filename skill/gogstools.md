---
name: gogstools
category: bioinformatics
description: GenOuest tools for manipulating Official Gene Sets (OGS) and gene annotations.
tags: [gogstools, gene-annotation, OGS, bioinformatics, utility]
author: oxo-call-community
source_url: "https://github.com/genouest/ogs-tools"
---

## Concepts

- **Official Gene Sets**: gogstools manipulates Official Gene Sets (OGS), which are standardized gene annotations for genomes.

- **Gene Annotation Processing**: Provides tools for filtering, merging, and transforming gene annotation files in various formats.

- **Format Conversion**: Converts between different gene annotation formats including GFF3, GTF, and BED.

- **Quality Control**: Validates gene structures and identifies potential issues in annotation files.

- **Gene Set Comparison**: Compares different gene sets to identify differences and commonalities.

- **Annotation Enrichment**: Enriches gene annotations with additional information from external databases.

## Pitfalls

- **Format Compatibility**: Ensure input files match the expected format. Mixed formats in a single file can cause parsing errors.

- **Annotation Versioning**: Different versions of gene annotations may have different structures. Check compatibility before processing.

- **Memory Usage**: Processing very large annotation files may require significant memory. Consider splitting large files.

- **Coordinate Systems**: Ensure consistency between 0-based and 1-based coordinate systems in input files.

- **Database Connectivity**: Some features require internet access for database queries. Ensure network connectivity.

## Examples

### Convert GFF3 to GTF
**Args:** `gogstools convert -i input.gff3 -f gtf -o output.gtf`
**Explanation:** Converts a GFF3 file to GTF format for compatibility with RNA-seq analysis tools.

### Filter genes by biotype
**Args:** `gogstools filter -i input.gtf -t protein_coding -o filtered.gtf`
**Explanation:** Filters the annotation file to include only protein-coding genes.

### Merge multiple annotations
**Args:** `gogstools merge -i annot1.gtf annot2.gtf -o merged.gtf`
**Explanation:** Merges two annotation files into a single combined annotation.

### Validate annotation file
**Args:** `gogstools validate -i input.gff3 -o report.txt`
**Explanation:** Validates the annotation file and generates a report of potential issues.

### Compare gene sets
**Args:** `gogstools compare -i set1.gtf set2.gtf -o comparison.txt`
**Explanation:** Compares two gene sets and identifies differences in gene structure and annotations.

### Enrich annotations
**Args:** `gogstools enrich -i input.gtf -d uniprot -o enriched.gtf`
**Explanation:** Enriches gene annotations with additional information from UniProt database.

### Extract gene sequences
**Args:** `gogstools extract -i input.gtf -g genome.fasta -o sequences.fasta`
**Explanation:** Extracts gene sequences from the genome based on annotation coordinates.