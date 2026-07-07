---
name: gff2bed
category: formatting
description: gff2bed - Convert GFF3-formatted data to BED format.
tags: [gff2bed, formatting, GFF3, BED, conversion]
author: oxo-call-community
source_url: "https://gitlab.com/salk-tm/gff2bed"
---

## Concepts
- **Format Conversion**: Converts GFF3 to BED format.
- **Genomic Annotations**: Processes genomic annotation data.
- **Data Transformation**: Transforms annotation formats.
- **Track Conversion**: Converts genome browser tracks.
- **Batch Processing**: Processes multiple files.

## Pitfalls
- **Format Compatibility**: Requires valid GFF3 format.
- **Coordinate System**: Requires correct coordinate handling.
- **Annotation Quality**: Depends on input annotation quality.
- **Output Format**: Requires correct BED format.
- **Data Loss**: May lose information during conversion.

## Examples
### Convert GFF3 to BED
**Args:** `gff2bed -i annotations.gff3 -o annotations.bed`
**Explanation:** Converts GFF3 to BED format.

### With options
**Args:** `gff2bed -i annotations.gff3 -s -o annotations.bed`
**Explanation:** Converts with strand information.

### Batch processing
**Args:** `gff2bed -l files.txt -o ./beds/`
**Explanation:** Processes multiple GFF3 files.

### Compressed input
**Args:** `gff2bed -i annotations.gff3.gz -o annotations.bed`
**Explanation:** Handles compressed input files.

### Generate report
**Args:** `gff2bed -i annotations.gff3 -r -o report.txt`
**Explanation:** Generates conversion report.