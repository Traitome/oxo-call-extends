---
name: geno2phenotb
category: antimicrobial-resistance
description: Geno2PhenoTB - Prediction of Mycobacterium tuberculosis drug resistance from WGS data.
tags: [geno2phenotb, tb, drug-resistance, wgs]
author: oxo-call-community
source_url: "https://geno2phenotb.readthedocs.io/en/latest"
---

## Concepts
- **Drug Resistance Prediction**: Predicts drug resistance in TB.
- **Whole Genome Sequencing**: Analyzes WGS data for resistance markers.
- **Mycobacterium tuberculosis**: Specific to TB pathogen.
- **Resistance Markers**: Identifies genetic markers for drug resistance.
- **Clinical Decision Support**: Supports clinical treatment decisions.

## Pitfalls
- **Specificity**: Designed specifically for M. tuberculosis.
- **Genomic Variation**: May miss novel resistance mutations.
- **Quality Control**: Requires high-quality sequencing data.
- **Database Updates**: Requires regular database updates.
- **Clinical Validation**: Results require clinical confirmation.

## Examples
### Predict drug resistance
**Args:** `geno2phenotb -i genome.fasta -o resistance.txt`
**Explanation:** Predicts drug resistance from genome sequence.

### With VCF input
**Args:** `geno2phenotb -i variants.vcf -o resistance.txt`
**Explanation:** Uses variant calls for resistance prediction.

### Batch processing
**Args:** `geno2phenotb -i ./genomes/ -o ./results/`
**Explanation:** Processes multiple genome files in batch.

### Update database
**Args:** `geno2phenotb --update`
**Explanation:** Updates resistance marker database.

### Generate report
**Args:** `geno2phenotb -i genome.fasta -r -o report.html`
**Explanation:** Generates comprehensive resistance report.