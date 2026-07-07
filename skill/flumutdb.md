---
name: flumutdb
category: programming
description: "FluMutDB is a utility module for accessing and querying the FluMut database of influenza virus mutations."
tags: [flumutdb, programming, influenza, virus, database, bioinformatics, virology]
author: oxo-call-community
source_url: "https://github.com/izsvenezie-virology/FluMutDB"
---

## Concepts
- **Tool Overview**: FluMutDB provides programmatic access to the FluMut database containing molecular markers and mutations of influenza viruses.
- **Core Function**: Query and retrieve influenza virus mutation data, including marker effects and biological characteristics.
- **Input/Output**: Input: Query parameters (gene, position, mutation type). Output: Mutation records, marker annotations.
- **Database Integration**: Connects to FluMut database for efficient querying of mutation data.
- **Marker Classification**: Classifies mutations by their potential impact on viral characteristics (pathogenicity, drug resistance).
- **Data Export**: Supports exporting results in various formats for downstream analysis.
- **Installation**: `conda install -c bioconda flumutdb` or clone from GitHub. Requires Python 3.x.

## Pitfalls
- **Database Connection**: Requires network access to FluMut database or local database installation.
- **Data Updates**: Database content may not be current. Check for updates regularly.
- **Query Complexity**: Complex queries may require optimization for performance.
- **Data Format**: Output formats may require conversion for specific analysis tools.
- **Reference Genome**: Mutation positions are relative to specific reference strains. Verify reference compatibility.
- **API Rate Limits**: Remote database queries may have rate limits. Use local database for heavy querying.

## Examples
### Basic mutation query
**Args:** `flumutdb query --gene HA --position 156`
**Explanation:** Queries mutations at position 156 in the HA gene.

### Search by mutation effect
**Args:** `flumutdb query --effect drug_resistance --subtype H5N1`
**Explanation:** Finds mutations associated with drug resistance in H5N1 subtype.

### Export results
**Args:** `flumutdb query --gene NA --output mutations.csv`
**Explanation:** Exports NA gene mutations to CSV file.

### List all markers
**Args:** `flumutdb list --type marker`
**Explanation:** Lists all molecular markers in the database.

### Get marker details
**Args:** `flumutdb info --marker M2_S31N`
**Explanation:** Retrieves detailed information about specific marker.
