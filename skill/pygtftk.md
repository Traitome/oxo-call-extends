---
name: pygtftk
category: annotation
description: pygtftk is a suite for manipulating genomic annotations in GTF format.
tags: [pygtftk, annotation, gtf, genomics]
author: oxo-call-community
source_url: "http://github.com/dputhier/pygtftk"
---

## Concepts

- **Tool Overview**: pygtftk manipulates GTF files.
- **Core Function**: GTF annotation processing.
- **Algorithm**: Uses GTF parsing.
- **Input Format**: Accepts GTF files.
- **Output**: Produces modified GTF.
- **Use Case**: Annotation analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Format Compliance**: Must follow GTF specs.
- **Gene Naming**: May have inconsistencies.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pygtftk --help`
**Explanation:** Shows available options and usage instructions.

### Filter GTF
**Args:** `pygtftk filter -i genes.gtf -t exon -o exons.gtf`
**Explanation:** Filters GTF by feature type.

### With parameters
**Args:** `pygtftk filter -i genes.gtf -p params.yaml -o filtered.gtf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pygtftk -v filter -i genes.gtf -o filtered.gtf`
**Explanation:** Runs with verbose output.

### Extract transcripts
**Args:** `pygtftk extract -i genes.gtf -a transcript_id -o transcripts.txt`
**Explanation:** Extracts transcript IDs.

### Merge GTFs
**Args:** `pygtftk merge -i genes1.gtf genes2.gtf -o merged.gtf`
**Explanation:** Merges multiple GTF files.

### Generate report
**Args:** `pygtftk stats -i genes.gtf --report report.html`
**Explanation:** Generates HTML report.