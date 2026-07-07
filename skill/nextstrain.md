---
name: nextstrain
category: utility
description: Nextstrain is an open-source project for pathogen genome analysis and visualization.
tags: [nextstrain, utility, pathogen, bioinformatics, epidemiology]
author: oxo-call-community
source_url: "https://nextstrain.org"
---

## Concepts

- **Tool Overview**: Nextstrain provides tools for real-time pathogen surveillance and genomic epidemiology.
- **Core Function**: Analyzes pathogen genomes to track spread and evolution during outbreaks.
- **Algorithm**: Combines sequence alignment, phylogenetic analysis, and visualization.
- **Input Format**: Accepts FASTA sequences and metadata files.
- **Output**: Produces phylogenetic trees and interactive visualizations.
- **Use Case**: Outbreak tracking, public health surveillance, and evolutionary biology research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Quality**: Results depend on sequence quality and completeness.
- **Computational Resources**: Large datasets require significant computing power.
- **Metadata Requirements**: Requires detailed sample metadata.
- **Phylogenetic Accuracy**: Depends on tree building parameters.
- **Real-time Updates**: Requires continuous data updates for surveillance.

## Examples

### Display help
**Args:** `nextstrain --help`
**Explanation:** Shows available options and usage instructions.

### Run build
**Args:** `nextstrain build .`
**Explanation:** Runs Nextstrain analysis pipeline in current directory.

### View results
**Args:** `nextstrain view auspice/`
**Explanation:** Opens interactive visualization in browser.

### Upload to server
**Args:** `nextstrain upload auspice/ my-outbreak`
**Explanation:** Uploads results to Nextstrain server.

### Check setup
**Args:** `nextstrain check-setup`
**Explanation:** Verifies environment configuration.

### Run with Docker
**Args:** `nextstrain build --docker .`
**Explanation:** Runs pipeline using Docker container.

### List analyses
**Args:** `nextstrain list`
**Explanation:** Lists analyses on Nextstrain server.