---
name: hiphase
category: variant-calling
description: HiPhase is a tool for jointly phasing small, structural, and tandem repeat variants from PacBio HiFi sequencing data.
tags: [hiphase, variant-phasing, PacBio, HiFi, structural-variants]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/HiPhase"
---

## Concepts

- **Variant Phasing**: HiPhase assigns alleles at heterozygous variants to haplotypes.

- **Multi-type Variants**: Jointly phases SNVs, indels, structural variants, and tandem repeats.

- **HiFi Sequencing**: Optimized for PacBio HiFi long-read sequencing data.

- **Global Re-alignment**: Uses global re-alignment for improved phasing accuracy.

- **A*-algorithm**: Implements a novel application of the A*-algorithm to phasing.

- **Phase Block Spanning**: Logic allows phase blocks to span breaks caused by alignment issues.

## Pitfalls

- **Input Requirements**: Requires DeepVariant VCF, pbsv structural variant VCF, and TRGT tandem repeat VCF.

- **Computational Resources**: May require significant computational resources for large datasets.

- **Memory Usage**: Large genomes may require substantial memory.

- **Parameter Tuning**: Requires careful parameter optimization for optimal results.

- **Reference Genome**: Must use appropriate reference genome matching the sequencing data.

## Examples

### Run HiPhase with default settings
**Args:** `hiphase --bam alignments.bam --vcf variants.vcf --output phased.vcf`
**Explanation:** Runs variant phasing on HiFi sequencing data.

### With structural variants
**Args:** `hiphase --bam alignments.bam --vcf snvs.vcf --sv-vcf svs.vcf --output phased.vcf`
**Explanation:** Incorporates structural variants from pbsv into phasing analysis.

### With tandem repeat variants
**Args:** `hiphase --bam alignments.bam --vcf snvs.vcf --tr-vcf trgt.vcf --output phased.vcf`
**Explanation:** Includes tandem repeat variants from TRGT in phasing.

### Using global re-alignment
**Args:** `hiphase --bam alignments.bam --vcf variants.vcf --global-realign --output phased.vcf`
**Explanation:** Enables global re-alignment mode for improved accuracy.

### With multiple threads
**Args:** `hiphase --bam alignments.bam --vcf variants.vcf --threads 16 --output phased.vcf`
**Explanation:** Utilizes multiple threads for faster processing.

### Generate phased alignments
**Args:** `hiphase --bam alignments.bam --vcf variants.vcf --output-phased-bam phased.bam`
**Explanation:** Outputs phased alignments in BAM format.

### Help command
**Args:** `hiphase --help`
**Explanation:** Shows available options and usage information.