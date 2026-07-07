---
name: meta_eukaryome_detect
category: metagenomics
description: Pathogen, Parasite, Eukaryote and Virus detection in metagenomes.
tags: [meta_eukaryome_detect, metagenomics, pathogen-detection, eukaryote]
author: oxo-call-community
source_url: "https://github.com/grp-bork/meta_eukaryome_detect"
---

## Concepts

- **Tool Overview**: meta_eukaryome_detect v0.1.1 is a tool for detecting pathogens, parasites, eukaryotes, and viruses in metagenomic sequencing data.
- **Core Function**: Identifies and quantifies eukaryotic organisms, pathogens, and viruses present in metagenomic samples.
- **Multi-organism Detection**: Capable of detecting a wide range of organisms including fungi, protozoa, helminths, and viruses.
- **Reference Database**: Uses comprehensive reference databases for accurate organism identification.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs detection results with taxonomic classifications and abundance estimates.
- **Sensitivity**: Designed for high-sensitivity detection even for low-abundance organisms.

## Pitfalls

- **Database Completeness**: Detection accuracy depends on reference database completeness.
- **Host DNA**: High host DNA content can reduce detection sensitivity.
- **Sequence Quality**: Poor quality reads may lead to false positives or false negatives.
- **Computational Resources**: Large datasets may require significant computational resources.
- **False Positives**: May detect contaminants from laboratory reagents.
- **Low Abundance**: Very low abundance organisms may not be detected.

## Examples

### Detect pathogens in metagenome
**Args:** `meta_eukaryome_detect -i reads.fastq -o results/`
**Explanation:** Detects pathogens, parasites, eukaryotes, and viruses in metagenomic reads.

### Paired-end analysis
**Args:** `meta_eukaryome_detect -i reads_1.fastq reads_2.fastq -o results/`
**Explanation:** Processes paired-end sequencing data for detection.

### Specify database
**Args:** `meta_eukaryome_detect -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses a custom reference database for detection.

### Output detailed report
**Args:** `meta_eukaryome_detect -i reads.fastq -o results/ -r detailed_report.txt`
**Explanation:** Generates a detailed detection report.

### Filter by confidence
**Args:** `meta_eukaryome_detect -i reads.fastq -o results/ -c 0.9`
**Explanation:** Filters results to minimum confidence score of 0.9.