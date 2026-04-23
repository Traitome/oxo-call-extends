---
name: biocantor
category: annotation
description: Coordinate Manipulation and Genome Annotation Data Model
tags: [coordinates, annotation, genomic-intervals]
author: oxo-call-community
source_url: "https://github.com/ifiddes/BioCantor"
---

## Concepts
- **Tool Overview**: BioCantor is a Python library for coordinate manipulation and genome annotation data modeling. It provides robust handling of genomic coordinates and annotations.
- **Coordinate Operations**: Interconversion between different coordinate systems, interval arithmetic, and coordinate validation.
- **Annotation Model**: Standardized representation of genomic features (genes, transcripts, exons, CDS).
- **Applications**: Annotation processing, coordinate conversion, feature overlap analysis.

## Pitfalls
- **Coordinate System**: Be aware of 0-based vs 1-based coordinate conventions.
- **Strand Handling**: Proper strand orientation is critical for coordinate operations.

## Examples
### Convert coordinates
**Args:** `biocantor convert --input coords.bed --output converted.gff`
**Explanation:** Converts between coordinate formats.
