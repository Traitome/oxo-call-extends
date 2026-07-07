---
name: rustynuc
category: variant_analysis
description: Quick analysis of pileups for likely 8-oxoG locations.
tags: ["rustynuc", "8-oxoG", "DNA damage", "variant analysis", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/bjohnnyd/rustynuc"
---

## Concepts

- **Tool Overview**: rustynuc (v0.3.1) is a bioinformatics tool for rapid analysis of sequencing pileups to identify likely 8-oxoG (8-oxoguanine) DNA damage sites. 8-oxoG is a common oxidative DNA lesion associated with aging and disease.
- **Core Function**: Analyzes BAM pileup data to detect patterns characteristic of 8-oxoG damage, which causes G→T transversions during sequencing.
- **Algorithm**: Uses statistical analysis of base mismatches in pileup data, specifically looking for excess G→T transversions that indicate oxidative damage.
- **Input Format**: BAM files with aligned reads, requires indexed BAM for efficient pileup generation.
- **Output Format**: VCF-like format with potential 8-oxoG sites, including quality scores and supporting read counts.
- **Use Case**: Identifying oxidative DNA damage in sequencing data, quality control for sequencing experiments, studying DNA repair mechanisms.

## Pitfalls

- **Requires deep coverage**: Minimum coverage required for reliable detection.
- **False positives**: Other sequencing errors can mimic 8-oxoG patterns.
- **Strand bias**: Damage may be strand-specific, affecting detection.
- **Base quality**: Poor base quality can confound damage detection.
- **PCR artifacts**: PCR amplification can introduce similar patterns.
- **Reference bias**: Variant calling against reference may mask true damage.

## Examples

### Basic 8-oxoG detection
**Args:** `rustynuc -i input.bam -o oxog_sites.vcf`
**Explanation:** `-i` input BAM file; `-o` output VCF with detected 8-oxoG sites.

### Minimum coverage threshold
**Args:** `rustynuc -i input.bam -o oxog_sites.vcf -c 20`
**Explanation:** `-c` minimum coverage required for analysis.

### Filter by quality
**Args:** `rustynuc -i input.bam -o oxog_sites.vcf -q 30`
**Explanation:** `-q` minimum base quality for considering mismatches.

### Output bed format
**Args:** `rustynuc -i input.bam -o oxog_sites.bed --bed`
**Explanation:** `--bed` outputs in BED format instead of VCF.

### Verbose mode
**Args:** `rustynuc -i input.bam -o oxog_sites.vcf -v`
**Explanation:** `-v` verbose output with detailed statistics.

### Specific region analysis
**Args:** `rustynuc -i input.bam -o oxog_sites.vcf -r chr1:100000-200000`
**Explanation:** `-r` analyze only specified genomic region.

### Report all mismatches
**Args:** `rustynuc -i input.bam -o oxog_sites.vcf --all`
**Explanation:** `--all` reports all mismatches, not just potential 8-oxoG.
