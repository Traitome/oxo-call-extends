---
name: gff3toddbj
category: annotation
description: gff3toddbj - Create a DDBJ annotation file from GFF3 and FASTA files.
tags: [gff3toddbj, annotation, DDBJ, GFF3, FASTA]
author: oxo-call-community
source_url: "https://github.com/yamaton/gff3toddbj"
---

## Concepts
- **Annotation Conversion**: Converts annotations to DDBJ format.
- **Data Submission**: Prepares data for DDBJ submission.
- **Genomic Annotation**: Processes genomic annotation data.
- **Format Conversion**: Converts between annotation formats.
- **Sequence Integration**: Integrates sequence and annotation data.

## Pitfalls
- **Format Compatibility**: Requires valid GFF3 and FASTA.
- **DDBJ Requirements**: Must meet DDBJ submission requirements.
- **Sequence Quality**: Requires high-quality sequence data.
- **Annotation Completeness**: Requires complete annotations.
- **Validation**: Requires submission validation.

## Examples
### Create DDBJ file
**Args:** `gff3toddbj -g annotations.gff3 -f genome.fasta -o ddbj.txt`
**Explanation:** Creates DDBJ annotation file.

### With options
**Args:** `gff3toddbj -g annotations.gff3 -f genome.fasta -s "MySpecies" -o ddbj.txt`
**Explanation:** Specifies species name.

### Batch processing
**Args:** `gff3toddbj -l samples.txt -o ./ddbj/`
**Explanation:** Processes multiple samples.

### Validate output
**Args:** `gff3toddbj -g annotations.gff3 -f genome.fasta -v -o ddbj.txt`
**Explanation:** Validates DDBJ output.

### Generate report
**Args:** `gff3toddbj -g annotations.gff3 -f genome.fasta -r -o report.html`
**Explanation:** Generates submission report.