---
name: gffread
category: formatting
description: gffread - GFF/GTF utility for format conversions, region filtering, and FASTA sequence extraction.
tags: [gffread, formatting, GFF, GTF, FASTA, conversion]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/stringtie/gff.shtml#gffread"
---

## Concepts
- **Format Conversion**: Converts between GFF and GTF formats.
- **Sequence Extraction**: Extracts sequences from GFF/GTF.
- **Region Filtering**: Filters genomic regions.
- **Transcript Processing**: Processes transcript annotations.
- **Quality Control**: Validates GFF/GTF files.

## Pitfalls
- **Format Compatibility**: Requires correct input format.
- **Coordinate System**: Requires correct coordinate handling.
- **Memory Usage**: Large files require significant memory.
- **Sequence Quality**: Depends on reference genome quality.
- **Validation**: Requires validation of output.

## Examples
### Convert GFF to GTF
**Args:** `gffread -E annotations.gff3 -T -o annotations.gtf`
**Explanation:** Converts GFF3 to GTF format.

### Extract sequences
**Args:** `gffread -w transcripts.fasta -g genome.fasta annotations.gtf`
**Explanation:** Extracts transcript sequences.

### Filter by region
**Args:** `gffread -r chr1:1-100000 annotations.gtf -o filtered.gtf`
**Explanation:** Filters features by region.

### Validate GFF
**Args:** `gffread -E annotations.gff3 -o /dev/null`
**Explanation:** Validates GFF3 file.

### Batch processing
**Args:** `gffread -E annotations.gff3 -T -o annotations.gtf`
**Explanation:** Converts multiple files in batch.