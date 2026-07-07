---
name: clinvar-this
category: programming
description: ClinVar Submission API Made Easy
tags: [clinvar-this, clinvar, variant-submission, api, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bihealth/clinvar-this"
---

## Concepts

- **Tool Overview**: clinvar-this simplifies interacting with the ClinVar Submission API, enabling programmatic submission of variant data to ClinVar.
- **Core Function**: Facilitates submission of genetic variants and their clinical interpretations to the ClinVar database.
- **Algorithm**: Handles API authentication, data formatting, and submission workflow.
- **Input**: Variant data in VCF or other standard formats.
- **Output**: Submission confirmation and tracking information.
- **Application**: Clinical variant submission, variant annotation, and database curation.
- **Installation**: Install via bioconda: `conda install -c bioconda clinvar-this`

## Pitfalls

- **API Credentials**: Requires valid ClinVar API credentials.
- **Data Format**: Must follow ClinVar submission format requirements.
- **Authentication**: Proper authentication is required for submissions.
- **Rate Limits**: May be subject to API rate limits.
- **Submission Guidelines**: Must follow ClinVar submission guidelines.

## Examples

### Submit variants to ClinVar
**Args:** `clinvar-this submit -i variants.vcf -c credentials.json -o submission.log`
**Explanation:** Submits variants from VCF file to ClinVar.

### Check submission status
**Args:** `clinvar-this status -s submission_id -c credentials.json`
**Explanation:** Checks the status of a submitted batch.

### Validate submission
**Args:** `clinvar-this validate -i variants.vcf`
**Explanation:** Validates variant data before submission.

### Display help
**Args:** `clinvar-this --help`
**Explanation:** Shows all available options and usage information.