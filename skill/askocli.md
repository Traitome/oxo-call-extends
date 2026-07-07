---
name: askocli
category: utility
description: AskOmics CLI - Command line interface for AskOmics data integration platform
tags: [askocli, utility, askomics, data-integration, omics]
author: oxo-call-community
source_url: "https://github.com/askomics/askocli"
---

## Concepts

- **Tool Overview**: askocli is the command-line interface for AskOmics, a web-based platform for integrating, analyzing, and visualizing omics data. Version 0.5.
- **Core Function**: Provides command-line access to AskOmics server for data upload, query execution, and result retrieval.
- **Data Integration**: Uploads and integrates various omics data types (genomics, transcriptomics, proteomics) into AskOmics knowledge base.
- **SPARQL Queries**: Executes SPARQL queries against integrated omics data for complex data exploration.
- **Remote Access**: Interacts with remote AskOmics instances for cloud-based data analysis.
- **Input/Output**: Supports multiple omics data formats (FASTA, GFF, CSV, etc.) and outputs query results.
- **Installation**: `conda install -c bioconda askocli` or install from GitHub.

## Pitfalls

- **Server Connection**: Requires active AskOmics server connection. Server downtime affects all operations.
- **Authentication**: Requires valid AskOmics credentials. Incorrect login fails all commands.
- **Data Format**: Data must conform to AskOmics import specifications. Incorrect formats cause import failures.
- **Network Dependency**: Requires network connectivity to remote AskOmics server.
- **Query Complexity**: Complex SPARQL queries may be slow or time out. Optimize queries for performance.
- **Server Version**: CLI version must be compatible with server version. Mismatched versions cause compatibility issues.

## Examples

### Display help
**Args:** `askocli --help`
**Explanation:** Shows all available command-line options and subcommands.

### Login to AskOmics server
**Args:** `askocli login --url https://askomics.example.com --username user --password pass`
**Explanation:** Authenticates with AskOmics server and stores session credentials.

### Upload data
**Args:** `askocli upload --file data.fasta --type fasta --name my_data`
**Explanation:** Uploads FASTA file to AskOmics server with specified data type and name.

### Execute SPARQL query
**Args:** `askocli query --sparql "SELECT ?gene ?expression WHERE { ?gene :hasExpression ?expression }"`
**Explanation:** Runs SPARQL query against AskOmics knowledge base and returns results.

### List uploaded datasets
**Args:** `askocli datasets list`
**Explanation:** Lists all datasets uploaded to current AskOmics project.

### Download query results
**Args:** `askocli query --sparql "SELECT * WHERE { ?x a :Gene }" --output results.tsv`
**Explanation:** Executes query and saves results to TSV file for downstream analysis.

### Create new project
**Args:** `askocli project create --name my_project --description "My analysis project"`
**Explanation:** Creates new project in AskOmics for organizing data and queries.

### Import GFF annotation
**Args:** `askocli upload --file genes.gff --type gff --name gene_annotations`
**Explanation:** Uploads GFF annotation file for gene model integration.

### Get server status
**Args:** `askocli status`
**Explanation:** Checks connection status to AskOmics server and API availability.