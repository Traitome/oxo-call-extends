---
name: convert_zero_one_based
category: formatting
description: Convert between zero-based and one-based coordinate systems
tags: [convert_zero_one_based, coordinate-conversion, bioinformatics-formats, gff, bed]
author: oxo-call-community
source_url: "https://github.com/griffithlab/convert_zero_one_based"
---

## Concepts

- **Tool Overview**: convert_zero_one_based is a utility for converting between zero-based and one-based coordinate systems commonly used in bioinformatics file formats.
- **Core Function**: Transforms genomic coordinates between zero-based (BED, SAM) and one-based (GFF, VCF) indexing systems.
- **Algorithm**: Adjusts start and end coordinates by +1 or -1 depending on conversion direction.
- **Input**: Genomic coordinate files in various formats (BED, GFF, VCF, etc.).
- **Output**: Coordinate-converted files in the target format.
- **Application**: Format conversion, data integration, and tool compatibility.
- **Installation**: Install via bioconda: `conda install -c bioconda convert_zero_one_based`

## Pitfalls

- **Off-by-one Errors**: Easy to introduce bugs when converting coordinates manually.
- **Half-open vs Closed Intervals**: BED uses half-open intervals, GFF uses closed.
- **Strand Awareness**: Negative strands require careful handling.
- **File Format Differences**: Different formats have different conventions.
- **Zero-based Start**: Some tools use zero-based start, others use one-based.

## Examples

### Convert BED to GFF (zero to one-based)
**Args:** `convert_zero_one_based -i input.bed -o output.gff -f bed2gff`
**Explanation:** Converts BED (zero-based) to GFF (one-based).

### Convert GFF to BED (one to zero-based)
**Args:** `convert_zero_one_based -i input.gff -o output.bed -f gff2bed`
**Explanation:** Converts GFF (one-based) to BED (zero-based).

### Convert VCF to BED
**Args:** `convert_zero_one_based -i input.vcf -o output.bed -f vcf2bed`
**Explanation:** Converts VCF positions to BED format.

### Display help
**Args:** `convert_zero_one_based --help`
**Explanation:** Shows all available options and usage information.