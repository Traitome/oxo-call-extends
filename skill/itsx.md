---
name: itsx
category: utility
description: Extracts ITS1 and ITS2 subregions from ribosomal ITS sequences for fungal barcoding.
tags: [itsx, utility, ITS, fungi, barcoding]
author: oxo-call-community
source_url: "http://microbiology.se/software/itsx/"
---

## Concepts

- **ITS Region Extraction**: Identifies and extracts ITS1 and ITS2 subregions from ITS sequences.
- **Fungal Barcoding**: Optimized for fungal ITS sequences used in DNA barcoding.
- **Multiple Databases**: Uses curated databases for accurate ITS region identification.
- **Taxonomic Filtering**: Filters sequences by taxonomic group.
- **Quality Control**: Includes quality checks for extracted sequences.
- **Output Formats**: Generates output in multiple bioinformatics formats.

## Pitfalls

- **Sequence Quality**: Poor quality sequences affect extraction accuracy.
- **Database Completeness**: Incomplete databases may miss some ITS regions.
- **Ambiguous Boundaries**: Some ITS boundaries may be ambiguous.
- **Non-Fungal Sequences**: Designed primarily for fungal sequences.
- **Parameter Sensitivity**: Results may be sensitive to alignment parameters.
- **Memory Requirements**: Processing large datasets requires significant memory.

## Examples

### Basic ITS extraction
**Args:** `itsx -i sequences.fasta -o extracted/`
**Explanation:** Extracts ITS1 and ITS2 regions from input sequences.

### Specify taxonomic group
**Args:** `itsx -i sequences.fasta -o extracted/ -t Fungi`
**Explanation:** Filters sequences for fungal ITS regions.

### Extract specific region
**Args:** `itsx -i sequences.fasta -o extracted/ --region ITS1`
**Explanation:** Extracts only the ITS1 region.

### Multiple output formats
**Args:** `itsx -i sequences.fasta -o extracted/ --format fasta,tab`
**Explanation:** Generates output in multiple formats.

### Quality filtering
**Args:** `itsx -i sequences.fasta -o extracted/ --min-quality 20`
**Explanation:** Filters sequences based on quality score.

### Batch processing
**Args:** `itsx -batch input_list.txt -o results/`
**Explanation:** Processes multiple input files in batch.