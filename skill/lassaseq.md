---
name: lassaseq
category: virology
description: Lassa virus sequence analysis workflow - from download to phylogenetics
tags: [lassaseq, virology, Lassa-virus, phylogeny, viral-analysis, workflow]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/LassaSeq"
---

## Concepts

- **Lassa Virus**: Designed specifically for Lassa virus analysis
- **Bi-segmented Genome**: Handles Lassa's bi-segmented genome structure
- **Sequence Download**: Automates downloading of viral sequences
- **Phylogenetic Analysis**: Creates phylogenetic trees
- **Workflow Automation**: Streamlines complete analysis pipeline
- **Epidemiology**: Supports epidemiological investigations

## Pitfalls

- **Database Updates**: Sequence databases require regular updates
- **Genome Segments**: Both genome segments must be analyzed together
- **Sequence Quality**: Poor quality sequences affect analysis
- **Reference Selection**: Different references may give different results
- **Phylogenetic Resolution**: May need multiple alignment strategies
- **Geographic Bias**: Limited geographic sampling affects conclusions

## Examples

### Download sequences
**Args:** `lassaseq download -o sequences.fasta`
**Explanation:** Downloads Lassa virus sequences.

### Create alignment
**Args:** `lassaseq align -i sequences.fasta -o alignment.fasta`
**Explanation:** Creates multiple sequence alignment.

### Build phylogeny
**Args:** `lassaseq tree -i alignment.fasta -o phylogeny.nwk`
**Explanation:** Builds phylogenetic tree.

### Segment-specific analysis
**Args:** `lassaseq analyze -i sequences.fasta --segment L`
**Explanation:** Analyzes L segment specifically.

### Batch processing
**Args:** `lassaseq batch -d sequences/ -o results/`
**Explanation:** Processes multiple sequence datasets.

### Export results
**Args:** `lassaseq report -i results/ -o report.pdf`
**Explanation:** Generates analysis report.