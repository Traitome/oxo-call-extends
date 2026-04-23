---
name: bio-vcf
category: variant-calling
description: Smart VCF parser for filtering and manipulating variant files
tags: [vcf, variant-filtering, parsing]
author: oxo-call-community
source_url: "https://github.com/vcflib/bio-vcf"
---

## Concepts
- **Tool Overview**: bio-vcf is a smart VCF parser for filtering, manipulating, and querying VCF (Variant Call Format) files. It provides flexible filtering and transformation capabilities.
- **Filtering**: Supports complex filters based on variant properties (quality, depth, allele frequency, etc.).
- **Manipulation**: Can extract specific fields, merge VCFs, and convert formats.
- **Streaming**: Processes VCF files in streaming mode for efficiency with large files.

## Pitfalls
- **Header Preservation**: VCF header information must be preserved for valid output.
- **Complex Filters**: Complex filter expressions may require careful syntax.

## Examples
### Filter variants by quality
**Args:** `bio-vcf filter -i input.vcf -e 'QUAL>30 && DP>10' -o filtered.vcf`
**Explanation:** Filters variants with quality >30 and depth >10.

### Extract specific fields
**Args:** `bio-vcf extract -i input.vcf -f CHROM,POS,REF,ALT > variants.tsv`
**Explanation:** Extracts chromosome, position, ref, and alt fields to TSV.

### Count variants per chromosome
**Args:** `bio-vcf count -i input.vcf --by-chrom`
**Explanation:** Reports variant counts per chromosome.
