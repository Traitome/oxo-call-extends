---
name: beacon2-import
category: variant-calling
description: beacon2-import - Import and query genomic variant data from Beacon instances
tags: [beacon2-import, variant-calling, Beacon, variant-data, data-import]
author: oxo-call-community
source_url: "https://pypi.org/project/beacon2-import/"
---

## Concepts

- **Tool Overview**: beacon2-import (v2.2.4) enables seamless import and querying of genomic variant data from Beacon network instances, facilitating data integration and analysis.
- **Core Function**: Imports genetic variants from Galaxy histories or local repositories into Beacon instances for centralized access.
- **Beacon Network**: Integrates with the Beacon network for standardized variant data sharing.
- **Data Import**: Supports importing variants from multiple sources into Beacon instances.
- **Variant Query**: Enables querying variant data across Beacon instances.
- **Input/Output**: Accepts VCF files and Galaxy history IDs; outputs data to Beacon instances.
- **Installation**: `conda install -c bioconda beacon2-import`.

## Pitfalls

- **Beacon Instance**: Requires access to a running Beacon instance for data import.
- **Network Access**: Requires network access to query remote Beacon instances.
- **Authentication**: Some Beacon instances may require authentication credentials.
- **Data Format**: Input data must conform to Beacon data standards.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Import VCF to Beacon
**Args:** `beacon2-import vcf -i variants.vcf -b http://beacon.example.com -o imported_data`
**Explanation:** Imports VCF file into specified Beacon instance.

### Query Beacon for variants
**Args:** `beacon2-import query -b http://beacon.example.com -c chr1 -s 1000 -e 2000`
**Explanation:** Queries Beacon instance for variants in specified genomic region.

### Import from Galaxy history
**Args:** `beacon2-import galaxy -h history_id -a api_key -b http://beacon.example.com`
**Explanation:** Imports variants from Galaxy history into Beacon instance.

### List available Beacons
**Args:** `beacon2-import list`
**Explanation:** Lists available Beacon instances in the network.

### Validate data before import
**Args:** `beacon2-import validate -i variants.vcf`
**Explanation:** Validates VCF file against Beacon data standards.

### Export from Beacon
**Args:** `beacon2-import export -b http://beacon.example.com -o exported.vcf`
**Explanation:** Exports variant data from Beacon instance to VCF file.

### Display help
**Args:** `beacon2-import --help`
**Explanation:** Shows all available command-line options and usage information.