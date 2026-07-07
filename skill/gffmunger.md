---
name: gffmunger
category: formatting
description: gffmunger - Munges GFF3 files exported from Chado database for WebApollo.
tags: [gffmunger, formatting, GFF3, Chado, WebApollo]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/gffmunger"
---

## Concepts
- **GFF3 Processing**: Processes GFF3 from Chado.
- **WebApollo Preparation**: Prepares files for WebApollo.
- **Data Transformation**: Transforms annotation data.
- **Format Conversion**: Converts between annotation formats.
- **Database Export**: Handles Chado exports.

## Pitfalls
- **Chado Specific**: Designed for Chado exports.
- **Format Compatibility**: Requires correct input format.
- **Data Loss**: May lose some annotation information.
- **WebApollo Compatibility**: Must meet WebApollo requirements.
- **Validation**: Requires validation after processing.

## Examples
### Munge GFF3
**Args:** `gffmunger -i chado_export.gff3 -o webapollo.gff3`
**Explanation:** Converts Chado GFF3 to WebApollo format.

### With options
**Args:** `gffmunger -i chado_export.gff3 -t -o webapollo.gff3`
**Explanation:** Preserves transcript information.

### Batch processing
**Args:** `gffmunger -l files.txt -o ./processed/`
**Explanation:** Processes multiple files.

### Validate output
**Args:** `gffmunger -i chado_export.gff3 -v -o webapollo.gff3`
**Explanation:** Validates output format.

### Generate report
**Args:** `gffmunger -i chado_export.gff3 -r -o report.html`
**Explanation:** Generates processing report.