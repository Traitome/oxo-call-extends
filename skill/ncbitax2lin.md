---
name: ncbitax2lin
category: formatting
description: NCBItax2lin converts NCBI taxonomy dump into lineage information for sequence classification.
tags: [ncbitax2lin, formatting, taxonomy, ncbi, lineage]
author: oxo-call-community
source_url: "https://github.com/zyxue/ncbitax2lin"
---

## Concepts

- **Tool Overview**: NCBItax2lin is a tool for converting NCBI taxonomy dump files into lineage information.
- **Core Function**: Extracts taxonomic lineage information (kingdom, phylum, class, etc.) from NCBI taxonomy data.
- **Algorithm**: Parses NCBI taxonomy dump files (nodes.dmp, names.dmp) and builds lineage paths.
- **Input Format**: Requires NCBI taxonomy dump files downloaded from NCBI FTP.
- **Output**: Produces lineage files mapping taxonomic IDs to their full lineage paths.
- **Use Case**: Taxonomic classification, metagenomics analysis, and sequence annotation workflows.

## Pitfalls

- **Database Updates**: Requires regular updates of NCBI taxonomy database.
- **Large Files**: Taxonomy dump files can be large and require significant storage.
- **Memory Usage**: Processing large taxonomy datasets requires sufficient memory.
- **Version Differences**: Options may vary between versions.
- **Network Dependency**: Requires downloading taxonomy files from NCBI.
- **Format Changes**: NCBI may change dump file formats between releases.

## Examples

### Display help
**Args:** `ncbitax2lin --help`
**Explanation:** Shows available options and usage instructions.

### Basic conversion
**Args:** `ncbitax2lin -i nodes.dmp -n names.dmp -o lineage.tsv`
**Explanation:** Converts NCBI taxonomy dump to lineage file.

### Download taxonomy dump
**Args:** `ncbitax2lin --download -o taxonomy/`
**Explanation:** Downloads latest NCBI taxonomy dump files.

### Filter by rank
**Args:** `ncbitax2lin -i nodes.dmp -n names.dmp -r species -o species_lineage.tsv`
**Explanation:** Filters output to include only species-level lineages.

### Output JSON format
**Args:** `ncbitax2lin -i nodes.dmp -n names.dmp --json -o lineage.json`
**Explanation:** Outputs lineage information in JSON format.

### Update existing lineage
**Args:** `ncbitax2lin -i nodes.dmp -n names.dmp -u existing_lineage.tsv -o updated.tsv`
**Explanation:** Updates existing lineage file with new taxonomy data.