---
name: elastic-blast
category: utility
description: "ElasticBLAST is a cloud-based tool to perform your BLAST searches faster and make you more effective."
tags: [elastic-blast, utility, BLAST, cloud-computing, sequence-alignment]
author: oxo-call-community
source_url: "https://github.com/ncbi/elastic-blast"
---

## Concepts

- **Tool Overview**: ElasticBLAST is a cloud-based BLAST tool that leverages cloud computing resources to accelerate sequence similarity searches at scale.
- **Core Function**: Performs BLAST searches using AWS, GCP, or other cloud providers, enabling parallel processing of large query datasets.
- **Input/Output**: Input: Query sequences (FASTA), BLAST database name or path. Output: BLAST results (tabular, XML, JSON), summary reports.
- **Algorithm**: Parallelizes BLAST searches across multiple cloud instances, distributes queries, and aggregates results.
- **Key Features**: Cloud scalability, cost optimization, support for NCBI databases, automatic resource management, result aggregation, monitoring dashboard.
- **Installation**: `pip install elastic-blast`

## Pitfalls

- **Cloud Costs**: Running large searches can incur significant cloud costs.
- **Network Requirements**: Requires stable internet connection for cloud communication.
- **Database Availability**: Depends on NCBI database availability and update schedules.
- **Instance Configuration**: Improper instance types can affect performance and cost.
- **Result Storage**: Large result sets require appropriate storage solutions.

## Examples

### Basic cloud BLAST search
**Args:** `elastic-blast submit --query query.fasta --db nr --results gs://my-bucket/results`
**Explanation:** Submits BLAST search against NCBI nr database to GCP.

### With custom database
**Args:** `elastic-blast submit --query query.fasta --db /path/to/custom/db --results s3://my-bucket/results`
**Explanation:** Uses custom BLAST database for search.

### Monitor job status
**Args:** `elastic-blast status --results gs://my-bucket/results`
**Explanation:** Checks status of running BLAST job.

### Retrieve results
**Args:** `elastic-blast results --results gs://my-bucket/results -o local_results/`
**Explanation:** Downloads results from cloud storage.

### Clean up resources
**Args:** `elastic-blast delete --results gs://my-bucket/results`
**Explanation:** Deletes cloud resources and results.