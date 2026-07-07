---
name: gff3toembl
category: annotation
description: gff3toembl - Convert GFF3 files to EMBL format for genome submission.
tags: [gff3toembl, annotation, EMBL, GFF3, submission]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/gff3toembl/"
---

## Concepts
- **Format Conversion**: Converts GFF3 to EMBL format.
- **Genome Submission**: Prepares genomes for EMBL submission.
- **Prokka Integration**: Works with Prokka annotations.
- **Data Validation**: Validates annotation data.
- **Quality Control**: Ensures submission quality.

## Pitfalls
- **Format Requirements**: Must meet EMBL format requirements.
- **Annotation Quality**: Requires high-quality annotations.
- **Data Completeness**: Requires complete annotation data.
- **Validation**: Results should be validated before submission.
- **Submission Process**: Complex submission process.

## Examples
### Convert to EMBL
**Args:** `gff3toembl -i annotations.gff3 -f genome.fasta -o embl.txt`
**Explanation:** Converts GFF3 to EMBL format.

### With options
**Args:** `gff3toembl -i annotations.gff3 -f genome.fasta -s "MySpecies" -o embl.txt`
**Explanation:** Specifies species name.

### Batch processing
**Args:** `gff3toembl -l samples.txt -o ./embl/`
**Explanation:** Processes multiple samples.

### Validate output
**Args:** `gff3toembl -i annotations.gff3 -f genome.fasta -v -o embl.txt`
**Explanation:** Validates EMBL output.

### Generate report
**Args:** `gff3toembl -i annotations.gff3 -f genome.fasta -r -o report.html`
**Explanation:** Generates submission report.