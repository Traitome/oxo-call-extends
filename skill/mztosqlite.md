---
name: mztosqlite
category: formatting
description: mzToSQLite - Convert proteomics data files into SQLite database
tags: [mztosqlite, formatting, proteomics, sqlite, database, mzml]
author: oxo-call-community
source_url: "https://github.com/galaxyproteomics/mzToSQLite"
---

## Concepts

- **Tool Overview**: mzToSQLite v2.1.1 converts proteomics data files (mzML, mzXML) into SQLite databases for efficient querying and analysis. Designed primarily for use within the Galaxy bioinformatics platform.
- **Core Function**: Parses raw mass spectrometry files and stores spectral data, peptide identifications, and metadata in a normalized SQLite schema for fast SQL-based queries.
- **Database Schema**: Stores spectra, scans, MS runs, peptides, proteins, and their relationships in a well-defined schema enabling complex queries across large proteomics datasets.
- **Input Format**: Accepts mzML (preferred) and mzXML files containing raw mass spectrometry data. Can process individual files or batch process directories.
- **Output**: Produces a SQLite database file (.db) containing all spectral and identification data from input files.
- **Use Case**: Galaxy proteomics workflows, proteomics data mining, cross-dataset queries, and building custom proteomics analysis pipelines.

## Pitfalls

- **Large Files**: Very large mzML files can consume significant time and memory during conversion. Consider processing in batches.
- **SQLite Limitations**: SQLite has file size limits (~140TB) and concurrent write limitations. Not suitable for truly massive proteomics repositories.
- **Database Indexing**: Creating indexes on large databases takes additional time but dramatically improves query performance.
- **File Validation**: Corrupt or non-standard mzML files cause conversion failures. Validate files before batch processing.
- **Metadata Loss**: Some metadata fields may not be fully captured in the SQLite schema. Check schema documentation for coverage.
- **Galaxy Integration**: While designed for Galaxy, can be used standalone with proper configuration.

## Examples

### Basic conversion
**Args:** `-i sample.mzML -o proteomics.db`
**Explanation:** Standard conversion. Parses mzML and creates SQLite database with all spectral data.

### Batch process directory
**Args:** `-i mzml_dir -o combined.db`
**Explanation:** Converts all mzML files in a directory into a single SQLite database.

### Create with full indexes
**Args:** `-i runs/*.mzML -o indexed.db --index`
**Explanation:** Creates database with full indexes for optimized query performance.

### Validate database
**Args:** `-i output.db --validate`
**Explanation:** Validates database schema integrity and data completeness.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
