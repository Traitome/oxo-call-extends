---
name: genomad
category: mobile-genetic-elements
description: geNomad - Identification of mobile genetic elements.
tags: [genomad, mobile-genetic-elements, mge, annotation]
author: oxo-call-community
source_url: "https://portal.nersc.gov/genomad"
---

## Concepts
- **Mobile Genetic Elements**: Identifies mobile genetic elements in genomes.
- **MGE Detection**: Detects transposons, plasmids, and phages.
- **Genome Annotation**: Annotates mobile elements in sequences.
- **Horizontal Gene Transfer**: Identifies potential HGT events.
- **Virulence Factors**: Detects virulence factors in mobile elements.

## Pitfalls
- **False Positives**: May detect false MGE signals.
- **Database Dependencies**: Results depend on database completeness.
- **Computational Resources**: Large genomes require significant resources.
- **Sensitivity Thresholds**: Requires careful threshold setting.
- **Validation**: Results should be validated experimentally.

## Examples
### Identify mobile elements
**Args:** `genomad end-to-end -i genome.fasta -o results/`
**Explanation:** Runs complete MGE identification pipeline.

### Annotate sequence
**Args:** `genomad annotate -i genome.fasta -o annotations.txt`
**Explanation:** Annotates mobile genetic elements.

### Classify elements
**Args:** `genomad classify -i elements.fasta -o classification.txt`
**Explanation:** Classifies mobile elements.

### Download database
**Args:** `genomad download-db -o ./database/`
**Explanation:** Downloads reference database.

### Batch processing
**Args:** `genomad end-to-end -i ./genomes/ -o ./results/`
**Explanation:** Processes multiple genome files in batch.