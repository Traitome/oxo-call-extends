---
name: miru-hero
category: population-genomics
description: Compute MIRU and Spoligotype from a M. tuberculosis genome
tags: [miru-hero, population-genomics, sequence]
author: oxo-call-community
source_url: "https://gitlab.com/LPCDRP/miru-hero"
---

## Concepts

- **Tool Overview**: miru-hero v0.10.0 computes MIRU and Spoligotype from M. tuberculosis genomes.
- **Core Function**: Identifies MIRU-VNTR loci and Spoligotype patterns.
- **MIRU Analysis**: Detects Mycobacterial Interspersed Repetitive Units.
- **Spoligotyping**: Identifies spacer oligonucleotide typing patterns.
- **Lineage Prediction**: Predicts M. tuberculosis lineage.
- **Input/Output**: Accepts genome sequences; outputs typing results.

## Pitfalls

- **M. tuberculosis Specific**: Designed for Mycobacterium tuberculosis analysis.
- **Computational Resources**: Processing large genomes may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal typing.
- **Data Quality**: Results depend on input sequence quality.
- **Reference Standards**: Requires appropriate reference databases.

## Examples

### Compute MIRU and Spoligotype
**Args:** `miru-hero -i genome.fasta -o results.txt`
**Explanation:** Computes MIRU and Spoligotype from genome.

### With verbose output
**Args:** `miru-hero -i genome.fasta -o results.txt -v`
**Explanation:** Shows detailed typing results.

### Lineage prediction
**Args:** `miru-hero -i genome.fasta -o results.txt -l`
**Explanation:** Predicts M. tuberculosis lineage.

### Batch processing
**Args:** `miru-hero -i fasta/ -o results/`
**Explanation:** Processes multiple genome files.

### Generate report
**Args:** `miru-hero -i genome.fasta -o results.txt -r report.html`
**Explanation:** Generates HTML analysis report.