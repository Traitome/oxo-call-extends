---
name: beacon2-ri-tools
category: population-genomics
description: beacon2-ri-tools - Tools for populating Beacon v2 MongoDB database
tags: [beacon2-ri-tools, population-genomics, VCF, BFF, MongoDB]
author: oxo-call-community
source_url: "https://github.com/EGA-archive/beacon2-ri-tools-v2/tree/main"
---

## Concepts

- **Tool Overview**: beacon2-ri-tools (v2.0.6) is a package of tools designed to simplify the population of a Beacon v2 MongoDB database, converting variant data into BFF (Beacon Format Framework) format.
- **Core Function**: Generates BFF data from CSV or VCF files for loading into Beacon v2 instances.
- **BFF Format**: Converts input data into Beacon Format Framework (BFF) format for standardized data sharing.
- **MongoDB Integration**: Populates MongoDB databases with variant data for Beacon v2 instances.
- **Data Conversion**: Supports conversion from VCF and CSV formats to BFF format.
- **Input/Output**: Accepts VCF/CSV files; outputs BFF-formatted data for MongoDB.
- **Installation**: `conda install -c bioconda beacon2-ri-tools`.

## Pitfalls

- **MongoDB Setup**: Requires running MongoDB instance for data population.
- **BFF Standards**: Output must conform to Beacon v2 BFF specifications.
- **Data Volume**: Large datasets may require substantial storage and processing time.
- **Version Compatibility**: Ensure compatibility with Beacon v2 specifications.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Convert VCF to BFF
**Args:** `beacon2-ri-tools vcf2bff -i variants.vcf -o bff_output/`
**Explanation:** Converts VCF file to BFF format for Beacon v2.

### Populate MongoDB
**Args:** `beacon2-ri-tools populate -i bff_output/ -m mongodb://localhost:27017/beacon`
**Explanation:** Populates MongoDB database with BFF data.

### Validate BFF data
**Args:** `beacon2-ri-tools validate -i bff_output/`
**Explanation:** Validates BFF data against Beacon v2 specifications.

### Convert CSV to BFF
**Args:** `beacon2-ri-tools csv2bff -i data.csv -o bff_output/`
**Explanation:** Converts CSV file to BFF format.

### Generate metadata
**Args:** `beacon2-ri-tools metadata -i samples.txt -o metadata.json`
**Explanation:** Generates metadata JSON for Beacon v2 instance.

### Export from MongoDB
**Args:** `beacon2-ri-tools export -m mongodb://localhost:27017/beacon -o exported.bff`
**Explanation:** Exports data from MongoDB to BFF format.

### Display help
**Args:** `beacon2-ri-tools --help`
**Explanation:** Shows all available command-line options and usage information.