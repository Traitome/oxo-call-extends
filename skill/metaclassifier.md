---
name: metaclassifier
category: alignment
description: MetaClassifier is an integrated pipeline for classifying and quantifying DNA metabarcoding data into taxonomy groups
tags: [metaclassifier, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/ewafula/MetaClassifier"
---

## Concepts

- **Tool Overview**: metaclassifier v1.0.1 - MetaClassifier is an integrated pipeline for identifying the floral composition of honey using DNA metabarcoding to determine the plants that honey bees visit. MetaClassifier utilizes a database of marker sequences and their corresponding taxonomy lineage information to classify high-throughput metabarcoding sample sequencing reads data into taxonomic groups and quantify taxon abundance. MetaClassifier can also be employed in other studies that utilize barcoding, metabarcoding, and metagenomics techniques to characterize richness, abundance, relatedness, and interactions in ecological communities..
- **Core Function**: MetaClassifier is an integrated pipeline for classifying and quantifying DNA metabarcoding data into taxonomy groups
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metaclassifier`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
