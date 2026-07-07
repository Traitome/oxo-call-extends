---
name: hivtrace
category: molecular-epidemiology
description: HIV-TRACE identifies potential transmission clusters within FASTA sequence data and can search against the Los Alamos HIV Sequence Database.
tags: [hivtrace, HIV, transmission-clusters, molecular-epidemiology, FASTA]
author: oxo-call-community
source_url: "https://github.com/veg/hivtrace"
---

## Concepts

- **Transmission Cluster Detection**: HIV-TRACE identifies molecular transmission clusters.

- **Codon-aware Alignment**: Uses codon-aware pairwise alignment to reference sequences.

- **Genetic Distance Estimation**: Calculates pairwise genetic distances among all sequences.

- **Large-scale Analysis**: Capable of analyzing tens or hundreds of thousands of sequences.

- **Real-time Processing**: Processes large surveillance databases in minutes to hours.

- **Pathogen Surveillance**: Applied to HIV-1 and other rapidly evolving pathogens.

## Pitfalls

- **Sequence Quality**: Results depend on input sequence quality.

- **Distance Threshold**: Selection of appropriate genetic distance threshold is critical.

- **Ambiguity Handling**: Ambiguity threshold affects cluster assignment.

- **Computational Resources**: Large datasets may require significant resources.

- **Database Connection**: Searching Los Alamos database requires network access.

## Examples

### Run HIV-TRACE on FASTA file
**Args:** `hivtrace --input sequences.fasta --output clusters.json`
**Explanation:** Identifies transmission clusters from HIV sequence data.

### With genetic distance threshold
**Args:** `hivtrace --input sequences.fasta --distance-threshold 0.015 --output clusters.json`
**Explanation:** Sets maximum genetic distance for cluster inclusion.

### Search against Los Alamos database
**Args:** `hivtrace --input sequences.fasta --search-database --output clusters.json`
**Explanation:** Searches for potential links against Los Alamos HIV database.

### With ambiguity threshold
**Args:** `hivtrace --input sequences.fasta --ambiguity-threshold 0.015 --output clusters.json`
**Explanation:** Sets threshold for ambiguous base handling.

### Generate visualization
**Args:** `hivtrace --input sequences.fasta --output clusters.json --visualize`
**Explanation:** Generates visualization of transmission clusters.

### Batch processing
**Args:** `for f in *.fasta; do hivtrace --input $f --output ${f%.fasta}_clusters.json; done`
**Explanation:** Processes multiple FASTA files.

### Help command
**Args:** `hivtrace --help`
**Explanation:** Shows available options and usage information.