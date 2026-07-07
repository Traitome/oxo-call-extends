---
name: gnali
category: variant-calling
description: gNALI (gene nonessentiality and loss-of-function identifier) queries gnomAD to identify potential loss-of-function variants in gene lists.
tags: [gnali, variant-calling, loss-of-function, gnomad, gene]
author: oxo-call-community
source_url: "https://phac-nml.github.io/gnali/"
---

## Concepts

- **Gene Nonessentiality Analysis**: gNALI identifies genes with loss-of-function (LoF) variants by querying the gnomAD database. It focuses on high-confidence LoF variants including start lost, stop gained, splice donor, splice acceptor, and frameshift variants.

- **Input Format**: The tool accepts a plain text file containing gene names as HGNC symbols, one per line. Genes in non-standard formats will be logged but not analyzed. Supported input formats include TXT, TSV, and CSV.

- **Database Support**: gNALI supports gnomADv2.1.1 (GRCh37/hg19) and gnomADv3.1.1 (GRCh38/hg38). Users can also configure custom VCF databases with appropriate YAML configuration files.

- **Filtering System**: The tool provides predefined filters (homozygous, heterozygous, homozygous-controls) and additional filters based on VCF INFO column annotations (AC, AN, AF, DP, MQ, QD, etc.).

- **Output Files**: gNALI generates two output files - a basic file listing genes with LoF variants (Nonessential_Host_Genes_(Basic).txt) and a detailed file with variant annotations (Nonessential_Host_Genes_(Detailed).txt). Using --vcf flag generates a third VCF output file.

- **Population Frequency Data**: With the --pop_freqs flag, gNALI outputs allele count (AC), allele number (AN), and allele frequency (AF) by population group for each variant.

## Pitfalls

- **HGNC Symbol Requirement**: Input gene names must be valid HGNC symbols. Non-standard gene names (e.g., Entrez IDs, Ensembl IDs without conversion) will not be recognized and will be logged in the output directory.

- **Default High-Confidence Filtering**: By default, gNALI filters for high-confidence LoF variants only. There is no way to disable this default filtering behavior - use predefined or additional filters to refine results.

- **Output Directory Pre-existence**: The --output directory must not already exist. Use the --force flag to overwrite an existing output directory.

- **Config Template Generation**: When generating custom database configuration templates using --config_template_grch37 or --config_template_grch38, ensure the resulting YAML file is properly filled before using with --config.

- **VCF Header Compatibility**: When using custom databases, ensure the VCF headers contain all annotations referenced in additional filters, otherwise filtering may fail silently.

## Examples

### Query genes for loss-of-function variants
**Args:** `--input genes.txt --output results/`
**Explanation:** This basic command queries gnomADv2.1.1 (default database) for LoF variants in genes listed in genes.txt. Each gene name should be on a separate line using HGNC symbols. The results will be written to a new directory called "results/" containing basic and detailed output files.

### Use gnomAD v3.1.1 with GRCh38
**Args:** `--input genes.txt --database gnomADv3.1.1 --output results_grch38/`
**Explanation:** This command explicitly specifies the gnomAD v3.1.1 database which uses the GRCh38 reference genome. Use this when your gene list is based on GRCh38 coordinates or when you need more recent variant calling.

### Filter for homozygous variants only
**Args:** `--input genes.txt --predefined_filters homozygous --output homozygous_results/`
**Explanation:** The --predefined_filters option applies built-in filters. Using "homozygous" selects only variants with a non-zero number of homozygous samples in the database, which is useful for identifying recessive candidate genes.

### Apply multiple filters and get population frequencies
**Args:** `--input genes.txt --predefined_filters homozygous-controls --additional_filters "AC>3" "AN>10" --pop_freqs --output filtered_results/`
**Explanation:** Combining predefined and additional filters provides fine-grained control. This example filters for variants with homozygous samples in controls AND alternate allele count > 3 AND total allele number > 10. The --pop_freqs flag adds population-stratified allele frequency information to the detailed output.

### Generate custom database configuration template
**Args:** `--config_template_grch37`
**Explanation:** This command creates a fillable YAML configuration template for a GRCh37-based VCF database. Edit the template to point to your custom VCF files, then use --config template.yaml to query your database instead of gnomAD.

### Overwrite existing output directory
**Args:** `--input genes.txt --output existing_results/ --force`
**Explanation:** The --force flag allows gNALI to overwrite an already existing output directory. Without this flag, gNALI will refuse to run if the output directory exists to prevent accidental data loss.
