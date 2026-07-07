---
name: proteomiqon-peptidedb
category: formatting
description: proteomiqon-peptidedb creates a peptide database in SQLite format for proteomics analysis.
tags: [proteomiqon-peptidedb, formatting, proteomics, database]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/PeptideDB.html"
---

## Concepts

- **Tool Overview**: proteomiqon-peptidedb builds peptide databases.
- **Core Function**: Database creation.
- **Algorithm**: Uses SQLite storage methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces SQLite database.
- **Use Case**: Proteomics database searching.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Data Quality**: Results depend on input quality.
- **Database Size**: May affect performance.
- **Runtime**: Building may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proteomiqon-peptidedb --help`
**Explanation:** Shows available options and usage instructions.

### Create database
**Args:** `proteomiqon-peptidedb -i proteins.fasta -o peptide_db.sqlite`
**Explanation:** Creates peptide database from FASTA.

### With parameters
**Args:** `proteomiqon-peptidedb -i proteins.fasta --params params.yaml -o peptide_db.sqlite`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proteomiqon-peptidedb -v -i proteins.fasta -o peptide_db.sqlite`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proteomiqon-peptidedb -t 4 -i proteins.fasta -o peptide_db.sqlite`
**Explanation:** Uses 4 threads for parallel processing.

### Add decoys
**Args:** `proteomiqon-peptidedb -i proteins.fasta -o peptide_db.sqlite --decoy`
**Explanation:** Includes decoy sequences.

### Generate report
**Args:** `proteomiqon-peptidedb -i proteins.fasta -o peptide_db.sqlite --report report.html`
**Explanation:** Generates HTML report.