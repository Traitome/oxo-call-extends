---
name: oncotator
category: variant-calling
description: Oncotator annotates human genomic point mutations and indels with cancer-relevant data.
tags: [oncotator, variant-calling, variant-annotation, cancer-genomics]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/oncotator"
---

## Concepts

- **Tool Overview**: Oncotator annotates genomic variants with cancer-specific information.
- **Core Function**: Adds cancer-relevant annotations to variants.
- **Algorithm**: Uses multiple annotation databases for comprehensive annotation.
- **Input Format**: Accepts VCF files with genomic variants.
- **Output**: Produces annotated variants with clinical and functional information.
- **Use Case**: Cancer genomics, variant interpretation, and precision medicine.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Database Updates**: Requires regular database updates.
- **Input Quality**: Results depend on variant call quality.
- **Memory Usage**: Large VCF files require memory.
- **Computational Cost**: Annotation can be computationally intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `oncotator --help`
**Explanation:** Shows available options and usage instructions.

### Annotate VCF
**Args:** `oncotator -i input.vcf -o annotated.vcf -d hg19`
**Explanation:** Annotates VCF file with cancer-relevant data.

### With custom database
**Args:** `oncotator -i input.vcf -o annotated.vcf -d custom.db`
**Explanation:** Uses custom annotation database.

### Output format
**Args:** `oncotator -i input.vcf -o annotated.tsv --tsv`
**Explanation:** Outputs results in TSV format.

### Verbose mode
**Args:** `oncotator -i input.vcf -o annotated.vcf -v`
**Explanation:** Runs with verbose output.

### Filter annotations
**Args:** `oncotator -i input.vcf -o annotated.vcf -f filter.txt`
**Explanation:** Filters annotations based on criteria.

### Batch processing
**Args:** `oncotator batch -d vcfs/ -o annotated/`
**Explanation:** Processes multiple VCF files.