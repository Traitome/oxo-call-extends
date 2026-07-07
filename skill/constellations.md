---
name: constellations
category: utility
description: SARS-CoV-2 mutation constellation definitions and analysis
tags: [constellations, sars-cov-2, mutation-analysis, covid-19, variant-tracking]
author: oxo-call-community
source_url: "https://github.com/cov-lineages/constellations"
---

## Concepts

- **Tool Overview**: Constellations is a tool for defining and analyzing constellations of mutations in the SARS-CoV-2 virus, used for variant tracking and lineage assignment.
- **Core Function**: Provides mutation profiles that define SARS-CoV-2 lineages and variants of concern.
- **Algorithm**: Uses predefined mutation sets to characterize viral lineages and track evolutionary changes.
- **Input**: SARS-CoV-2 genome sequences or variant definitions.
- **Output**: Mutation constellation assignments and lineage classifications.
- **Application**: COVID-19 surveillance, variant tracking, and outbreak investigation.
- **Installation**: Install via bioconda: `conda install -c bioconda constellations`

## Pitfalls

- **Variant Evolution**: New variants may not match existing constellations.
- **Database Updates**: Requires regular updates as new lineages emerge.
- **Sequence Quality**: Poor quality sequences may produce incorrect assignments.
- **Recombination**: Recombinant lineages may have mixed constellation features.
- **Geographic Bias**: Constellation definitions may be biased toward well-sampled regions.

## Examples

### Assign lineage to sequence
**Args:** `constellations assign -i sequence.fasta -o lineage_assignment.txt`
**Explanation:** Assigns SARS-CoV-2 lineage based on mutation constellation.

### List available constellations
**Args:** `constellations list`
**Explanation:** Lists all available mutation constellations and their definitions.

### Export constellation definitions
**Args:** `constellations export -o constellations.json`
**Explanation:** Exports constellation definitions in JSON format.

### Display help
**Args:** `constellations --help`
**Explanation:** Shows all available options and usage information.