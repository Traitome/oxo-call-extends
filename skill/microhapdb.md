---
name: microhapdb
category: variant-calling
description: Portable database of microhaplotype marker and allele frequency data.
tags: [microhapdb, variant-calling, forensics]
author: oxo-call-community
source_url: "https://github.com/bioforensics/MicroHapDB/"
---

## Concepts

- **Tool Overview**: MicroHapDB v0.12 is a portable database of microhaplotype marker and allele frequency data.
- **Core Function**: Provides access to microhaplotype marker data for forensic genetics.
- **Microhaplotype Markers**: Contains data on microhaplotype genetic markers.
- **Allele Frequencies**: Provides population-specific allele frequencies.
- **Input/Output**: Accepts marker queries; outputs microhaplotype data.
- **Forensic Applications**: Used in forensic DNA analysis and identification.

## Pitfalls

- **Database Updates**: Database content may require periodic updates.
- **Population Specificity**: Allele frequencies are population-specific.
- **Memory Requirements**: Loading large databases may require significant memory.
- **Parameter Tuning**: May require parameter adjustment for specific queries.
- **Data Quality**: Results depend on database completeness.
- **Forensic Focus**: Primarily designed for forensic applications.

## Examples

### Query microhaplotype data
**Args:** `microhapdb query -m marker_name -o result.txt`
**Explanation:** Queries microhaplotype marker information.

### List all markers
**Args:** `microhapdb list -o markers.txt`
**Explanation:** Lists all available microhaplotype markers.

### Population-specific frequencies
**Args:** `microhapdb freq -m marker_name -p population -o frequencies.txt`
**Explanation:** Retrieves population-specific allele frequencies.

### Batch query
**Args:** `microhapdb batch -i markers.txt -o results.txt`
**Explanation:** Processes multiple marker queries in batch mode.

### Export database
**Args:** `microhapdb export -o database.csv`
**Explanation:** Exports database to CSV format.