---
name: agat
category: annotation
description: Another GFF Analysis Toolkit - comprehensive suite for handling gene annotations in any GTF/GFF format
tags: [gff, gtf, annotation, conversion, filtering, statistics]
author: oxo-call-community
source_url: "https://github.com/NBISweden/AGAT"
---

## Concepts

- **Tool Overview**: AGAT is a powerful GFF/GTF toolkit that can check, fix, pad missing information, and perform almost any operation on gene annotation files.
- **Core Function**: Processes, validates, converts, filters, and analyzes GFF/GTF annotation files with robust parsing that handles format variants and errors.
- **Input/Output**: Input: GFF/GTF files (any variant). Output: Standardized GFF3/GTF2, statistics reports, filtered annotations, extracted sequences.
- **Tool Categories**: `agat_convert_*` (format conversion), `agat_sp_*` (standard processing), `agat_sq_*` (sequence/query operations).
- **Installation**: Install via bioconda: `conda install -c bioconda agat`

## Pitfalls

- **Format Variants**: AGAT handles many GFF/GTF variants but may need explicit format specification for edge cases.
- **Feature Hierarchy**: Some operations require proper parent-child feature relationships - use `agat_sp_statistics.pl` to check structure.
- **Memory Usage**: Large annotation files may require significant memory - consider splitting large files.
- **ID Uniqueness**: AGAT can fix duplicate IDs but may change original identifiers - check ID management tools.

## Examples

### Display help for a tool
**Args:** `agat_sp_statistics.pl --help`
**Explanation:** Shows options for the statistics tool to analyze annotation file.

### Convert GFF to GTF format
**Args:** `agat_convert_sp_gff2gtf.pl --gff input.gff3 --gtf output.gtf`
**Explanation:** Converts GFF3 format to GTF2 format for tools requiring GTF input.

### Fix and standardize annotation
**Args:** `agat_sp_fix_features_locations_duplicated.pl --gff input.gff --out fixed.gff`
**Explanation:** Fixes duplicated feature locations and standardizes the annotation file.

### Generate annotation statistics
**Args:** `agat_sp_statistics.pl --gff annotation.gff3`
**Explanation:** Produces comprehensive statistics about gene models, exons, introns, and other features.

### Filter by gene length
**Args:** `agat_sp_filter_gene_by_length.pl --gff input.gff --min 200 --out filtered.gff`
**Explanation:** Retains only genes with minimum length of 200bp.

### Add intron features
**Args:** `agat_sp_add_introns.pl --gff input.gff --out with_introns.gff`
**Explanation:** Adds explicit intron features to annotation if missing.

### Extract sequences from annotation
**Args:** `agat_sp_extract_sequences.pl --gff annotation.gff3 --fasta genome.fa --type cds --out sequences.fa`
**Explanation:** Extracts CDS sequences based on annotation coordinates.

### Keep only longest isoform
**Args:** `agat_sp_keep_longest_isoform.pl --gff input.gff --out longest_only.gff`
**Explanation:** Retains only the longest transcript isoform for each gene.

### Compare two annotations
**Args:** `agat_sp_compare_two_annotations.pl --gff1 annot1.gff3 --gff2 annot2.gff3`
**Explanation:** Compares two annotation files and reports differences in gene structure.
