---
name: mirge-build
category: utility
description: "miRge-build: Building libraries of small RNA sequencing Data"
tags: [mirge-build, utility, microrna]
author: oxo-call-community
source_url: "https://github.com/mhalushka/miRge3_build"
---
## Concepts

- **Tool Overview**: miRge-build v0.0.1 builds small RNA reference libraries.
- **Core Function**: Creates custom small RNA reference databases.
- **Reference Building**: Generates databases for miRNA analysis.
- **Custom Libraries**: Builds species-specific small RNA libraries.
- **Input/Output**: Accepts sequence data; outputs reference libraries.
- **miRNA Analysis**: Supports downstream miRNA quantification.

## Pitfalls

- **Database Building**: Designed for reference library construction.
- **Computational Resources**: Building large libraries may require significant resources.
- **Memory Requirements**: Memory usage depends on database size.
- **Parameter Tuning**: May require parameter adjustment for optimal library building.
- **Data Quality**: Results depend on input sequence quality.
- **Reference Sequences**: Requires high-quality input sequences.

## Examples

### Build reference library
**Args:** `mirge-build -i sequences.fasta -o library/`
**Explanation:** Builds small RNA reference library.

### With annotations
**Args:** `mirge-build -i sequences.fasta -a annotations.gtf -o library/`
**Explanation:** Includes annotation information.

### Custom parameters
**Args:** `mirge-build -i sequences.fasta -o library/ -k 21`
**Explanation:** Uses custom k-mer size.

### Batch processing
**Args:** `mirge-build -i fasta/ -o libraries/`
**Explanation:** Processes multiple FASTA files.

### Generate statistics
**Args:** `mirge-build -i sequences.fasta -o library/ -s stats.txt`
**Explanation:** Generates library statistics.