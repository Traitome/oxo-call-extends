---
name: rsidx
category: variant-analysis
description: rsidx is a library and command-line tool for indexing VCF files to enable fast random access searches by RSID (dbSNP identifier).
tags: ["rsidx", "vcf", "indexing", "rsid", "gwas", "variant-analysis"]
author: oxo-call-community
source_url: "https://github.com/bioforensics/rsidx"
---

## Concepts

- **Tool Overview**: rsidx (v0.3.1, Bioforensics Lab) is a tool for creating SQLite-based indexes of VCF files that allow fast lookup of variants by their RSID (dbSNP identifier). It extracts RSIDs and maps them to chromosome positions for efficient queries.
- **Core Function**: Builds an index mapping RSIDs to chromosome-position coordinates, enabling rapid retrieval of specific variants without scanning the entire VCF file. Particularly useful for GWAS summary data analysis.
- **Algorithm**: Parses VCF files to extract ID field (containing RSIDs), creates a SQLite database with RSID as primary key and chromosome/position as values. Uses binary search for fast lookups.
- **Input Format**: VCF or VCF.gz files. Supports standard VCF format with RSIDs in the ID column.
- **Output Format**: SQLite database file (`.rsidx`) containing indexed RSID-to-position mappings. Query results returned as VCF records or tabular format.
- **Use Case**: Fast variant lookup in large GWAS datasets, annotation of variants by RSID, integration with GWAS analysis pipelines, and quick validation of variant identifiers.

## Pitfalls

- **Requires RSIDs in VCF ID field**: Indexing fails if variants lack RSID annotations. Use `bcftools annotate` to add RSIDs before indexing.
- **Case sensitivity**: RSIDs must be uppercase (e.g., "rs12345", not "RS12345"). Mixed-case RSIDs may not be found.
- **Memory for large VCF files**: Indexing whole-genome VCFs (>10M variants) requires sufficient memory. Consider chunking by chromosome for very large files.
- **SQLite database size**: Index files are typically 10-20% of VCF size. Store on fast storage for optimal query performance.
- **Multi-allelic variants**: rsidx indexes the first allele only for multi-allelic sites. Querying by RSID returns all alleles at that position.
- **No support for non-RSID identifiers**: Designed specifically for dbSNP RSIDs. Custom identifiers require preprocessing.

## Examples

### Create index for a VCF file
**Args:** `rsidx build input.vcf.gz output.rsidx`
**Explanation:** `build` subcommand creates an index from `input.vcf.gz` and saves it to `output.rsidx`. Automatically detects gzipped input.

### Query by single RSID
**Args:** `rsidx query output.rsidx rs12345`
**Explanation:** `query` subcommand looks up RSID `rs12345` in the index and returns the chromosome and position.

### Batch query multiple RSIDs
**Args:** `rsidx query output.rsidx -l rsids.txt`
**Explanation:** `-l` specifies a file containing one RSID per line. Returns all matching variants in tabular format.

### Extract variants from VCF using index
**Args:** `rsidx extract input.vcf.gz output.rsidx rs12345 > variant.vcf`
**Explanation:** `extract` retrieves the full VCF record for `rs12345` from the indexed file. Outputs to stdout or specified file.

### Build index with progress
**Args:** `rsidx build -v input.vcf.gz output.rsidx`
**Explanation:** `-v` enables verbose mode, showing progress during index creation. Useful for large VCF files.

### Validate index integrity
**Args:** `rsidx validate output.rsidx`
**Explanation:** `validate` checks the index for corruption or inconsistencies. Reports any errors found.

### Convert index to BED format
**Args:** `rsidx export output.rsidx > positions.bed`
**Explanation:** `export` converts the index to BED format for use with other tools. Each line contains chromosome, start, end, and RSID.