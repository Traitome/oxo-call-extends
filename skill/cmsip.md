---
name: cmsip
category: programming
description: Detect differential 5hmC regions from CMS-IP sequencing data
tags: [cmsip, dna-methylation, 5hmc, sequencing-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lijinbio/cmsip"
---

## Concepts

- **Tool Overview**: cmsip is a package for detecting differential 5-hydroxymethylcytosine (5hmC) regions from CMS-IP (chemical modification-assisted bisulfite sequencing with immunoprecipitation) sequencing data.
- **Core Function**: Identifies differentially hydroxymethylated regions between sample groups from CMS-IP sequencing data.
- **Algorithm**: Uses statistical methods to detect significant differences in 5hmC levels between conditions.
- **Input**: CMS-IP sequencing data (BAM files or coverage files).
- **Output**: Differential 5hmC regions with statistical significance.
- **Application**: Epigenomics research, DNA hydroxymethylation analysis, and epigenetic regulation studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cmsip`

## Pitfalls

- **Data Quality**: Requires high-quality CMS-IP sequencing data.
- **Control Samples**: Needs proper control samples for comparison.
- **Coverage**: Requires sufficient sequencing coverage for reliable detection.
- **Statistical Threshold**: Results depend on significance thresholds used.
- **Batch Effects**: May be affected by batch effects in sequencing data.

## Examples

### Detect differential 5hmC regions
**Args:** `cmsip -i treatment.bam control.bam -o diff_5hmc.txt`
**Explanation:** Detects differential 5hmC regions between treatment and control samples.

### With custom parameters
**Args:** `cmsip -i treatment.bam control.bam -o diff_5hmc.txt -p 0.05 -f 2`
**Explanation:** Uses p-value cutoff of 0.05 and minimum fold change of 2.

### From coverage files
**Args:** `cmsip -c treatment.coverage control.coverage -o diff_5hmc.txt`
**Explanation:** Uses precomputed coverage files instead of BAM files.

### Display help
**Args:** `cmsip --help`
**Explanation:** Shows all available options and usage information.