---
name: libgff
category: annotation
description: Library for parsing GFF/GTF annotation files
tags: [libgff, annotation, GFF, GTF, parsing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/libgff"
---

## Concepts

- **GFF Parsing**: Parses GFF (General Feature Format) files
- **GTF Support**: Supports GTF (Gene Transfer Format)
- **Feature Extraction**: Extracts genomic features
- **Coordinate Handling**: Manages genomic coordinates
- **Annotation Processing**: Processes sequence annotations
- **File Validation**: Validates GFF/GTF format

## Pitfalls

- **Format Variants**: Different GFF versions have different formats
- **Coordinate System**: Zero-based vs one-based considerations
- **Memory Usage**: Large annotation files require memory management
- **Performance**: May be slow for very large files
- **Error Handling**: Requires careful validation
- **Version Compatibility**: Different GFF versions

## Examples

### Parse GFF file
**Args:** `gff parse -i annotation.gff -o parsed.json`
**Explanation:** Parses GFF file into structured format.

### Extract features
**Args:** `gff extract -i annotation.gff -t gene -o genes.gff`
**Explanation:** Extracts specific feature types.

### Validate file
**Args:** `gff validate -i annotation.gff`
**Explanation:** Validates GFF file format.

### Convert to BED
**Args:** `gff convert -i annotation.gff -o annotation.bed`
**Explanation:** Converts GFF to BED format.

### Count features
**Args:** `gff count -i annotation.gff`
**Explanation:** Counts features in GFF file.

### Filter by chromosome
**Args:** `gff filter -i annotation.gff -c chr1 -o chr1.gff`
**Explanation:** Filters features by chromosome.