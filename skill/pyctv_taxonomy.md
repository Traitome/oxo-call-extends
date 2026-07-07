---
name: pyctv_taxonomy
category: utility
description: pyctv_taxonomy downloads and uses the ICTV Virus Metadata Resource for viral taxonomy analysis.
tags: [pyctv_taxonomy, utility, virus-taxonomy, ICTV]
author: oxo-call-community
source_url: "https://github.com/linsalrob/pyctv"
---

## Concepts

- **Tool Overview**: pyctv_taxonomy accesses ICTV data.
- **Core Function**: Viral taxonomy lookup.
- **Algorithm**: Uses database queries.
- **Input Format**: Accepts virus names/IDs.
- **Output**: Produces taxonomy information.
- **Use Case**: Virus classification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Access**: Requires internet connection.
- **Data Updates**: Database may change.
- **Name Resolution**: May have synonyms.
- **Service Availability**: Dependent on ICTV.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyctv_taxonomy --help`
**Explanation:** Shows available options and usage instructions.

### Download database
**Args:** `pyctv_taxonomy download -o database/`
**Explanation:** Downloads ICTV virus metadata.

### With parameters
**Args:** `pyctv_taxonomy query -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyctv_taxonomy -v query -n VirusName -o results.txt`
**Explanation:** Runs with verbose output.

### Query taxonomy
**Args:** `pyctv_taxonomy query -n "SARS-CoV-2" -o taxonomy.txt`
**Explanation:** Queries taxonomy for virus.

### List taxa
**Args:** `pyctv_taxonomy list -o taxa.txt`
**Explanation:** Lists available taxa.

### Generate report
**Args:** `pyctv_taxonomy query -n VirusName -o results.txt --report report.html`
**Explanation:** Generates HTML report.