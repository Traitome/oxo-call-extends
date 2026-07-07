---
name: hap-ibd
category: bioinformatics
description: Hap-IBD detects identity-by-descent (IBD) segments and homozygosity-by-descent (HBD) segments in phased genotype data.
tags: [hap-ibd, IBD, HBD, population-genetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/browning-lab/hap-ibd"
---

## Concepts

- **IBD Detection**: Hap-IBD detects identity-by-descent segments.

- **HBD Detection**: Identifies homozygosity-by-descent segments.

- **Phased Genotypes**: Works with phased genotype data.

- **Population Genetics**: Analyzes genetic relationships between individuals.

- **Segment Identification**: Identifies shared genetic segments.

- **Relatedness Analysis**: Determines genetic relatedness.

## Pitfalls

- **Phasing Quality**: Results depend on phasing quality.

- **Sample Size**: Requires sufficient sample size for accurate detection.

- **Marker Density**: Requires sufficient marker density.

- **Population Structure**: Account for population structure.

- **Segment Size**: Small segments may be missed.

## Examples

### Detect IBD segments
**Args:** `hap-ibd --vcf input.vcf --out ibd_results.txt`
**Explanation:** Detects IBD segments from phased VCF.

### With genetic map
**Args:** `hap-ibd --vcf input.vcf --map genetic_map.txt --out ibd_results.txt`
**Explanation:** Uses genetic map for improved IBD detection.

### Detect HBD segments
**Args:** `hap-ibd --vcf input.vcf --hbd --out hbd_results.txt`
**Explanation:** Detects homozygosity-by-descent segments.

### Filter by segment length
**Args:** `hap-ibd --vcf input.vcf --min-length 1.0 --out ibd_results.txt`
**Explanation:** Filters IBD segments by minimum length.

### Batch processing
**Args:** `for chr in {1..22}; do hap-ibd --vcf chr${chr}.vcf --out chr${chr}_ibd.txt; done`
**Explanation:** Processes multiple chromosome files.

### Generate statistics
**Args:** `hap-ibd --vcf input.vcf --stats --out stats.txt`
**Explanation:** Generates IBD detection statistics.

### Help command
**Args:** `hap-ibd --help`
**Explanation:** Shows available options and usage information.