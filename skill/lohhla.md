---
name: lohhla
category: variant-calling
description: LOHHLA - HLA loss evaluation using next-generation sequencing data
tags: [lohhla, variant-calling, HLA, loss-of-heterozygosity, bioinformatics]
author: oxo-call-community
source_url: "https://bitbucket.org/mcgranahanlab/lohhla"
---

## Concepts

- **HLA Loss**: Detection of HLA loss events
- **Loss of Heterozygosity**: LOH analysis in HLA region
- **NGS Data**: Next-generation sequencing data analysis
- **HLA Typing**: HLA typing from sequencing data
- **Tumor Analysis**: Tumor-specific HLA loss detection
- **Allele Imbalance**: Detection of allele imbalance

## Pitfalls

- **HLA Complexity**: HLA region is highly polymorphic
- **Read Quality**: Poor quality reads affect detection
- **Mapping Quality**: Requires accurate read mapping
- **Coverage Depth**: Requires sufficient coverage depth
- **Memory Usage**: Memory-intensive for large datasets
- **False Positives**: May produce false positive calls

## Examples

### Run LOHHLA
**Args:** `LOHHLA.pl --bam input.bam --outputDir results/ --ref hla_reference.fasta`
**Explanation:** Runs HLA loss analysis.

### Sample information
**Args:** `LOHHLA.pl --bam input.bam --outputDir results/ --patientId Sample1`
**Explanation:** Specifies patient ID.

### Threads
**Args:** `LOHHLA.pl --bam input.bam --outputDir results/ --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `LOHHLA.pl --bam input.bam --outputDir results/ --minCoverage 10`
**Explanation:** Sets minimum coverage threshold.

### Quality filtering
**Args:** `LOHHLA.pl --bam input.bam --outputDir results/ --minBaseQuality 20`
**Explanation:** Filters by minimum base quality.

### Verbose output
**Args:** `LOHHLA.pl --bam input.bam --outputDir results/ --verbose`
**Explanation:** Provides detailed output.