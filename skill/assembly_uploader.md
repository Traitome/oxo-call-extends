---
name: assembly_uploader
category: expression
description: Assembly Uploader - Upload metagenome/metatranscriptome assemblies to ENA
tags: [assembly_uploader, expression, ena, submission, metagenomics]
author: oxo-call-community
source_url: "https://github.com/EBI-Metagenomics/assembly_uploader/blob/main/README.md"
---

## Concepts

- **Tool Overview**: Assembly Uploader is a set of Python scripts for uploading primary metagenome and metatranscriptome assemblies to the European Nucleotide Archive (ENA) on a per-study basis. Version 1.3.5.
- **Core Function**: Automates the submission process by generating XML files for study registration and creating manifests required for ENA submission via webin-cli.
- **ENA Submission**: Facilitates data submission to ENA, ensuring compliance with ENA's data standards and formats.
- **XML Generation**: Creates XML files for study registration, sample metadata, and experiment information.
- **Manifest Creation**: Generates submission manifests required by webin-cli for batch uploads.
- **Metagenomics Focus**: Specifically designed for metagenome and metatranscriptome assembly submissions.
- **Input/Output**: Accepts assembly files and metadata, outputs XML files and submission manifests.
- **Installation**: `conda install -c bioconda assembly_uploader` or install from GitHub.

## Pitfalls

- **ENA Credentials**: Requires valid ENA/Webin credentials for submission. Incorrect credentials cause submission failures.
- **Metadata Requirements**: Strict metadata requirements must be met. Missing or incorrect metadata causes rejection.
- **File Format**: Assembly files must conform to ENA format specifications. Incorrect formats cause validation errors.
- **Study Registration**: New studies require proper registration before assembly submission.
- **Network Dependency**: Requires internet connection for ENA API access and file uploads.
- **Webin-CLI Dependency**: Requires webin-cli to be installed and configured for actual submission.

## Examples

### Display help
**Args:** `assembly_uploader --help`
**Explanation:** Shows all available command-line options and usage information.

### Create submission manifest
**Args:** `assembly_uploader --input assembly.fasta --metadata metadata.tsv --output submission/`
**Explanation:** Creates submission manifest and XML files for ENA upload.

### Register new study
**Args:** `assembly_uploader --register-study --study-name "My Metagenome Study" --description "Analysis of soil metagenome"`
**Explanation:** Registers new study with ENA and outputs study XML for submission.

### Generate sample XML
**Args:** `assembly_uploader --generate-sample-xml --sample-file samples.tsv --output samples.xml`
**Explanation:** Generates XML file for sample registration from tab-separated metadata.

### Batch submission preparation
**Args:** `assembly_uploader --batch --input-dir assemblies/ --metadata metadata.tsv --output batch_submission/`
**Explanation:** Prepares multiple assemblies for batch submission to ENA.

### Validate submission
**Args:** `assembly_uploader --validate --input assembly.fasta --metadata metadata.tsv`
**Explanation:** Validates assembly and metadata before actual submission.

### Specify center name
**Args:** `assembly_uploader --input assembly.fasta --metadata metadata.tsv --center-name MY_INSTITUTE --output submission/`
**Explanation:** Specifies submitting center name for ENA tracking.

### Dry run mode
**Args:** `assembly_uploader --input assembly.fasta --metadata metadata.tsv --dry-run`
**Explanation:** Shows what would be generated without actual submission.

### Upload using webin-cli
**Args:** `assembly_uploader --input assembly.fasta --metadata metadata.tsv --output submission/ && webin-cli submit -username user -password pass -manifest submission/manifest.txt`
**Explanation:** Prepares submission files and uploads to ENA using webin-cli.