---
name: search_ncbi
category: data-retrieval
description: search_ncbi - Package for searching and processing NCBI data
tags: ["search_ncbi", "data-retrieval", "NCBI", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/Bluetea577/search_ncbi"
---

## Concepts

- **Tool Overview**: search_ncbi (v0.1.2) is a package for searching and processing NCBI data.
- **Core Function**: Provides interface to NCBI databases for data retrieval.
- **Algorithm**: Uses NCBI Entrez API for data access.
- **Input/Output**: Accepts search queries and produces biological data.
- **NCBI Integration**: Connects to various NCBI databases.
- **Applications**: Data retrieval, sequence analysis, and bioinformatics research.

## Pitfalls

- **API Rate Limits**: Subject to NCBI API rate limits.
- **Network Dependencies**: Requires internet connection.
- **Data Volume**: May return large amounts of data.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Documentation**: Some features have limited documentation.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Basic search
**Args:** `search_ncbi -d gene -q "BRCA1" -o brca1.gb`
**Explanation:** `-d` database; `-q` query; `-o` output file.

### Protein search
**Args:** `search_ncbi -d protein -q "P53" -o p53.fasta`
**Explanation:** Searches protein database.

### Nucleotide search
**Args:** `search_ncbi -d nuccore -q "MT-ND1" -o nd1.fasta`
**Explanation:** Searches nucleotide database.

### Batch search
**Args:** `search_ncbi -d gene -l genes.txt -o results/`
**Explanation:** `-l` specifies list of queries.

### Verbose logging
**Args:** `search_ncbi -d gene -q "BRCA1" -v -o brca1.gb`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `search_ncbi --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `search_ncbi --version`
**Explanation:** Shows current version.