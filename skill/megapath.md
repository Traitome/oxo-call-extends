---
name: megapath
category: qc
description: Sensitive and rapid pathogen detection using metagenomic NGS data.
tags: [megapath, pathogen-detection, metagenomics]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/MegaPath"
---

## Concepts

- **Tool Overview**: MegaPath detects pathogens from metagenomic sequencing data.
- **Core Function**: Rapid and sensitive pathogen identification.
- **Reference Mapping**: Maps reads against pathogen reference databases.
- **Amplicon Filtering**: Specialized filtering for amplicon data.
- **Antimicrobial Resistance**: Detects AMR genes.
- **Installation**: `conda install -c bioconda megapath`

## Pitfalls

- **Database Requirements**: Requires up-to-date pathogen databases.
- **Memory Requirements**: High memory for large databases.
- **Computation Time**: Slow for complex metagenomes.
- **False Positives**: May detect non-pathogenic organisms.
- **Sensitivity**: May miss low-abundance pathogens.
- **Parameter Tuning**: Requires careful threshold adjustment.

## Examples

### Detect pathogens
**Args:** `megapath -i reads.fastq -o results/`
**Explanation:** Detects pathogens from metagenomic reads.

### With custom database
**Args:** `megapath -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses custom pathogen database.

### Amplicon filtering
**Args:** `megapath-amplicon -i reads.fastq -o filtered.fastq`
**Explanation:** Filters amplicon data.

### AMR detection
**Args:** `megapath -i reads.fastq --amr -o results/`
**Explanation:** Detects antimicrobial resistance genes.

### Help documentation
**Args:** `megapath --help`
**Explanation:** Displays available options.
