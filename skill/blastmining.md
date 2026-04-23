---
name: blastmining
category: annotation
description: Mining NCBI BLAST outputs for functional annotation
tags: [blastmining, blast, annotation, mining, functional]
author: oxo-call-community
source_url: "https://github.com/NuruddinKhoiry/blastMining"
---

## Concepts

- **Tool Overview**: blastMining extracts and summarizes functional annotation from BLAST output files.
- **Core Function**: Parses BLAST results to extract gene names, GO terms, and functional descriptions.
- **Input**: BLAST tabular output (-outfmt 6).
- **Output**: Summarized annotation tables with functional information.
- **Features**: Extracts top hits, gene names, and functional descriptions automatically.
- **Installation**: Install via bioconda: `conda install -c bioconda blastmining`

## Pitfalls

- **BLAST Format**: Requires tabular BLAST output with specific columns.
- **Database Type**: Results depend on the database used for BLAST search.
- **Annotation Quality**: Top hit may not always be the correct annotation.
- **Output Columns**: Specify desired output columns for custom reports.

## Examples

### Extract top annotations
**Args:** `blastMining -i blast_results.tsv -o annotations.tsv`
**Explanation:** Extracts top hit annotations from BLAST tabular output.

### Extract with GO terms
**Args:** `blastMining -i blast_results.tsv -g -o annotations_with_go.tsv`
**Explanation:** Includes Gene Ontology terms in annotation output.

### Set number of top hits
**Args:** `blastMining -i blast_results.tsv -n 5 -o top5_annotations.tsv`
**Explanation:** Extracts top 5 hits per query for comprehensive annotation.

### Custom e-value filter
**Args:** `blastMining -i blast_results.tsv -e 1e-10 -o filtered_annotations.tsv`
**Explanation:** Applies e-value threshold for annotation filtering.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
