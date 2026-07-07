---
name: multisub
category: utility
description: multiSub is a command-line tool to prepare and submit SARS-CoV-2 genome sequences to NCBI Genbank, EBI ENA and GISAID repositories.
tags: [multisub, sars-cov-2, covid-19, genome-submission, ncbi, gisaid, ena]
author: oxo-call-community
source_url: "https://github.com/maximilianh/multiSub"
---

## Concepts

- **Tool Overview**: multiSub is a command-line tool for preparing and submitting SARS-CoV-2 genome sequences to the NCBI Genbank, EBI ENA, and GISAID sequence repositories. It automates the metadata formatting and submission process required by each repository.
- **Core Function**: Streamlines SARS-CoV-2 genome submission by handling metadata preparation, fasta formatting, and compatibility with each repository's specific requirements. Supports both individual and batch submissions.
- **Input Format**: Accepts FASTA files containing SARS-CoV-2 genome sequences. Requires sample metadata in tabular format (TSV/CSV) with fields like sample collection date, location, host, and variant designation.
- **Output**: Generates properly formatted submission files ready for upload to each repository. Creates separate submission packages for Genbank, ENA, and GISAID with repository-specific metadata requirements.
- **Workflow**: Validates sequences against SARS-CoV-2 reference, checks for N content and sequence quality, and generates assembly quality reports before submission.
- **Installation**: Available via pip (`pip install multiSub`) and Bioconda (`conda install -c bioconda multisub`).

## Pitfalls

- **Metadata Requirements**: Each repository has different mandatory metadata fields. multiSub validates against repository-specific schemas but users must ensure accurate sample information.
- **Sequence Quality Thresholds**: Sequences with excessive N characters or low coverage may be rejected. The tool performs pre-submission quality checks but manual review is recommended.
- **GISAID Account**: GISAID submissions require prior registration and approval. The tool prepares GISAID-formatted files but cannot automate the actual GISAID submission process.
- **Version Compatibility**: Repository submission formats change frequently (especially during pandemic updates). Ensure using the latest multiSub version for current submission requirements.
- **Batch Size Limits**: Large batch submissions may hit repository-specific limits. Split large batches into smaller chunks to avoid timeouts or validation failures.
- **Sample Naming Conventions**: Sample names must follow repository-specific naming rules. Special characters, spaces, or length restrictions may cause submission failures.

## Examples

### Validate a FASTA file before submission
**Args:** `multiSub validate sequences.fasta --metadata samples.tsv`
**Explanation:** Validates sequences and metadata against submission requirements. Checks sequence quality, N content, and metadata completeness before generating submission files.

### Prepare Genbank submission files
**Args:** `multiSub submit sequences.fasta --metadata samples.tsv --repository genbank --out genbank_submission/`
**Explanation:** Generates Genbank-formatted submission files in the specified output directory. Includes Sequin-format files and metadata spreadsheet.

### Submit to GISAID
**Args:** `multiSub submit sequences.fasta --metadata samples.tsv --repository gisaid --out gisaid_submission/`
**Explanation:** Prepares GISAID-compatible submission files. Note: Actual GISAID upload requires manual login to GISAID website.

### Generate submission for all three repositories
**Args:** `multiSub submit sequences.fasta --metadata samples.tsv --repository all --out all_submissions/`
**Explanation:** Creates separate submission packages for Genbank, ENA, and GISAID in subdirectories. Each package follows that repository's specific format requirements.

### Check sequence quality summary
**Args:** `multiSub quality sequences.fasta --min-length 29000 --max-n 0.05`
**Explanation:** Reports quality metrics for all sequences, including length distribution, N content percentage, and identifies sequences that may fail submission thresholds.

### Batch submission with multiple batches
**Args:** `multiSub submit batch*.fasta --metadata all_samples.tsv --repository ncbi --batch-size 100`
**Explanation:** Submits multiple FASTA files as separate batches of 100 sequences each to stay within repository limits and enable progress tracking.
