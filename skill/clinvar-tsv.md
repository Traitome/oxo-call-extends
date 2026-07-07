---
name: clinvar-tsv
category: formatting
description: Snakemake-based program to download ClinVar and convert to easy-to-use TSV files
tags: [clinvar-tsv, clinvar, tsv, data-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bihealth/clinvar-tsv"
---

## Concepts

- **Tool Overview**: clinvar-tsv is a Snakemake-based pipeline that downloads ClinVar data and converts it into easy-to-use TSV (Tab-Separated Values) files for downstream analysis.
- **Core Function**: Automates downloading, parsing, and converting ClinVar XML data into structured TSV format.
- **Algorithm**: Uses Snakemake workflow management to orchestrate data download and conversion steps.
- **Input**: ClinVar XML data (automatically downloaded).
- **Output**: Structured TSV files with variant information.
- **Application**: Variant annotation, clinical variant analysis, and database querying.
- **Installation**: Install via bioconda: `conda install -c bioconda clinvar-tsv`

## Pitfalls

- **Network Access**: Requires internet access to download ClinVar data.
- **Data Size**: ClinVar database is large; may require significant storage.
- **Update Frequency**: May need regular updates to keep data current.
- **Snakemake Dependencies**: Requires Snakemake to run the pipeline.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Run full pipeline
**Args:** `snakemake -s clinvar-tsv.smk --cores 4`
**Explanation:** Runs the complete pipeline to download and convert ClinVar data.

### Download only
**Args:** `snakemake -s clinvar-tsv.smk download --cores 1`
**Explanation:** Only downloads the ClinVar data without conversion.

### Convert existing data
**Args:** `snakemake -s clinvar-tsv.smk convert --cores 2`
**Explanation:** Converts already downloaded data to TSV format.

### Display help
**Args:** `snakemake -s clinvar-tsv.smk --help`
**Explanation:** Shows available targets and options.