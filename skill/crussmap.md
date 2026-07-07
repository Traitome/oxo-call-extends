---
name: crussmap
category: assembly
description: crussmap is a Rust implementation of CrossMap for fast conversion of genome coordinates between reference assemblies using chain files
tags: [crussmap, coordinate-conversion, assembly, BED, chain, liftover, genome]
author: oxo-call-community
source_url: "https://github.com/JianYang-Lab/crussmap"
---

## Concepts

- **Tool Overview**: crussmap (v1.0.1+) is a Rust reimplementation of CrossMap for faster genome coordinate conversion between reference assemblies.
- **Core Function**: Converts genomic coordinates and annotations from one assembly to another (e.g., hg19 to hg38) using UCSC chain files. Supports BED and chain file formats.
- **Algorithm**: (1) Parse chain file using nom parser combinator. (2) Build interval tree from chain blocks. (3) For each query region, perform O(log n) lookup to find overlapping chain blocks. (4) Calculate converted coordinates based on block offsets.
- **Input/Output**: Accepts BED and chain files; outputs converted BED coordinates to stdout or file
- **Installation**: `cargo install crussmap` (requires Rust toolchain) or download prebuilt binaries
- **Performance**: ~254ms for 10,000 BED lines and 253,000 chain blocks; significantly faster than Python CrossMap

## Pitfalls

- **Chain File Required**: You must obtain the appropriate chain file for your assembly conversion (e.g., hg19ToHg38.over.chain.gz from UCSC).
- **Unmapped Regions**: Some coordinates may not map due to assembly gaps, missing regions in target, or structural variations. Use `--unmap` to track unmapped entries.
- **Coordinate System**: crussmap uses 0-based half-open intervals for BED format internally but converts to/from 1-based as needed.

## Examples

### View chain file in TSV format
**Args:** `crussmap view --input test.chain --output chain_view.tsv`
**Explanation:** Display chain file content in readable block-pair format showing source and target coordinate relationships.

### View chain file in CSV format
**Args:** `crussmap view --input test.chain --output chain_view.csv --csv`
**Explanation:** Export chain file in CSV format for easier parsing by downstream tools.

### Convert BED coordinates between assemblies
**Args:** `crussmap bed --bed data/test.bed --input hg19ToHg38.chain --output hg38_coords.bed`
**Explanation:** Standard coordinate conversion from hg19 to hg38 using appropriate chain file. Outputs BED with new coordinates.

### Convert with unmapped output
**Args:** `crussmap bed --bed data/test.bed --input hg19ToHg38.chain --output hg38_coords.bed --unmap unmapped.bed`
**Explanation:** Track coordinates that could not be mapped (due to gaps, structural changes) in separate file for review.

### Batch conversion with multiple samples
**Args:** `crussmap bed --bed samples/*.bed --input hg38ToHg19.chain --output hg19_results/`
**Explanation:** Process multiple BED files in a directory for batch coordinate conversion.
