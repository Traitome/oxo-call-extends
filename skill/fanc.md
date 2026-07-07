---
name: fanc
category: programming
description: "Framework for the ANalysis of C-data."
tags: [fanc, programming, Hi-C, 3D-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vaquerizaslab/fanc"
---

## Concepts

- **Tool Overview**: FAN-C is a comprehensive framework for analyzing Hi-C and other chromosome conformation capture (3C) data.
- **Core Function**: Provides tools for processing, analyzing, and visualizing 3D genomic interactions.
- **Input/Output**: Input: Hi-C contact matrices, BAM files, genome annotations. Output: Interaction maps, compartment calls, TAD boundaries.
- **Algorithm**: Implements various algorithms for Hi-C data normalization, compartment detection, and TAD calling.
- **Key Features**: Hi-C data processing, 3D genome visualization, compartment analysis, TAD detection, multi-resolution analysis, Python API.
- **Installation**: `conda install -c bioconda fanc`

## Pitfalls

- **Data Quality**: Requires high-quality Hi-C data.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Genome Assembly**: Results depend on reference genome quality.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic Hi-C processing
**Args:** `fanc process -i hic_data.cool -o processed.hic`
**Explanation:** Processes raw Hi-C data.

### Compartment analysis
**Args:** `fanc compartments -i processed.hic -o compartments.bed`
**Explanation:** Identifies A/B compartments from Hi-C data.

### TAD detection
**Args:** `fanc tads -i processed.hic -o tads.bed`
**Explanation:** Detects topologically associating domains.

### Visualization
**Args:** `fanc plot -i processed.hic -o interaction_map.png`
**Explanation:** Generates visualization of Hi-C interactions.

### Python API usage
**Args:** `python -c "from fanc import FANCHic; hic = FANCHic('processed.hic')"`
**Explanation:** Accesses Hi-C data through Python API.