---
name: somalier
category: qc
description: Somalier - Fast sample-swap and relatedness checks for sequencing data
tags: [somalier, qc, sample-swap, relatedness, bam, vcf]
author: oxo-call-community
source_url: "https://github.com/brentp/somalier"
---

## Concepts

- **Tool Overview**: somalier (v0.3.2) - A sample identity and relatedness checker
- **Core Function**: Detects sample swaps and calculates relatedness
- **Input/Output**: Accepts BAM/CRAM/VCF/GVCF; outputs relatedness matrix
- **Algorithm**: Uses allele frequencies to check sample identity
- **Installation**: `conda install -c bioconda somalier`
- **Key Features**: Sample swap detection, relatedness calculation, fast processing

## Pitfalls

- **Input Requirements**: Requires properly formatted BAM/VCF files
- **Reference Sites**: Requires known variant sites for comparison
- **Sample Names**: Sample names must be correctly identified
- **Coverage**: Requires sufficient coverage for reliable results
- **Population**: Population-specific allele frequencies affect results
- **Output Format**: Output format depends on analysis type

## Examples

### Display help
**Args:** `somalier --help`
**Explanation:** Shows available options and usage information.

### Extract from BAM
**Args:** `somalier extract --sites sites.vcf -f sample.bam -o sample.somalier`
**Explanation:** Extract sample information from BAM.

### Extract from VCF
**Args:** `somalier extract --sites sites.vcf -f sample.vcf -o sample.somalier`
**Explanation:** Extract sample information from VCF.

### Calculate relatedness
**Args:** `somalier relate -o relatedness.tsv sample1.somalier sample2.somalier`
**Explanation:** Calculate relatedness between samples.

### Ancestry check
**Args:** `somalier ancestry --sites sites.vcf -f sample.vcf -o ancestry.tsv`
**Explanation:** Check sample ancestry.

### Sample swap detection
**Args:** `somalier relate --expected-pairs pairs.txt -o relatedness.tsv *.somalier`
**Explanation:** Detect sample swaps.

### Generate report
**Args:** `somalier relate -o relatedness.tsv *.somalier --report`
**Explanation:** Generate relatedness report.

### Plot results
**Args:** `somalier relate -o relatedness.tsv *.somalier --plot`
**Explanation:** Plot relatedness results.