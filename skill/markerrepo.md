---
name: markerrepo
category: annotation
description: A tool for marker list management and annotation in the single cell context.
tags: [markerrepo, annotation, single-cell, markers]
author: oxo-call-community
source_url: "https://pypi.org/project/markerrepo/"
---

## Concepts

- **Tool Overview**: markerrepo v0.1.5 - A tool for marker list management and annotation in single-cell analysis.
- **Core Function**: Manages and annotates cell type marker genes for single-cell RNA-seq analysis.
- **Input/Output**: Input: Marker gene lists, single-cell data; Output: Annotated markers, cell type predictions.
- **Installation**: `conda install -c bioconda markerrepo`
- **Marker Management**: Organizes and maintains marker gene lists.
- **Cell Type Annotation**: Uses markers for cell type identification.

## Pitfalls

- **Marker Quality**: Poor quality markers affect cell type annotation.
- **Reference Data**: Outdated marker databases reduce accuracy.
- **Format Compatibility**: Requires specific input formats.
- **Memory Usage**: Large marker lists require significant memory.
- **Cell Type Specificity**: Markers may not be cell type specific.
- **Parameter Tuning**: Incorrect thresholds affect annotation.

## Examples

### Load marker database
**Args:** `markerrepo load -m markers.json -d database/`
**Explanation:** Loads marker genes into database.

### Annotate cell types
**Args:** `markerrepo annotate -i expression.csv -d database/ -o annotations.txt`
**Explanation:** Annotates cell types using marker genes.

### Search markers
**Args:** `markerrepo search -d database/ -q "T-cell"`
**Explanation:** Searches for T-cell markers.

### Export markers
**Args:** `markerrepo export -d database/ -o markers.txt`
**Explanation:** Exports marker list from database.

### Update database
**Args:** `markerrepo update -d database/ -f new_markers.json`
**Explanation:** Updates marker database with new markers.

### Validate markers
**Args:** `markerrepo validate -d database/ -i expression.csv`
**Explanation:** Validates marker specificity using expression data.