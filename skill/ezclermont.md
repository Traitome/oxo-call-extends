---
name: ezclermont
category: utility
description: "easily determine the Clermont 2013 E coli phylotype"
tags: [ezclermont, utility, E.coli, phylotyping, bacterial-typing]
author: oxo-call-community
source_url: "https://github.com/nickp60/ezclermont"
---

## Concepts

- **Tool Overview**: ezclermont is a tool for determining the Clermont 2013 phylotype of E. coli strains using in silico quadriplex PCR.
- **Core Function**: Identifies E. coli phylotypes (A, B1, B2, D, E, F) based on genetic markers.
- **Input/Output**: Input: E. coli genome sequence (FASTA). Output: Phylotype classification, marker presence/absence.
- **Algorithm**: Performs in silico PCR to detect specific genetic markers for phylotype classification.
- **Key Features**: E. coli phylotyping, in silico PCR, batch processing, detailed reporting, marker visualization.
- **Installation**: `conda install -c bioconda ezclermont`

## Pitfalls

- **Genome Quality**: Requires high-quality genome assembly.
- **Marker Database**: Classification depends on marker database completeness.
- **Strain Specificity**: Designed specifically for E. coli.
- **False Positives**: May produce false positive results for closely related species.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic phylotyping
**Args:** `ezclermont -i ecoli_genome.fasta -o phylotype_result.txt`
**Explanation:** Determines Clermont phylotype for E. coli genome.

### With verbose output
**Args:** `ezclermont -i ecoli_genome.fasta -o phylotype_result.txt --verbose`
**Explanation:** Outputs detailed marker information.

### Batch processing
**Args:** `ezclermont -i genomes/ -o results/ --batch`
**Explanation:** Processes multiple genomes in batch mode.

### Marker visualization
**Args:** `ezclermont -i ecoli_genome.fasta -o phylotype_result.txt --plot markers.png`
**Explanation:** Generates visualization of detected markers.

### Custom marker database
**Args:** `ezclermont -i ecoli_genome.fasta -o phylotype_result.txt -d custom_markers.txt`
**Explanation:** Uses custom marker database for classification.