---
name: markermag
category: metagenomics
description: linking MAGs with 16S rRNA marker genes
tags: [markermag, metagenomics, MAGs, 16S]
author: oxo-call-community
source_url: "https://pypi.org/project/MarkerMAG/"
---

## Concepts

- **Tool Overview**: markermag v1.1.28 - A tool for linking Metagenome-Assembled Genomes (MAGs) with 16S rRNA marker genes.
- **Core Function**: Connects MAGs to their corresponding 16S rRNA sequences for taxonomic classification and validation.
- **Input/Output**: Input: MAG sequences, 16S databases; Output: Linked MAG-16S associations, taxonomic assignments.
- **Installation**: `conda install -c bioconda markermag`
- **MAG Validation**: Validates MAG completeness using 16S rRNA markers.
- **Taxonomic Linking**: Links MAGs to known taxa via 16S rRNA sequences.

## Pitfalls

- **MAG Quality**: Poor quality MAGs affect linking accuracy.
- **Database Completeness**: Incomplete 16S databases miss matches.
- **Memory Usage**: Large MAG collections require significant memory.
- **Computational Time**: Many MAGs may take time to process.
- **False Positives**: May find spurious 16S matches.
- **Parameter Tuning**: Incorrect thresholds affect results.

## Examples

### Link MAGs with 16S
**Args:** `markermag -i mags/ -d 16s_database/ -o links.txt`
**Explanation:** Links MAGs to 16S rRNA sequences.

### With confidence filtering
**Args:** `markermag -i mags/ -d 16s_database/ -o links.txt -c 0.9`
**Explanation:** Filters results by confidence threshold.

### Batch processing
**Args:** `markermag -i mags/ -d 16s_database/ -o results/ --batch`
**Explanation:** Processes MAGs in batch mode.

### Verbose mode
**Args:** `markermag -i mags/ -d 16s_database/ -o links.txt -v`
**Explanation:** Provides detailed logging during analysis.

### Generate report
**Args:** `markermag -i mags/ -d 16s_database/ -o links.txt --report`
**Explanation:** Generates comprehensive linking report.

### Taxonomic assignment
**Args:** `markermag -i mags/ -d 16s_database/ -o links.txt --taxonomy`
**Explanation:** Includes taxonomic assignments.