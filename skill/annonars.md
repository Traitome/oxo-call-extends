---
name: annonars
category: annotation
description: Genome annotation tool based on Rust and RocksDB for efficient variant annotation storage and querying
tags: [annonars, genome-annotation, variant-annotation, RocksDB, Rust, CADD, dbNSFP]
author: oxo-call-community
source_url: "https://github.com/varfish-org/annonars"
---

## Concepts

- **Tool Overview**: annonars (v0.44.2) is a high-performance genome annotation tool built in Rust using RocksDB for persistent storage. Designed for efficient storage and querying of variant annotations at scale.
- **Core Function**: Imports variant annotation data (from sources like CADD, dbNSFP, gnomAD) into RocksDB databases for fast lookup queries.
- **SPDI Coordinates**: Uses SPDI representation (1-based, inclusive) for variant specification as described in Holmes et al. 2020.
- **TSV Import**: Supports importing variant annotations from TSV files, inferring schema from data and handling multiple genome builds.
- **Parallel Processing**: Utilizes Rayon for parallel import operations, with support for tabix indices to speed up database building.
- **API Server**: Provides REST API endpoints for gene lookup, variant annotation queries, and ClinVar information retrieval.
- **Supported Databases**: CADD, dbNSFP, gnomAD, ClinVar gene annotations, and structural variant annotations.
- **Installation**: Available via Bioconda (`conda install -c bioconda annonars`) or Cargo (`cargo install annonars`).

## Pitfalls

- **Version Differences**: API endpoints and CLI options may vary between versions.
- **Genome Build Consistency**: Ensure all annotations use the same genome build (GRCh37/GRCh38).
- **Memory Usage**: Large annotation databases require significant disk space; RocksDB compaction is recommended after import.
- **Tabix Indexing**: Provide .tbi files for parallel import; otherwise files are processed sequentially.
- **Schema Inference**: May fail for complex TSV files; consider providing explicit JSON schema.
- **WAL Files**: After import, check for write-ahead log files (*.log) that can be safely deleted if zero-sized.

## Examples

### Display help
**Args:** `annonars --help`
**Explanation:** Shows available options and subcommands.

### Import CADD annotations
**Args:** `annonars tsv import --path-in-tsv whole_genome_SNVs_inclAnno.tsv.gz --path-out-rocksdb cadd-rocksdb --genome-release grch37 --db-name cadd --db-version 1.6 --col-chrom Chrom --col-start Pos --col-ref Ref --col-alt Alt --skip-row-count=1 --inference-row-count 100000 --add-default-null-values`
**Explanation:** Imports CADD variant annotations into RocksDB database with schema inference from first 100,000 rows.

### Import dbNSFP annotations
**Args:** `annonars tsv import $(for f in dbNSFP4.4a_variant.*.gz; do echo --path-in-tsv $f; done) --path-out-rocksdb dbnsfp-rocksdb --genome-release grch37 --db-name dbnsfp --db-version 4.4a --col-chrom hg19_chr --col-start hg19_pos(1-based) --col-ref ref --col-alt alt --inference-row-count 100000 --null-values=.`
**Explanation:** Imports multiple dbNSFP annotation files into single RocksDB database.

### Query by variant
**Args:** `annonars tsv query --path-rocksdb cadd-rocksdb --range GRCh37:1:1000:A:T`
**Explanation:** Queries annotations for specific variant at position 1:1000 with REF=A, ALT=T.

### Query by position
**Args:** `annonars tsv query --path-rocksdb cadd-rocksdb --pos GRCh37:1:1000`
**Explanation:** Retrieves all variants at a specific genomic position.

### Query by region
**Args:** `annonars tsv query --path-rocksdb cadd-rocksdb --range GRCh37:1:1000-2000`
**Explanation:** Queries all variants within specified genomic region.

### Start API server
**Args:** `annonars server --path-rocksdb /path/to/annotations/`
**Explanation:** Starts REST API server for annotation queries via HTTP endpoints.

### Lookup gene information
**Args:** `annonars tsv query --path-rocksdb genes-rocksdb --gene BRCA1`
**Explanation:** Retrieves annotation information for specified gene symbol.