---
name: sawfish
category: variant-calling
description: Joint structural variant and copy number variant caller for HiFi sequencing data
tags: ["sawfish", "variant-calling", "HiFi", "structural-variants", "copy-number"]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/sawfish"
---

## Concepts

- **Tool Overview**: Sawfish (v2.2.1) is a joint structural variant and copy number variant caller specifically designed for PacBio HiFi sequencing data.
- **Core Function**: Detects structural variants (SVs) and copy number variants (CNVs) from highly accurate long-read alignments.
- **Algorithm**: Combines split-read mapping, read depth analysis, and haplotype phasing for comprehensive variant detection.
- **Input/Output**: Accepts BAM files with HiFi alignments and reference genome, produces VCF with SV and CNV calls.
- **HiFi Optimization**: Optimized for PacBio HiFi reads with high accuracy (>99.9%).
- **Applications**: Genome structural variation analysis, CNV detection, and comprehensive variant calling.

## Pitfalls

- **HiFi Specific**: Designed for PacBio HiFi data, may not work well with other sequencing platforms.
- **Read Depth**: Requires sufficient sequencing depth for reliable CNV detection.
- **Computational Resources**: High memory and CPU requirements for large genomes.
- **Reference Genome**: Results depend on reference genome quality and completeness.
- **Complex Regions**: May struggle with highly repetitive or segmental duplication regions.
- **Runtime**: Processing time can be significant for large datasets.

## Examples

### Basic variant calling
**Args:** `sawfish call -i hifi.bam -r reference.fasta -o variants.vcf`
**Explanation:** `-i` input BAM; `-r` reference genome; `-o` output VCF with SV and CNV calls.

### With phasing
**Args:** `sawfish call -i hifi.bam -r reference.fasta --phase -o phased.vcf`
**Explanation:** `--phase` enables haplotype phasing of variants.

### Copy number only
**Args:** `sawfish call -i hifi.bam -r reference.fasta --cnv-only -o cnv.vcf`
**Explanation:** `--cnv-only` focuses on copy number variant detection only.

### Quality filtering
**Args:** `sawfish call -i hifi.bam -r reference.fasta -q 20 -o filtered.vcf`
**Explanation:** `-q 20` filters variants with quality below 20.

### Targeted analysis
**Args:** `sawfish call -i hifi.bam -r reference.fasta -t chr1:100000-200000 -o targeted.vcf`
**Explanation:** `-t` specifies target region for focused analysis.

### Generate BED output
**Args:** `sawfish call -i hifi.bam -r reference.fasta -f bed -o variants.bed`
**Explanation:** `-f bed` outputs in BED format instead of VCF.

### Verbose logging
**Args:** `sawfish call -i hifi.bam -r reference.fasta -v -o variants.vcf`
**Explanation:** `-v` enables verbose logging for debugging.