---
name: admixtools
category: population-genomics
description: Software package for formal tests of admixture, inferring admixture proportions and dates in population genetics
tags: [admixture, population-genetics, f-statistics, qp3pop, qpDstat, ancestry]
author: oxo-call-community
source_url: "https://github.com/DReichLab/AdmixTools"
---

## Concepts

- **Tool Overview**: ADMIXTOOLS provides formal statistical tests for detecting admixture events and estimating admixture proportions and dates in population genetic analysis.
- **Core Function**: Calculates f-statistics (f3, f4, D-statistics) to test for admixture and estimate mixture proportions between populations.
- **Main Programs**: qp3Pop (f3 statistics), qpDstat (D-statistics/f4), qpF4Ratio (admixture proportions), convertf (format conversion), rolloff (admixture dating).
- **Input/Output**: Input: EIGENSTRAT or PLINK format genotype files. Output: Statistical test results with Z-scores and standard errors.
- **Installation**: Install via bioconda: `conda install -c bioconda admixtools`

## Pitfalls

- **File Format**: Requires EIGENSTRAT format (geno, snp, ind files) or PLINK format - use convertf to convert between formats.
- **Sample Size**: Small sample sizes can lead to unreliable f-statistics - recommended minimum of 5-10 individuals per population.
- **SNP Ascertainment**: f-statistics are sensitive to SNP ascertainment bias - use appropriate reference populations.
- **Chromosome Count**: Default assumes 22 autosomes; use `numchrom:` parameter for non-human species.

## Examples

### Display help for a program
**Args:** `qp3Pop`
**Explanation:** Shows usage information and parameter file format for f3 statistics calculation.

### Convert PLINK to EIGENSTRAT format
**Args:** `convertf -p convert.par`
**Explanation:** Converts genotype data using parameter file specifying input/output formats and file paths.

### Run f3 statistics test
**Args:** `qp3Pop -p qp3Pop.par`
**Explanation:** Calculates f3 statistics for testing admixture using parameter file with population specifications.

### Run D-statistics (f4) test
**Args:** `qpDstat -p qpDstat.par`
**Explanation:** Calculates D-statistics for formal test of admixture between four populations.

### Estimate admixture proportion with F4 ratio
**Args:** `qpF4Ratio -p qpF4Ratio.par`
**Explanation:** Estimates admixture proportion using F4 ratio test with specified population combinations.

### Run with custom chromosome count
**Args:** `qp3Pop -p qp3Pop.par numchrom: 10`
**Explanation:** Runs f3 analysis with 10 autosomes instead of default 22 (for non-human species).

### Use block jackknife grouping
**Args:** `qpDstat -p qpDstat.par blockname: snp_blocks.txt`
**Explanation:** Uses custom SNP grouping for block jackknife standard error estimation.
