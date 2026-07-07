---
name: haproh
category: bioinformatics
description: hapROH identifies runs of homozygosity and contamination in low coverage ancient human DNA data using modern reference panels.
tags: [haproh, ancient-DNA, runs-of-homozygosity, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hringbauer/hapROH"
---

## Concepts

- **Runs of Homozygosity**: hapROH identifies ROH segments in genomic data.

- **Ancient DNA Analysis**: Optimized for low coverage ancient human DNA.

- **Contamination Detection**: Detects sample contamination in aDNA data.

- **Modern Reference Panel**: Uses modern reference panels for comparison.

- **1240K SNPs**: Works with 1240K SNP capture data.

- **Population Genetics**: Supports population genetics studies.

## Pitfalls

- **DNA Degradation**: Account for DNA degradation in ancient samples.

- **Coverage Depth**: Low coverage may affect results.

- **Reference Panel**: Ensure using appropriate reference panel.

- **Contamination Levels**: Very low contamination may be missed.

- **Computational Resources**: May require significant resources.

## Examples

### Identify ROH
**Args:** `haproh --input genotypes.vcf --reference ref_panel.vcf --output roh_results.txt`
**Explanation:** Identifies runs of homozygosity in genomic data.

### Detect contamination
**Args:** `haproh --input genotypes.vcf --reference ref_panel.vcf --contamination --output contamination.txt`
**Explanation:** Detects contamination in ancient DNA samples.

### Batch processing
**Args:** `for chr in {1..22}; do haproh --input chr${chr}.vcf --reference ref_panel.vcf --output chr${chr}_roh.txt; done`
**Explanation:** Processes multiple chromosome files.

### Generate report
**Args:** `haproh --input genotypes.vcf --reference ref_panel.vcf --report --output report.html`
**Explanation:** Generates comprehensive analysis report.

### Quality filtering
**Args:** `haproh --input genotypes.vcf --reference ref_panel.vcf --min-quality 30 --output roh_results.txt`
**Explanation:** Filters variants by quality score.

### Visualization
**Args:** `haproh --input genotypes.vcf --reference ref_panel.vcf --plot --output plot.pdf`
**Explanation:** Generates visualization of ROH results.

### Help command
**Args:** `haproh --help`
**Explanation:** Shows available options and usage information.