---
name: goleft
category: bioinformatics
description: goleft is a collection of bioinformatics tools distributed as a single static binary for processing sequencing data.
tags: [goleft, bioinformatics, sequencing, utility, tools]
author: oxo-call-community
source_url: "https://github.com/brentp/goleft"
---

## Concepts

- **Tool Collection**: goleft bundles multiple bioinformatics tools into a single static binary for easy deployment.

- **BAM Processing**: Includes tools for processing and analyzing BAM files, including depth calculation and QC metrics.

- **Variant Analysis**: Provides utilities for variant calling and filtering, including VCF processing.

- **QC Metrics**: Generates quality control metrics for sequencing experiments, including coverage and mapping statistics.

- **Visualization**: Creates visualizations of sequencing data, including coverage plots and variant distributions.

- **Cross-Platform**: Distributed as a static binary, ensuring compatibility across different Linux distributions.

## Pitfalls

- **Tool Specificity**: Each subcommand has its own options and requirements. Check help for each tool individually.

- **Memory Usage**: Processing large BAM files requires sufficient memory. Consider downsampling for very large datasets.

- **Reference Requirements**: Some tools require a reference genome. Ensure the reference is available and correctly indexed.

- **File Format**: Ensure input files are in the correct format (BAM, VCF, etc.) and properly indexed.

- **Version Compatibility**: Different versions may have different tool availability. Check the version before use.

## Examples

### Calculate sequencing depth
**Args:** `goleft depth -i input.bam -o depth.txt`
**Explanation:** Calculates sequencing depth across the genome and outputs results to depth.txt.

### Generate coverage plot
**Args:** `goleft covplot -i input.bam -o coverage.png`
**Explanation:** Creates a visualization of sequencing coverage across the genome.

### QC metrics for BAM file
**Args:** `goleft qc -i input.bam -o qc_report.html`
**Explanation:** Generates a comprehensive QC report for the BAM file in HTML format.

### Filter VCF by quality
**Args:** `goleft filter -i input.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters variants with quality scores below 30 from the VCF file.

### Collect mapping statistics
**Args:** `goleft stats -i input.bam -o stats.txt`
**Explanation:** Collects mapping statistics including mapping rate, insert size, and duplication rate.

### Phase variants
**Args:** `goleft phase -i input.vcf -o phased.vcf`
**Explanation:** Phases variants based on read haplotypes to determine allele combinations.

### Merge BAM files
**Args:** `goleft merge -i bam1.bam bam2.bam -o merged.bam`
**Explanation:** Merges multiple BAM files into a single sorted BAM file.